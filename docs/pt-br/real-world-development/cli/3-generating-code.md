---
title: "Lição 3 - Adicionar recursos ao projeto com o GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Como você pode imaginar, uma das principais tarefas realizadas com o GitHub Copilot CLI é adicionar recursos, funcionalidades e código a um projeto. Vamos pegar uma das issues do seu backlog e pedir ao Copilot que ajude a implementá-la.

## Cenário

Chegou a hora de concluir a filtragem no projeto. Você já tem a issue de filtragem no backlog e um helper de base da lição anterior. Vamos fazer o Copilot recuperar os detalhes da issue, considerar o trabalho existente e criar a funcionalidade restante.

Nesta lição, você irá:

- usar o modo plan para gerar um plano de implementação da funcionalidade de filtragem.
- gerar o código necessário para adicionar a filtragem ao site com o Copilot.

Ao final desta lição, você terá adicionado uma nova funcionalidade ao projeto.

## Usar o modo plan

Um dos melhores usos da IA é o planejamento. Muitas vezes, você tem uma boa ideia do que quer criar, mas só precisa trocar algumas ideias. Ferramentas de IA podem ajudar a organizar melhor o raciocínio ao fazer perguntas de acompanhamento e analisar diferentes armadilhas ou componentes ausentes. Para apoiar esse processo, o Copilot CLI oferece um modo plan. Além disso, o tempo dedicado ao planejamento ajudará o Copilot a gerar um código que corresponda melhor aos requisitos definidos.

Você iniciará o processo de criação da nova funcionalidade usando o modo plan no Copilot CLI.

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

1. Digite o prompt a seguir no Copilot CLI para criar um plano com base na issue de filtragem:

    ```
    /plan Retrieve the issue on the repository related to adding filtering. We already added a publishers helper in src/lib/publishers.ts, so treat that as existing work and plan the remaining updates (games filtering logic, UI, and tests).
    ```

2. O Copilot pode fazer perguntas de acompanhamento enquanto monta o plano. Quando isso acontecer, responda com base em como você implementaria a funcionalidade.
3. Quando o plano for gerado, revise o esboço. Você deverá notar que ele recomenda as mudanças restantes na camada de dados e na interface, além da geração de testes.
4. O Copilot CLI oferecerá a opção de fornecer feedback adicional sobre o plano. Você pode mover o cursor para baixo até a seção indicada e então digitar suas sugestões. O Copilot incorporará suas observações em uma nova versão do plano.
5. Quando estiver satisfeito, selecione a opção oferecida pelo Copilot para começar a criar o novo recurso.

> [!NOTE]
> Como o Copilot é probabilístico, o texto exato e as opções apresentadas variam. Ainda assim, você verá uma opção para iniciar a implementação semelhante a:
>
> `Yes, and switch to autopilot mode`.
>
> O Copilot pode oferecer a opção de habilitar o [autopilot mode](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot), como mostrado no exemplo acima. O modo autopilot permite que o Copilot CLI avance em uma tarefa sem esperar sua entrada após cada etapa. Depois que você fornece a instrução inicial, o Copilot CLI trabalha de forma autônoma em cada etapa até considerar a tarefa concluída. Como estamos em um ambiente isolado, não há problema em usar o autopilot e permitir todas as ferramentas.

6. O Copilot começará a gerar os arquivos.

> [!NOTE]
> Essa operação provavelmente levará vários minutos. Você verá o Copilot editar e criar arquivos, atualizar e gerar testes e executar todos os testes para garantir que tudo funcione. Este é um bom momento para refletir sobre o que você explorou até aqui ou aproveitar uma bebida.

## Revisar o código

Todo código gerado por IA deve ser revisado antes de ser enviado para produção. Vamos aproveitar este momento para explorar os arquivos que o Copilot criou e modificou ao implementar o novo recurso.

1. Use o Copilot CLI para exibir o diff ou as alterações de código usando o comando a seguir no Copilot CLI:

    ```
    /diff
    ```

2. Observe quais arquivos foram alterados. Use as setas do teclado para alternar entre eles. Você deverá ver atualizações em arquivos como a página de listagem de jogos, onde ficam os novos controles de filtro e a filtragem no cliente, além de `src/lib/games.ts` e testes como `games.test.ts`. Também pode haver atualizações em `publishers.ts` se o Copilot refinar o helper existente para alinhá-lo à implementação completa.

## Resumo e próximos passos

Agora você adicionou a funcionalidade de filtragem ao site com a ajuda do Copilot CLI. Em especial, você:

- usou o modo plan para gerar um plano de implementação da funcionalidade de filtragem.
- gerou o código necessário para adicionar a filtragem ao site com o Copilot.

Claro, o próximo passo é garantir que tudo funcione. Vamos [testar o recurso com o servidor MCP do Playwright][next-lesson] antes de abrir um pull request.

## Recursos

- [Usar o Copilot CLI][using-copilot-cli]
- [Sobre o Copilot CLI][about-copilot-cli]
- [Gerenciamento de contexto no Copilot CLI][context-management]

[previous-lesson]: ../2-custom-instructions/
[next-lesson]: ../4-mcp/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
