---
title: "Exercise 9 - Explore slash commands and CLI options"
description: "Inspect context, model and session controls, review sharing destinations, and explore CLI flags without launching another feature."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

The three PR milestones are complete. Now explore the CLI controls that help you understand and manage a session. This exercise does not implement another feature, delegate work, or open another PR.

From the updated learner checkout, start `copilot` in **Interactive** mode. Use `/help` and the [command reference][cli-reference] to confirm which commands your installed version supports; current documentation can describe newer controls than your installation.

## Inspect context and session information

1. Send a bounded, read-only request:

   ```plaintext
   Summarize the repository's instruction files, quality-checks skill, and QA profile. Explain how they support filtering verification. Do not modify files, execute checks, delegate work, commit, or open a PR.
   ```

2. Enter `/context` to inspect context-window usage. Notice how messages, instructions, and tool definitions consume context.
3. Enter `/compact`, then `/context` again. Compaction summarizes history to reduce its size; a short session may show little change.
4. Enter `/session` to inspect the current session, and `/usage` to inspect usage information.

Compaction is not a substitute for supplying requirements. When changing tasks or agents, carry forward the issue URL, approved criteria, checkout identity, and relevant evidence explicitly.

`/clear` starts a new conversation; it does not undo files or switch Git branches. `/resume` opens the session picker for returning to prior work. Explore the picker, then press <kbd>Esc</kbd> to leave it without resuming another task. Do not clear the only copy of acceptance criteria or assume a resumed conversation means its old verification is still current.

## Inspect models and modes

Enter `/model` to inspect models available to your account, including **Auto** where offered. Read the selection details and usage information; model availability and pricing can change. Press <kbd>Esc</kbd> to leave the picker without changing the model. If you do change it, confirm the displayed selection and the scope your CLI version applies.

Use <kbd>Shift</kbd>+<kbd>Tab</kbd> to inspect the mode indicator as you cycle between **Interactive**, **Plan**, and **Autopilot**, then return to **Interactive** without sending an implementation prompt. Recall the distinction:

- Plan is for agreeing the work before coding.
- Autopilot continues through an approved, bounded task.
- Interactive gives you deliberate review and decision points.
- Permissions separately control which tool actions are allowed.

## Inspect command-line options

In a separate terminal, run:

```bash
copilot --help
```

Compare these documented options with the help for your installed version:

| Option | Purpose |
| --- | --- |
| `--model MODEL` | Choose the model for an invocation; confirm availability first |
| `--agent AGENT` | Select a custom agent for an invocation |
| `-p PROMPT` | Run a prompt programmatically and exit when it completes |
| `--output-format json` | Emit structured JSONL output, one JSON object per line |
| `--resume` | Resume an existing session |
| `--enable-all-github-mcp-tools` | Expose the full built-in GitHub MCP tool set |

These are controls to understand, not another task to launch. Programmatic mode can execute real tool actions; a JSON output format does not make a request read-only. Agent selection is the verified workflow from [Exercise 7][qa-lesson], not a reason to replace custom-agent activation with a default-agent request to read the profile. Permissions and access still apply.

## Review before sharing

`/share` can send session content to different destinations. The [CLI command reference][cli-reference] documents `/share file [session|research] [PATH]` for Markdown export and `/share gist [session|research]` for gist publishing. With no subcommand, the current documented behavior creates a shareable GitHub link when logged in and synced, falling back to a Markdown export otherwise. Do not run the bare command while assuming it only previews content.

For this workshop, explicitly select a local session export and filename rather than publishing:

```text
/share file session cli-session-review.md
```

Open the exported file in your editor and inspect what it actually contains. Review prompts, responses, tool output, file paths, repository data, and any credentials or personal information. Do not assume the export contains every internal step or that it has automatically removed sensitive content.

> [!CAUTION]
> A gist or shared link is an external disclosure. A secret gist is not private access control: anyone with its URL can view it. Confirm the destination, recipients, permissions, and your organization's policy before sharing. If redaction is needed, share only the reviewed, redacted artifact through an approved channel; do not publish the original session afterward.

Keep this export out of the feature PR and repository history. After inspecting it, remove the file you just generated or move it to your approved local notes location. Do not remove unrelated files.

Cloud delegation can create remote work and an additional PR, so do not run `/delegate` here. The [Cloud agent workshop][cloud-workshop] covers that separate workflow.

## Summary and next steps

You've inspected context, usage, model and mode controls, command-line options, and sharing destinations without starting another feature. Continue to [Exercise 10 - Wrap-up and next steps][next-lesson] to review the workflow and artifacts you've built.

[previous-lesson]: ../8-create-pull-request/
[next-lesson]: ../10-review/
[qa-lesson]: ../7-qa-agent/
[cloud-workshop]: ../../cloud/
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
