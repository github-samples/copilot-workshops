---
title: "Lição 1 - Instalar o GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-09-11
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

1. Volte ao codespace e aguarde o término da configuração.
2. Abra uma janela de terminal pressionando <kbd>Ctrl</kbd>+<kbd>`</kbd>.
3. Você verá um painel de terminal aparecer na parte inferior da janela do VS Code.

## Confirmar o ambiente do participante

No terminal do codespace, confirme que você está no próprio repositório Tailspin Toys, não no repositório de conteúdo do workshop. Leia o `README.md` e o `package.json` para conhecer a configuração e os comandos de verificação. O Tailspin Toys atualmente exige Node.js 22.13 ou posterior, as dependências do projeto e o Chromium do Playwright para testes E2E.

```bash
pwd
git remote -v
node --version
gh auth status
```

A GitHub CLI (`gh`) ajudará a examinar PRs e CI. Se faltar autenticação, use `gh auth login` e siga as instruções do navegador. Confirme que sua conta pode enviar branches e criar e integrar PRs neste repositório; políticas da organização podem exigir outro revisor. Resolva pré-requisitos ausentes usando as instruções de configuração do repositório antes de alterar código e revise qualquer instalação antes de autorizá-la.

A CLI atua na cópia de trabalho em que você a inicia; começar uma conversa não cria automaticamente um worktree isolado. Este workshop usa uma branch por marco de PR. Você integrará primeiro as avaliações por estrelas e a demonstração de instruções e manterá a mesma branch de filtragem durante as Lições 4–8.

## Instalar o Copilot CLI

Você pode instalar o Copilot CLI por [npm][install-npm], [WinGet][install-winget] e [Homebrew][install-homebrew]. Como o GitHub Codespaces já inclui o Node.js, você usará o npm para instalar o Copilot CLI.

1. No terminal, confirme que o Node.js está instalado e atende ao requisito de versão:

    ```bash
    node --version
    ```

    O Tailspin Toys exige a versão 22.13 ou posterior, mesmo que o requisito da própria CLI seja diferente. Siga as instruções de configuração do repositório do participante se a sua versão for antiga demais.

2. Instale o Copilot CLI globalmente no codespace com npm:

    ```bash
    npm install -g @github/copilot
    ```

3. Verifique a instalação consultando a versão:

    ```bash
    copilot --version
    ```

    Você deve ver o número da versão exibido, por exemplo `v1.0.XX`.

> [!NOTE]
> Se a instalação falhar por erro de permissão, examine a configuração do npm ou peça ajuda à pessoa que conduz o workshop, em vez de executar novamente um comando desconhecido com privilégios elevados.

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

    ```plaintext
    Quais arquivos existem neste projeto?
    ```

4. O Copilot deverá explorar o repositório e fornecer um resumo da estrutura do projeto.
5. Experimente o comando `/help` para ver os comandos de barra disponíveis:

    ```text
    /help
    ```

6. Saia desta sessão digitando o comando a seguir no prompt do Copilot. Você iniciará uma sessão nova para a primeira alteração.

    ```text
    /exit
    ```

## Entender modos e permissões

O Copilot CLI trabalha no diretório e na branch Git em que você o inicia. Confiar em um diretório permite usar o contexto do repositório; isso não equivale a aprovar todas as ações de ferramentas. Revise solicitações de permissão para alterações de arquivos, comandos de shell e operações do GitHub.

Inicie as lições de código a partir da raiz do repositório do participante com:

```bash
copilot --enable-all-github-mcp-tools
```

O servidor MCP do GitHub é integrado. Essa opção expõe todas as suas ferramentas para trabalhar com issues e PRs; autenticação, permissões do repositório e aprovações de ferramentas continuam se aplicando. Ela não autoriza um commit ou PR por si só.

Use <kbd>Shift</kbd>+<kbd>Tab</kbd> para alternar entre os modos padrão **Interactive**, **Plan** e **Autopilot**. Verifique o indicador de modo antes de enviar uma solicitação. Você manterá Interactive nas primeiras alterações, planejará a filtragem antes de criá-la e voltará explicitamente a Interactive antes de criar e revisar personalizações.

> [!CAUTION]
> As configurações de modo e permissão são diferentes. O Autopilot continua trabalhando de forma autônoma; `--allow-all` e seu alias `--yolo` concedem todas as permissões de ferramentas, caminhos e URLs. Este workshop não exige iniciar todas as sessões com permissões irrestritas. Revise o escopo antes de conceder acesso, mesmo dentro de um codespace.

## Resumo e próximos passos

Parabéns! Você instalou e autenticou o GitHub Copilot CLI com sucesso. Você aprendeu a:

- instalar o Copilot CLI com npm.
- autenticar com sua conta do GitHub.
- confiar em um diretório para o Copilot CLI trabalhar com ele.
- verificar se a instalação está funcionando corretamente.

Agora que o Copilot CLI está instalado, faça uma alteração pequena e revisável na [Lição 2 - Adicionar avaliações por estrelas: uma melhoria rápida][next-lesson].

## Recursos

- [Instalar o GitHub Copilot CLI][install-copilot-cli]
- [Sobre o Copilot CLI][about-copilot-cli]
- [Usar o Copilot CLI][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
