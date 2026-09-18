---
title: "Lição 4 - Testar seu recurso com o servidor MCP do Playwright"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Você acabou de gerar o recurso de filtragem com o Copilot CLI. Antes de abrir um pull request, confirme que tudo funciona no navegador. Em vez de testar o aplicativo manualmente, você conectará o **servidor MCP do Playwright** e deixará o Copilot controlar um navegador real para testar o recurso.

Nesta lição, você irá:

- entender o que é o Model Context Protocol (MCP) e como os servidores MCP ampliam o Copilot CLI.
- adicionar o servidor MCP do Playwright ao Copilot CLI.
- pedir ao Copilot que o use para testar manualmente o recurso de filtragem em um navegador.

## O que é o Model Context Protocol (MCP)?

O [Model Context Protocol (MCP)](https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/) fornece aos agentes de IA uma maneira de se comunicar com ferramentas e serviços externos. Ao usar o MCP, agentes de IA podem se comunicar com ferramentas e serviços externos em tempo real. Isso permite acessar informações atualizadas, por meio de recursos, e executar ações em seu nome, por meio de ferramentas.

Essas ferramentas e esses recursos são acessados por um servidor MCP, que atua como ponte entre o agente de IA e as ferramentas e serviços externos. O servidor MCP é responsável por gerenciar a comunicação entre o agente de IA e as ferramentas externas, como APIs existentes ou ferramentas locais, como pacotes NPM. Cada servidor MCP representa um conjunto diferente de ferramentas e recursos que o agente de IA pode acessar.

Alguns servidores MCP populares são:

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**: este servidor fornece acesso a um conjunto de APIs para gerenciar seus repositórios do GitHub. Ele permite que o agente de IA execute ações como criar novos repositórios, atualizar os existentes e gerenciar issues e pull requests.
- **[Playwright MCP Server](https://github.com/microsoft/playwright-mcp)**: este servidor fornece automação de navegador com Playwright. Ele permite que o agente de IA execute ações como navegar por páginas web, preencher formulários e selecionar botões.

Há muitos outros servidores MCP disponíveis que fornecem acesso a diferentes ferramentas e recursos. O GitHub mantém um [registro MCP](https://github.com/mcp) para facilitar a descoberta e a contribuição para o ecossistema.

> [!CAUTION]
> Em termos de segurança, trate servidores MCP como qualquer outra dependência do projeto. Antes de usar um servidor MCP, revise o código-fonte com cuidado, verifique quem o publicou e considere as implicações de segurança. Use apenas servidores MCP em que você confie e tenha cautela ao conceder acesso a recursos ou operações sensíveis.

> [!NOTE]
> O [GitHub MCP server][github-mcp-server] já vem **integrado** ao Copilot CLI — ele já está disponível sem configuração, e é assim que o Copilot vem lendo e escrevendo no seu repositório ao longo do workshop. Nesta lição, você adicionará um *segundo* servidor, o Playwright, para dar ao Copilot acesso a um navegador.

## Adicionar o servidor MCP do Playwright

A forma mais rápida de adicionar um servidor é com o comando interativo `/mcp add`. Você registrará o [Playwright MCP server][playwright-mcp-server], que dá ao Copilot um navegador que ele pode controlar.

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

1. Na sua sessão do Copilot CLI, digite:

    ```text
    /mcp add
    ```

2. Um formulário de configuração será exibido. Use <kbd>Tab</kbd> para mover entre os campos e preencha-o assim:

    - **Server Name**: `playwright`
    - **Server Type**: selecione **Local** (também rotulado como **STDIO**)
    - **Command**: `npx @playwright/mcp@latest --headless`
    - **Tools**: deixe `*` para permitir todas as ferramentas do servidor

3. Pressione <kbd>Ctrl</kbd>+<kbd>S</kbd> para salvar. O servidor será adicionado e ficará disponível imediatamente — não é necessário reiniciar.

A flag `--headless` instrui o Playwright a executar o navegador sem janela visível, o que é necessário em um codespace, onde não existe uma área de trabalho para exibição. Nos bastidores, isso grava o servidor no arquivo `~/.copilot/mcp-config.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "type": "local",
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--headless"],
      "tools": ["*"]
    }
  }
}
```

4. Confirme que o servidor está registrado e ativo listando seus servidores MCP:

    ```text
    /mcp show
    ```

5. Você deverá ver `playwright` listado ao lado do servidor interno `github`.

> [!NOTE]
> O projeto Tailspin Toys já usa o Playwright para testes de ponta a ponta, então o navegador de que o Playwright precisa normalmente já está instalado. Se mais tarde o Copilot informar que falta um navegador, peça que ele execute `npx playwright install chromium` e tente novamente.

## Iniciar o site

O servidor MCP do Playwright precisa de um aplicativo em execução para testar. Inicie o servidor de desenvolvimento do Astro em um **terminal separado** para que ele continue em execução enquanto você trabalha no Copilot CLI.

1. Abra um novo terminal no codespace pressionando <kbd>Ctrl</kbd>+<kbd>`</kbd>.
2. Inicie o site:

    ```bash
    npm run dev
    ```

3. Deixe esse terminal em execução. Quando você vir o banner `Astro server: http://localhost:4321`, o aplicativo estará pronto.

## Testar o recurso de filtragem

Volte à sessão do Copilot CLI e peça ao Copilot para testar o recurso.

O [Playwright MCP server][playwright-mcp-server] dá ao Copilot um navegador real para controlar. Em vez de você verificar manualmente o aplicativo, o agente pode abrir uma página, navegar, aplicar filtros e informar o resultado — depois resumir o que viu. Essa é a maneira mais rápida de confirmar que um recurso se comporta como esperado sem sair da conversa.

Internamente, o servidor MCP do Playwright trabalha a partir da [árvore de acessibilidade][playwright-mcp-server] da página, em vez de usar capturas de tela. Isso significa que o agente raciocina sobre elementos estruturados e rotulados, como botões, links e itens de lista, da mesma forma que tecnologias assistivas fazem. Assim, uma verificação funcional rápida também funciona como uma checagem básica de acessibilidade.

Com o servidor conectado e o aplicativo em execução, peça ao Copilot para exercitar o recurso de filtragem que você acabou de criar:

```text
Using the Playwright MCP server, open a browser to the running app at http://localhost:4321 and verify the new game filtering feature:

1. Go to the games page and note how many games are listed.
2. Apply a category filter and confirm the list updates to only show games in that category.
3. Clear it, then apply a publisher filter and confirm the list updates to that publisher.
4. Combine a category and a publisher filter and confirm the results respect both.

Report what you observe at each step, and call out anything that does not behave as expected.
```

O Copilot iniciará um navegador por meio do servidor MCP do Playwright, executará cada etapa e informará o que encontrou. Leia o resumo em comparação com os critérios de aceitação da issue. Se algo parecer incorreto, faça perguntas de acompanhamento ou peça que ele corrija o código antes de abrir um pull request.

> [!NOTE]
> O aplicativo precisa estar em execução em `http://localhost:4321` para este teste. Se você tiver parado o servidor de desenvolvimento, inicie-o novamente antes de enviar o prompt. Na primeira vez em que o Copilot usar o servidor MCP do Playwright, talvez seja necessário baixar um navegador. Se ele informar que falta um navegador, peça que execute `npx playwright install chromium` e tente novamente.

[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp

## Resumo e próximos passos

Parabéns, você usou o servidor MCP do Playwright para testar manualmente o recurso com o Copilot CLI. Para recapitular, você:

- aprendeu o que é o Model Context Protocol (MCP) e como os servidores MCP ampliam o Copilot CLI.
- adicionou o servidor MCP do Playwright com `/mcp add`.
- pediu ao Copilot que controlasse um navegador e verificasse o recurso de filtragem antes da entrega.

Agora que você confirmou que o recurso funciona, pode continuar para a próxima lição, na qual [abrirá um pull request com a ajuda de uma skill de agente][next-lesson].

## Recursos

- [O que é MCP e por que todo mundo está falando sobre isso?][mcp-blog-post]
- [Servidor MCP do Microsoft Playwright][playwright-mcp-server]
- [Adicionar servidores MCP ao Copilot CLI][cli-add-mcp]
- [Servidor MCP do GitHub][github-mcp-server]

[previous-lesson]: ../3-generating-code/
[next-lesson]: ../5-agent-skills/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[github-mcp-server]: https://github.com/github/github-mcp-server
[cli-add-mcp]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
