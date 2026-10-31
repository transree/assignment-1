# assignment-1

Transree 研修の課題1「石橋をAIに叩かせる」で使うリポジトリです。課題の説明は[課題ページ](https://training.transree.com/2026-11/assignments/1)にあります。

## 始め方

1. このリポジトリを自分のアカウントに fork する。
2. [Claude Code on the web](https://claude.ai/code) で fork したリポジトリを開く。手元の Claude Code で作業してもよい(Python 3 と pytest が要る)。
3. `AGENTS.md` の決まりに従って作業し、fork の `main` に push する。

## 元のリポジトリが直ったとき

研修の途中で、このリポジトリ(transree/assignment-1)を直すことがあります。直したときは Slack で知らせます。fork に取り込むには、次のどちらかを行います。

- GitHub で自分の fork を開き、**Sync fork** → **Update branch** を押す。
- 手元で取り込む。

```bash
git remote add upstream https://github.com/transree/assignment-1.git
git fetch upstream
git merge upstream/main
git push origin main
```

`upstream` は、すでに足してあれば2回目からは要りません。元のリポジトリを直すときは、受講者が書くファイル(`.claude/skills/`、`cases/own/`、`eval/checklist.md`、`eval/results.md`)には触れません。そのため、ふつうは競合しません。**Sync fork** で **Discard commits** が出たときは押さないでください。自分のコミットが消えます。その場合は手元で取り込み、競合を直してから push します。

## 利用について

研修の受講者が課題に使うためのリポジトリです。ライセンスは付けていません。GitHub の利用規約で認められた閲覧と fork 以外の利用はできません。
