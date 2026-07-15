---
description: 'Markdown accessibility guidelines based on GitHub''s 5 best practices for inclusive documentation'
applyTo: '**/*.md'
---

# Markdown Accessibility Review Guidelines

This file is the single home for **accessibility** conventions in this repo. Mechanical Markdown formatting lives in [`markdown.instructions.md`](./markdown.instructions.md); the accessibility rationale for those conventions lives here.

When writing or reviewing Markdown files, check for the following accessibility issues based on GitHub's [5 tips for making your GitHub profile page accessible](https://github.blog/developer-skills/github/5-tips-for-making-your-github-profile-page-accessible/) and the Smashing Magazine article [Improving The Accessibility Of Your Markdown](https://www.smashingmagazine.com/2021/09/improving-accessibility-of-markdown/). Flag violations and suggest fixes with clear explanations of the accessibility impact.

## 1. Descriptive Links

- Flag generic link text such as "click here," "here," "this," "read more," "learn more," or "link."
- Link text must make sense when read out of context, because assistive technology can present links as an isolated list.
- Weave the link into the prose with descriptive text; never add a sentence whose only job is to point at a link.
- Flag multiple links on the same page that share identical text but point to different destinations.
- Bare URLs in prose should be converted to descriptive links.

Bad: `Read my blog post [here](https://example.com)`
Good: `Read my blog post "[Crafting an accessible resume](https://example.com)"`

## 2. Image Alternative (alt) Text

- Flag images with empty alt text (e.g., `![](path/to/image.png)`) unless they are explicitly decorative. In this repo, Starlight treats alt text as required.
- Flag alt text that is a filename (e.g., `img_1234.jpg`) or generic placeholder (e.g., `screenshot`, `image`).
- Alt text should be succinct and descriptive. Include any text visible in the image.
- Use "screenshot of" where relevant, but do not prefix with "image of" since screen readers announce that automatically.
- For complex images (charts, infographics), suggest summarizing the data in alt text and providing longer descriptions via `<details>` tags or linked content.
- When suggesting alt text improvements, present them as recommendations for the author to review. Alt text requires understanding of visual content and context that only the author can properly assess.

## 3. Heading Hierarchy

- Headings must follow a logical hierarchy and never skip levels (e.g., `##` followed by `####` is a violation).
- Flag bold text (`**text**`) used as a visual substitute for a proper heading.
- Proper heading structure allows assistive technology users to navigate by section and helps sighted users scan content.

This repo has two repo-specific rules that override the generic "one H1 per document" guidance:

- **Lesson pages have no H1 in the body.** The title comes from Markdown frontmatter and Starlight renders it as the H1. Body headings start at `##`.
- **Repository docs carry their own H1.** README, contributing, instruction, and skill files start with a single `#` title.

## 4. Plain Language

- Flag unnecessarily complex or jargon-heavy language that could be simplified.
- Favor short sentences, common words, and active voice.
- Flag long, dense paragraphs that could be broken into smaller sections or lists.
- When describing UI navigation, write actions as sequential steps in plain language first (e.g., "open Settings, then select Preferences"). Use generic, stable labels rather than icon names or visual descriptions.
- A parenthetical visual reference may follow as supplemental context (e.g., "(gear icon > Preferences)"), but never use visual breadcrumb notation or icon names as the sole way to describe a navigation path.
- When suggesting plain language improvements, present them as recommendations for the author to review. Language decisions require understanding of audience, context, and tone.

### Input-agnostic action verbs

- Use input-agnostic verbs so instructions work for keyboard, screen reader, touch, and mouse users. Prefer **select** over "click", "press", or "tap" when referring to UI elements (buttons, tabs, menu items, links).
- Reserve "press" for physical keyboard shortcuts (e.g., "press <kbd>Enter</kbd>").

## 5. Lists and Emoji Usage

### Lists

- Flag emoji or special characters used as bullet points instead of proper markdown list syntax (`-`, `*`, `+`, or `1.`).
- Flag sequential items in plain text that should be structured as a proper list.
- Proper list markup allows screen readers to announce list context (e.g., "item 1 of 3").

### Emoji

- Flag multiple consecutive emoji, which are disruptive to screen reader users since each emoji name is read aloud in full (e.g., "rocket" "sparkles" "fire").
- Flag emoji used to convey meaning that is not also communicated in text.
- Emoji should be used sparingly and thoughtfully.

## 6. Multimedia

- Provide captions for videos and transcripts for recorded audio.
- Do not auto-play audio and video.
- It's recommended that animated images and other animations are paused on page load.

## 7. Other

- Links: Avoid opening links in a new tab or window.
- Bold and Italics: Screen readers often don't announce bold or italic emphasis, so critical information should not rely on this styling alone.
- Tables: Use tables for data only. Do not use tables for page layout. Avoid nested tables. Avoid complex tables as they are difficult to represent in an accessible format in standard Markdown.

## Review Priority

When multiple issues exist, prioritize in this order:

1. Missing or empty alt text on images
2. Skipped heading levels or heading hierarchy issues
3. Non-descriptive link text
4. Emoji used as bullet points or list markers
5. Plain language improvements
6. Multimedia
7. Other

## Review Tone

- Explain the accessibility impact of each issue, specifying which users are affected (e.g., screen reader users, people with cognitive disabilities, non-native speakers).
- Do not remove personality or voice from the writing. Accessibility and engaging content are not mutually exclusive.
- Keep suggestions actionable and specific.
