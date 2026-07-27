---
title: "Lição 7 - Comandos de barra no GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Como toda boa ferramenta de CLI, o GitHub Copilot CLI inclui vários comandos de barra para interação. Esses comandos expõem funcionalidades avançadas, informações de bastidores ou opções adicionais de configuração. Você já explorou alguns deles, como `/clear` para limpar o contexto e `/mcp` para inspecionar servidores MCP. Agora, vamos explorar outros comandos poderosos, incluindo `/context`, `/model`, `/share` e `/delegate`.

## Cenário

Você concluiu os fluxos centrais da CLI. Agora, vamos conhecer algumas capacidades adicionais — compartilhar sessões, trocar de modelo e delegar tarefas ao [agente de nuvem do Copilot][about-cloud-agent].

Nesta lição, você usará:

- `/share` para criar uma GitHub gist e compartilhar sua sessão com a equipe.
- `/context` para ver o contexto que o Copilot CLI está usando no momento.
- `/model` para explorar a lista de modelos disponíveis e selecionar outro, se quiser.
- `/delegate` para, opcionalmente, encaminhar uma tarefa ao agente de nuvem. Isso requer o agente de nuvem, disponível nos planos Copilot Student, Pro, Pro+, Business ou Enterprise — todos, exceto Copilot Free.

## Compartilhar uma sessão

Usar qualquer ferramenta, inclusive uma ferramenta de IA, é uma habilidade. Trabalhar em equipe e compartilhar aprendizados é a melhor forma de melhorar a experiência de todas as pessoas e gerar código de maior qualidade. Para apoiar isso, o Copilot CLI oferece o comando `/share`. O comando `/share` pode gerar um arquivo markdown ou uma GitHub gist com os detalhes da sessão, incluindo os prompts usados e a lógica seguida pelo Copilot.

Vamos criar uma GitHub gist que você poderia compartilhar com a equipe.

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

1. Na janela de prompt do Copilot CLI, envie o comando a seguir:

    ```
    /share gist
    ```

2. Em poucos instantes, o Copilot criará uma gist e exibirá o link.
3. Copie o texto do link.
4. Em uma nova guia do navegador, cole o link para explorar a gist. Observe como a gist destaca os prompts enviados, as skills e os agentes usados, o processo de raciocínio do Copilot e até o código e os resultados de comandos executados localmente.

As gists e os arquivos markdown gerados por `/share` podem ser usados para documentar como o código foi criado ou para compartilhar com a equipe como determinadas ações foram executadas para obter os resultados desejados com o Copilot.

## Explorar o contexto do Copilot CLI

Ao trabalhar em tarefas maiores ou mais complexas, você pode atingir o limite da janela de contexto do modelo. O tamanho exato dessa janela varia de acordo com o modelo usado e a versão do Copilot CLI. Quando a janela de contexto fica cheia, o Copilot CLI a compacta automaticamente, resumindo as informações e removendo tudo o que considerar irrelevante para a tarefa atual. Você pode ver o estado atual do contexto e também compactá-lo manualmente com comandos de barra. Vamos explorar a janela de contexto.

1. Na janela de prompt do Copilot CLI, envie o comando a seguir:

    ```
    /context
    ```

2. Em poucos instantes, o Copilot CLI gerará uma representação visual do contexto atual:

    ![Captura de tela da janela de contexto do Copilot CLI](../../_images/cli-7-context-window.png)

3. Observe o modelo exibido, que pode ser diferente do mostrado na imagem, e a porcentagem atual de tokens usados. O restante das informações destaca:

    | Título | Descrição |
    | ------------ | ------------------------------------------------------ |
    | System/Tools | Arquivos de instruções, conteúdo de arquivos e definições de ferramentas |
    | Messages | Histórico da conversa entre você e o Copilot |
    | Buffer | Espaço reservado pelo Copilot CLI para gerar respostas |
    | Free space | Espaço livre restante |

4. Compacte o histórico da conversa enviando o seguinte comando de barra ao Copilot CLI:

    ```
    /compact
    ```

5. Quando a operação terminar, envie o comando a seguir para exibir novamente as estatísticas atuais do contexto:

    ```
    /context
    ```

6. Observe a mudança no contexto. Talvez ela não seja drástica, já que a janela de contexto provavelmente ainda está relativamente pequena neste momento.

> [!NOTE]
> O Copilot CLI compactará o contexto automaticamente quando ele estiver cheio. Ao se aproximar de 100% da capacidade, ele exibirá a porcentagem logo acima da janela de prompt. Normalmente, a compactação acontece de forma assíncrona, permitindo que você continue interagindo com o Copilot enquanto ele faz esse trabalho. No entanto, em alguns casos ele pode bloquear uma operação em andamento por vários segundos durante o processo.

### Boas práticas com contexto

Na maioria das sessões, o contexto será gerenciado com eficiência pelo próprio Copilot sem orientações específicas. Mesmo assim, pode haver situações em que você decida instruir manualmente o Copilot a limpar ou compactar o histórico:

- Se você for mudar para outra parte do aplicativo ou para uma tarefa não relacionada, pode usar `/clear` para começar de novo e evitar confundir o Copilot com contexto antigo e irrelevante.
- Se você estiver se aproximando do limite máximo da janela de contexto, pode usar `/compact` manualmente para controlar quando a compactação acontecerá.

> [!CAUTION]
> Novamente, na maior parte do tempo, o Copilot gerenciará o contexto sem interação direta sua. Se você perceber que o Copilot está um pouco confuso por causa de informações antigas, ou estiver prestes a mudar para uma tarefa sem relação com a atual, considere usar os comandos manuais.

## Escolher seu modelo

Modelos diferentes têm pontos fortes diferentes, e pessoas desenvolvedoras diferentes têm preferências diferentes. O Copilot CLI permite listar e selecionar o modelo que você quer usar.

1. Exiba a lista de modelos enviando o comando de barra a seguir ao Copilot CLI:

    ```
    /model
    ```

2. Observe a lista de modelos. Cada modelo exibirá tanto seu nome quanto o modificador de custo por solicitação.
3. Se quiser, selecione um novo modelo. Ou pressione <kbd>Esc</kbd> para sair da lista.

> [!CAUTION]
> A seleção de modelo persiste no Copilot CLI.

## Delegar ao agente de nuvem (opcional)

Há situações em que você quer continuar trabalhando no terminal, mas precisa delegar uma tarefa mais demorada ao agente de nuvem do Copilot. O comando `/delegate` envia a sessão atual do Copilot CLI para o GitHub.com, onde o agente de nuvem a assume, trabalha de forma assíncrona e abre um pull request quando termina.

> [!NOTE]
> `/delegate` requer o agente de nuvem, disponível nos planos Copilot Student, Pro, Pro+, Business ou Enterprise — todos, exceto Copilot Free. Se você não tiver acesso, leia esta seção e pule a parte prática.

1. Primeiro, limpe a sessão atual para evitar delegar o contexto acumulado do workshop:

    ```
    /clear
    ```

2. Envie um prompt pequeno e bem delimitado. Por exemplo, você pode delegar a meta extra de paginação do seu backlog:

    ```
    Implement pagination on the game list page so it shows a fixed number of games per page with Previous and Next controls, and add tests.
    ```

3. Envie o comando de barra a seguir para entregar a sessão ao agente de nuvem e confirme o prompt que deseja delegar:

    ```
    /delegate
    ```

4. Abra [Copilot agents](https://github.com/copilot/agents) no navegador para acompanhar o progresso.
5. Você não precisa esperar a conclusão do pull request neste percurso. Pode voltar a ele mais tarde. Se quiser se aprofundar no gerenciamento de trabalho assíncrono com agentes, continue no [percurso do agente de nuvem](../../cloud/).

## Resumo e próximos passos

Usar comandos de barra no Copilot CLI permite configurá-lo, compartilhar sessões e obter informações internas sobre como o Copilot está trabalhando. Nesta lição, você usou ou explorou:

- `/share` para criar uma GitHub gist e compartilhar sua sessão com a equipe.
- `/context` para ver o contexto que o Copilot CLI está usando no momento.
- `/model` para explorar a lista de modelos disponíveis e selecionar outro, se quiser.
- `/delegate` como uma ponte opcional para o agente de nuvem.

É claro que há mais comandos de barra disponíveis e muito mais para explorar no Copilot CLI. Vamos encerrar essa jornada [revendo o que aprendemos][next-lesson] e vendo alguns próximos passos para continuar aprendendo.

## Recursos

- [Usar o Copilot CLI][using-copilot-cli]
- [Sobre o Copilot CLI][about-copilot-cli]
- [Gerenciamento de contexto no Copilot CLI][context-management]
- [Compartilhar sessões com o Copilot CLI][share-sessions]
- [Selecionar modelos no Copilot CLI][selecting-models]

[previous-lesson]: ../6-custom-agents/
[next-lesson]: ../8-review/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[about-cloud-agent]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
[share-sessions]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#share-sessions
[selecting-models]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#select-an-llm
