---
title: "Lesson 9 - Slash commands in GitHub Copilot CLI"
description: "Explore slash commands for managing context, selecting models, sharing sessions, and optional cloud delegation."
authors:
  - geektrainer
lastUpdated: 2026-09-18
---

Like any good CLI tool, GitHub Copilot CLI includes many slash commands to interact with it. These commands expose advanced functionality, behind-the-scenes information, and additional configuration options. You've already used commands such as `/diff`, `/mcp`, `/skills`, `/agent`, and `/pr`. Let's explore a few other useful ones.

In this lesson, you will:

- use `/context` and `/compact` to explore how Copilot manages conversation context.
- use `/model` to explore the models available to you.
- learn how `/share` can export or share a session.
- explore optional commands for parallel work, worktrees, and delegation to cloud agent.

## Scenario

You've wrapped the core CLI workflow. Now let's look at a few additional capabilities — managing context, switching models, sharing sessions, and optionally delegating work to [Copilot cloud agent][about-cloud-agent].

## Explore Copilot CLI context

When working on larger or more complex tasks, you may bump into the maximum context window for the model. Copilot CLI automatically compacts the conversation when needed, and you can inspect or compact it yourself with slash commands.

1. Start Copilot CLI from the repository root if it is not already open.
2. Enter:

   ```plaintext
   /context
   ```

3. Note the model, current token usage, and how the context is divided among system instructions, tools, messages, and free space.
4. Compact the conversation:

   ```plaintext
   /compact
   ```

5. Enter `/context` again and compare the result. There might not be a drastic change if the conversation is already small.

> [!NOTE]
> Copilot CLI automatically compacts context as the window fills. Use `/compact` when you want to choose the timing. Use `/clear` or `/new` when you are switching to an unrelated task and want a fresh conversation instead.

## Choose your model

Different models have different strengths, and different developers have different preferences. Copilot CLI allows you to list and select the model you want to use.

1. Enter:

   ```plaintext
   /model
   ```

2. Explore the available models and usage information.
3. Keep the current model, select another one, or press <kbd>Esc</kbd> to close the list.

## Share a session

Working together as a team and sharing learnings helps everyone improve their use of AI tools. The `/share` command can export a session to a Markdown or HTML file, create a shareable link, or publish a GitHub gist.

1. Enter `/help` and review the `/share` options in your installed version.
2. If you want to share this session, choose the destination that fits your needs, such as `/share file` for a local Markdown export.
3. Review the exported content before sending it to anyone or publishing it. Session exports can include prompts, responses, and project details.

Publishing a link or gist is optional. Don't publish repository or conversation content that your team does not intend to share.

## Optional: scale out or delegate

The core workshop is complete. Copilot CLI also provides commands for larger tasks:

- `/fleet` can divide independent subtasks among subagents and run them in parallel.
- `/worktree` can create an isolated Git worktree for a separate task.
- `/delegate` can send a task to Copilot cloud agent, which works asynchronously and may open a pull request.

These commands are optional because they can create additional worktrees or remote work. Start a fresh, well-scoped task before trying them, and review the result through your normal workflow. If you want to dig deeper into asynchronous agent work, continue with the [cloud agent workshop][cloud-workshop].

## Summary and next steps

Using slash commands in Copilot CLI allows you to configure it, share sessions, and see what's going on behind the scenes. In this lesson, you:

- used `/context` and `/compact` to explore how Copilot manages conversation context.
- used `/model` to explore the models available to you.
- learned how `/share` can export or share a session.
- explored optional commands for parallel work, worktrees, and delegation to cloud agent.

There are more slash commands available and more to explore with Copilot CLI! Let's close out our journey by [reviewing what we've learned][next-lesson] and some next steps to continue learning.

## Resources

- [Copilot CLI command reference][cli-reference]
- [Context management in Copilot CLI][context-management]
- [About Copilot cloud agent][about-cloud-agent]

[previous-lesson]: ../8-create-pull-request/
[next-lesson]: ../10-review/
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[context-management]: https://docs.github.com/copilot/concepts/agents/copilot-cli/context-management
[about-cloud-agent]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent
[cloud-workshop]: ../../cloud/
