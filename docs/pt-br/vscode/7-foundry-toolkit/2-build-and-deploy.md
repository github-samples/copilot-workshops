---
title: "Criar e implantar um agente"
description: "Gere a estrutura inicial e depure o Backer Concierge no VS Code; depois, implante e teste-o como agente hospedado do Foundry."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← Módulo anterior: Preparar um projeto e um modelo][previous-lesson] |
|:--|

Este módulo usa o catálogo e o modelo testado de [Preparar um projeto e um modelo][previous-lesson]. O Microsoft Foundry Toolkit e seu agente personalizado **AIAgentExpert** orientam a criação local e a implantação hospedada no VS Code.

## Objetivos

- Gerar a estrutura inicial de um agente fundamentado no catálogo no espaço de trabalho existente da Tailspin Toys.
- Depurar o comportamento local com o Agent Inspector.
- Implantar no projeto existente do Foundry e verificar o agente hospedado.

## Cenário

Uma recomendação confiável precisa resistir a mais de uma conversa. A Tailspin Toys precisa que o assistente mantenha os limites do catálogo quando os apoiadores fazem perguntas vagas ou insistem em detalhes de financiamento indisponíveis. Um assistente hospedado deve se comportar com a mesma confiabilidade de um testado em um ambiente privado.

## Retomar o espaço de trabalho

O agente usa a implantação de modelo existente; não há um novo projeto do Foundry a criar.

1. Abra o mesmo repositório da Tailspin Toys no VS Code em `foundry-agent-vscode`. Confirme que `db/catalog.json` existe e que o projeto `tailspin-toys` e a implantação do modelo testado estão visíveis em **Foundry Toolkit** > **My Resources**.
2. Confirme que o [marco de conclusão anterior][previous-lesson] foi atingido. Se os recursos foram removidos, conclua novamente a preparação do projeto e do modelo antes de prosseguir.
3. Instale a Azure Developer CLI (`azd`) se ela ainda não estiver disponível. A implantação de agentes hospedados usa essa ferramenta; escolha apenas o comando para o seu sistema operacional:

   ```bash
   # macOS / Linux
   curl -fsSL https://aka.ms/install-azd.sh | bash

   # Windows (PowerShell)
   winget install microsoft.azd
   ```

4. Faça login na assinatura usada pelo projeto existente:

   ```bash
   azd auth login
   ```

> [!IMPORTANT]
> Os agentes hospedados e o Foundry Toolkit estão em versão prévia pública. A implantação cria recursos sujeitos a cobrança. Confirme a assinatura, as permissões, a região, a cota e o custo estimado antes de aprovar comandos.

## Criar e depurar o agente

O toolkit gera a estrutura inicial do código no repositório atual e abre uma conversa especializada no Copilot Chat. O Agent Inspector torna visíveis as solicitações locais, os eventos e as chamadas de ferramentas antes da implantação.

1. Selecione **Foundry Toolkit**, expanda **Developer Tools**, expanda **+ Build** e selecione **+ Create Agent**. Em **Create Agent**, selecione **Code an agent with Copilot**.

   ![Captura de tela mostrando a página de criação de agente.](../../../_images/vscode-create-agent.png)

2. Na nova conversa, confirme que ela muda para **AIAgentExpert**. Substitua o prompt gerado pelo prompt personalizado e envie-o:

   ```text
   /foundrytk-quick-start Create a backer concierge AI agent called 'Backer Concierge'. The agent should use the model I deployed to answer catalog questions and recommend games grounded strictly in db/catalog.json. Review the acceptance criteria in the issue titled 'Add a Backer Concierge assistant for catalog questions' and ensure the agent meets them. Generate the code into agent/backer-concierge in the current workspace and ask me if anything is unclear.
   ```

3. Revise o código gerado em `agent/backer-concierge`. Confirme que o catálogo está incluído no agente a ser implantado, que os testes específicos passam e que nenhuma credencial ou arquivo de ambiente local será incluído nos commits.
4. Selecione **Run and Debug** na barra de atividades e inicie o depurador com <kbd>F5</kbd>. Confirme que o **Agent Inspector** carrega e se conecta ao servidor do agente.
5. Reutilize os seis prompts de [Testar o modelo implantado][model-tests]. Verifique as respostas em relação ao `db/catalog.json` completo, em vez de presumir que a classificação do subconjunto de nove jogos corresponde à classificação do catálogo completo.
6. Alterne entre **Input & Output**, **Events** e **Tools** para inspecionar os dados das solicitações e respostas, os eventos da sessão e as chamadas de ferramentas. Se o comportamento violar os critérios de aceitação, peça ao Copilot para corrigi-lo e execute novamente os testes específicos e as verificações do Inspector antes de implantar.

   ![Captura de tela mostrando o fluxo de depuração local do agente.](../../../_images/vscode-agent-debug.png)

## Implantar e testar o agente hospedado

A transferência **Go production** empacota o agente existente para o Foundry. Ela não transforma o futuro proxy do site em um serviço público pronto para produção.

1. Na conversa de criação de agente do Copilot Chat, selecione **Go production**, substitua o prompt padrão pelo seguinte e envie-o:

   ```text
   /foundrytk-quick-start Review this agent for deployment readiness, run its tests, then deploy it to my existing tailspin-toys Foundry project. Show me the deployment status and test the deployed agent.
   ```

   ![Captura de tela mostrando as opções de transferência do agente AIAgentExpert.](../../../_images/vscode-go-production-handoff.png)

2. Revise a conversa e o terminal para conferir os parâmetros e as aprovações de comandos. Confirme que a implantação tem como destino o projeto `tailspin-toys` existente e revise os recursos sujeitos a cobrança antes de aprovar.
3. Se o Copilot oferecer uma suíte de avaliação, você pode aceitá-la e executá-la como verificação adicional.
4. Selecione **Foundry Toolkit**, expanda **My Resources** e selecione **Agents**. Na guia **Agents**, mude para **Hosted Agent**.

   ![Captura de tela mostrando o agente hospedado implantado.](../../../_images/vscode-agent-deployed.png)

5. Selecione o nome do agente e confirme que o status da implantação é **Running**. Mude para **Playground** e repita as verificações de fundamentação, dados ausentes, itens fora do catálogo, falta de especificidade e classificação em relação ao catálogo implantado.

   ![Captura de tela mostrando uma resposta do agente hospedado implantado.](../../../_images/vscode-agent-response.png)

6. Se a implantação ou as respostas falharem, inspecione o status informado e os logs com o Copilot, corrija a falha no projeto existente e repita as verificações. Não prossiga com uma implantação não verificada.

## Marco de conclusão

Você criou a estrutura inicial do Backer Concierge, depurou sua fundamentação no catálogo com o Agent Inspector, implantou o agente no Foundry pelo repasse **Go production** e testou novamente a versão hospedada no Playground. O marco de conclusão deste módulo é um agente hospedado em execução que respeita o catálogo sem inventar informações ausentes.

Em seguida, você usará o mesmo projeto `tailspin-toys`, a implantação do modelo e o agente hospedado para conectar o agente ao site. Se parar aqui, [limpe os recursos do Azure][cleanup] para evitar custos contínuos.

| [Próximo módulo: Conectar o agente ao site →][next-lesson] |
|--:|

[previous-lesson]: ../1-project-and-model/
[model-tests]: ../1-project-and-model/#testar-o-modelo-implantado
[next-lesson]: ../3-connect-to-site/
[cleanup]: ../#limpar-os-recursos
