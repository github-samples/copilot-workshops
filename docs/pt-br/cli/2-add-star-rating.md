---
title: "Lição 2 - Adicionar avaliações por estrelas: uma melhoria rápida"
description: "Exiba as avaliações existentes dos jogos, revise e valide a alteração e integre seu primeiro pull request."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Comece com uma pequena alteração que você possa entender e verificar. O Tailspin Toys já armazena o `starRating` de cada jogo e o mostra na página de detalhes. Você exibirá esse valor existente nos cards dos jogos, incluindo uma mensagem clara quando um jogo não tiver avaliação.

Nesta lição, você vai:

- solicitar uma alteração específica em uma sessão Interactive da CLI.
- examinar o diff e verificar cards com e sem avaliação.
- fazer commit, abrir, revisar e integrar o PR 1.

## Iniciar o primeiro marco

Na raiz do repositório do participante, confirme que a árvore de trabalho está limpa, atualize `main` e crie uma branch. Se `git status` mostrar alterações inesperadas, resolva-as antes de mudar de branch; não as descarte.

```bash
git status
git switch main
git pull --ff-only
git switch -c add-star-rating
copilot --enable-all-github-mcp-tools
```

Confie no repositório quando solicitado. Verifique se está no modo **Interactive** e use `/model` para examinar os modelos disponíveis ou selecionar **Auto**. Revise as aprovações de ferramentas conforme aparecerem.

## Solicitar a alteração

Envie este prompt:

```plaintext
Nos cards dos jogos, mostre a avaliação por estrelas de cada jogo. O tipo Game já inclui um campo starRating: um número em uma escala de cinco, ou null quando o jogo ainda não foi avaliado. Exiba-o em cada card em src/components/GameCard.astro e, quando starRating for null, mostre "No rating yet". Mantenha a alteração pequena e não reestruture o layout do card.

Examine e siga as instruções do repositório. Use o modelo de dados existente; não adicione uma API de avaliações, um novo esquema ou um recurso não relacionado. Adicione ou atualize os testes adequados para os casos com e sem avaliação. Não faça commit, push nem abra um pull request ainda.
```

O Copilot deve examinar o tipo e o componente existentes antes de editar. Leia a atividade das ferramentas, além da resposta final. Um resumo confiante não comprova que a implementação está correta.

## Revisar e validar

1. Digite `/diff` e examine todos os arquivos alterados no editor ou na visualização de diff.
2. Confirme que o card usa o `starRating` existente, exibe um valor em uma escala de cinco e mostra `No rating yet` para `null`. Uma verificação baseada apenas na conversão do valor para verdadeiro ou falso pode tratar incorretamente o zero numérico como ausência de avaliação.
3. Verifique se a alteração preserva o layout do card e dá à avaliação um rótulo de texto significativo, em vez de depender apenas de uma estrela ou cor.
4. Peça ao Copilot que verifique a alteração usando as verificações existentes:

   ```plaintext
   Examine package.json e a configuração de testes e execute lint, verificações de tipos e os testes de unidade ou E2E existentes adequados a esta alteração de card. Verifique tanto as avaliações numéricas quanto a alternativa para null; relate os comandos exatos e os resultados, incluindo lacunas de cobertura ou verificações bloqueadas. Não instale nada, não mude de branch, não faça commit, push nem abra um PR.
   ```

5. Revise a saída dos comandos e as alterações de testes. Resolva falhas antes da entrega; pergunte antes de instalar pré-requisitos ausentes.

Para observar o card em um navegador, abra um segundo terminal nesta mesma cópia de trabalho e execute:

```bash
npm run dev
```

Abra a porta encaminhada no painel **Ports** do codespace. Examine os cards avaliados na página inicial. Se os dados iniciais atuais não tiverem exemplo sem avaliação, exija um teste automatizado com dados que cubram `null`; não afirme que observou um card sem avaliação. Pare o servidor de desenvolvimento com <kbd>Ctrl</kbd>+<kbd>C</kbd> no terminal dele antes de verificações E2E ou de sair da lição. Os testes automatizados do Playwright não devem reutilizar um servidor de outra cópia de trabalho.

## Criar e integrar o PR 1

Após revisar a alteração e passar nas verificações, autorize este marco separadamente:

```plaintext
Revise o diff atual e os resultados das verificações. Faça commit apenas da alteração revisada de avaliações por estrelas e seus testes, envie a branch atual e crie um pull request para main usando o modelo de PR deste repositório, se existir. Inclua o resumo da alteração e os resultados reais de verificação. Não integre o PR nem comece outra tarefa.
```

Abra a URL retornada do PR. Examine **Files changed** e os resultados das verificações, não apenas o resumo do agente. Revise as definições dos fluxos de trabalho do repositório Tailspin ao interpretar a CI; ela não substitui sua observação no navegador. Resolva falhas e verifique novamente o código alterado.

Quando o PR atender aos requisitos de revisão e verificação do repositório, selecione **Merge pull request** e confirme o merge no GitHub. Se a proteção de branch exigir outro revisor, aguarde essa aprovação. Confirme que o PR está **Merged** antes de continuar.

Saia da sessão do Copilot com `/exit`. Na próxima lição, você atualizará o `main` local antes de criar a branch de instruções; não a inicie a partir desta branch de recurso ainda não integrada.

## Resumo e próximos passos

Você concluiu o primeiro ciclo: um prompt com escopo limitado, código revisado, evidências de verificação e um PR integrado. Em seguida, [oriente o Copilot com instruções personalizadas][next-lesson] e demonstre uma convenção de documentação em um segundo PR pequeno.

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-custom-instructions/
