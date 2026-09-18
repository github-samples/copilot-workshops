---
title: "Módulo 2 - Crie e implante o agente"
description: "Use o GitHub Copilot CLI e a skill do Microsoft Foundry para gerar a estrutura, testar e implantar o Backer Concierge."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

No [Módulo 1][previous-lesson], você preparou o catálogo e testou um modelo implantado. Este segundo módulo da [série opcional do concierge][overview] transforma essa base em um agente hospedado.

Neste módulo, você vai:

- gerar a estrutura do agente com sua própria cópia do catálogo para implantação.
- testar localmente a fundamentação das respostas e a continuidade da conversa.
- implantar o agente e invocá-lo remotamente.

## Cenário

O Tailspin Toys precisa de mais do que uma resposta isolada de um modelo. Os apoiadores esperam que o concierge se lembre dos jogos que acabou de recomendar e responda a perguntas de acompanhamento sobre eles. A equipe também precisa que essas respostas continuem confiáveis quando o concierge sair da máquina de desenvolvimento para um serviço hospedado.

## Continue com seu projeto

Este módulo dá continuidade ao modelo funcional do Módulo 1. Você manterá o mesmo projeto e a mesma implantação em vez de criar outro conjunto de recursos do Azure.

1. Volte ao repositório do Tailspin Toys na branch `foundry-agent-cli` e à sessão do Copilot CLI do Módulo 1.
2. Confirme que `db/catalog.json` está disponível e que você ainda tem o projeto do Foundry, a implantação do modelo selecionado e a sessão autenticada no Azure usados no teste do modelo. Se ainda não concluiu essa configuração, termine primeiro [Prepare o projeto e o modelo][previous-lesson].

> [!IMPORTANT]
> Os agentes hospedados estão em versão prévia pública e criam recursos do Azure que geram custos. As [instruções de limpeza][cleanup] se aplicam se você parar após este módulo.

## Gere a estrutura do agente Backer Concierge

Agora, você pedirá à skill do Microsoft Foundry para gerar a estrutura do agente hospedado dentro do repositório existente do Tailspin Toys e inspecionará o empacotamento e a configuração antes de executá-lo.

1. Insira o seguinte prompt no Copilot CLI:

    ```text
    Use the Microsoft Foundry Skill to scaffold a hosted Backer Concierge in this existing repository using the project and model deployment we selected. Start from the Python 3.13 Basic hosted-agent sample, use Microsoft Agent Framework with the Responses API and code deployment, and keep the agent in agent/backer-concierge. Keep one azure.yaml at the repository root with a service using host: azure.ai.agent.

    Ground every answer in db/catalog.json. Never invent games, publishers, ratings, funding totals, backer counts, pledge tiers, prices, player counts, play times, or release dates. Ask one short clarifying question when a request is vague and preserve conversation context. Ensure the catalog is copied into the deployable service during preparation so the deployed agent never depends on a file outside its service directory. Add focused tests for catalog loading and grounding behavior.

    Scaffold and test locally, but do not deploy the hosted agent yet. Stop and ask me to authenticate if needed.
    ```

2. Acompanhe a sessão para responder a perguntas sobre o projeto do Foundry, a implantação do modelo, o nome do agente ou o ambiente.
3. Quando o Copilot terminar, inspecione as alterações:

    ```text
    /diff
    ```

    Confirme que:

    - `azure.yaml` contém um serviço com `host: azure.ai.agent`.
    - o serviço aponta para `agent/backer-concierge`.
    - o pacote do serviço implantado inclui sua própria cópia gerada do catálogo.
    - um script ou uma etapa de build atualiza essa cópia a partir de `db/catalog.json`, em vez de manter dois catálogos editados manualmente.
    - o agente usa a implantação do modelo selecionado e a Responses API.
    - as instruções rejeitam explicitamente fatos ausentes do catálogo.
    - nenhuma credencial, token de acesso, arquivo `.env` ou arquivo de ambiente `.azure` está preparado para commit.

    Use a seguinte estrutura como referência para verificar o resultado após a geração:

    ```text
    tailspin-toys/
    ├── azure.yaml
    ├── agent/
    │   └── backer-concierge/
    │       ├── catalog.json
    │       └── requirements.txt
    ├── db/
    │   └── catalog.json
    └── src/
    ```

> [!IMPORTANT]
> `azd deploy` empacota o diretório do serviço do agente hospedado. Uma referência em tempo de execução de `agent/backer-concierge` ao arquivo `db/catalog.json` na raiz do repositório pode funcionar localmente e falhar após a implantação. A cópia gerada deve estar disponível no diretório `agent/backer-concierge/` antes da implantação.

4. Peça ao Copilot para executar os testes específicos e inspecionar a configuração gerada antes de iniciar o serviço:

    ```text
    Run the focused Backer Concierge tests. Then verify that the selected model deployment, Responses API protocol, service path, startup command, catalog preparation step, and azure.ai.agent host configuration are consistent. Fix only problems in this hosted-agent project and rerun the failed checks.
    ```

    Não continue até que os testes específicos sejam aprovados.

    ![Verificação da estrutura gerada do agente](../../../_images/cli-8-verify-generated-agent.png)

## Teste o agente localmente

Agora, você verificará a fundamentação das respostas e o comportamento de conversação do agente por meio da Responses API local. O serviço local do agente ocupa seu terminal enquanto está em execução, portanto, mantenha o Copilot CLI aberto no terminal atual e inicie o agente em um segundo terminal.

1. Abra outro terminal usando <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
2. Na raiz do repositório do Tailspin Toys, execute:

    ```bash
    azd ai agent run
    ```

    A primeira execução local cria um ambiente Python, instala dependências e inicia o agente hospedado. Deixe esse terminal em execução.

3. Volte ao Copilot CLI no primeiro terminal e insira:

    ```text
    Test the running Backer Concierge through its Responses API. Run each acceptance prompt below, preserve the response ID for the two-turn conversation test, and compare every response with the expected behavior. Show a concise pass or fail table and the evidence for any failure. Do not change code yet.

    1. "I love puzzle games about tracking down bugs. What should I back?" Expected: only real catalog titles with correct details.
    2. "How much has Pipeline Conquest raised so far, and how many backers does it have?" Expected: explains that the catalog doesn't track funding or backers, then offers known information.
    3. "I need something for four players, about an hour long." Expected: explains that player count and play time are missing, then asks one actionable follow-up question.
    4. "Do you have Wingspan? If not, what's the closest thing you've got?" Expected: says Wingspan isn't in the catalog, doesn't describe it from outside knowledge, and pivots to catalog titles.
    5. "Recommend me something good." Expected: asks one short clarifying question and doesn't recommend a title yet.
    6. "What are your three highest rated games?" Expected: the three highest-rated catalog entries in the correct order with correct ratings.
    7. In one conversation, send "Show me two highly rated strategy games." followed by "Which of those has the higher rating?" Expected: the second response compares only the two earlier titles using catalog ratings.
    ```

    ![Testes da implantação do agente hospedado aprovados](../../../_images/cli-8-passing-acceptance-scenarios.png)

4. Revise os resultados. Se o agente não conseguir se conectar, confirme que o segundo terminal ainda está executando o serviço. Se um teste falhar, peça ao Copilot para corrigir apenas o defeito local, executar os testes específicos e informar quando reiniciar `azd ai agent run`. Reinicie o serviço e execute novamente o teste de aceitação que falhou após cada alteração.

## Implante o agente hospedado

Com os testes de aceitação locais aprovados, você está pronto para implantar o agente no Microsoft Foundry. Você usará o mesmo fluxo orientado pela skill para verificar se tudo está pronto para a implantação e testar o endpoint remoto.

1. Pare o serviço local com <kbd>Ctrl</kbd>+<kbd>C</kbd> depois que todos os testes de aceitação forem aprovados.
2. Volte ao Copilot CLI e insira o seguinte prompt. Revise os recursos propostos e o custo estimado antes de aprovar a implantação:

    ```text
    Continue with the Microsoft Foundry Skill workflow. Review the hosted agent for deployment readiness, then deploy it to Microsoft Foundry, show the deployment status and playground link, and invoke it remotely with: "I love puzzle games about tracking down bugs. What should I back?"
    ```

3. Se for solicitado que você selecione uma fonte para a suíte de avaliação, escolha **Não, configurar mais tarde**.

    ![Status da implantação do agente hospedado e link do playground](../../../_images/cli-8-hosted-agent-deployment.png)

4. Revise o status da implantação e a resposta remota. Confirme que o agente está em execução e recomenda apenas jogos reais do catálogo. Se a implantação ou a invocação falhar, peça ao Copilot para diagnosticar a falha e repetir o teste remoto antes de continuar.

O link do playground exibido permite interagir com o agente hospedado implantado no portal do Microsoft Foundry.

O fluxo orientado pela skill usa `azd deploy` para empacotar o código-fonte do serviço, resolver dependências, compilá-lo remotamente e publicá-lo no Microsoft Foundry. Ele usa o fluxo de invocação do Foundry para testar o endpoint implantado.

## Resumo e próximos passos

Você gerou a estrutura de um agente com uma cópia do catálogo para implantação, testou a fundamentação das respostas e a continuidade da conversa e verificou uma resposta remota do Microsoft Foundry. Agora, você tem um Backer Concierge hospedado e funcional.

A seguir, você manterá o mesmo repositório, a branch, a sessão do Copilot CLI e o agente implantado para [conectar o concierge ao site][next-lesson]. Se um agente hospedado for suficiente para sua exploração, você pode parar por aqui e [limpar seus recursos do Azure][cleanup].

[overview]: ../
[previous-lesson]: ../1-project-and-model/
[next-lesson]: ../3-connect-to-site/
[cleanup]: ../#limpe-seus-recursos
