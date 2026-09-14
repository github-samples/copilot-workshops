---
title: "Lição 4 - Criar a filtragem com Plan e Autopilot"
description: "Acorde os requisitos de filtragem, aprove um plano de implementação, valide o código e salve um checkpoint na branch do recurso."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Agora crie o recurso maior: permitir que os usuários filtrem jogos por categoria e distribuidora. Você planejará antes de programar, autorizará explicitamente o **Autopilot**, revisará e testará a implementação e salvará um checkpoint. Esta lição não cria a skill, o agente de QA ou o PR do recurso.

## Iniciar o marco de filtragem

Confirme que os PRs 1 e 2 estão integrados. No terminal do repositório do participante:

```bash
git status
git switch main
git pull --ff-only
git switch -c add-game-filtering
copilot --enable-all-github-mcp-tools
```

Continue apenas com uma árvore de trabalho limpa e uma atualização bem-sucedida a partir de `main`. As Lições 4–8 usam esta mesma branch e cópia de trabalho. Os próximos commits de checkpoint adicionarão a skill e o perfil de QA; não crie uma branch por lição.

## Recuperar a issue real

Encontre **Allow users to filter games by category and publisher** na aba **Issues** do repositório e copie a URL. Não presuma que o nome de arquivo do modelo ou um número de issue identifica a issue na sua cópia.

A issue atual exige:

- selecionar uma ou mais categorias.
- filtrar por distribuidora e combinar com as categorias.
- funções auxiliares de acesso a dados em `src/lib/` que suportem ambos os filtros.
- controles acessíveis com navegação por teclado, ARIA apropriado, estados de foco visíveis e atributos `data-testid`.
- cobertura unitária com Vitest para as funções auxiliares e cobertura E2E com Playwright para o comportamento de filtragem.

Leia a issue atual como fonte de verdade. Mantenha sua URL e todos os esclarecimentos aprovados disponíveis para o prompt de QA da Lição 7.

## Planejar antes de programar

Use <kbd>Shift</kbd>+<kbd>Tab</kbd> para selecionar o modo **Plan**, ou comece com `/plan`. Substitua o marcador da issue e envie:

```plaintext
Planeje o recurso de filtragem descrito nesta issue: <filtering-issue-URL>. Leia a issue, as instruções do repositório, as funções auxiliares de acesso a dados existentes, a interface e os testes antes de propor alterações. Trate a cópia de trabalho atual como ponto de partida; não presuma que uma função auxiliar de distribuidoras já foi criada.

Cubra seleção de múltiplas categorias, filtragem por distribuidora, sua combinação, suporte de acesso a dados, controles acessíveis e cobertura unitária/E2E. Peça que eu esclareça comportamentos não especificados, como a combinação de múltiplas categorias, a limpeza de filtros e resultados vazios; registre as decisões com o plano aprovado. Preserve a arquitetura estática do Astro em vez de introduzir uma API de servidor desnecessária.

Planeje a implementação na branch atual, incluindo os testes de unidade e E2E necessários e a verificação com npm run lint, npm run test:unit, npm run test:e2e e npm run typecheck:all. Examine primeiro os pré-requisitos e a quem pertence o servidor; relate bloqueios em vez de instalar software ou parar processos não relacionados.

Inclua estes limites de execução no plano: depois que eu aprovar, implemente apenas o recurso de filtragem e os testes necessários, execute as verificações e pare para que eu possa revisar. Não crie a skill quality-checks, um agente de QA ou outros ativos de lições posteriores. Não mude de branch, não faça commit, push nem abra ou integre um PR.

Não edite código da aplicação nem comece a implementação até eu aprovar o plano.
```

Responda às perguntas de acompanhamento. Não adicione critérios de aceitação ocultos depois: salve as respostas acordadas com a URL da issue para que implementação, verificações no navegador e QA usem os mesmos requisitos.

Revise se o plano inclui alterações na camada de dados e na interface, testes, controles acessíveis e a convenção de documentação integrada. Confirme que inclui explicitamente as quatro verificações, a parada para revisão e as proibições de criar ativos posteriores do workshop, mudar de branch, fazer commits, pushes e operações de PR. Peça revisões antes da aprovação se faltar algum limite ou critério ou se o plano propuser trabalho fora da issue.

## Aprovar explicitamente o Autopilot

Somente depois que o plano incluir o escopo e os limites de execução revisados, use a opção de aprovação **Accept plan and build on autopilot**. Se a sua versão usar outro texto, selecione explicitamente a opção que muda para **Autopilot** e verifique o indicador de modo. A aprovação inicia a execução do plano delimitado; não dependa de um prompt posterior para adicionar limites depois que o trabalho começar.

> [!CAUTION]
> O Autopilot controla a continuidade do trabalho, não apenas as permissões de ferramentas. Revise a caixa de diálogo de permissões antes de escolher. Permissões completas permitem acesso a ferramentas, caminhos e URLs; permissões limitadas podem bloquear ações que exigem aprovação. Um codespace não dá permissão para expor segredos ou alterar recursos não relacionados. Resolva deliberadamente o acesso bloqueado em vez de tratar verificações ignoradas como aprovadas.

Monitore o trabalho e os resultados dos comandos. O Autopilot pode pausar em um limite de continuação ou relatar um bloqueio antes de concluir o plano. Revise esse estado antes de autorizar a continuação, preservando o mesmo escopo.

## Voltar a Interactive e revisar

Quando a implementação parar, use <kbd>Shift</kbd>+<kbd>Tab</kbd> para voltar ao modo **Interactive** antes de enviar outros prompts. O Autopilot pode continuar ativo após uma tarefa; não presuma que voltou automaticamente.

Digite `/diff` e examine todos os arquivos alterados. Compare a implementação com a issue e os esclarecimentos aprovados:

- Os usuários conseguem selecionar múltiplas categorias, filtrar por distribuidora e combiná-las conforme acordado?
- As funções auxiliares de acesso a dados realmente suportam os filtros, em vez de mudar apenas a interface?
- Os controles têm rótulos significativos, suporte de teclado, foco visível e identificadores de teste estáveis?
- Os testes verificam comportamento, incluindo os casos acordados de limpeza e resultados vazios, sem enfraquecer as asserções existentes?
- O código segue a convenção de documentação e preserva a arquitetura estática da aplicação?

Revise as evidências das quatro verificações npm. Você ainda não criou `quality-checks`, então essas verificações são executadas diretamente. A configuração E2E do Playwright compila e serve uma prévia; antes de executar a suíte, pare apenas um servidor de desenvolvimento que você iniciou para impedir a reutilização de conteúdo desatualizado. Um conflito de porta ou navegador ausente é um bloqueio a resolver, não motivo para encerrar outro processo ou afirmar que uma verificação passou.

Peça correções específicas se necessário, execute novamente as verificações afetadas e garanta que a implementação final tenha verificação completa. A observação direta no navegador vem na Lição 6; ela tem uma finalidade diferente desta verificação automatizada.

## Salvar o checkpoint de implementação

Quando o diff e os resultados forem satisfatórios, autorize um checkpoint local:

```plaintext
Revise o diff atual e os resultados de verificação. Crie um commit de checkpoint contendo apenas a implementação de filtragem revisada e seus testes. Mantenha a branch e a cópia de trabalho de filtragem atuais. Não faça push, não abra um PR nem crie a skill ou o agente de QA ainda.
```

Registre a revisão testada e mantenha a URL da issue e os esclarecimentos aprovados. Permaneça em **Interactive** e continue nesta mesma cópia de trabalho com a [Lição 5 - Criar e usar uma skill quality-checks][next-lesson].

## Recursos

- [Modo Autopilot e permissões][autopilot] explica a continuação autônoma e a volta a Interactive.
- [Referência de comandos do Copilot CLI][cli-reference] lista os controles de modo e comandos atuais.

[previous-lesson]: ../3-custom-instructions/
[next-lesson]: ../5-agent-skills/
[autopilot]: https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
