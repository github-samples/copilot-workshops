---
title: "Lição 8 - Criar e integrar o PR do recurso"
description: "Revise todo o marco de filtragem, reutilize as evidências atuais de QA e integre o terceiro pull request após a CI e a revisão."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Agora reúna o marco de filtragem no PR 3. Permaneça na branch e na cópia de trabalho usadas nas Lições 4–7. Elas contêm a implementação de filtragem, a skill quality-checks e seus scripts, o perfil de QA e os testes associados.

Nesta lição, você vai:

- revisar o diff do marco completo e as evidências atuais de QA.
- solicitar um PR de recurso e examinar suas verificações e comentários de revisão.
- integrar explicitamente o PR revisado e atualizar o `main` local.

## Cenário

O trabalho de filtragem está distribuído em vários checkpoints, mas os revisores precisam avaliar um recurso completo. A Tailspin Toys quer um PR que conecte os requisitos, a implementação, as verificações reutilizáveis e os achados de QA. Você preparará essa entrega e resolverá os bloqueios antes de integrar.

Esta é uma solicitação normal de PR com escopo delimitado que usa as convenções do repositório. Ela não exige uma skill de contribuição.

> [!NOTE]
> Uma equipe de produção poderia separar um recurso da infraestrutura de qualidade reutilizável. Este workshop os combina deliberadamente para mostrar o fluxo completo em um único PR de recurso. Os PRs anteriores de avaliações por estrelas e instruções já devem estar integrados em `main`, não aparecer novamente como trabalho não relacionado.

## Verificar prontidão e evidências

1. Revise o parecer de QA e o mapeamento entre requisitos e evidências. Um **NO-GO**, evidências de navegador ausentes ou uma verificação obrigatória ignorada é um bloqueio a resolver antes do merge.
2. Confirme que as quatro verificações realmente foram executadas pela skill quality-checks: lint, testes de unidade, E2E e verificações de tipos.
3. Revise a revisão testada e quaisquer alterações posteriores às verificações. Reutilize as evidências atuais de QA apenas enquanto o código testado, os testes e os scripts de verificação permanecerem inalterados. Um commit de checkpoint por si só não invalida conteúdos idênticos dos arquivos, mas alterações de código invalidam.
4. Se a implementação ou as entradas testadas mudaram, execute novamente as verificações relevantes da skill e as observações no navegador e atualize as evidências. Não repita toda a suíte apenas porque está abrindo um PR quando os resultados atuais de QA ainda se aplicam.
5. Examine o diff completo da branch, não apenas o último checkpoint ou as alterações sem commit.

Em outro terminal na mesma cópia de trabalho:

```bash
git status
git fetch origin
git log --oneline origin/main..HEAD
git diff --stat origin/main...HEAD
git --no-pager diff origin/main...HEAD
```

A comparação com três pontos mostra as alterações desta branch desde o ancestral comum com `origin/main`, incluindo checkpoints anteriores. Verifique se inclui apenas o marco de filtragem pretendido. Examine também os arquivos novos; arquivos inesperados não rastreados ou sem commit precisam ser revisados antes de adicioná-los à área de preparação.

## Solicitar o PR 3

A Lição 7 retornou você a uma sessão **Interactive** normal antes do checkpoint. Continue nessa sessão estabelecida se o perfil de QA não estiver mais ativo e a cópia de trabalho e a branch de filtragem estiverem inalteradas. Mantenha disponíveis a URL da issue, os esclarecimentos aprovados no planejamento e o relatório atual de QA, incluindo a revisão testada e os resultados das verificações.

O perfil de QA proíbe ações de commit e PR durante QA. Se ele ainda estiver ativo, volte a uma sessão normal antes de solicitar o PR:

1. Aguarde QA ficar ocioso e digite `/exit` no prompt da CLI. Se a CLI continuar aberta porque outra sessão está ativa, conclua ou preserve esse trabalho antes de voltar ao prompt normal e pressionar <kbd>Ctrl</kbd>+<kbd>D</kbd> para encerrar esta instância da CLI.
2. No prompt do shell, permaneça na mesma cópia de trabalho e branch de filtragem. Confirme sua identidade e inicie uma sessão normal nova sem `--agent qa` nem uma opção de retomada:

   ```bash
   pwd
   git branch --show-current
   git status
   copilot
   ```

3. Confirme que você está no modo **Interactive** e que o perfil de QA não está mais ativo. Não crie outro worktree, não mude de branch nem retome a sessão de QA.

Substitua todos os marcadores abaixo pela URL real da issue, os esclarecimentos aprovados e as evidências atuais de QA. Forneça-os explicitamente mesmo se tiver permanecido na sessão normal da Lição 7; uma conversa nova não deve depender da memória da sessão de QA.

```plaintext
Prepare o PR do recurso de filtragem para esta issue: <filtering-issue-URL>. Estes são os critérios de aceitação adicionais que aprovei durante o planejamento: <cole os esclarecimentos acordados ou escreva none>. Estas são as evidências atuais de QA: <cole o relatório de QA, incluindo a revisão testada, as observações no navegador, a avaliação de cobertura, os resultados das quatro verificações e quaisquer limitações>.

Confirme a cópia de trabalho e a branch de filtragem atual. Examine o diff completo em relação a main, todos os commits de checkpoint do marco, git status, o modelo de PR do repositório e as evidências de QA fornecidas. Inclua apenas a implementação de filtragem revisada, a skill quality-checks e os scripts incluídos, a definição do agente de QA e os testes associados.

Reutilize os resultados de QA enquanto eles ainda descreverem o conteúdo final dos arquivos. Se código, testes ou scripts de verificação mudaram depois, relate isso e execute as verificações relevantes pela skill e a validação de navegador afetada antes de apresentá-los como atuais. Não rotule verificações com falha, bloqueadas ou ignoradas como aprovadas.

Faça commit de quaisquer alterações revisadas restantes do marco, se necessário, envie esta branch atual e crie um único PR para main seguindo as convenções do repositório. Inclua a issue e os critérios aprovados, o resumo da implementação, os testes adicionados ou por que nenhum foi necessário, as observações no navegador, os resultados das quatro verificações e as limitações restantes. Não faça o merge, não crie outra branch, não invoque uma skill de contribuição nem comece outro recurso.
```

## Revisar o PR e a CI

Abra a URL retornada e examine **Files changed** em todo o PR. Verifique se os scripts da skill e o perfil de QA estão incluídos e se nenhuma credencial, configuração local do MCP, arquivo não relacionado, relatório gerado ou instalação de dependência entrou no diff.

Use a aba **Checks** do PR ou execute estes comandos no terminal na branch do recurso:

```bash
gh pr view
gh pr diff
gh pr checks --watch
```

Examine `.github/workflows/` no seu repositório em vez de presumir que um indicador verde cobre todos os tipos de verificação. O fluxo atual **Run tests** do Tailspin executa lint, verificações de tipos, testes de unidade do Vitest e testes E2E do Playwright contra o site estático compilado. Ele não substitui as observações diretas no navegador via MCP do relatório de QA. A compilação Astro e as verificações de links do site do workshop validam outro repositório.

Se uma verificação falhar, examine os logs e resolva a causa. Uma correção específica precisa ser revisada e verificada novamente na revisão atualizada antes do push. Se `main` mudar e a resolução de um conflito alterar o recurso, atualize também as evidências afetadas. Aguarde qualquer revisão humana obrigatória; a aprovação do próprio agente não substitui a proteção de branch.

## Integrar e atualizar o main local

Quando o PR atender a todos os requisitos de revisão e verificação, escolha explicitamente **Merge pull request** no GitHub e confirme o merge. Verifique se o PR 3 está **Merged**.

Saia da sessão da CLI com `/exit`. Com a árvore de trabalho limpa, atualize a cópia local:

```bash
git status
git switch main
git pull --ff-only
```

## Resumo e próximos passos

Não é necessária uma branch nova para a próxima lição. Você integrou exatamente três PRs do workshop: avaliações por estrelas; instruções e uma demonstração; e filtragem com a skill de qualidade, o perfil de QA e os testes.

Continue na [Lição 9 - Explorar comandos de barra e opções da CLI][next-lesson] para um percurso delimitado pelos controles da CLI, não outra tarefa de implementação.

[previous-lesson]: ../7-qa-agent/
[next-lesson]: ../9-slash-commands/
