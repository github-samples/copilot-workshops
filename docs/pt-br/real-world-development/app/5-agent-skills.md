---
title: "Lição 5 - Personalizar e usar uma skill quality-checks"
description: "Explore a skill quality-checks existente, personalize o formato do relatório e use-a para validar a filtragem."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Escrever código envolve mais do que apenas escrever código. Conseguimos validar manualmente que o código funciona e usamos arquivos de instruções para garantir que ele siga nossos padrões. Mas e os testes? O lint? Todas as outras partes da integração contínua (CI)?

Para esses tipos de tarefa, as **skills de agente** são a melhor opção! As skills ajudam o Copilot a entender como executar corretamente operações como essas.

Nesta lição, você vai:

- explorar a skill `quality-checks` existente e os scripts incluídos nela.
- personalizar o formato dos resultados.
- executar a skill e revisar sua saída.

## Cenário

A Tailspin Toys tem um conjunto de testes de unidade e de ponta a ponta que sempre precisam ser executados antes da criação de qualquer pull request (PR). Como você pode imaginar, é importante garantir que esses testes sejam executados de forma correta e consistente. A equipe já criou uma skill de agente para executar esses testes, mas quer melhorar a saída para facilitar a leitura.

## Instruções, scripts e recursos

As skills de agente reúnem instruções de tarefas reutilizáveis, scripts executáveis e recursos de apoio que um agente carrega sob demanda. Em sua essência, elas são uma pasta com o nome da skill e um arquivo Markdown chamado `SKILL.md`. O Markdown contém um frontmatter com nome e descrição para definir a skill, uma visão geral do que ela faz e orientações sobre quando deve ser chamada. A pasta também pode conter subpastas com scripts e outros recursos que a skill pode usar quando for chamada.

> [!NOTE]
> Pastas e arquivos adicionais não são obrigatórios para uma skill! Em nosso exemplo, a skill executará comandos `npm` para rodar testes e linters. Portanto, não precisamos de arquivos de apoio adicionais.

As skills podem ficar na pasta `.github/skills` de um projeto para se tornarem um recurso do repositório compartilhado e reutilizado pelo restante da equipe ou na pasta raiz do Copilot, normalmente `~/.copilot/skills`.

## Explorar a skill

Vamos explorar a skill criada pela equipe da Tailspin Toys para executar testes e linters, chamada `quality-checks`.

1. Se você ainda não tiver um canvas de **Files** aberto, selecione **+** no painel de revisão e depois **File**.
2. Pesquise `.github/skills/quality-checks/SKILL.md`.
3. Leia `name` e `description` na parte superior. Observe a descrição, que ajuda o Copilot a entender quando chamar a skill.
4. Leia as instruções e observe como elas orientam o Copilot pelo processo de testes e lint.

## Executar a skill antes de fazer uma alteração

As skills podem ser chamadas diretamente com um comando de barra (`/`) ou por meio de linguagem natural. Como você pode observar na descrição, a skill deve ser usada sempre que houver uma solicitação para executar testes ou lint. Vamos executar a skill pedindo ao Copilot que rode nossos testes!

1. Confirme que o Copilot está no modo **Interactive**, selecionando-o no menu suspenso de modo.
2. Use o prompt a seguir para pedir ao Copilot que execute os testes e o linter, o que chamará a skill:

    ```plaintext
    Run the tests and linters.
    ```

3. Observe o relatório ao final.

## Personalizar o relatório

Queremos um relatório melhor, que mostre os testes executados, as taxas de sucesso e falha e o tempo de execução. Vamos atualizar a skill para que o Copilot crie esse relatório!

1. Volte ao canvas de **Files**.
2. Se ainda não estiver aberto, abra `.github/skills/quality-checks/SKILL.md`.
3. Localize o cabeçalho **Results output formatting** na parte inferior do arquivo.
4. Logo abaixo desse cabeçalho, adicione o seguinte para garantir que os resultados sejam exibidos de acordo com nossas especificações:

    ```markdown
    Upon completion of all tests, generate a report that provides a quick overview of both success and failure of the tests, and how long they took to ran. In particular, we need sections for:

    - Unit tests, total number of tests, number succeeded, number failed, a percentage thereof, and the amount of time testing took.
    - End to end tests, total number of tests, number succeeded, number failed, a percentage thereof, and the amount of time testing took.
    - Linting, number of lines scanned, number of violations, and the percentage of lines of code that meet the linting requirements.
    ```

O arquivo será salvo automaticamente.

## Executar a skill atualizada

Com a alteração feita, vamos vê-la em ação! Usaremos exatamente o mesmo prompt de antes.

1. Confirme que o Copilot está no modo **Interactive**, selecionando-o no menu suspenso de modo.
2. Use o prompt a seguir para pedir ao Copilot que execute os testes e o linter, o que chamará a skill:

    ```plaintext
    Run the tests and linters.
    ```

3. Observe o relatório ao final.

## Resumo e próximos passos

Você personalizou e usou uma skill de agente existente. Nesta lição, você:

- explorou a skill `quality-checks` e os scripts incluídos nela.
- personalizou o formato dos resultados.
- executou a skill e revisou sua saída.

Essa alteração acompanhará a filtragem no PR do recurso. Em seguida, você permitirá que o Copilot interaja diretamente com o site [por meio do servidor MCP do Playwright][next-lesson].

## Mais exemplos de skills

Estes exemplos da comunidade são referências, não tarefas adicionais. Revise seus pré-requisitos e comportamento antes de adotá-los:

- [Especificação de Agent Skills][skill-spec].
- [Fluxo de contribuição: `make-repo-contribution`][contribution-example].
- [Documentos de requisitos: `prd`][prd-example].
- [Diagramas e um script de exportação incluído: `drawio`][drawio-example].
- [Testes de navegador: `webapp-testing`][browser-example].

O exemplo original de contribuição se chama `make-repo-contribution`; modelos antigos do Tailspin usavam outro nome, `make-contribution`. Este workshop não depende de nenhuma dessas skills de contribuição.

[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
