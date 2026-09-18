---
title: "Preparar um projeto e um modelo"
description: "Exporte o catálogo da Tailspin e teste um modelo implantado em relação aos critérios de aceitação do Backer Concierge."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← Opcional: Incorporar o Foundry][overview] |
|:--|

Este primeiro módulo prepara os dados e o modelo para o Backer Concierge usando o VS Code e o Microsoft Foundry Toolkit. Trabalhe no seu próprio repositório da Tailspin Toys usado no workshop obrigatório.

## Objetivos

- Exportar o catálogo e identificar os limites das informações disponíveis.
- Preparar um projeto do Foundry e selecionar um modelo de acordo com os critérios de aceitação e a cota.
- Verificar o comportamento de fundamentação no Model Playground antes de escrever o código do agente.

## Cenário

Os apoiadores da Tailspin querem recomendações em que possam confiar. Quem gosta de quebra-cabeças espera títulos reais e avaliações precisas, não totais de financiamento inventados. O assistente precisa respeitar claramente os limites do catálogo e ter o hábito de fazer uma pergunta útil em vez de adivinhar o que um apoiador quer.

## Preparar o espaço de trabalho

O toolkit traz a descoberta de modelos, a implantação, a engenharia de prompts, a avaliação e a implantação de agentes para o VS Code. O acesso ao Azure e uma branch de funcionalidade sem alterações pendentes preparam o trabalho a seguir.

> [!IMPORTANT]
> O Foundry Toolkit e os agentes hospedados estão em versão prévia pública. Este módulo cria recursos do Azure sujeitos a cobrança. Confirme as permissões da assinatura, a região, a cota e o custo estimado antes de aprovar a criação. A [limpeza][cleanup] está disponível mesmo se você parar antes de criar um agente.

1. Confirme o acesso a uma assinatura do Azure. As [contas gratuitas do Azure com US$ 200 em crédito][azure-free] e o [Azure for Students com US$ 100 em créditos][azure-students] são opções, sujeitas aos critérios de elegibilidade e aos limites de serviço.
2. No VS Code, selecione **Extensions** na barra de atividades, pesquise **Foundry Toolkit** e selecione **Install**. O ícone aparecerá na barra de atividades.
3. Selecione o ícone **Azure**, selecione **Sign in to Azure…** e escolha a assinatura para o projeto do Foundry. Com o toolkit autenticado, o Copilot pode usar a [Microsoft Foundry Skill][foundry-skill] para preparar recursos por meio de uma conversa.
4. No espaço de trabalho da Tailspin Toys, abra **Terminal** > **New Terminal** ou pressione <kbd>Control</kbd>+<kbd>\`</kbd> (Mac) ou <kbd>Ctrl</kbd>+<kbd>\`</kbd> (Windows/Linux). Confirme que o trabalho anterior foi registrado em commits e enviado ao repositório remoto e, em seguida, crie a branch de funcionalidade:

   ```bash
   git checkout main
   git pull
   git checkout -b foundry-agent-vscode
   ```

5. Abra uma nova conversa no Copilot Chat no modo **Agent** e peça:

   ```text
   Show me the open issue about a Backer Concierge assistant and summarize its acceptance criteria.
   ```

6. Confirme que o Copilot apresenta **Add a Backer Concierge assistant for catalog questions**. Os critérios de aceitação exigem respostas fundamentadas, nenhum número de financiamento inventado, uma pergunta de esclarecimento e uma interface acessível com cobertura de ponta a ponta.

## Gerar a exportação do catálogo

O script de exportação do catálogo fornece a fonte de dados que fundamenta as respostas do agente.

1. No terminal do repositório da Tailspin Toys, execute as migrações, preencha os dados iniciais e grave `db/catalog.json`:

   ```bash
   npm install
   npm run db:setup
   npm run db:export
   ```

2. Abra `db/catalog.json` e confirme que ele contém vinte e um jogos, cada um com título, descrição, categoria, editora e avaliação em estrelas, além de um campo `note` que descreve as informações ausentes. Totais de financiamento, números de apoiadores, níveis de contribuição e datas de lançamento não estão presentes; o agente deve respeitar esse limite.

## Configurar um projeto do Foundry

O projeto contém o modelo e, posteriormente, o agente hospedado. Ao retomar este módulo, use o mesmo projeto em vez de criar outro.

1. Selecione **Foundry Toolkit** na barra de atividades, expanda **Help and Feedback** e selecione **Ask Copilot**. Confirme o modelo de sua escolha no menu suspenso e envie o prompt `/foundrytk-quick-start` gerado.

   ![Captura de tela mostrando a sequência de início rápido do Foundry Toolkit.](../../../_images/vscode-foundry-setup.png)

2. No fluxo interativo, responda a **Where are you starting from?** com **Set up Foundry** e, em seguida, a **What do you have already?** com **I have an Azure subscription or Foundry resources**.
3. Revise as aprovações de ferramentas. Se os comandos propostos e seu escopo forem adequados, selecione **Allow azmcp …** para esta sessão para reduzir as solicitações repetidas de aprovação.
4. Em **Microsoft Foundry: Create Project**, selecione **Create new resource group** em **Choose a resource group**, insira `rg-tailspin-toys`, escolha uma região que ofereça o modelo pretendido e insira `tailspin-toys` em **Enter project name**. `East US 2` e `Sweden Central` são opções iniciais com ampla disponibilidade de modelos; a disponibilidade atual e a cota determinam a escolha efetiva. Se estiver retomando o trabalho, selecione o projeto existente.
5. Aguarde a notificação de implantação bem-sucedida. No toolkit, expanda **My Resources** e confirme que este projeto é o padrão.

## Descobrir e implantar um modelo

Seguir regras e fundamentar as respostas importa mais aqui do que escolher o maior ou mais recente modelo. A issue fornece critérios concretos para comparar velocidade, fidelidade, disponibilidade regional e cota.

1. No Copilot Chat, selecione **+**, depois **GitHub Issues**, e anexe **Add a Backer Concierge assistant for catalog questions**. Envie:

   ```text
   /microsoft-foundry recommend a model for the agent described in this issue. There's no math or multi-step planning here, so reasoning depth isn't a priority. Prioritize speed instead. Recommend 2-3 candidates available in my Azure region with the trade-offs between them, tell me which you'd pick and why, and check my quota. Avoid deprecated & older models according to the model retirement schedule
   ```

2. Leia as recomendações e escolha o modelo mais adequado aos requisitos e à cota disponível. Peça ao Copilot para implantá-lo:

   ```text
   /microsoft-foundry Deploy the model I selected to the tailspin-toys project and use the model name as the deployment name. Confirm the available quota and capacity with me before creating it.
   ```

3. Confirme o projeto, a implantação, a capacidade e o custo antes de aprovar. Se for adequado após revisar o escopo, selecione **Allow az …** para esta sessão para reduzir as solicitações repetidas.
4. Selecione **Foundry Toolkit**, expanda **My Resources** e selecione **Models**. Confirme que o modelo implantado aparece no Foundry. A captura de tela é um exemplo; sua região pode oferecer um modelo diferente.

   ![Captura de tela mostrando um exemplo de implantação de modelo no Foundry Toolkit.](../../../_images/vscode-model-deployed.png)

## Testar o modelo implantado

O Model Playground não tem o arquivo do catálogo. Um subconjunto reduzido de nove jogos no prompt de sistema é suficiente para testar se o modelo obedece às regras de fundamentação.

1. Em **Models**, selecione o nome do modelo implantado para abrir o **Model Playground** com esse modelo já preenchido. Cole o seguinte prompt de sistema:

   ```text
   You're the Backer Concierge for Tailspin Toys. Only recommend games from this catalog — never invent games, publishers, ratings, or any funding/price/date info. If a request is vague, ask one short question first.

   CATALOG

   | Title | Category | Publisher | Rating |
   | --- | --- | --- | --- |
   | Bug Buster Brainteaser | Puzzle | GitHub Games | 3.0 |
   | Merge Conflict Mystery | Puzzle | DevMasters Inc. | 3.8 |
   | Stack Trace Secrets | Puzzle | Ops Interactive | 3.6 |
   | Deployment Dynasty | Simulation | Ops Interactive | 5.0 |
   | Script Strike | Action | CodeForge Studios | 5.0 |
   | Pipeline Conquest | Strategy | DevMasters Inc. | 3.9 |
   | Repo Rulers | Strategy | Ops Interactive | 4.1 |
   | Server Siege | Strategy | GitHub Games | 3.3 |
   | Code Quest Odyssey | Adventure | CodeForge Studios | 4.8 |
   ```

2. Teste a fundamentação com `I love puzzle games about tracking down bugs. What should I back?` Espere títulos reais da lista com informações corretas.
3. Teste a ausência de dados com `How much has Pipeline Conquest raised so far, and how many backers does it have?` Espere uma recusa clara, pois o catálogo não acompanha financiamento nem apoiadores, seguida das informações que ele de fato contém.
4. Teste outro limite com `I need something for four players, about an hour long.` Espere uma explicação de que o número de jogadores e o tempo de jogo não estão disponíveis, seguida de uma pergunta que ajude a avançar.
5. Teste a pressão por itens fora do catálogo com `Do you have Wingspan? If not, what's the closest thing you've got?` Espere que o modelo não afirme que Wingspan está no catálogo, não o descreva usando conhecimento externo e redirecione a conversa para títulos reais da Tailspin.
6. Teste a falta de especificidade com `Recommend me something good.` Espere uma pergunta curta de esclarecimento e nenhuma recomendação até que a categoria ou o tema sejam conhecidos.
7. Teste a classificação com `What are your three highest rated games?` Espere Deployment Dynasty e Script Strike com 5.0, seguidos de Code Quest Odyssey com 4.8, na ordem correta e com os números corretos.
8. Se alguma verificação falhar, discuta a resposta que falhou e a regra com o Copilot, ajuste a configuração ou a escolha do modelo e repita as verificações antes de continuar.

## Marco de conclusão

Você preparou o espaço de trabalho do VS Code, exportou o catálogo, criou um projeto do Foundry e testou um modelo implantado em relação às regras de fundamentação do Backer Concierge. O marco de conclusão deste módulo é um modelo que recomenda jogos reais do catálogo sem inventar informações ausentes; ainda não há um agente implantado.

Em seguida, você usará o mesmo projeto `tailspin-toys` e a implantação do modelo selecionada para criar e implantar o agente. Se parar aqui, [limpe os recursos do Azure][cleanup] para evitar custos contínuos.

| [Próximo módulo: Criar e implantar um agente →][next-lesson] |
|--:|

[overview]: ../
[next-lesson]: ../2-build-and-deploy/
[cleanup]: ../#limpar-os-recursos
[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[foundry-skill]: https://github.com/microsoft/azure-skills/blob/main/skills/microsoft-foundry/SKILL.md
