---
title: "Lição 1 - Instalar o GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

O [GitHub Copilot CLI][about-copilot-cli] é um poderoso assistente de programação baseado em agentes que é executado no terminal, permitindo explorar bases de código, gerar código, executar comandos e interagir com ferramentas externas — tudo pela linha de comando. Ele permite delegar tarefas, solicitar alterações e manter o foco. Como você pode imaginar, o primeiro passo é instalar a ferramenta. Felizmente, isso pode ser feito com ferramentas que você já conhece.

Nesta lição, você aprenderá a:

- instalar o GitHub Copilot CLI com npm.
- autenticar com sua conta do GitHub.
- verificar a instalação.

## Cenário

Sua equipe está começando a usar agentes de IA para avançar em um backlog crescente. O Copilot CLI leva essa capacidade para o terminal, onde muitas pessoas desenvolvedoras já trabalham. Nesta lição, você fará a instalação, a autenticação e a configuração inicial para usá-lo no restante do workshop.

## Abrir um terminal no codespace

Antes de instalar o Copilot CLI, você precisa abrir uma janela de terminal no codespace.

1. Volte ao codespace, caso ainda não esteja nele.
2. Abra uma janela de terminal pressionando <kbd>Ctrl</kbd>+<kbd>`</kbd>.
3. Você verá um painel de terminal aparecer na parte inferior da janela do VS Code.

## Instalar o Copilot CLI

Você pode instalar o Copilot CLI por [npm][install-npm], [WinGet][install-winget] e [Homebrew][install-homebrew]. Como o GitHub Codespaces já inclui o Node.js, você usará o npm para instalar o Copilot CLI.

1. No terminal, confirme que o Node.js está instalado e atende ao requisito de versão:

    ```bash
    node --version
    ```

    Você deve ver a versão 22 ou posterior, por exemplo `v22.x.x`.

2. Instale o Copilot CLI globalmente no codespace com npm:

    ```bash
    npm install -g @github/copilot
    ```

3. Verifique a instalação consultando a versão:

    ```bash
    copilot --version
    ```

    Você deve ver o número da versão exibido, por exemplo `v1.0.XX`.

> [!TIP]
> Se você encontrar erros de permissão, talvez precise usar `sudo npm install -g @github/copilot` em alguns sistemas. No entanto, isso não deve ser necessário no GitHub Codespaces.

## Autenticar com o GitHub

Na primeira execução, o Copilot CLI solicitará que você autentique sua conta do GitHub.

1. Inicie o Copilot CLI:

    ```bash
    copilot
    ```

2. Se você ainda não tiver feito login, verá um prompt de autenticação. O Copilot CLI exibirá um código de dispositivo e solicitará que você acesse uma URL.
3. Siga as instruções na tela:
   - Abra a URL fornecida no navegador
   - Insira o código do dispositivo quando solicitado
   - Autorize o Copilot CLI a acessar sua conta do GitHub
4. Depois da autenticação, você verá o prompt do Copilot CLI, pronto para receber suas perguntas e comandos.

> [!NOTE]
> Em um codespace, você talvez já esteja autenticado por meio da sua sessão do GitHub. Se o Copilot CLI iniciar sem pedir autenticação, está tudo certo.

## Confiar no diretório e verificar se tudo funciona

Agora que você está no prompt do Copilot CLI pela primeira vez, vamos confiar neste repositório do workshop e confirmar que o Copilot CLI está instalado e conectado corretamente.

1. Quando o Copilot CLI pedir que você confirme que confia nos arquivos desta pasta, verá três opções:
   - **Yes, proceed**: confiar apenas nesta sessão
   - **Yes, and remember this folder for future sessions**: confiar permanentemente
   - **No, exit (Esc)**: não permitir acesso aos arquivos
2. Neste workshop, selecione **Yes, and remember this folder for future sessions**, já que você trabalhará neste repositório ao longo de toda a atividade.
3. Faça uma pergunta simples ao Copilot para verificar se tudo funciona:

    ```
    What files are in this project?
    ```

4. O Copilot deverá explorar o repositório e fornecer um resumo da estrutura do projeto.
5. Experimente o comando `/help` para ver os comandos de barra disponíveis:

    ```
    /help
    ```

6. Saia do Copilot CLI digitando o comando a seguir no terminal. Voltaremos ao Copilot CLI em uma lição futura.

    ```
    exit
    ```

## Resumo e próximos passos

Parabéns! Você instalou e autenticou o GitHub Copilot CLI com sucesso. Você aprendeu a:

- instalar o Copilot CLI com npm.
- autenticar com sua conta do GitHub.
- confiar em um diretório para o Copilot CLI trabalhar com ele.
- verificar se a instalação está funcionando corretamente.

Agora que o Copilot CLI está instalado, vamos fornecer ao Copilot algum contexto sobre o projeto. Continue para a [Lição 2 - Instruções personalizadas com a CLI][next-lesson].

## Recursos

- [Instalar o GitHub Copilot CLI][install-copilot-cli]
- [Sobre o Copilot CLI][about-copilot-cli]
- [Usar o Copilot CLI][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-custom-instructions/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
