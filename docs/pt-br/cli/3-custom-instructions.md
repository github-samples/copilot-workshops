---
title: "Lição 3 - Orientar o Copilot com instruções personalizadas"
description: "Adicione uma convenção de documentação específica, demonstre-a em código existente e integre o segundo pull request."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

O contexto ajuda o Copilot a entender não apenas *o que* criar, mas *como* sua equipe espera que o código seja escrito. Você adicionará uma convenção de documentação específica, observará seu efeito em código real e integrará as instruções e a demonstração juntas como PR 2.

Nesta lição, você vai:

- explorar instruções gerais do repositório e com escopo de caminho.
- adicionar um padrão de documentação sem implementar a filtragem antes da hora.
- demonstrar o padrão em uma pequena função auxiliar ou componente existente.
- validar e integrar o marco de instruções.

## Cenário

A equipe da Tailspin Toys quer que a documentação útil do código seja uma convenção repetível, não uma solicitação que alguém precise lembrar em cada conversa. Você adicionará o padrão às instruções do repositório e o demonstrará no código existente, sem mudar o comportamento nem começar a filtragem antes da hora.

## Explorar as instruções

O repositório já contém dois tipos úteis de instruções:

- `.github/copilot-instructions.md` fornece contexto geral do repositório, como tecnologias, estrutura e práticas comuns.
- `.github/instructions/*.instructions.md` fornece orientações de escopo limitado. Um glob `applyTo` no frontmatter identifica os arquivos aos quais as instruções se aplicam.

Abra estes arquivos no editor:

1. Leia `.github/copilot-instructions.md` e localize os padrões atuais de código e verificação.
2. Explore `.github/instructions/`, incluindo as orientações de Astro, camada de dados e testes.
3. Em `unit-tests.instructions.md`, examine o padrão `applyTo` e as convenções de teste.
4. Em `drizzle.instructions.md`, examine os padrões de acesso a dados e as referências a exemplos.

Mantenha as instruções gerais concisas, coloque detalhes específicos de arquivos no arquivo de escopo relevante e evite cópias conflitantes da mesma regra. A [referência de suporte a instruções do GitHub][instruction-support] explica quais formatos cada ambiente suporta.

> [!NOTE]
> As instruções influenciam a geração; elas não garantem conformidade. Sua revisão verificará tanto o texto das instruções quanto seu efeito no código. Se o Copilot já produzir bons comentários, o objetivo da lição é tornar a convenção explícita e repetível, não forçar uma falha para comparar antes e depois.

## Partir do PR 1 integrado

Confirme que o PR de avaliações por estrelas foi integrado. No terminal do repositório do participante, inicie o próximo marco a partir de `main` atualizado:

```bash
git status
git switch main
git pull --ff-only
git switch -c update-custom-instructions
copilot --enable-all-github-mcp-tools
```

Se a árvore de trabalho não estiver limpa ou a atualização falhar, resolva esse estado antes de continuar. Permaneça no modo **Interactive**.

Na aba **Issues** do repositório, encontre **Update our repository coding standards** e copie sua URL real. A issue fornece o contexto mais amplo: explicar a intenção, documentar funções exportadas da camada de dados e contratos de componentes e manter os comentários atualizados. Esta lição aborda uma parte limitada da documentação, não uma refatoração de todo o repositório ou a promessa de concluir todos os critérios da issue.

## Adicionar a convenção de documentação

Substitua o marcador pela URL real da issue e envie:

```plaintext
Leia esta issue de padrões de código como contexto: <coding-standards-issue-URL>. Examine as instruções existentes do repositório e de escopo limitado. Adicione uma convenção de documentação específica: explique a intenção em vez de repetir o código, documente funções exportadas em db/ e src/lib/ com TSDoc/JSDoc cobrindo propósito, parâmetros e valores de retorno, documente os contratos de Props dos componentes reutilizáveis de Astro e mantenha os comentários atualizados quando o código relacionado mudar.

Coloque cada regra no arquivo de instruções existente adequado e evite duplicações ou contradições. Preserve os padrões existentes de formatação e lint; inclua um link ou resumo da convenção de documentação em README quando apropriado. Limite esta alteração ao padrão de documentação, não a uma migração de ferramentas de formatação ou reescrita de todo o repositório. Não crie uma skill ou agente, não implemente a filtragem, não faça commit, push nem abra um PR. Pare para que eu possa examinar as instruções antes da demonstração.
```

Examine o diff. A convenção deve incentivar comentários úteis, não exigir um cabeçalho genérico em todos os arquivos ou comentários que apenas repitam código óbvio. Peça correções antes de prosseguir.

## Demonstrar a convenção em código real

Escolha uma pequena função auxiliar exportada ou um componente reutilizável existente após examinar o repositório. Não precisa ser uma função auxiliar de distribuidoras, e não há exigência de que `src/lib/publishers.ts` já exista.

Envie:

```plaintext
Usando as instruções atualizadas, selecione uma pequena função auxiliar exportada ou componente reutilizável de Astro existente que se beneficiaria de uma documentação mais clara. Aplique a convenção diretamente a esse arquivo sem mudar o comportamento em execução ou adicionar filtragem. Explique qual instrução orientou a alteração e pare antes de fazer commit ou abrir um PR.
```

Abra o arquivo real alterado. Para uma função auxiliar, verifique se os comentários descrevem corretamente os parâmetros, o valor de retorno e qualquer argumento de banco de dados injetado. Para um componente, verifique se seu contrato de `Props` está documentado. Confirme que a explicação corresponde ao código, em vez de apenas procurar um bloco de comentários.

> [!TIP]
> Um trecho ilustrativo no chat não é a demonstração: examine uma alteração real do repositório. Se o código selecionado já atender à convenção, escolha outro alvo pequeno existente em que uma melhoria seja justificada, em vez de adicionar comentários redundantes.

## Validar e integrar o PR 2

Peça ao Copilot que valide as alterações revisadas:

```plaintext
Revise as alterações de instruções e a pequena demonstração de documentação. Confirme que o comportamento em execução não mudou. Examine package.json, execute npm run lint e npm run typecheck:all e execute os testes existentes afetados quando a alteração de código justificar. Relate os comandos exatos e os resultados. Não instale nada, não crie uma skill, não faça commit, push nem abra um PR ainda.
```

Resolva falhas e examine o diff final. Depois, autorize o marco:

```plaintext
Faça commit apenas das instruções de documentação revisadas, da atualização diretamente relacionada de README e da pequena demonstração de código. Envie a branch atual e crie um PR para main seguindo o modelo de PR do repositório. Inclua os resultados de verificação e referencie a issue de padrões de código como contribuição parcial; não use uma palavra-chave de fechamento, a menos que todos os critérios da issue estejam realmente satisfeitos. Não faça o merge nem comece a filtragem.
```

Abra a URL do PR, examine **Files changed** e revise a CI. Depois que todas as verificações e revisões obrigatórias passarem, faça o merge no GitHub e confirme que o PR 2 está **Merged**. Saia da sessão da CLI com `/exit`. Não inicie o próximo marco até este PR ser integrado.

## Resumo e próximos passos

A convenção de documentação e uma demonstração real agora estão em `main`. Em seguida, você [criará a filtragem com Plan e Autopilot][next-lesson] em uma branch nova baseada nesse estado integrado.

## Recursos

- [Adicionar instruções personalizadas ao repositório][repository-instructions] explica orientações gerais e com escopo de caminho.
- [Awesome Copilot][awesome-copilot] oferece exemplos para revisar e adaptar, não adotar cegamente.

[previous-lesson]: ../2-add-star-rating/
[next-lesson]: ../4-build-filtering/
[instruction-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[repository-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[awesome-copilot]: https://github.com/github/awesome-copilot
