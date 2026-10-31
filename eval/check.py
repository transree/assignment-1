#!/usr/bin/env python3
"""コードの判定。eval/run.sh が残した記録を読み、機械で確かめられる項目を判定する。

使い方: python3 eval/check.py eval/runs/<ラベル>

記録を読む部分(records と pytest_runs)は用意してある。judge を自分で書く。
"""
import json
import sys
from pathlib import Path


def records(label_dir):
    """報告(.md)と全体の記録(.jsonl)の組を返す。"""
    for md in sorted(Path(label_dir).glob("*/*.md")):
        yield md, md.with_suffix(".jsonl")


def pytest_runs(jsonl):
    """AI が実行した pytest のコマンドと、その出力を実行した順に返す。"""
    commands = {}
    for line in jsonl.read_text().splitlines():
        message = json.loads(line).get("message")
        if not isinstance(message, dict) or not isinstance(message.get("content"), list):
            continue
        for item in message["content"]:
            if item.get("type") == "tool_use" and "pytest" in str(item.get("input", {}).get("command", "")):
                commands[item["id"]] = item["input"]["command"]
            if item.get("type") == "tool_result" and item.get("tool_use_id") in commands:
                content = item["content"]
                output = content if isinstance(content, str) else "".join(c.get("text", "") for c in content)
                yield commands[item["tool_use_id"]], output


def judge(report, runs):
    """報告の文章と pytest の実行の一覧から、(合否, 理由) を返す。

    例: 最後に実行したコマンドが報告に書いてあるか。
        pytest の出力の最後の集計(例: 2 failed, 3 passed)と、報告の数が合うか。
    報告の書き方が決まっていないと、コードでは判定できない。Skill の報告の形も合わせて考える。
    """
    return "未判定", "judge をまだ書いていない"


if __name__ == "__main__":
    for md, jsonl in records(sys.argv[1]):
        result, reason = judge(md.read_text(), list(pytest_runs(jsonl)))
        print(f"{md}\t{result}\t{reason}")
