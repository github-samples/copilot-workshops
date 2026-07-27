---
title: "Lição 6 - Agentes personalizados com o GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

## O que são agentes personalizados?

[Agentes personalizados][custom-agents-concept] no GitHub Copilot permitem criar assistentes de IA especializados e adaptados a tarefas ou domínios específicos do seu fluxo de desenvolvimento. Ao definir agentes por meio de arquivos markdown na pasta `.github/agents` do repositório, você fornece ao Copilot instruções direcionadas, boas práticas, padrões de código e conhecimento específico do domínio para orientá-lo a executar determinados tipos de trabalho com mais eficácia. As equipes podem transformar sua experiência em agentes reutilizáveis — um agente de acessibilidade que aplica conformidade com a [WCAG][wcag], um agente de segurança que segue práticas de programação segura ou um agente de testes que mantém padrões consistentes.

Agentes personalizados são definidos por arquivos markdown na pasta `.github/agents` do projeto, ou globalmente em `~/.copilot/agents`. Cada arquivo tem frontmatter YAML com pelo menos `name` e `description`, seguido de um prompt em markdown que define o comportamento, a especialização e as instruções do agente.

### Agentes personalizados em comparação com skills de agente

Há alguma sobreposição lógica entre agentes personalizados e [skills de agente][agent-skills-concept]. Ambos são definidos principalmente com arquivos markdown e dizem à IA como executar operações. A forma mais clara de diferenciá-los é: um **agente personalizado** é o executor, e as **skills** são ferramentas.

Agentes personalizados têm sua própria janela de contexto e são criados para orquestrar skills, e até outros agentes, como parte do trabalho. Neste laboratório, o agente personalizado de acessibilidade revisa e atualiza o site com base em diretrizes de acessibilidade; como parte desse trabalho, ele poderia chamar skills como uma skill de fluxo de pull request ou outra que execute e gerencie testes.

> [!NOTE]
> Não existe uma única forma "correta" de criar um agente personalizado. Como em qualquer coisa relacionada à IA, teste e itere para descobrir o que funciona melhor nos seus ambientes e cenários.

[custom-agents-concept]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[agent-skills-concept]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/

## Cenário

Muitos aplicativos web ainda não são acessíveis para todas as pessoas usuárias, e o site em que você está trabalhando não é exceção. Você usará um agente personalizado para identificar e corrigir problemas de acessibilidade.

A Tailspin Toys está comprometida em garantir que sua plataforma de financiamento coletivo seja acessível a todas as pessoas usuárias, independentemente de suas capacidades visuais ou preferências. Comentários recentes de usuários destacaram que algumas pessoas têm dificuldade para ler o tema escuro atual por causa do contraste insuficiente entre as cores de texto e de fundo. Para tratar essa preocupação de acessibilidade, a equipe de design solicitou a implementação de um modo de alto contraste que usuários possam ativar e desativar.

Como a acessibilidade é crítica, você quer garantir que isso seja implementado o mais rápido possível. Você usará um agente personalizado para gerar essa funcionalidade.

Nesta lição, você irá:

- explorar agentes personalizados.
- habilitar um agente personalizado e atribuir uma tarefa a ele usando o Copilot CLI.

## Revisar o agente personalizado de acessibilidade

Um agente personalizado de acessibilidade já foi criado para você. Vamos revisar o conteúdo para entender como ele orientará o Copilot.

1. Abra `.github/agents/accessibility.md`.
2. Observe o frontmatter YAML com os campos `name` e `description`.

> [!CAUTION]
> O frontmatter com `name` e `description` é obrigatório para agentes personalizados.

3. A partir daí, revise as seções seguintes, que destacam:
   - responsabilidades principais ao gerar código para um site acessível.
   - boas práticas de acessibilidade.
   - exemplos de código em HTML, CSS e JavaScript.
   - uma lista de armadilhas e erros comuns.

## Usar um agente personalizado no Copilot CLI

Você pode iniciar um agente personalizado no Copilot CLI com o comando `/agent`. Vamos fazer uma revisão de acessibilidade no site.

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

1. Abra a lista de agentes digitando `/agent` na janela de prompt do Copilot CLI e pressionando <kbd>Enter</kbd>.
2. Selecione o **Accessibility agent** na lista de agentes disponíveis.
3. Use o prompt a seguir para pedir que o agente de acessibilidade faça uma revisão e gere correções para o item de backlog relacionado à acessibilidade:

    ```
    Perform an accessibility review of the site. Pull the related issue down from the repository for details. Implement a high-contrast mode toggle that persists the user's preference across page reloads. Ensure there are e2e tests for any updates made to the project. Then create a PR with the updates.
    ```

4. O Copilot começará a trabalhar na tarefa. Ele recuperará a issue, fará a revisão, gerará as atualizações e, por fim, criará o PR. Você também deve notar que, ao criar o PR, ele usa a skill do projeto voltada a pull requests.

> [!NOTE]
> Esse processo provavelmente levará alguns minutos. É um bom momento para refletir sobre tudo o que você aprendeu, aproveitar uma bebida ou adiantar a próxima lição, que apresenta alguns comandos adicionais disponíveis no Copilot CLI.

## Resumo e próximos passos

Esta lição explorou [agentes personalizados][custom-agents] no GitHub Copilot, assistentes de IA especializados e adaptados a tarefas e domínios específicos. Com agentes personalizados, você pode transformar a experiência e os padrões da sua equipe em agentes reutilizáveis que orientam o Copilot a executar determinados tipos de trabalho com mais eficácia.

Você explorou estes conceitos:

- como agentes personalizados são definidos.
- usar um agente personalizado no Copilot CLI.

Em seguida, vamos explorar [alguns comandos de barra][next-lesson] para aprender outros truques do Copilot CLI.

## Recursos

- [Agentes personalizados][custom-agents]
- [Criar agentes personalizados para um repositório][creating-custom-agents]
- [Agentes personalizados no awesome-copilot][awesome-copilot-agents]
- [Preparar o uso de agentes personalizados na sua organização][org-custom-agents]
- [Preparar o uso de agentes personalizados na sua empresa][enterprise-custom-agents]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-slash-commands/
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[creating-custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents
[awesome-copilot-agents]: https://github.com/github/awesome-copilot/tree/main/agents
[org-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
[enterprise-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
