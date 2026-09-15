---
title: "Lição 2 - Adicionar avaliações por estrelas: uma melhoria rápida"
description: "Inicie sua primeira sessão de agente no aplicativo GitHub Copilot, faça uma pequena alteração nos cards dos jogos e integre-a como seu primeiro pull request."
authors:
  - geektrainer
lastUpdated: 2026-07-09
---

Na lição anterior, você conheceu o espaço de trabalho e usou um chat rápido. Agora é hora de iniciar uma **sessão de agente** e fazer sua primeira alteração no projeto. A mudança será pequena: os dados dos jogos já têm uma avaliação por estrelas, mas os cards dos jogos na página inicial ainda não a exibem. Você pedirá ao agente que mostre essa avaliação, revisará a alteração e fará o merge dela como seu primeiro pull request.

Nesta lição, você vai:

- iniciar uma sessão de agente e aprender como ela é estruturada.
- pedir ao agente que faça uma alteração pequena e específica no projeto.
- revisar a alteração na visualização de diff do espaço de trabalho.
- executar o aplicativo localmente para confirmar a alteração no navegador.
- abrir e fazer merge do seu primeiro pull request.

## Cenário

Cada jogo no Tailspin Toys pode ter uma avaliação por estrelas, que já aparece na página de detalhes do jogo. No entanto, os cards dos jogos na página inicial mostram apenas título, categoria, distribuidora e descrição. Como aquecimento, você fará com que o agente exiba em cada card a avaliação existente. Essa alteração pequena e independente é perfeita para sua primeira sessão.

## Anatomia de uma sessão

Uma **sessão** é uma conversa com um agente. Neste workshop, você escolhe **new working tree**, dando à sessão uma cópia de trabalho e uma branch dedicadas. Isso isola cada marco de PR sem uma branch separada para cada lição. Suas sessões aparecem na barra lateral agrupadas por repositório. Selecione qualquer uma delas para acessá-la.

Em uma sessão, você verá três elementos: a **conversa** com o agente, a **atividade de ferramentas** do agente enquanto ele explora e edita arquivos e a lista de **arquivos alterados** com os respectivos diffs.

## Iniciar uma sessão e solicitar a alteração

Vamos iniciar uma nova sessão para começar a explorar o projeto e implementar o recurso. Em uma [lição anterior][prior-lesson], você adicionou o projeto por meio do repositório do GitHub. Criaremos uma nova sessão para esse repositório e solicitaremos a alteração.

1. Volte ao aplicativo GitHub Copilot ou abra-o.
2. Selecione **Home screen**.
3. Verifique se `tailspin-toys` está selecionado como repositório.

   ![Caixa de prompt do aplicativo GitHub Copilot com o seletor de repositório definido como tailspin-toys e o seletor de modelo exibido abaixo do prompt](../../_images/app-2-start-session.png)

4. Escolha **new working tree** e o modo **Interactive** abaixo da caixa de prompt. Use o prompt a seguir para solicitar a alteração:

   ```plaintext
   Antes de editar, identifique esta cópia de trabalho e a branch, confirme que é um worktree novo e limpo, busque as atualizações de origin e avance a branch desta sessão por fast-forward até origin/main. Confirme que HEAD corresponde a origin/main. Pare e explique se houver alterações pendentes, divergências ou se não for possível atualizar; não redefina nem descarte trabalho.

   Nos cards dos jogos, mostre a avaliação por estrelas de cada jogo. O tipo Game já inclui um campo starRating: um número em uma escala de cinco, ou null quando o jogo ainda não foi avaliado. Exiba-o em cada card em src/components/GameCard.astro e, quando starRating for null, mostre "No rating yet". Mantenha a alteração pequena e não reestruture o layout do card nem altere o modelo de dados.

   Siga as instruções do repositório, adicione ou atualize os testes adequados e execute as verificações npm existentes relevantes. Examine os pré-requisitos e pergunte antes de instalar qualquer coisa. Relate os arquivos alterados e os resultados das verificações e pare para minha revisão. Não faça commit, push, não abra um pull request nem implemente outro recurso.
   ```

> [!NOTE]
> Observe que o prompt contém o nome do arquivo que o Copilot deve atualizar. Embora não seja obrigatório especificar os arquivos que o Copilot deve incluir no trabalho, indicar a direção certa ajuda o Copilot a gerar código mais rapidamente e reduz o uso de tokens.

5. Pressione <kbd>Enter</kbd> para enviar o prompt ao Copilot.

O aplicativo Copilot começa criando um novo worktree, uma cópia isolada do projeto. Em seguida, ele explora o projeto, localiza os arquivos que precisam ser atualizados e cria o código necessário para adicionar o novo recurso. Você acabou de adicionar um recurso com o aplicativo Copilot.

## Revisar o diff

Todas as alterações geradas por IA devem ser revisadas antes do merge, mesmo as pequenas. Vamos explorar as alterações diretamente no aplicativo Copilot.

1. No canto superior direito do aplicativo, selecione **Toggle review panel**. A tela de diff será aberta com todas as alterações pendentes feitas pelo Copilot.

   ![Barra de ferramentas superior do aplicativo GitHub Copilot com uma seta apontando para o botão Toggle review panel à direita de Create PR](../../_images/app-2-review-panel.png)

2. Você verá código adicionado a `GameCard.astro`, o arquivo principal usado para exibir os detalhes do jogo. Ele deve ser semelhante ao exemplo a seguir: um pequeno bloco que renderiza a avaliação quando ela existe e usa "No rating yet" quando `starRating` é `null`:

   ```astro
   {game.starRating !== null ? (
       <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-amber-900/60 text-amber-300" data-testid="game-rating">
           ★ {game.starRating} / 5
       </span>
   ) : (
       <span class="text-xs font-medium text-slate-500" data-testid="game-rating-empty">
           No rating yet
       </span>
   )}
   ```

> [!NOTE]
> Como o Copilot, assim como todas as ferramentas de IA generativa, é probabilístico, e não determinístico, o código exato pode ser diferente do exemplo. No entanto, ele deve ser relativamente semelhante.

## Verificar as alterações

Revise os resultados das verificações automatizadas do agente antes de abrir um navegador. Confirme que os testes cobrem um `starRating` numérico e a alternativa para `null`, usando os scripts npm existentes do projeto em vez de uma skill que ainda não existe. Um pré-requisito ausente ou uma verificação ignorada não conta como aprovação.

Depois, examine o aplicativo manualmente pelo terminal integrado da sessão. Identifique o worktree antes de iniciar o servidor e não reutilize um servidor de outra cópia de trabalho.

1. No painel de revisão à direita do aplicativo Copilot, selecione **Terminal**. Se não houver um botão **Terminal**, selecione **+** (identificado como **Open in panel**) e depois selecione **Terminal**.

   ![Botão Terminal no painel de revisão do aplicativo GitHub Copilot](../../_images/app-terminal-screenshot.png)

2. Digite o comando a seguir na janela do terminal para iniciar o servidor de desenvolvimento do aplicativo Web:

   ```shell
   npm run dev
   ```

3. Quando o servidor iniciar, o que levará apenas alguns instantes, abra uma janela do navegador.
4. Abra a URL local exibida pelo servidor, normalmente `http://localhost:4321`. Se a porta estiver ocupada, identifique seu responsável em vez de interromper um processo não relacionado.
5. Confirme que os cards de jogos avaliados mostram a nota em uma escala de cinco. Quando houver dados sem avaliação, confirme que **No rating yet** aparece; caso contrário, use o teste automatizado para verificar o caso null em vez de afirmar que o observou.
6. Volte à janela do terminal.
7. Pressione <kbd>Control</kbd>+<kbd>C</kbd> (Mac) ou <kbd>Ctrl</kbd>+<kbd>C</kbd> (Windows/Linux) para interromper o servidor de desenvolvimento que você iniciou.

## Abrir e fazer merge do primeiro pull request

A alteração está correta. Agora é hora de entregar o PR 1. Primeiro, autorize o commit e o PR separadamente da implementação:

```plaintext
Revise o diff completo da alteração de avaliações por estrelas e seus testes, resuma a verificação e faça commit das alterações revisadas na branch desta sessão. Envie a branch e crie um pull request destinado a main usando o modelo de PR do repositório. Não faça o merge.
```

1. Abra o link do PR criado na sessão. Se o aplicativo apresentar uma confirmação **Create PR**, selecione-a para aprovar a solicitação em vez de criar um segundo PR.
2. Se solicitado, selecione **Sign in with your browser** e siga as instruções para se autenticar.
3. O Copilot começará a criar o PR.

Após a criação do PR, examine o diff completo e as verificações em **My work**. Leia os resultados dos fluxos de trabalho do repositório do participante; aguarde as verificações e revisões obrigatórias e resolva falhas antes do merge. **Ready to merge** não substitui a revisão da alteração ou das evidências locais.

4. Selecione o indicador **PR** logo acima do chat para abrir o PR no painel de revisão e visualizá-lo. Faça as revisões necessárias nesse painel.
5. Quando estiver tudo pronto, selecione **Ready to merge**.
6. Na nova caixa de diálogo, selecione **Merge pull request** para fazer o merge do pull request.

Confirme que o PR 1 foi integrado a `main` antes de continuar. Fazer merge no repositório do participante não implanta um site por si só. A próxima lição inicia um worktree novo e o atualiza a partir de `origin/main` para incluir esse PR.

## Resumo e próximos passos

Você iniciou sua primeira sessão de agente e entregou sua primeira alteração. Especificamente, você:

- iniciou uma sessão de agente e aprendeu como as sessões são estruturadas.
- orientou o agente a fazer uma alteração pequena e específica nos cards dos jogos.
- revisou a alteração na visualização de diff do espaço de trabalho.
- executou o aplicativo localmente para confirmar a avaliação por estrelas no navegador.
- abriu o PR 1, revisou as verificações e fez o merge explicitamente.

Em seguida, você usará o aplicativo para adicionar um padrão de instruções personalizadas ao repositório, começando por uma das issues do backlog. Continue para a [Lição 3 - Orientar o Copilot com instruções personalizadas][next-lesson].

## Recursos

- [Trabalhar com sessões de agente no aplicativo GitHub Copilot][agent-sessions]
- [Sobre o aplicativo GitHub Copilot][about-copilot-app]
- [Gerenciar issues e pull requests com o aplicativo GitHub Copilot][managing-issues-prs]

[prior-lesson]: ../1-install-copilot-app/#instalar-e-configurar-o-aplicativo-github-copilot
[previous-lesson]: ../1-install-copilot-app/
[next-lesson]: ../3-custom-instructions/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests