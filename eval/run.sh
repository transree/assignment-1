#!/usr/bin/env bash
# Skill がある・ないで、各ケースを同じ頼み方で何回か実行し、結果を eval/runs/<ラベル>/ に残す。
# 使い方: eval/run.sh [-n 回数] [-l ラベル] [-p 同時に動かす数] [ケース ...]
#   例: eval/run.sh -l before            全部のケースを5回ずつ
#       eval/run.sh -n 2 cases/02        cases/02 だけを2回ずつ
# モデルは費用を抑えるため Haiku に固定している。
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
runs=5
label=$(date +%Y%m%d-%H%M%S)
parallel=4
while getopts "n:l:p:" option; do
  case $option in
    n) runs=$OPTARG ;;
    l) label=$OPTARG ;;
    p) parallel=$OPTARG ;;
    *) exit 2 ;;
  esac
done
shift $((OPTIND - 1))

cd "$root"
# pip install --user や pipx で入れた pytest も見つかるようにする
export PATH="$HOME/.local/bin:$PATH"
if ! command -v pytest > /dev/null; then
  echo "pytest が見つかりません。README の始め方を確認してください。" >&2
  exit 1
fi
if [ $# -gt 0 ]; then
  cases=("${@%/}")
else
  mapfile -t cases < <(ls -d cases/[0-9]*/ cases/own/*/ 2>/dev/null | sed 's#/$##')
fi
out="$root/eval/runs/$label"
mkdir -p "$out"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

# 1回ごとに、リポジトリの写しを作って実行する(実行が本物のファイルを変えないように)。
# Skill なしの回は、写しから .claude/skills を消す。それ以外の条件は同じ。
copy_repo() {
  local dest=$1 mode=$2
  mkdir -p "$dest"
  tar -C "$root" --exclude=./.git --exclude=./eval/runs -cf - . | tar -C "$dest" -xf -
  if [ "$mode" = without ]; then rm -rf "$dest/.claude/skills"; fi
}

run_one() {
  local case=$1 mode=$2 i=$3
  local name=${case//\//_}
  local dest="$work/$name-$mode-$i"
  local log="$out/$name/$mode-$i"
  mkdir -p "$out/$name"
  copy_repo "$dest" "$mode"
  # 頼み方は Skill がある・ないで同じにする
  # 写しは信頼されていないフォルダなので、許可はコマンドの引数で渡す。
  # ファイルの編集はさせず、手元の個人の設定・Skill・MCP は読まない。
  (cd "$dest" && timeout 600 claude -p --model haiku --output-format stream-json --verbose \
    --setting-sources project --strict-mcp-config \
    --allowedTools "Bash(pytest *)" "Bash(python3 -m pytest *)" "Bash(python -m pytest *)" "Bash(ls *)" Read Glob Grep Skill \
    --disallowedTools Edit Write NotebookEdit \
    -- "$case のテストを実行して、結果を報告してください。" > "$log.jsonl" 2> "$log.err") || true
  # 最後の返事だけを Markdown に取り出す
  python3 - "$log.jsonl" > "$log.md" <<'PY'
import json, sys
result = ""
for line in open(sys.argv[1], encoding="utf-8"):
    try:
        event = json.loads(line)
    except json.JSONDecodeError:
        continue
    if event.get("type") == "result":
        result = event.get("result") or ""
print(result if result else "(返事がありません。.jsonl と .err を確認してください)")
PY
  # 写しを信頼していないという決まった警告は消し、ほかのエラーだけを残す
  grep -v "has not been trusted" "$log.err" > "$log.err.tmp" || true
  mv "$log.err.tmp" "$log.err"
  [ -s "$log.err" ] || rm -f "$log.err"
  echo "done $case $mode $i"
}

jobs_list=()
for case in "${cases[@]}"; do
  for mode in with without; do
    for i in $(seq 1 "$runs"); do jobs_list+=("$case $mode $i"); done
  done
done
echo "${#jobs_list[@]} 回を実行します(ラベル: $label)"
running=0
for job in "${jobs_list[@]}"; do
  # shellcheck disable=SC2086
  run_one $job &
  running=$((running + 1))
  if [ "$running" -ge "$parallel" ]; then wait -n; running=$((running - 1)); fi
done
wait
echo "結果: eval/runs/$label/<ケース>/<with|without>-<回>.md(全体の記録は .jsonl)"
