---
title: "Connect the agent to the site"
description: "Integrate the hosted Backer Concierge through a local credential-safe proxy, test the widget, and use Agent merge."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/app/8-foundry-canvas/2-build-and-deploy/
  label: Build and deploy the agent
next:
  link: /copilot-workshops/app/9-review/
  label: Review and next steps
---

This final module connects the tested hosted agent from [Build and deploy the agent][previous-module] to the locally running Tailspin Toys website.

By the end, you will have:

- A local Azure Functions proxy that protects Foundry credentials and conversation identifiers.
- An accessible chat widget with verified end-to-end behavior.
- A reviewed change handed to Agent merge and a resource cleanup checkpoint.

## Scenario

Tailspin Toys backers need catalog advice where they browse games. The Backer Concierge should preserve the conversation, work with keyboard navigation, and handle unavailable information and errors clearly. That convenience must not expose service credentials or internal conversation details to the browser.

## Resume the hosted-agent checkpoint

The integration uses the existing hosted agent rather than creating new Foundry resources.

1. Resume the same Tailspin Toys repository, worktree branch, and **Add a Backer Concierge assistant for catalog questions** issue session from the earlier modules. Confirm the root `azure.yaml`, agent source, and catalog are present, and check the recorded subscription, dedicated resource group, Foundry project, model deployment, and tested hosted-agent version.
2. Reopen Microsoft Foundry Canvas and confirm the same project, deployment, and hosted-agent status. If resources were cleaned up, restore the relevant [project and model][project-module] and [tested hosted deployment][previous-module] before integration. Otherwise, reuse them without creating another project.

## Build the server-side proxy

Tailspin Toys is fully pre-rendered. Browser code must never call the hosted agent directly or receive Foundry credentials. A local Azure Functions **server-side credential boundary** authenticates to Foundry and returns only the agent response to the browser. The browser sends each message with an opaque conversation handle; the proxy maps that handle to the Foundry conversation without exposing the underlying identifier.

The proxy is the only piece of code allowed to access your Azure credentials. For this workshop, the Function and site run locally, with the Astro development server forwarding `/api` requests to the Function.

> [!IMPORTANT]
> This workshop proxy is for local development only. It must not be deployed as an anonymous public endpoint. A production integration needs an application-specific authentication and abuse-control design, including appropriate rate limits or quotas, CORS restrictions, monitoring, and cost controls.

3. In the same Copilot session, enter:

   ```plaintext
   Add a local Azure Functions proxy in api for the static Astro site to call my deployed Backer Concierge during development. Use my existing local Azure sign-in, keep credentials and Foundry conversation identifiers out of the browser, return an opaque conversation handle, validate requests, sanitize errors, and add focused tests. Configure the Astro development server so /api requests reach the local Function. Don't create public deployment infrastructure.
   ```

4. Review the generated proxy and focused tests for request validation, sanitized errors, opaque conversation handles, and the server-only credential boundary. Ask Copilot to run the focused tests and fix any failures.
5. Open another terminal, start the local Function using the command provided by Copilot, and leave it running.
6. Return to chat and ask Copilot to test the local proxy:

   ```plaintext
   Test the local /api/concierge endpoint by asking "Which games are under $30?" Show me the sanitized response and confirm that no credentials or internal conversation identifiers are returned.
   ```

7. Inspect the response: it should explain that the catalog doesn't contain prices. Confirm it contains no Foundry token, credential, internal conversation identifier, project endpoint, or stack trace. If the Function cannot be reached or the response leaks details or invents prices, send the sanitized failure to Copilot, fix it, and rerun the proxy tests before continuing.

   ![Local proxy test](../../_images/app-8-local-proxy-test.png)

## Build and test the chat widget

With the proxy running, the widget provides the visible conversation on the site without exposing Foundry details.

8. Ask Copilot to create the site integration:

   ```plaintext
   Add an accessible Backer Concierge chat widget to the Astro site. Connect it to /api/concierge, preserve the conversation using the returned opaque handle, follow the existing design guidance, support keyboard use, keep Foundry details out of the browser, and add end-to-end tests covering the chat flow, conversation continuity, accessibility, error handling, and grounding boundaries.
   ```

9. Start the Astro development server in another terminal using the command provided by Copilot. Keep both the site and the local Function running.
10. Ask Copilot to run the end-to-end tests:

    ```plaintext
    Run the end-to-end tests for the Backer Concierge widget in the Tailspin Toys site. Verify its core chat flow, conversation continuity, accessibility, error handling, grounding boundaries, and secure use of the local proxy. Report the results and include evidence for any failures.
    ```

11. Review the report and verify the claimed behavior in the browser, including keyboard use and the two-turn conversation from the [hosted-agent acceptance checks][agent-checks]. Confirm browser requests go through `/api/concierge` with an opaque handle, not directly to Foundry, and responses expose no credentials or internal Foundry identifiers. Check that recommendations and missing-data answers stay within the catalog boundary. Address failing tests with Copilot, restart the affected local service if needed, and rerun the tests.

    ![End-to-end test results for the Backer Concierge widget](../../_images/app-8-e2e-test-results.png)

## Create and merge the pull request

Agent merge wraps up the same issue-linked change after the local integration passes its checks.

12. Review all changed files in the same Tailspin Toys worktree session, including the agent, root `azure.yaml`, local proxy, widget, and tests. Confirm no anonymous public proxy infrastructure was added.
13. Confirm generated environment files, local settings, tokens, and credentials aren't included.
14. Select the dropdown next to **Create PR**, then select **Agent merge**.
15. Select **Agent merge** to create the pull request and monitor its checks. Review and address any reported failures before considering the change complete.

## Checkpoint and next steps

The complete checkpoint combines hosted-agent evidence with a locally verified website integration; it is not a production deployment of the proxy or site.

16. Record the proxy and end-to-end test results and the pull request/check status in the same issue session. Confirm the record identifies the same Tailspin Toys repository, worktree branch, Foundry project, model deployment, and hosted-agent version used throughout the three modules.
17. Follow [Clean up your resources][cleanup] when finished experimenting, including stopping both local services and removing only dedicated workshop Azure resources.
18. Continue to [Review and next steps][core-review] on the existing core workshop route.

[previous-module]: ../2-build-and-deploy/
[project-module]: ../1-project-and-model/
[agent-checks]: ../2-build-and-deploy/#inspect-the-agent-locally
[cleanup]: ../#clean-up-your-resources
[core-review]: ../../9-review/
