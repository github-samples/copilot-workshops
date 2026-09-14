---
title: "Lição 9 - Criar um canvas de triagem"
description: "Crie e revise um canvas de triagem salvo no repositório, integre o PR 4 e reabra-o para adicionar contexto de issues sem iniciar outro recurso."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Até agora, você orientou agentes pelo chat. No entanto, grande parte do trabalho não acontece em uma conversa, mas em um quadro, documento ou checklist. Os **canvases** oferecem a você e ao agente uma superfície compartilhada exatamente para esse tipo de trabalho, dentro do aplicativo. Nesta lição, você criará um canvas simples para planejar e acompanhar o backlog no qual vem trabalhando.

Nesta lição, você vai:

- entender o que é um canvas e quando usá-lo.
- criar um canvas compartilhado de quadro Kanban para fazer a triagem do backlog.
- salvar o canvas no repositório e integrá-lo para a equipe.
- reabrir o canvas e adicionar contexto de issues sem implementar outro recurso.

## Cenário

Analisar uma lista de issues pode ser desafiador. As pessoas desenvolvedoras da Tailspin Toys querem uma ferramenta para fazer a triagem de issues e adicionar seus detalhes ao contexto de uma sessão. Adicionar contexto não autoriza implementar uma issue; este exercício termina com um quadro reutilizável, não com um quinto PR.

## O que é um canvas?

Um [canvas][canvas-docs] é uma superfície interativa e compartilhada para um artefato de trabalho, como um plano, um quadro de triagem, um checklist de lançamento, um painel ou um documento. Embora o chat seja ótimo para descrever intenções e analisar ambiguidades, a maior parte do trabalho acontece em uma *superfície*. Os canvases permitem colaborar com o agente diretamente nessa superfície.

Os canvases são **bidirecionais**: o agente pode atualizar o canvas enquanto trabalha, e você pode editar a mesma superfície. Quando você cria um canvas, o agente o desenvolve com base no prompt e no fluxo de trabalho. Você pode pedir que ele adicione, remova ou revise recursos durante o processo. Depois de criado, o canvas é aberto no painel direito do aplicativo.

Alguns exemplos comuns incluem:

- **Canvases Markdown** para planejar o dia e priorizar issues e pull requests.
- **Quadros Kanban agênticos** nos quais pessoas e agentes adicionam cards e movem o trabalho entre colunas.
- **Quadros de triagem de issues** que resumem as principais issues e os temas recorrentes de um repositório.

## Por que usar um canvas?

Use um canvas quando uma tarefa exigir estrutura, iteração e verificação e o chat não for suficiente. Um canvas permite:

- fundamentar o trabalho do agente em um artefato real adequado ao seu fluxo de trabalho.
- orientar ou corrigir o trabalho diretamente na superfície compartilhada e depois permitir que o agente continue a partir das suas alterações.
- acompanhar o progresso como alterações visíveis em um artefato, e não apenas como respostas no chat.

## Criar um canvas para acompanhar o trabalho

Confirme que o PR 3 foi integrado. As avaliações por estrelas, o padrão de documentação, o recurso de filtragem, a skill de qualidade e o perfil QA devem estar em `main` antes de iniciar o canvas. Use uma sessão nova e uma branch para este último marco de PR.

1. Volte ao aplicativo GitHub Copilot ou abra-o.
2. Selecione **Home screen**.
3. Verifique se `tailspin-toys` está selecionado como repositório.
4. Escolha **new working tree** e o modo **Interactive**. Envie esta solicitação de estado inicial antes de criar arquivos:

   ```plaintext
   Prepare esta nova sessão de canvas sem implementar nada. Confirme que este é um worktree novo e limpo, busque as atualizações de origin e avance a branch da sessão atual por fast-forward até origin/main. Informe a cópia de trabalho, a branch e as revisões correspondentes de HEAD e origin/main. Verifique se o PR de filtragem foi integrado e se o recurso de filtragem, a skill quality-checks e o perfil QA estão presentes.

   Pare se houver alterações pendentes, divergências ou se o merge anterior estiver ausente. Não redefina, não descarte trabalho, não mude de branch nem crie outra branch. Pare após informar o estado inicial.
   ```

5. Verifique o relatório do estado inicial e solicite o canvas salvo no repositório:

   ```plaintext
   Crie um canvas Kanban básico de triagem salvo neste repositório usando o fluxo de extensões de canvas suportado pelo aplicativo. Salve sua definição em .github/extensions/ para que a equipe possa reutilizá-lo. Examine as extensões existentes e preserve-as; não sobrescreva o explorador de banco de dados incluído.

   Leia as issues abertas atuais. Destaque as três com maior probabilidade de precisar de atenção e mostre as demais abaixo. Inclua em cada issue destacada o título, o resumo do conteúdo, a URL e uma justificativa para sua prioridade. Trate a classificação como sugestão, não como instrução para alterar issues.

   Dê a cada card uma ação Add to current context que anexe os detalhes da issue apenas a esta sessão. Ela não deve iniciar a implementação, criar sessões ou branches, alterar o estado da issue nem criar PRs. Mantenha o escopo do canvas limitado e torne-o acessível por teclado.

   Mostre os arquivos gerados e abra o canvas para inspeção. Não altere código da aplicação, não faça commit, push nem crie um PR. Pergunte antes de instalar qualquer coisa ou adicionar dependências.
   ```

O Copilot cria os arquivos do canvas e abre a superfície compartilhada. Revise a extensão gerada antes de confiar em suas ações; ela é conteúdo executável do repositório, não apenas uma imagem.

> [!NOTE]
> Se a primeira versão precisar de melhorias, solicite alterações específicas dentro do escopo de triagem. Não transforme este exercício na implementação de uma issue do backlog.

## Inspecionar e exercitar o canvas

1. Abra **Changes** e confirme que a definição do canvas está salva no repositório em `.github/extensions/`, não apenas para seu usuário ou sessão. Verifique se as extensões existentes e os arquivos da aplicação permanecem inalterados.
2. Compare o quadro com as issues abertas reais e avalie as explicações da classificação.
3. Verifique se os cards e controles são legíveis e utilizáveis por teclado.
4. Selecione **Add to current context** em uma issue e confirme que apenas seus detalhes entram na conversa. Nenhuma implementação ou alteração de estado da issue deve começar.
5. Revise as correções e peça ao Copilot que execute a validação existente aplicável aos arquivos alterados. Registre resultados e bloqueios, em vez de presumir que uma superfície interativa está correta apenas porque abriu.

## Salvar o canvas e integrá-lo ao repositório

O canvas já é um ativo do repositório. Faça commit e envie apenas o trabalho revisado do canvas como PR 4:

1. Na mesma sessão, envie:

   ```plaintext
   Revise o diff do canvas de triagem salvo no repositório e suas evidências de validação. Faça commit dos arquivos aprovados do canvas na branch desta sessão, envie-a e crie um único PR destinado a main usando o modelo de PR do repositório. Descreva o comportamento do canvas e como verificamos que adicionar uma issue apenas adiciona contexto. Não faça o merge ainda nem implemente uma issue do backlog.
   ```

2. Revise o diff completo do PR e as verificações em **My work**. Confirme que ele contém o canvas, não trabalho da aplicação não relacionado.
3. Na mesma sessão do canvas, abra o menu suspenso de ações de PR e selecione **Agent merge**. Revise as ações permitidas e mantenha **Merge pull request** desativado até aprovar o resultado final.
4. Defina o escopo antes de iniciar o Agent Merge:

   ```plaintext
   Gerencie este PR de canvas existente com o Agent Merge. Resolva apenas bloqueios de revisão e CI dentro do escopo; pergunte antes de alterações não relacionadas ou instalações. Se o canvas mudar, repita a validação afetada e atualize as evidências. Não faça o merge até eu habilitar explicitamente Merge pull request após a revisão. Não implemente issues do backlog nem crie outro PR.
   ```

5. Selecione **Agent merge** e revise as alterações posteriores. Examine as verificações reais de CI do repositório do participante e resolva falhas; a CI não substitui o exercício do canvas.

6. Quando o diff final e as evidências atuais estiverem aprovados e as verificações e revisões obrigatórias passarem, autorize explicitamente o Agent Merge a fazer o merge selecionando seu menu suspenso e depois **Merge pull request**.

   ![Menu suspenso Agent merge mostrando as ações permitidas ao agente — Address reviews, Fix CI failures, Resolve conflicts — com uma seta apontando para Merge pull request](../../_images/app-agent-merge-merge.png)

7. Confirme que o GitHub mostra o PR 4 como **Merged** antes de continuar.

Você criou um novo canvas compartilhado para a equipe.

## Reabrir o canvas sem iniciar outro recurso

Reabra o canvas salvo no repositório na mesma sessão do canvas após o merge do PR. Esta é uma etapa de inspeção, não outra branch ou marco de PR.

1. Volte à sessão do canvas, mantenha o modo **Interactive** e feche o painel do canvas se ainda estiver aberto.
2. Envie:

   ```plaintext
   Reabra o canvas de triagem do repositório nesta mesma sessão. Adicionarei uma issue ao contexto apenas para examinar seus detalhes. Não edite arquivos, não implemente a issue, não altere seu estado, não crie outra sessão ou branch, não faça commit, push nem abra um PR.
   ```

3. Confirme que o canvas salvo abre novamente sem regenerar sua definição.
4. Selecione **Add to current context** em uma das issues que mais lhe interessam.
5. Confirme que os detalhes da issue selecionada aparecem no contexto sem iniciar a implementação. Pare aqui: o workshop tem quatro marcos de PR, não cinco.

Você usou um canvas criado por você para otimizar o processo de desenvolvimento.

## Resumo e próximos passos

Você criou uma superfície compartilhada na qual você e o agente podem colaborar. Você:

- aprendeu o que são canvases e quando usá-los.
- criou com o agente um canvas compartilhado de quadro Kanban para triagem.
- salvou o canvas no repositório e fez o merge dele com o Agent Merge.
- reabriu o canvas integrado e adicionou contexto de issues sem iniciar outro recurso.

Com o backlog acompanhado, é hora de revisar tudo o que você criou e decidir os próximos passos. Continue para a [Lição 10 - Revisão e próximos passos][next-lesson].

## Recursos

- [Trabalhar com extensões de canvas no aplicativo GitHub Copilot][canvas-docs]
- [Canvases no Awesome Copilot][awesome-copilot-canvases]
- [Sobre o aplicativo GitHub Copilot][about-copilot-app]

[previous-lesson]: ../8-create-pull-request/
[next-lesson]: ../10-review/
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[awesome-copilot-canvases]: https://awesome-copilot.github.com/extensions/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app