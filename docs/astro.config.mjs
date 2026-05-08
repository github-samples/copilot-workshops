// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
  site: 'https://github-samples.github.io',
  base: '/agents-in-sdlc',
  trailingSlash: 'always',
  integrations: [
    starlight({
      title: 'Agents in the SDLC Workshop',
      description:
        'A hands-on workshop exploring GitHub Copilot agents across VS Code, the Copilot CLI, and the Copilot cloud agent.',
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/github-samples/agents-in-sdlc',
        },
      ],
      editLink: {
        baseUrl:
          'https://github.com/github-samples/agents-in-sdlc/edit/main/workshop-content/',
      },
      sidebar: [
        { label: 'Home', link: '/' },
        { label: 'Prerequisites', link: '/shared/0-prereqs/' },
        {
          label: 'VS Code path',
          items: [
            { label: 'Overview', link: '/vscode/' },
            { label: '1. Custom instructions', link: '/shared/1-custom-instructions/' },
            { label: '2. Custom instructions hands-on', link: '/vscode/2-custom-instructions/' },
            { label: '3. MCP with VS Code', link: '/vscode/3-mcp/' },
            { label: '4. Agent mode', link: '/vscode/4-agent-mode/' },
            { label: '5. Cloud agent', link: '/vscode/5-cloud-agent/' },
            { label: '6. Custom agents', link: '/vscode/6-custom-agents/' },
            { label: '7. Managing agents', link: '/vscode/7-managing-agents/' },
            { label: '8. Iterating', link: '/vscode/8-iterating/' },
          ],
        },
        {
          label: 'Copilot CLI path',
          items: [
            { label: 'Overview', link: '/cli/' },
            { label: '1. Custom instructions', link: '/shared/1-custom-instructions/' },
            { label: '2. Install Copilot CLI', link: '/cli/2-install-copilot-cli/' },
            { label: '3. MCP with CLI', link: '/cli/3-mcp/' },
            { label: '4. Generating code', link: '/cli/4-generating-code/' },
            { label: '5. Agent skills', link: '/cli/5-agent-skills/' },
            { label: '6. Custom agents', link: '/cli/6-custom-agents/' },
            { label: '7. Slash commands', link: '/cli/7-slash-commands/' },
            { label: '8. Review', link: '/cli/8-review/' },
          ],
        },
        {
          label: 'Cloud agent path',
          items: [
            { label: 'Overview', link: '/cloud/' },
            { label: '1. Custom instructions', link: '/shared/1-custom-instructions/' },
            { label: '2. Cloud agent', link: '/cloud/2-cloud-agent/' },
            { label: '3. Custom agents', link: '/cloud/3-custom-agents/' },
            { label: '4. Managing agents', link: '/cloud/4-managing-agents/' },
            { label: '5. Iterating', link: '/cloud/5-iterating/' },
          ],
        },
      ],
    }),
  ],
});
