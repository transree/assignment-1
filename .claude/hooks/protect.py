"""用意したケース・課題の決まり・設定の書き換えを止める PreToolUse の hook。

権限設定の deny と同じファイルを、もう一度ここで止める。
止めるときは終了コード2を返し、理由を標準エラーに書く(Claude に伝わる)。
"""
import json
import os
import sys

PROTECTED_FILES = {"AGENTS.md", "README.md", "eval/run.sh", ".claude/settings.json"}
PROTECTED_DIRS = (".claude/hooks/",)


def is_protected(rel):
    if rel in PROTECTED_FILES or rel.startswith(PROTECTED_DIRS):
        return True
    # 用意したケース(cases/01 など)は止め、受講者が足す cases/own/ は許す
    parts = rel.split("/")
    return len(parts) >= 2 and parts[0] == "cases" and parts[1][:1].isdigit()


def main():
    data = json.load(sys.stdin)
    tool_input = data.get("tool_input", {})
    path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
    if not path:
        return 0
    root = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
    rel = os.path.relpath(os.path.realpath(os.path.join(root, path)), root).replace(os.sep, "/")
    if is_protected(rel):
        print(f"{rel} は課題で書き換えないファイルです(AGENTS.md を参照)。", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
