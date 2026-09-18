---
title: "Módulo 3 - Conecte o agente ao site"
description: "Conecte o Backer Concierge hospedado ao Tailspin Toys por meio de um proxy local do Azure Functions e um widget de chat acessível."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
next: false
---

No [Módulo 2][previous-lesson], você implantou e testou o Backer Concierge. Este último módulo da [série opcional do concierge][overview] disponibiliza esse agente no site local do Tailspin Toys.

Neste módulo, você vai:

- criar um proxy local do Azure Functions que mantém as credenciais do Foundry no servidor.
- adicionar um widget de chat acessível ao site.
- verificar o fluxo completo da conversa e limpar seus recursos.

## Cenário

Os apoiadores descobrem jogos no site do Tailspin Toys, não no terminal de desenvolvimento ou em um portal do Azure. A equipe quer disponibilizar o concierge junto ao catálogo, com uma experiência de chat que permita perguntas de acompanhamento e proteja as credenciais do serviço.

## Continue com seu agente hospedado

A integração com o site precisa do agente implantado no Módulo 2. Você manterá esse agente em execução no Foundry enquanto o proxy e o site são executados localmente.

1. Volte ao repositório do Tailspin Toys na branch `foundry-agent-cli` e à sessão existente do Copilot CLI.
2. Confirme que o Backer Concierge está implantado e que a invocação remota de [Crie e implante o agente][previous-lesson] foi bem-sucedida. Se você já removeu os recursos do Azure, recrie-os seguindo os módulos anteriores antes de continuar.

> [!IMPORTANT]
> O proxy e o site deste módulo são executados localmente; esta não é uma implantação do site em produção. O modelo e o agente hospedado continuam sendo recursos do Azure que geram custos até que você conclua a [limpeza][cleanup].

## Crie o proxy do lado do servidor

O Tailspin Toys é totalmente pré-renderizado. O código do navegador nunca deve chamar o agente hospedado diretamente nem receber credenciais do Foundry. Você adicionará uma **barreira de proteção de credenciais do lado do servidor** com o Azure Functions local, que se autentica no Foundry e retorna ao navegador apenas a resposta do agente.

A skill `microsoft-foundry` é responsável pelo fluxo de trabalho do agente hospedado, enquanto as skills mais abrangentes do Azure no mesmo plugin podem preparar o projeto local da Function. Você usará essas skills para criar o proxy e verificará se ele acessa o agente sem expor credenciais.

1. No Copilot CLI, insira:

    ```text
    Use the Azure skills to add an Azure Functions v4 Node.js and TypeScript project in api with one POST /api/concierge endpoint that invokes my deployed Backer Concierge hosted agent. This Function will run locally only; don't add it to azure.yaml or create Azure deployment infrastructure. Use DefaultAzureCredential with my local Azure sign-in. Keep the HTTP trigger thin, isolate the Foundry client in a unit-testable module, validate and limit request bodies, set explicit timeouts, and return sanitized errors. Store the Foundry project endpoint and agent name in local server-side settings that are excluded from version control. Never return credentials or access tokens to the browser. The Astro site is `output: 'static'` with no dev proxy, so also add a local-only Vite dev-server proxy for /api to the Function's port in astro.config.mjs, so relative /api/concierge requests reach it during `astro dev`.

    For conversation state, generate a high-entropy handle on the server, map it to the Foundry conversation server-side with an expiration, and never expose a raw Foundry conversation or thread identifier. Reject malformed, expired, and unknown handles. Add focused unit tests.
    ```

    ![Configuração do proxy local do Azure Functions](../../../_images/cli-8-azure-functions-proxy.png)

2. Abra outro terminal e inicie a Function local usando o comando fornecido pelo Copilot. Deixe a Function em execução.
3. Volte ao Copilot CLI e peça ao Copilot para testar o proxy local:

    ```text
    Send a request to the local /api/concierge endpoint asking "Which games are under $30?" and show me the sanitized JSON response. Confirm that the request reaches the deployed Backer Concierge through DefaultAzureCredential.
    ```

4. Inspecione a resposta. Ela deve explicar que o catálogo não contém preços. Não pode conter um token do Foundry, uma credencial, um endpoint de projeto, um identificador bruto de conversa do Foundry ou um rastreamento de pilha.

    ![Resposta JSON sanitizada do endpoint local do concierge](../../../_images/cli-8-sanitized-json-response.png)

## Crie o widget de chat

O proxy oferece ao navegador uma forma segura de acessar o concierge. Agora, você adicionará um widget de chat ao site e usará o Playwright para verificar o fluxo completo da conversa.

1. Peça ao Copilot para criar a integração com o site:

    ```text
    Add an accessible Backer Concierge chat widget as an Astro component and render it site-wide from Layout.astro. It should POST to /api/concierge and thread the conversation using the returned opaque conversation handle, follow the dark theme in style.instructions.md, support Escape to close, and include data-testid attributes.
    ```

2. Mantenha a Function local em execução e inicie o site Astro em outro terminal usando o comando fornecido pelo Copilot.
3. Volte ao Copilot CLI. O servidor MCP do Playwright que você adicionou na [Lição 4][playwright-lesson] já está disponível. Peça ao Copilot para testar o widget:

    ```text
    Use the Playwright MCP server to test the Backer Concierge widget end to end in the running Tailspin Toys site. Verify its core chat flow, conversation continuity, accessibility, error handling, grounding boundaries, and secure use of the local proxy. Report the results and include evidence for any failures.
    ```

    ![Captura de tela do widget Backer Concierge no site do Tailspin Toys](../../../_images/cli-8-backer-concierge-widget.png)

4. Revise os resultados com base nas evidências apresentadas. Se alguma verificação falhar, peça ao Copilot para corrigir o comportamento correspondente do proxy ou do widget e executar novamente as verificações que falharam antes de concluir.

## Limpe seus recursos

Você chegou ao resultado final: um concierge funcional no site local. As instruções de limpeza compartilhadas cobrem tanto os serviços locais quanto os recursos do Azure criados ao longo da série.

1. Conclua [Limpe seus recursos][cleanup], incluindo parar os serviços locais e verificar se a exclusão dos recursos do Azure foi concluída.

## Resumo e próximos passos

Você conectou o Backer Concierge hospedado ao Tailspin Toys por meio de um proxy local do lado do servidor e um widget de chat acessível. Ao longo da série, usou o GitHub Copilot CLI e o Foundry para preparar um modelo, criar e implantar um agente e verificar uma integração completa com o site.

Continue em [Revisão e próximos passos][review] para encerrar o workshop da CLI.

[overview]: ../
[previous-lesson]: ../2-build-and-deploy/
[review]: ../../9-review/
[playwright-lesson]: ../../4-mcp/
[cleanup]: ../#limpe-seus-recursos
