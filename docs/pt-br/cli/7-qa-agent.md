---
title: "Lição 7 - Criar e usar um agente de QA"
description: "Crie um perfil de QA que parta dos requisitos e combine cobertura de testes, a skill quality-checks e evidências diretas do navegador."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Você executou verificações repetíveis e explorou a filtragem pelo MCP do Playwright. Agora crie um **agente personalizado de QA** para reunir os requisitos, a cobertura e as evidências do navegador. Mantenha a sessão, a cópia de trabalho e a branch de filtragem; o PR do recurso vem na Lição 8.

## Criar o perfil de QA

Permaneça no modo **Interactive**. Um perfil define o papel e as instruções de um especialista; uma skill reúne instruções de tarefas reutilizáveis, scripts e recursos. O agente de QA usará sua skill e as ferramentas MCP configuradas em vez de substituí-las.

Envie este prompt e examine a definição antes de executá-la:

```plaintext
Crie um agente personalizado de QA reutilizável em .github/agents/qa.agent.md. Primeiro examine as instruções do repositório, package.json, a configuração de testes e .github/skills/quality-checks/SKILL.md. Forneça ao perfil um frontmatter YAML válido com name definido como QA e uma description que explique quando usá-lo. Não fixe um modelo nem adicione uma lista tools; herde as ferramentas e permissões disponíveis no ambiente. Crie apenas a definição do agente e pare para que eu possa examiná-la antes de executá-lo.

Nas instruções do agente, exija que toda tarefa de QA comece pela issue e por quaisquer critérios de aceitação aprovados fornecidos pelo usuário. Trate esses requisitos como fonte de verdade, não a implementação. Pergunte quando faltarem requisitos ou eles forem ambíguos. Examine o recurso e os testes existentes e mapeie cada critério à cobertura automatizada adequada e ao comportamento observável.

Exija validação direta no navegador pelo servidor MCP do Playwright configurado e execução de lint, testes de unidade, testes de ponta a ponta e verificações de tipos pela skill quality-checks existente e seus scripts incluídos. Leia a skill explicitamente se ela não tiver sido descoberta automaticamente. Relate skills, ferramentas MCP, pré-requisitos ou acesso ausentes como bloqueios; não substitua silenciosamente o fluxo por outro nem rotule verificações ignoradas como aprovadas. Identifique a cópia de trabalho e o servidor em teste, evite reutilizar o servidor de outro worktree, pare apenas os servidores iniciados pelo agente e pergunte antes de qualquer instalação ou de parar outro processo.

Permita que o agente de QA adicione os menores testes necessários para lacunas reais de cobertura, seguindo as instruções do repositório; não adicionar testes é válido quando a cobertura já é adequada. Não enfraqueça asserções, não desative testes com falha, não altere critérios de aceitação para corresponder ao código nem modifique código da aplicação sem minha aprovação. Após alterações, execute novamente as verificações afetadas e conclua a verificação final da revisão resultante. Exija um relatório conciso que mapeie critérios a evidências e ao status aprovado/reprovado/bloqueado, liste os testes adicionados ou explique por que nenhum foi necessário, relate os resultados das quatro verificações e identifique defeitos não resolvidos. GO exige todas as verificações e evidências obrigatórias; caso contrário, relate NO-GO e o motivo. Não mude de branch, não faça commit, push, não abra ou integre PRs nem crie agentes ou skills adicionais durante QA.
```

## Examinar o perfil

Abra `.github/agents/qa.agent.md` no editor e examine o diff. `description` é obrigatório; esta lição também fornece `QA` como `name` legível. Confirme que não há um `model` fixado nem uma lista de ferramentas inventada. Omitir `tools` herda as ferramentas disponíveis; não contorna as permissões do ambiente. Perfis de produção podem restringir ferramentas deliberadamente.

Confirme que as instruções começam pelos requisitos, exigem atividade real no navegador via MCP e scripts da skill, permitem apenas adições justificadas de testes e relatam bloqueios com veracidade. Nem um perfil especializado nem uma skill exige uma janela de contexto separada ou a orquestração de outros agentes.

## Executar QA em relação à issue

O prompt de execução é para o agente personalizado **QA** selecionado, não para o agente padrão lendo um perfil. Inicie uma conversa nova da CLI na mesma cópia de trabalho para carregar o novo perfil sem criar outra branch de recurso.

1. Preserve a URL da issue de filtragem e os esclarecimentos aprovados. Aguarde o agente atual terminar e digite `/exit` para voltar ao terminal.
2. Confirme que você ainda está no diretório do repositório de filtragem e na mesma branch com `git branch --show-current` e `git status --short`. Não mude de branch nem crie um worktree.
3. Inicie a CLI com o perfil do repositório:

   ```shell
   copilot --agent qa
   ```

4. Verifique se a CLI identifica **QA** como agente selecionado antes de executá-lo. A [referência de comandos da CLI][cli-reference] documenta `--agent`; escrever ou ler o perfil não é, por si só, ativação. Se a seleção falhar ou o agente não conseguir acessar as ferramentas MCP do Playwright configuradas e a skill, pause e resolva esse bloqueio com a pessoa que conduz o workshop.

Substitua os dois marcadores pela URL real da issue de filtragem e os esclarecimentos aprovados na Lição 4, ou por `none` quando a issue estiver completa. Não dependa da memória do agente anterior.

```plaintext
Verifique o recurso de filtragem em relação a esta issue: <filtering-issue-URL>. Estes são os critérios de aceitação adicionais que aprovei durante o planejamento: <cole os esclarecimentos acordados ou escreva none>.

Valide o comportamento com o servidor MCP do Playwright, examine a cobertura de testes, adicione testes apenas para lacunas de cobertura e execute a validação pela skill quality-checks. Relate evidências, resultados das verificações e bloqueios. Não altere código da aplicação sem minha aprovação, não crie um commit nem abra um pull request.
```

## Revisar as evidências

Compare o relatório com a issue: cada critério precisa de cobertura automatizada adequada e comportamento observável. Examine a atividade real das ferramentas MCP do Playwright, a identidade da cópia de trabalho e do servidor e os resultados dos quatro scripts da skill. As verificações no navegador e E2E automatizadas não devem reutilizar um servidor desatualizado ou outra cópia de trabalho.

Revise os testes adicionados: eles devem cobrir lacunas reais sem enfraquecer asserções. Não adicionar testes é correto quando a cobertura é adequada. Um parecer **NO-GO** por bloqueio ou falha é um resultado válido, não permissão para ignorar evidências.

Se QA identificar um defeito na aplicação, aprove separadamente uma correção específica e execute novamente as verificações e observações no navegador afetadas na revisão resultante. Pré-requisitos ou ferramentas ausentes precisam de uma resolução explícita. Não trate evidências antigas como prova de código alterado.

## Salvar um checkpoint

Quando QA terminar, preserve o relatório com a URL da issue, os esclarecimentos aprovados, a revisão testada, as observações no navegador e os resultados das verificações. Digite `/exit` e inicie `copilot` sem `--agent` no mesmo diretório e branch para voltar a uma conversa normal. Forneça esse contexto novamente; a conversa nova não herda as evidências da conversa de QA.

Após revisar o perfil, quaisquer alterações de testes e as evidências resultantes, envie a solicitação abaixo ao agente normal:

```plaintext
Revise o diff atual e crie um commit de checkpoint para a definição do agente de QA e quaisquer alterações de testes aprovadas. Permaneça na branch de filtragem existente. Não faça push nem abra um pull request.
```

Continue na [Lição 8 - Criar e integrar o PR do recurso][next-lesson] com o recurso de filtragem, a skill, o perfil de QA, os testes e as evidências atuais de verificação.

[previous-lesson]: ../6-mcp-playwright/
[next-lesson]: ../8-create-pull-request/
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
