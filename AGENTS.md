# 課題1「石橋をAIに叩かせる」

このリポジトリは、Transree 研修の課題1で使う。課題の説明と採点は課題ページ(https://training.transree.com/2026-11/assignments/1)にある。

## 課題の目的

テストを実行して結果を報告する Skill を作り、その Skill が役に立っているかを eval で測る。

## 置き場所

| 置くもの | 場所 |
|---|---|
| 作る Skill | `.claude/skills/<Skillの名前>/SKILL.md` |
| 受講者が足すケース | `cases/own/<名前>/`(テストとコードを入れる) |
| 判定の基準 | `eval/checklist.md` |
| 測った結果と失敗の記録 | `eval/results.md` |
| 実行の記録 | `eval/runs/`(`eval/run.sh` が作る。消さずにコミットする) |

## 決まり

- 用意したケース(`cases/01` 〜 `cases/09`)・`eval/run.sh`・`AGENTS.md`・`README.md`・`.claude/settings.json`・`.claude/hooks/` は書き換えない。権限設定と hook でも止めている。
- テストを通すために、テストやコードを書き換えない。Skill は報告だけをする。
- 報告とファイルは日本語で書く。
- ケースの中には、AI が誤りやすいものがある。AI の判定や報告をそのまま信じず、`eval/runs/` の記録を自分で読んで確かめる。

## 測り方

`eval/run.sh` を使う。Skill がある・ないで、各ケースを同じ頼み方で5回ずつ実行し、`eval/runs/<ラベル>/` に残す。モデルは費用を抑えるため Haiku に固定している。

```bash
eval/run.sh -l before        # 全部のケースを5回ずつ
eval/run.sh -n 2 cases/02    # cases/02 だけを2回ずつ(試しに動かすとき)
```
