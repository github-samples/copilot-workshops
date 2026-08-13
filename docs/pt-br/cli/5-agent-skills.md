---
title: "Lição 5 - Usar skills de agente"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

No desenvolvimento de aplicativos, é comum lidar com tarefas repetíveis, como gerar builds, executar testes ou criar pull requests. **Agent Skills** permitem orientar o Copilot — e outros agentes de IA — sobre como executar essas tarefas. Uma skill é uma pasta de instruções, scripts e recursos que o agente pode carregar sob demanda. O [Agent Skills][agent-skills-repo] é um padrão aberto usado por uma variedade de agentes, portanto a mesma skill pode funcionar no Copilot Chat em modo agente, no agente de nuvem do Copilot, no Copilot CLI e no aplicativo GitHub Copilot.

As skills ficam na pasta `.github/skills` de um projeto, ou globalmente em `~/.copilot/skills`. Cada skill é uma pasta que contém um arquivo `SKILL.md` com frontmatter YAML, incluindo `name` e `description`, seguido das instruções em markdown:

```yaml
---
name: make-contribution
description: All changes to code must follow the guidance documented in the repository. Before any issue is filed, branch is made, commits generated, or pull request (or PR) created, a search must be done to ensure the right steps are followed. Whenever asked to create an issue, commit messages, to push code, or create a PR, use this skill so everything is done correctly.
---
```

As skills também podem incluir subpastas com scripts, assets e material de referência. A estrutura completa é abordada na [especificação de Agent Skills][agent-skills-spec].

> [!TIP]
> As skills são carregadas dinamicamente. O agente decide qual skill se aplica com base no campo `description` — uma descrição clara e específica para o cenário é o que diferencia uma skill usada de uma skill ignorada.

[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification

Vamos explorar como uma skill pode garantir que pull requests sigam as especificações definidas pela equipe.

## Cenário

A equipe tem um conjunto de requisitos para pull requests (PR):

- mensagens de commit claras, com arquivos agrupados de forma lógica.
- todos os testes devem passar antes da criação de um PR.
- cada PR deve conter as seções a seguir:
    - uma descrição do motivo das alterações.
    - uma visão geral dos arquivos alterados.
    - trechos de blocos de código importantes.
    - detalhes das alterações agrupados de forma coerente.

Como a equipe está usando o Copilot para gerar código e PRs, ela quer garantir que as ferramentas de IA sigam esses requisitos.

Nesta lição, você irá:

- explorar uma skill existente para criar pull requests.
- aprender como as skills são usadas pelo agente de IA.
- criar um PR que siga as diretrizes com a ajuda da skill.

## Executar skills

As skills são carregadas dinamicamente quando o agente determina que elas são necessárias. A decisão sobre quais skills usar é guiada pela descrição no arquivo `SKILL.md`. Por isso, é importante ter descrições claras que definam o caso de uso da skill.

## Explorar a skill de PR

Como a Tailspin Toys tem um conjunto de requisitos para criar PRs, ela criou uma skill para ajudar ferramentas de IA a gerar PRs que sigam essas diretrizes. Vamos explorar a skill para entender o que ela fará.

1. Abra `.github/skills/make-contribution/SKILL.md`.
2. Observe o nome e a descrição. Perceba como a descrição destaca o cenário em que a skill deve ser usada, isto é, sempre que houver uma solicitação para criar um pull request ou fazer commit de código.
3. Leia a skill inteira. Observe como as regras definem a criação de branches, a geração de commits e o conteúdo do pull request.

## Usar a skill

Como destacado anteriormente, as skills são invocadas automaticamente pelo Copilot CLI. Portanto, basta pedir que o Copilot crie um PR.

> [!TIP]
> **Inicie uma sessão do Copilot CLI**
>
> Antes de iniciar os exercícios abaixo, volte ao codespace e abra um terminal (<kbd>Ctrl</kbd>+<kbd>`</kbd>, se ainda não houver um aberto). Em seguida, inicie o Copilot CLI com `--yolo` e `--enable-all-github-mcp-tools`:
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> Para retomar a sessão mais recente deste projeto em vez de iniciar uma nova, execute `copilot --yolo --enable-all-github-mcp-tools --continue`. Se o Copilot CLI já estiver em execução por causa de uma lição anterior, envie `/clear` para começar uma conversa limpa.
>
> `--enable-all-github-mcp-tools` habilita as ferramentas GitHub MCP de leitura e escrita para a sessão atual, para que o Copilot possa ler seu backlog e abrir pull requests durante o fluxo do workshop.

> [!CAUTION]
> `--yolo` habilita permissões automáticas completas (`--allow-all-tools`, `--allow-all-paths` e `--allow-all-urls`). Use-o apenas em um ambiente isolado, como um Codespace ou uma VM, e nunca o defina como alias padrão no seu desenvolvimento diário. Consulte [Allowing and denying tool use][allow-all-warning] para saber mais.

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools

1. Peça que o Copilot crie um PR usando o prompt a seguir:

    ```
    Can you please create a pull request for me!
    ```

2. O Copilot reconhecerá a solicitação. Após alguns instantes, você verá o Copilot indicar que está usando a skill **make-contribution**.

3. O Copilot seguirá as instruções da skill. Ele começará executando os testes, depois criará uma branch, fará commits e, por fim, abrirá o PR.
4. Quando o PR for criado, volte ao repositório e abra-o. Observe como as seções seguem as diretrizes definidas na skill e atendem aos requisitos da equipe.
5. Antes de passar para a próxima lição, redefina seu workspace local para uma branch nova criada a partir de `main`, para manter o trabalho de acessibilidade separado deste PR de filtragem:

    ```bash
    git checkout main
    git pull
    git checkout -b accessibility-cli
    ```

## Resumo e próximos passos

Com a ajuda de uma skill de agente, você criou um novo PR que segue requisitos documentados. Você:

- explorou uma skill existente para criar pull requests.
- aprendeu como as skills são usadas pelo agente de IA.
- criou um PR que segue as diretrizes com a ajuda da skill.

As skills são perfeitas para tarefas, mas, para operações mais robustas, vale aproveitar [agentes personalizados][next-lesson], que serão o próximo tópico.

## Recursos

- [Sobre Agent Skills][about-agent-skills]
- [Especificação de Agent Skills][agent-skills-spec]
- [Repositório Agent Skills][agent-skills-repo]
- [Agent Skills no awesome-copilot][awesome-copilot-skills]

[previous-lesson]: ../4-mcp/
[next-lesson]: ../6-custom-agents/
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[awesome-copilot-skills]: https://github.com/github/awesome-copilot/tree/main/skills
