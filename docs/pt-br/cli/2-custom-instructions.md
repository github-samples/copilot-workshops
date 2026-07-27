---
title: "Lição 2 - Instruções personalizadas (Copilot CLI)"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

[Lição anterior: Instalar o Copilot CLI ←][previous-lesson] · [Próxima lição: Gerar código com a CLI →][next-lesson]

O contexto é essencial ao trabalhar com IA generativa. Se uma tarefa precisar ser executada de uma maneira específica — ou se houver informações de contexto que o Copilot deva conhecer — você deve garantir que esse contexto esteja disponível. Há várias ferramentas para ajudar o Copilot, e você as explorará ao longo deste workshop. Vamos começar pelos [arquivos de instruções][instruction-files], que normalmente se concentram em como o próprio código deve ser estruturado. Isso ajuda o Copilot a entender não apenas *o que* você quer, mas também *como* o código deve ser organizado.

Nesta lição, você irá:

- explorar como o contexto específico do projeto, as diretrizes de programação e os padrões de documentação chegam ao Copilot por meio de instruções personalizadas do repositório e de arquivos de instrução com escopo por caminho,
- gerar a primeira parte dos dados de filtragem (um helper de editoras) com as instruções *atuais* em vigor,
- adicionar um novo padrão válido para todo o repositório em `.github/copilot-instructions.md`,
- executar um prompt de acompanhamento e observar o código regenerado adotar o novo padrão,
- fazer commit das atualizações de instruções e do helper para que a próxima lição possa se apoiar nelas.

> [!CAUTION]
> O código gerado pode divergir de alguns dos padrões que você definir. O Copilot é não determinístico. O objetivo é observar a *tendência* de mudança de comportamento após atualizar as instruções, e não reproduzir a saída caractere por caractere.

## Arquivos de instruções

### Cenário

Como toda boa equipe de desenvolvimento, a Tailspin Toys tem um conjunto de diretrizes e requisitos para as práticas de desenvolvimento. Entre eles:

- A camada de dados sempre precisa de testes unitários.
- A interface do usuário deve usar modo escuro e ter um visual moderno.
- A documentação deve ser adicionada ao código na forma de comentários TSDoc.
- Um bloco de comentários deve ser adicionado ao início de cada arquivo para descrever o que ele faz.

Com o uso de arquivos de instruções, você garantirá que o Copilot tenha as informações corretas para executar as tarefas de acordo com as práticas destacadas.

### Instruções personalizadas

As instruções personalizadas permitem fornecer contexto e preferências ao Copilot, para que ele entenda melhor seu estilo de programação e seus requisitos. Esse é um recurso poderoso para orientar o Copilot a gerar sugestões e trechos de código mais relevantes. Você pode especificar suas convenções de programação preferidas, bibliotecas e até os tipos de comentários que gosta de incluir no código. É possível criar instruções para todo o repositório ou para tipos específicos de arquivo, oferecendo contexto no nível da tarefa.

Há dois tipos de arquivos de instruções:

- `.github/copilot-instructions.md`, um único arquivo de instruções enviado ao Copilot em **toda** solicitação do repositório. Esse arquivo deve conter informações no nível do projeto — contexto relevante para a maioria das solicitações enviadas ao Copilot por chat ou pela CLI. Isso pode incluir a stack usada, uma visão geral do que está sendo criado, boas práticas e outras orientações globais.
- Arquivos `.github/instructions/*.instructions.md` podem ser criados para tarefas ou tipos de arquivo específicos. Você pode usá-los para fornecer orientações para determinadas linguagens, como TypeScript ou Astro, ou para tarefas como criar um componente de UI ou um novo conjunto de testes unitários.

> [!NOTE]
> Ao trabalhar no IDE, os arquivos de instruções são usados apenas para geração de código no Copilot Chat — não para autocompletar nem para sugestões da próxima edição.
>
> O Copilot Chat, o Copilot CLI e o agente de nuvem do Copilot usam tanto os arquivos no nível do repositório quanto os arquivos `*.instructions.md` (com frontmatter `applyTo`) ao gerar código.
>
> Por fim, o Copilot [também oferece suporte a arquivos de instruções que seguem outros padrões][custom-instructions-support], incluindo arquivos `AGENTS.md` e `CLAUDE.md`.

### Boas práticas para gerenciar arquivos de instruções

Uma discussão completa sobre como criar arquivos de instruções está além do escopo deste workshop. Ainda assim, os exemplos fornecidos no projeto de exemplo mostram uma abordagem representativa. Em alto nível:

- Mantenha as instruções em `copilot-instructions.md` focadas em orientações no nível do projeto, como uma descrição do que está sendo criado, a estrutura do projeto e padrões globais de programação.
- Use arquivos `*.instructions.md` para fornecer instruções específicas para tipos de arquivo (testes unitários, componentes Astro, a camada de dados) ou para tarefas específicas.
- Use linguagem natural. Mantenha as orientações claras. Forneça exemplos de como o código deve — e não deve — ser escrito.

Não existe uma forma única de criar arquivos de instruções, assim como não existe uma forma única de usar IA. Com experimentação, você descobrirá o que funciona melhor para o seu projeto.

> [!TIP]
> Todo projeto que usa o GitHub Copilot deveria ter uma coleção robusta de arquivos de instruções. Ao explorar os arquivos deste projeto, você pode notar que há instruções para vários tipos de tarefas, incluindo [atualizações de UI][ui-instructions] e [Astro][astro-instructions].
>
> O Copilot também pode ajudar a gerar arquivos de instruções para você. Cada superfície expõe isso de uma forma diferente, por exemplo **Configure Chat → Generate Agent Instructions** no VS Code ou `/init` no Copilot CLI — a lição do ambiente em que você está destacará isso quando for relevante.
>
> Procura modelos ou um ponto de partida? Explore o [awesome-copilot][awesome-copilot], um repositório repleto de arquivos de instruções, agentes personalizados e outros recursos.

[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[awesome-copilot]: https://github.com/github/awesome-copilot
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support

## Explorar os arquivos de instruções personalizadas deste projeto

Reserve um momento para ler os arquivos de instruções incluídos neste repositório — há um `copilot-instructions.md` principal e uma coleção de arquivos `*.instructions.md` para várias tarefas. Abra-os no editor ou na interface web do GitHub.

1. Abra `.github/copilot-instructions.md`.
2. Explore o arquivo e observe a breve descrição do projeto, além de seções como **Agent notes**, **Code standards**, **Scripts** e **Repository Structure**. Em **Code standards**, observe a orientação aninhada de **GitHub Actions Workflows**. Tudo isso se aplica a qualquer interação sua com o Copilot.
3. Abra a pasta `.github/instructions` e explore seu conteúdo. Observe que há instruções para arquivos Astro, para a camada de dados com Drizzle, para testes e muito mais.
4. Abra `.github/instructions/unit-tests.instructions.md`. Observe o campo `applyTo` no topo — ele define um glob (relativo à raiz do repositório) que determina a quais arquivos as instruções se aplicam. Aqui, qualquer arquivo de teste TypeScript, por exemplo um que corresponda a `**/*.test.ts`, será incluído.
5. Observe as instruções específicas para criar testes unitários neste projeto.
6. Por fim, abra `.github/instructions/drizzle.instructions.md` e role até o final. Observe os links para outros arquivos de instruções, como `unit-tests.instructions.md`, e para arquivos existentes no projeto. Isso permite dividir conjuntos maiores de instruções em arquivos menores e reutilizáveis, além de apontar o Copilot para exemplos a serem seguidos na geração de código. (Nesse caso, os caminhos são relativos ao arquivo de instruções, e não à raiz do repositório.)

> [!NOTE]
> A seção **Code formatting requirements** em `copilot-instructions.md` documenta os padrões de programação do projeto, mas ainda não exige documentação no código. Nas próximas etapas, você adicionará regras para comentários TSDoc e cabeçalhos de comentário no nível do arquivo.

## Criar uma branch

Você fará alterações no código, então crie uma branch para trabalhar.

1. No terminal do codespace, crie e troque para uma nova branch:

   ```bash
   git checkout -b update-custom-instructions
   ```

2. Confirme que o Copilot CLI está instalado e autenticado:

   ```bash
   copilot --version
   ```

   Se o comando não for encontrado ou se você ainda não tiver feito login, volte para a [Lição 1 - Instalar o GitHub Copilot CLI](../1-install-copilot-cli/).

## Usar o Copilot CLI *antes* de atualizar as instruções

Para ver o impacto das instruções personalizadas, comece gerando código com as instruções atuais em vigor. Mais tarde, você atualizará o arquivo e executará um prompt de acompanhamento.

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

1. Verifique se a sessão do Copilot CLI está em execução a partir da **raiz do repositório**, para que ela carregue `.github/copilot-instructions.md` automaticamente.
2. No prompt do Copilot CLI, peça que ele gere o helper de editoras que a UI de filtragem usará:

   ```plaintext
   Create a new data-access helper at src/lib/publishers.ts to return a list of all publishers. It should return the name and id for all publishers. Do not run the tests yet.
   ```

3. O Copilot CLI explorará o projeto, proporá um plano e escreverá o arquivo nesta sessão com `--yolo`. Acompanhe as alterações na saída do terminal e depois revise o resultado no editor.
4. Abra no editor o arquivo gerado `src/lib/publishers.ts`.
5. Observe que o helper é uma função tipada que recebe um cliente `db` como primeiro argumento e retorna um array tipado de editoras — isso vem das convenções da camada de dados em `.github/instructions/drizzle.instructions.md` (que se aplica a `src/lib/*.ts`).
6. Observe que no código gerado **faltam** comentários TSDoc e um cabeçalho de comentário no nível do arquivo.

> [!CAUTION]
> O Copilot é probabilístico — há uma chance de ele adicionar comentários de documentação mesmo sem receber essa instrução. Se isso acontecer, tudo bem. O principal aprendizado continua sendo a melhora de *consistência* depois da atualização das instruções.

## Adicionar um novo padrão ao repositório

Como destacado anteriormente, `.github/copilot-instructions.md` foi criado para fornecer informações no nível do projeto ao Copilot. Vamos garantir que os padrões de programação do repositório estejam documentados para melhorar as sugestões de código.

1. Abra novamente `.github/copilot-instructions.md`.
2. Localize a seção **Code formatting requirements**, que deve estar perto da linha 27. Observe como ela documenta os padrões de programação do projeto, mas ainda não traz nenhuma regra para documentação no código, e é por isso que o helper gerado não tinha comentários de documentação.
3. Adicione as linhas de markdown a seguir logo abaixo dos padrões existentes para instruir o Copilot a incluir cabeçalhos de comentário no arquivo e comentários TSDoc:

   ```markdown
   - Every exported function should have a TSDoc comment describing its purpose, parameters, and return value.
   - Before imports or any code, add a comment block to the file that explains its purpose.
   ```

4. Salve `copilot-instructions.md`.

> [!TIP]
> Como você viu na lição anterior, arquivos de instruções podem ser criados no nível do repositório (`.github/copilot-instructions.md`) para orientações globais, ou como arquivos `*.instructions.md` para linguagens, tipos de arquivo ou tarefas específicas. O arquivo do repositório é o local certo para padrões válidos em todo o projeto, como a regra de comentários de documentação que você acabou de adicionar.

## Executar o prompt novamente e observar a mudança

Agora que as instruções incluem uma regra para comentários de documentação, peça ao Copilot CLI para atualizar o arquivo de editoras que você acabou de gerar. A mesma diretriz de padrões orientará a reescrita.

1. Envie `/clear` na sessão do Copilot CLI para começar com uma conversa limpa.
2. Envie o prompt a seguir:

   ```plaintext
   Update src/lib/publishers.ts to follow the latest documentation conventions in .github/copilot-instructions.md.
   ```

3. Aguarde a edição terminar e depois abra novamente `src/lib/publishers.ts`.
4. Observe que o arquivo agora começa com um bloco de comentários parecido com este:

   ```typescript
   /**
    * Helpers de acesso a dados de editoras para a plataforma de financiamento coletivo Tailspin Toys.
    * Fornece funções para recuperar informações de editoras do banco de dados.
    */
   ```

5. Observe que a função gerada agora inclui um comentário TSDoc parecido com este:

   ```typescript
   /**
    * Retorna uma lista de todas as editoras com id e nome.
    *
    * @param db - O cliente de banco de dados Drizzle.
    * @returns Uma promessa que resolve para um array de objetos de editora.
    */
   ```

6. Mantenha esse arquivo atualizado como está. Essa é a primeira parte dos dados em que você se apoiará na próxima lição.

## Fazer commit e push desta primeira parte da filtragem

1. No terminal, verifique os arquivos alterados:

   ```bash
   git status
   ```

2. Adicione a atualização das instruções e o helper à área de stage:

   ```bash
   git add .github/copilot-instructions.md src/lib/publishers.ts
   ```

3. Faça commit das alterações:

   ```bash
   git commit -m "Add doc comment standards and publishers helper foundation"
   ```

4. Envie a branch:

   ```bash
   git push -u origin update-custom-instructions
   ```

## Resumo e próximos passos

Você explorou como o Copilot recebe contexto dos arquivos de instruções deste projeto e depois usou o Copilot CLI para:

- gerar a base de um helper de acesso a dados de editoras para a filtragem com as instruções *existentes*,
- adicionar um novo padrão válido para todo o repositório em `.github/copilot-instructions.md`,
- executar um prompt de acompanhamento e observar o código regenerado adotar o novo padrão,
- fazer commit e push tanto da atualização das instruções quanto da base do helper.

Em seguida, você aplicará essas instruções ao implementar trabalho do backlog na [lição de geração de código][next-lesson].

## Recursos

- [Arquivos de instruções para personalização do GitHub Copilot][instruction-files]
- [Boas práticas para criar instruções personalizadas][instructions-best-practices]
- [5 dicas para escrever instruções personalizadas melhores para o Copilot][copilot-instructions-five-tips]
- [Awesome Copilot — uma coleção de arquivos de instruções e outros recursos][awesome-copilot]

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-generating-code/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[copilot-instructions-five-tips]: https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/
