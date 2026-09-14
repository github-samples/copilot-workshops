---
title: "Lição 8 - Criar e integrar o PR do recurso"
description: "Revise a filtragem, a skill, o perfil QA e os testes em conjunto, crie o PR 3 e autorize explicitamente o Agent Merge."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

A implementação da filtragem, a skill quality-checks, o perfil QA e os testes associados estão salvos em commits de checkpoint em uma única branch. Revise-os em conjunto e use as evidências atuais de QA para preparar o PR 3. Você já fez o merge explicitamente dos PRs de avaliações por estrelas e instruções. Desta vez, usará o **Agent Merge** dentro do fluxo de PR, não como um recurso ou uma branch separados.

Nesta lição, você vai:

- aprender o que é o Agent Merge e como ele automatiza o ciclo de vida do merge.
- examinar o PR completo do recurso e as evidências de verificação.
- autorizar o Agent Merge somente após a revisão e confirmar que o PR foi integrado.

## Cenário

Nos últimos módulos, você explorou vários níveis de automação, desde a criação de código até permitir que o Copilot valide diretamente uma interface. Para acelerar ainda mais o desenvolvimento, a Tailspin Toys quer descobrir se pull requests já avaliados e validados podem ter o merge feito automaticamente.

## Apresentação do Agent Merge

O **Agent Merge** permite automatizar a etapa final de integração de um pull request por meio do aplicativo Copilot. Quando você o habilita, a sessão do aplicativo lê o pull request, resolve o que estiver bloqueando o merge, como verificações de CI com falha, comentários de revisão e a necessidade de rebase, e faz o merge assim que o GitHub permite. Ele é executado em segundo plano, continua funcionando após reinicializações do aplicativo e é desativado automaticamente quando o pull request é integrado.

Até aqui, você selecionou **Merge pull request** por conta própria. O Agent Merge pode assumir essa responsabilidade, mas sua capacidade de editar código e fazer merge ainda exige autorização explícita. Revise as ações permitidas e o trabalho antes de conceder permissão de merge.

## Revisar o marco completo

Permaneça na sessão de filtragem das Lições 4–7. Verifique o diff completo da branch em relação a `main`, não apenas o último checkpoint: ele deve conter a filtragem, `.github/skills/quality-checks/SKILL.md`, os scripts incluídos, `.github/agents/qa.agent.md` e os testes associados.

Use o seletor de agentes para voltar de **QA** ao agente geral do Copilot antes de solicitar commits ou ações de PR e mantenha o modo **Interactive**. O trabalho do perfil QA era verificar, não entregar. Mudar o agente selecionado não deve mudar a sessão, a cópia de trabalho ou a branch de filtragem.

Este workshop combina deliberadamente o trabalho do recurso e a infraestrutura reutilizável de qualidade em um PR. Uma equipe de produção poderia separá-los; aqui, os commits de checkpoint preservam etapas revisáveis sem branches empilhadas ou PRs adicionais.

Revise o relatório de QA da Lição 7. Reutilize suas evidências apenas se cobrirem a revisão final a ser enviada, com as quatro verificações e as observações relevantes no navegador concluídas. Se alterações de código, conflitos ou correções de CI modificarem o que foi testado, repita as verificações e observações afetadas e atualize as evidências. Um relatório **NO-GO** com falhas ou bloqueios não é aprovação de merge.

Quando o diff e as evidências estiverem prontos, envie:

```plaintext
Revise o diff completo da branch de filtragem em relação a main, incluindo o recurso de filtragem, a skill quality-checks e seus scripts, a definição do agente QA e os testes associados. Resuma os critérios da issue, os esclarecimentos aprovados e as evidências atuais de QA. Reutilize a verificação apenas se ela ainda se aplicar à revisão final; relate evidências desatualizadas, ausentes ou com falhas antes de prosseguir.

Se as alterações revisadas e a verificação estiverem prontas, faça commit de quaisquer alterações aprovadas restantes do marco, envie esta branch e crie um único PR do recurso destinado a main, usando o modelo de PR do repositório e a URL real da issue de filtragem. Mantenha o histórico de checkpoints nesta branch. Não use uma skill de contribuição, não crie outra branch ou PR nem faça o merge ainda.
```

Abra o PR em **My work** e examine **Files changed**, a descrição, as revisões e os resultados das verificações. Examine os próprios arquivos de fluxo de trabalho do Tailspin Toys e as verificações obrigatórias; não presuma que toda verificação local ou observação do navegador é executada na CI. O build Astro e o verificador de links que publicam o workshop pertencem a outro repositório e não validam este recurso.

## Usar o Agent Merge para gerenciar o PR

Após revisar o PR existente, configure o Agent Merge nesta mesma sessão. Não crie um segundo PR.

1. Volte à sessão de filtragem e confirme que ela está vinculada ao PR 3.
2. Abra o menu suspenso de ações de PR no canto superior direito. Antes de existir um PR, ele fica ao lado de **Create PR**; o rótulo pode mudar quando um PR está vinculado.
3. Selecione **Agent merge** para habilitá-lo.
4. Revise as permissões disponíveis, incluindo **Address reviews**, **Fix CI failures**, **Resolve conflicts** e **Merge pull request**. Mantenha a permissão de merge desativada enquanto houver achados ou verificações pendentes.
5. Antes de iniciá-lo, envie o escopo e a autorização a seguir e selecione **Agent merge**:

   ```plaintext
   Gerencie este PR de filtragem existente com o Agent Merge. Resolva bloqueios de revisão ou CI apenas dentro do escopo deste PR. Não enfraqueça testes ou requisitos e pergunte antes de alterações não relacionadas ou instalações. Qualquer alteração na revisão testada exige atualizar as verificações relevantes e as evidências do navegador; não trate resultados antigos de QA como prova de código alterado.

   Não faça o merge até eu habilitar explicitamente Merge pull request após revisar o diff final e as evidências. Não crie outro PR nem comece a tarefa do canvas.
   ```

6. Revise as alterações posteriores e os resultados atualizados. Quando o diff final estiver aprovado, a CI e as revisões obrigatórias passarem e as evidências de QA se aplicarem àquela revisão, autorize explicitamente o merge selecionando o menu suspenso ao lado de **Agent merge** e depois **Merge pull request**.

   ![Menu suspenso Agent merge mostrando as ações permitidas ao agente — Address reviews, Fix CI failures, Resolve conflicts — com uma seta apontando para Merge pull request](../../_images/app-agent-merge-merge.png)

7. Confirme que o GitHub mostra o PR 3 como **Merged**, não apenas apto para merge ou na fila. O Agent Merge não contorna proteções do repositório nem permissões ausentes; resolva esses bloqueios antes de continuar.

Somente após esse merge você deve iniciar o marco do canvas. A Lição 9 cria um worktree novo e avança sua branch de sessão por fast-forward até o `origin/main` mais recente para que o canvas comece com o recurso completo integrado.

## Resumo e próximos passos

Você automatizou várias partes do processo de desenvolvimento, incluindo a geração, o teste e a validação de código e, agora, o processo de pull request. Você:

- aprendeu o que é o Agent Merge e como ele automatiza o ciclo de vida do merge.
- revisou o diff completo de filtragem, skill, perfil QA e testes como PR 3.
- reutilizou as evidências atuais de QA, examinou a CI e autorizou explicitamente o Agent Merge.

Em seguida, você explorará **canvases**, uma maneira mais completa de planejar e visualizar o trabalho com o agente. Continue para a [Lição 9 - Criar um canvas de triagem][next-lesson].

## Recursos

- [Gerenciar issues e pull requests com o aplicativo GitHub Copilot][managing-issues-prs]
- [Sobre o aplicativo GitHub Copilot][about-copilot-app]

[previous-lesson]: ../7-qa-agent/
[next-lesson]: ../9-canvases/
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app