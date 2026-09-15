---
title: "Lição 7 - Criar e usar um agente de QA"
description: "Crie um perfil de QA que parta dos requisitos e combine cobertura de testes, a skill quality-checks e evidências diretas do navegador."
authors:
  - geektrainer
lastUpdated: 2026-09-14
---

Nas lições anteriores, você criou uma skill quality-checks e deu ao Copilot acesso a um navegador pelo MCP do Playwright. Agora reúna essas capacidades com um **agente personalizado de QA** que revise o recurso de filtragem em relação aos requisitos.

Nesta lição, você vai:

- entender como um agente personalizado trabalha com instruções, skills e ferramentas MCP.
- criar e examinar um perfil de QA reutilizável.
- selecionar o agente de QA e revisar suas conclusões em relação à issue de filtragem.
- salvar o perfil e quaisquer testes justificados para o PR do recurso.

## Cenário

A Tailspin Toys está se preparando para lançar a filtragem por categoria e editora. As verificações automatizadas e a exploração no navegador forneceram evidências úteis à equipe, mas passar nos testes não demonstra, por si só, que todos os requisitos acordados estão cobertos. Antes de abrir o PR, a equipe quer uma revisão focada do que foi solicitado, do que foi implementado e do que ainda precisa de atenção.

Você criará um agente de QA que parte da issue e das decisões de planejamento aprovadas, examina a cobertura e usa a skill e as ferramentas do navegador para reunir evidências. Seu papel é identificar lacunas e explicar se o recurso está pronto para revisão, não aprovar o próprio trabalho nem integrar o PR.

## O que é um agente personalizado?

Um agente personalizado é um papel especializado reutilizável definido em um perfil Markdown. Suas instruções orientam como o Copilot aborda uma tarefa; selecionar o perfil aplica esse papel à conversa. Neste workshop, você definirá o papel em `.github/agents/qa.agent.md` e o selecionará no aplicativo.

As personalizações que você criou têm funções distintas. As instruções do repositório descrevem os padrões da equipe. A skill quality-checks reúne verificações repetíveis. O MCP do Playwright fornece ferramentas de navegador. O perfil de QA informa ao Copilot como usar essas capacidades para avaliar requisitos e relatar conclusões. Ele não as substitui nem exige outra sessão de agente.

## Criar o perfil de QA

Continue na sessão de filtragem da Lição 6, mantendo o mesmo worktree e branch. Confirme que a sessão está no modo **Interactive**, que a skill quality-checks está presente e que o MCP do Playwright está disponível. O PR do recurso vem na Lição 8; esta lição adiciona um perfil e, apenas quando necessário, testes.

Envie o prompt a seguir ao agente padrão do Copilot. Você examinará o arquivo resultante antes de selecionar QA:

```plaintext
Crie um agente personalizado de QA reutilizável em .github/agents/qa.agent.md. Primeiro examine as instruções do repositório, package.json, a configuração de testes e .github/skills/quality-checks/SKILL.md. Forneça ao perfil um frontmatter YAML válido com name definido como QA e uma description que explique quando usá-lo. Não fixe um modelo nem adicione uma lista tools; herde as ferramentas e permissões disponíveis no ambiente. Crie apenas a definição do agente e pare para que eu possa examiná-la antes de executá-lo.

Nas instruções do agente, exija que toda tarefa de QA comece pela issue e por quaisquer critérios de aceitação aprovados fornecidos pelo usuário. Trate esses requisitos como fonte de verdade, não a implementação. Pergunte quando faltarem requisitos ou eles forem ambíguos. Examine o recurso e os testes existentes e mapeie cada critério à cobertura automatizada adequada e ao comportamento observável.

Exija validação direta no navegador pelo servidor MCP do Playwright configurado e execução de lint, testes de unidade, testes de ponta a ponta e verificações de tipos pela skill quality-checks existente e seus scripts incluídos. Leia a skill explicitamente se ela não tiver sido descoberta automaticamente. Relate skills, ferramentas MCP, pré-requisitos ou acesso ausentes como bloqueios; não substitua silenciosamente o fluxo por outro nem rotule verificações ignoradas como aprovadas. Identifique a cópia de trabalho e o servidor em teste, evite reutilizar o servidor de outro worktree, pare apenas os servidores iniciados pelo agente e pergunte antes de qualquer instalação ou de parar outro processo.

Permita que o agente de QA adicione os menores testes necessários para lacunas reais de cobertura, seguindo as instruções do repositório; não adicionar testes é válido quando a cobertura já é adequada. Não enfraqueça asserções, não desative testes com falha, não altere critérios de aceitação para corresponder ao código nem modifique código da aplicação sem minha aprovação. Após alterações, execute novamente as verificações afetadas e conclua a verificação final da revisão resultante. Exija um relatório conciso que mapeie critérios a evidências e ao status aprovado/reprovado/bloqueado, liste os testes adicionados ou explique por que nenhum foi necessário, relate os resultados das quatro verificações e identifique defeitos não resolvidos. GO exige todas as verificações e evidências obrigatórias; caso contrário, relate NO-GO e o motivo. Não mude de branch, não faça commit, push, não abra ou integre PRs nem crie agentes ou skills adicionais durante QA.
```

## Examinar o perfil

1. Abra **Changes** e selecione `.github/agents/qa.agent.md`. Você também pode encontrá-lo no painel de revisão de arquivos.
2. Leia o frontmatter. `description` é obrigatório, e `name: QA` torna o perfil reconhecível no seletor. Deixe `model` e `tools` sem especificar neste exercício para usar o modelo selecionado e as ferramentas disponíveis; as permissões normais continuam valendo.
3. Leia as instruções como uma lista de revisão: elas partem dos requisitos, usam a skill e as ferramentas do navegador, adicionam testes apenas para lacunas reais e distinguem falhas de verificações bloqueadas?
4. Peça ao Copilot que corrija as lacunas antes de selecionar o perfil. Confirme que ele criou a definição sem iniciar QA nem alterar a aplicação.

> [!NOTE]
> Um perfil especializado orienta o comportamento; ele não garante um resultado correto. Você ainda precisa examinar a atividade das ferramentas, as alterações nos testes e o relatório do agente.

## Executar QA em relação à issue

O prompt de execução é para o agente personalizado **QA** selecionado, não para o agente padrão lendo um perfil. Mantenha a mesma cópia de trabalho e branch de filtragem.

1. Na sessão atual, abra o seletor de agentes na caixa do prompt ou digite `/agent`, conforme a [documentação de personalização do aplicativo][customize-app].
2. Selecione **QA** e verifique se o aplicativo identifica visivelmente **QA** como agente ativo antes de enviar o prompt de execução.
3. Se **QA** não estiver listado ou você não conseguir confirmar que está ativo, pause e peça ajuda à pessoa que conduz o workshop, mantendo este worktree e branch. Não crie outra sessão de recurso, não invente uma sequência de recarga nem substitua esta etapa por um pedido ao agente padrão para ler `qa.agent.md`.

O seletor documentado está disponível durante uma sessão, mas a descoberta de um perfil de repositório recém-criado pode depender da versão do aplicativo. Não trate a criação do arquivo como prova de ativação.

Substitua os dois marcadores pela URL real da issue de filtragem e os esclarecimentos aprovados na Lição 4, ou por `none` quando a issue estiver completa. Não dependa da memória do agente anterior.

```plaintext
Verifique o recurso de filtragem em relação a esta issue: <filtering-issue-URL>. Estes são os critérios de aceitação adicionais que aprovei durante o planejamento: <cole os esclarecimentos acordados ou escreva none>.

Valide o comportamento com o servidor MCP do Playwright, examine a cobertura de testes, adicione testes apenas para lacunas de cobertura e execute a validação pela skill quality-checks. Relate evidências, resultados das verificações e bloqueios. Não altere código da aplicação sem minha aprovação, não crie um commit nem abra um pull request.
```

## Revisar as evidências

Leia o relatório junto com a issue de filtragem e os esclarecimentos aprovados:

1. Verifique se cada critério está conectado a testes adequados e comportamento observável. Por exemplo, combinar categorias e uma editora exige evidências sobre os jogos retornados, não apenas sobre a resposta dos controles.
2. Examine a atividade real das ferramentas MCP do Playwright e confirme que o servidor testado pertence a esta cópia de trabalho. As verificações no navegador e E2E automatizadas não devem reutilizar um servidor desatualizado ou outra cópia de trabalho.
3. Revise os resultados de lint, testes de unidade, testes E2E e verificações de tipos. As quatro verificações devem usar os scripts da skill quality-checks; um resumo de comandos planejados não é execução.
4. Abra **Changes** para examinar os testes adicionados e compará-los com as lacunas do relatório.

Revise os testes adicionados: eles devem cobrir lacunas reais sem enfraquecer asserções. Não adicionar testes é correto quando a cobertura é adequada. Um parecer **NO-GO** por bloqueio ou falha é um resultado válido, não permissão para ignorar evidências.

Se QA identificar um defeito na aplicação, aprove separadamente uma correção específica e execute novamente as verificações e observações no navegador afetadas na revisão resultante. Pré-requisitos ou ferramentas ausentes precisam de uma resolução explícita. Não trate evidências antigas como prova de código alterado.

## Salvar um checkpoint

O papel de QA é verificar, então volte ao agente padrão antes de solicitar um commit:

1. Mantenha o relatório de QA, a URL da issue, os esclarecimentos aprovados e a revisão testada disponíveis para a lição sobre o PR.
2. Na mesma sessão, use o seletor de agentes para voltar ao agente padrão do Copilot e confirme que **QA** não está mais selecionado.
3. Mantenha o mesmo worktree e branch. Se não encontrar a opção do agente padrão, peça ajuda à pessoa que conduz o workshop em vez de iniciar outra sessão de recurso ou enviar instruções de commit ao QA.

Após revisar o perfil, quaisquer alterações de testes e as evidências resultantes, envie a solicitação de checkpoint ao agente padrão com esse contexto de QA:

```plaintext
Revise o diff atual e crie um commit de checkpoint para a definição do agente de QA e quaisquer alterações de testes aprovadas. Permaneça na branch de filtragem existente. Não faça push nem abra um pull request.
```

## Resumo e próximos passos

Você adicionou um papel especializado reutilizável ao fluxo de trabalho e revisou o trabalho dele. Nesta lição, você:

- criou e examinou um perfil de QA que parte dos requisitos.
- selecionou o perfil para avaliar a cobertura e reunir evidências pela skill e pelo MCP do Playwright.
- revisou as conclusões e salvou o perfil com quaisquer alterações justificadas nos testes na branch de filtragem.

Agora você tem os elementos para revisar o recurso: a implementação, a skill, o perfil de QA, os testes e o relatório de verificação. Leve adiante os achados não resolvidos; um resultado com falha ou bloqueado não autoriza a integração. Continue na [Lição 8 - Criar e integrar o PR do recurso][next-lesson] para revisar o marco completo e usar Agent Merge.

## Recursos

- [Personalização do aplicativo GitHub Copilot, incluindo a seleção de agentes personalizados][customize-app]

[previous-lesson]: ../6-mcp-playwright/
[next-lesson]: ../8-create-pull-request/
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
