---
title: "Lição 4 - Criar a filtragem com Plan e Autopilot"
description: "Planeje a filtragem a partir da issue, aprove o Autopilot explicitamente, valide com as verificações npm existentes e uma visita manual ao navegador e salve um checkpoint."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Você integrou as avaliações por estrelas e o padrão de documentação com sua demonstração de código. Agora crie o recurso de filtragem. Este é o início de um marco de PR maior: mantenha esta mesma sessão, worktree e branch durante as Lições 4–8.

Nesta lição, você vai:

- partir de `main` atualizado e ler a issue real de filtragem.
- resolver os requisitos no modo **Plan** antes de aprovar explicitamente o **Autopilot**.
- revisar a filtragem e os testes e executar as quatro verificações npm existentes.
- visitar o recurso manualmente no navegador e salvar um checkpoint.

A skill, a validação MCP, o perfil QA e o PR do recurso vêm nos próximos módulos. Não os crie durante esta etapa de implementação.

## Modos de sessão

O seletor de modo abaixo do prompt controla a autonomia do agente:

- **Interactive** mantém você envolvido enquanto o agente trabalha e solicita informações.
- **Plan** prepara um plano para revisão antes da implementação.
- **Autopilot** implementa e itera de forma autônoma dentro do escopo e das permissões aprovados.

Planeje primeiro, aprove explicitamente e volte ao Interactive antes de criar personalizações reutilizáveis.

## Partir de main atualizado

Confirme que o PR 1 e o PR 2 foram integrados no GitHub. Crie um worktree novo para a filtragem em vez de continuar em qualquer uma das branches anteriores.

1. Selecione **My work** e encontre **Allow users to filter games by category and publisher** pelo título. Abra a issue e copie sua URL real; os números de issue variam entre repositórios.
2. Selecione **New session** e escolha **new working tree**. Mantenha o modo **Interactive** para atualizar o estado inicial.

   ![Visualização da issue no aplicativo GitHub Copilot com uma seta apontando para o botão New session](../../_images/app-new-session-from-issue.png)

3. Envie esta solicitação de preparação antes de planejar ou editar:

   ```plaintext
   Prepare esta nova sessão de filtragem sem implementar nada. Identifique a cópia de trabalho e a branch, confirme que o worktree está limpo, busque as atualizações de origin e avance a branch desta sessão por fast-forward até origin/main. Confirme que HEAD corresponde a origin/main e inclui os PRs integrados de avaliações por estrelas e padrões de código.

   Pare e explique se houver alterações pendentes, divergências ou se algum dos merges estiver ausente. Não redefina nem descarte trabalho, não mude de branch, não crie outra branch nem edite arquivos da aplicação. Informe a revisão inicial.
   ```

4. Verifique o estado inicial informado. Apenas buscar atualizações não atualiza o worktree: a branch da sessão atual deve avançar por fast-forward e seu `HEAD` deve corresponder ao `origin/main` obtido antes de começar o trabalho.

## Planejar o recurso de filtragem

Mude o seletor de modo para **Plan**. Substitua o marcador da issue abaixo pela URL que você copiou.

```plaintext
Planeje o recurso de filtragem a partir desta issue: <filtering-issue-URL>. Leia todos os critérios de aceitação e as instruções do repositório e examine a aplicação estática Astro atual, suas funções auxiliares de acesso a dados e os testes existentes. Não implemente ainda.

Cubra a seleção de várias categorias, a filtragem por distribuidora, a combinação de categorias e distribuidora, as funções auxiliares de acesso a dados adequadas, os controles acessíveis e a cobertura de unidade e de ponta a ponta exigida pela issue. Pergunte para que eu esclareça comportamentos não especificados, como a combinação de várias categorias, a limpeza dos filtros e os resultados vazios, em vez de inventar requisitos silenciosamente. Não introduza uma API de servidor, a menos que os requisitos e a arquitetura existente justifiquem.

Proponha um plano de implementação e verificação com escopo limitado que siga a convenção de documentação do repositório e adicione ou atualize os testes de unidade e de ponta a ponta necessários. Após confirmar os comandos em package.json, planeje executar npm run lint, npm run test:unit, npm run test:e2e e npm run typecheck:all com as ferramentas existentes do projeto. Registre a URL da issue e meus esclarecimentos aprovados no plano para que eu possa reutilizá-los no QA.

Inclua estas medidas de segurança de execução no plano antes da minha aprovação: identifique a cópia de trabalho e o servidor em teste; examine os pré-requisitos antes de executar verificações; pergunte antes de instalar software, dependências ou navegadores; não reutilize o servidor de outro worktree; pare apenas os servidores que você iniciou; e relate outros conflitos de porta em vez de interromper processos não relacionados. Pré-requisitos ausentes e verificações ignoradas devem ser relatados como bloqueios, não como verificações aprovadas.

Inclua este limite de implementação no plano: depois que eu aprovar explicitamente o Autopilot, implemente apenas o recurso de filtragem acordado e seus testes neste mesmo worktree e branch, execute as quatro verificações, relate a implementação e todos os resultados, incluindo falhas ou bloqueios, e pare para minha revisão e verificação manual no navegador. Não crie skills ou agentes personalizados, não configure MCP, não mude de branch, não faça commit, push nem abra um PR durante a implementação. A verificação manual no navegador e o commit de checkpoint ocorrerão depois, sob minha orientação separada.

Por enquanto, permaneça no modo Plan e pare com o plano para minha revisão. Não implemente, não crie skills ou agentes personalizados, não configure MCP, não mude de branch, não faça commit, push nem abra um PR.
```

Responda às perguntas de esclarecimento e compare o plano com a issue. Procure as alterações de acesso a dados, os controles acessíveis e os testes, em vez de aceitar uma implementação apenas de interface. Guarde a URL real da issue e os esclarecimentos aprovados do plano para as Lições 6 e 7; use `none` quando não forem necessários critérios adicionais.

Antes de aprovar, confirme que o próprio plano contém as quatro verificações, a convenção de documentação, as medidas de segurança de pré-requisitos e servidores, a exigência de manter o mesmo worktree e branch e a parada após implementação e verificação. Ele deve proibir skills, agentes e configuração MCP posteriores, commits, pushes e PRs durante a implementação. Se faltar algum limite, peça um plano revisado ainda no modo **Plan** e examine a revisão antes de aprovar.

## Aprovar o Autopilot explicitamente

Somente depois que o plano revisado contiver seus requisitos e todos os limites de execução, selecione **Approve and implement with autopilot** nos controles de aprovação do plano, ou a opção explícita equivalente de Autopilot exibida na sua versão. Confirme que o indicador de modo mostra **Autopilot**.

A aprovação pode iniciar a execução imediatamente. Portanto, todo o escopo de implementação, as regras de segurança e os limites de parada precisam estar no plano revisado antes da aprovação; não dependa de adicioná-los em uma mensagem posterior quando a execução já começou.

O Autopilot pode escrever código e testes e iterar sobre falhas, mas essa permissão não autoriza concluir os próximos módulos do workshop. Um pré-requisito ausente é um bloqueio a resolver com aprovação, não uma verificação aprovada.

## Revisar e verificar a implementação

1. Abra **Changes** e examine a implementação da filtragem e os testes.
2. Compare o resultado com a issue e os esclarecimentos aprovados, incluindo combinações de várias categorias e distribuidoras. Verifique se as funções auxiliares novas ou modificadas seguem o padrão de documentação da Lição 3.
3. Examine a saída real dos comandos das quatro verificações npm. Elas são executadas diretamente agora porque você ainda não criou a skill quality-checks.
4. Resolva falhas e execute novamente as verificações afetadas antes de aceitar a implementação. A configuração E2E do Playwright faz o build e serve uma prévia, podendo reutilizar um servidor local; confirme que o servidor testado pertence a este worktree, não a uma lição anterior.

## Verificar o recurso manualmente

Volte a sessão ao modo **Interactive** antes da revisão manual e mantenha-o para a Lição 5.

1. Abra **Terminal** no painel de revisão desta sessão. Se necessário, selecione **+** e depois **Terminal**.
2. Confirme que o terminal está no worktree de filtragem e execute:

   ```shell
   npm run dev
   ```

3. Abra no navegador a URL exibida por esse servidor, normalmente `http://localhost:4321`. Se a porta estiver ocupada, identifique seu responsável em vez de interromper um processo não relacionado ou presumir que o servidor existente contém suas alterações.
4. Exercite a seleção de categorias, a seleção de distribuidora e sua combinação conforme o comportamento aprovado. Verifique o acesso por teclado e os comportamentos acordados para limpeza dos filtros e resultados vazios.
5. Se algo falhar, solicite uma correção específica, revise o diff, execute novamente as verificações automatizadas afetadas e repita as verificações relevantes no navegador.
6. Volte ao terminal e pressione <kbd>Control</kbd>+<kbd>C</kbd> (Mac) ou <kbd>Ctrl</kbd>+<kbd>C</kbd> (Windows/Linux) para parar o servidor que você iniciou. Confirme que ele parou antes da execução E2E do próximo módulo.

Esta é sua observação manual no navegador. A observação no navegador conduzida pelo agente via MCP vem na Lição 6.

## Salvar um checkpoint

Após revisar as alterações e a verificação, autorize um commit local:

```plaintext
Revise o diff atual e crie um commit de checkpoint para a implementação da filtragem e seus testes. Mantenha esta mesma branch e worktree de filtragem. Não crie skills ou agentes, não configure MCP, não faça push nem abra um pull request.
```

Este checkpoint faz parte do PR 3, não de um PR separado. Permaneça no modo **Interactive**, na mesma sessão, para a [Lição 5 - Criar e usar uma skill quality-checks][next-lesson].

## Recursos

- [Trabalhar com sessões de agente no aplicativo GitHub Copilot][agent-sessions]
- [Sobre sandboxes locais e na nuvem para o GitHub Copilot][sandboxes]

[previous-lesson]: ../3-custom-instructions/
[next-lesson]: ../5-agent-skills/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
