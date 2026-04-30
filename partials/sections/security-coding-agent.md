## Security and GitHub Copilot coding agent

Because Copilot coding agent performs its tasks asynchronously and without supervision, certain security constraints have been put in place to ensure everything remains safe. These include:

- Copilot only has read access to your repository and write access **only** to the branch it will use for its code.
- Coding agent runs inside of GitHub Actions, where it will create a separate, ephemeral environment in which to work.
- Any GitHub Actions workflows require approval from a human before they can be run.
- [Access to external resources is limited by default](https://docs.github.com/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent), including MCP servers.
