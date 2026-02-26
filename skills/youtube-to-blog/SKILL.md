---
name: youtube-to-blog
description: Analyze a YouTube video via URL and automatically create a high-quality, long-form blog post (2x length) on Antigravity Lab.
metadata:
  {
    "openclaw":
      {
        "emoji": "📺",
        "requires": { "bins": ["summarize", "python3"] }
      },
  }
---

# YouTube to Blog Skill

Automatically convert insightful YouTube videos into professional blog posts.

## Usage

Provide a YouTube URL and ask the agent to "Create a blog post from this video".

## Process

1.  **Extract Transcript**: Uses the `summarize` tool with `--extract-only` to get the full raw text.
2.  **Analyze & Draft**:
    *   Analyzes the core message, key points, and unique insights.
    *   Drafts a long-form post (minimum 2x previous standard length).
    *   Category selection: "AI 최신뉴스", "AI를 활용한 개발정보", "OpenClaw", or "수익화 팁".
3.  **No Emojis/Special Chars**: Adheres to strict formatting (no emojis, no `**`).
4.  **Auto Deploy**: Uses `build_engine.py` and git to push the new post to `https://kimsungwuk.github.io`.

## Trigger Phrases

- "이 유튜브 영상 분석해서 블로그 포스팅해줘"
- "유튜브 요약해서 블로그에 올려줘"
- "Create a blog post from this YouTube video: <URL>"
