---
title: "Lição 10 - Revisão e próximos passos"
description: "Revise o fluxo de desenvolvimento compartilhado, os ativos reutilizáveis e os três marcos de pull request da CLI."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Você usou o Copilot CLI para passar de uma pequena alteração a um recurso planejado com verificação reutilizável. A configuração nas Lições 0–1 preparou seu ambiente; os nove módulos principais nas Lições 2–10 ensinaram um fluxo completo de desenvolvimento.

## Revisar os três marcos de PR

| Marco | Resultado integrado | Hábito de revisão |
| --- | --- | --- |
| PR 1: avaliações por estrelas | O `starRating` existente aparece nos cards dos jogos, incluindo `No rating yet` para `null` | Manter a alteração delimitada e verificar ambos os casos |
| PR 2: instruções personalizadas | Uma convenção de documentação específica e uma pequena demonstração em código real | Verificar se as instruções melhoram código real, não apenas exemplos no chat |
| PR 3: filtragem e verificação | Filtragem, a skill quality-checks, o perfil de QA e os testes associados | Revisar todos os checkpoints, as evidências atuais de QA e a CI antes do merge |

Os dois primeiros PRs foram integrados antes de iniciar o próximo marco a partir de `main` atualizado. As Lições 4–8 compartilharam uma branch e uma cópia de trabalho. Commits de checkpoint preservaram o progresso sem criar um PR para cada módulo. A lição de controles não iniciou outro recurso ou PR.

## Revisar os ativos compartilhados

Estes são os mesmos resultados principais do [workshop do aplicativo Copilot][app-workshop], alcançados por uma interface de terminal:

- **As instruções do repositório** explicam o contexto e os padrões do projeto; instruções com escopo de caminho acrescentam detalhes para os arquivos relevantes.
- **A implementação de filtragem e os testes** atendem à issue e aos esclarecimentos aprovados durante o planejamento.
- **A skill quality-checks** reúne instruções reutilizáveis e scripts reais de shell que executam as quatro verificações do projeto.
- **A configuração do MCP do Playwright** fornece ferramentas de navegador para observação direta. Neste fluxo da CLI, ela fica na configuração do usuário, não no PR do recurso.
- **O agente personalizado de QA** define um papel reutilizável que parte dos requisitos, verifica a cobertura, usa a skill e as ferramentas de navegador e relata resultados verdadeiros.
- **O PR e as evidências de verificação** conectam as alterações revisadas aos resultados de testes, observações no navegador, limitações e CI.

Uma skill é mais do que uma lista de comandos, e um perfil é mais do que um nome de arquivo. Você examinou os ativos gerados, confirmou a execução real e selecionou o agente personalizado antes de confiar no relatório.

## Distinguir as finalidades da validação

O planejamento esclareceu os requisitos antes da implementação. O Autopilot executou esse plano delimitado; voltar a Interactive restabeleceu pontos deliberados de revisão antes de criar personalizações.

A implementação usou as verificações npm existentes antes de haver uma skill. A lição da skill comprovou que seus scripts incluídos e o encaminhamento de argumentos funcionavam. O MCP demonstrou interação direta com o navegador em vez de repetir uma suíte completa. QA combinou critérios, cobertura, evidências de navegador e as quatro verificações executadas pela skill. O PR reutilizou os resultados atuais de QA enquanto a CI verificou a revisão enviada.

Falhas e bloqueios são resultados úteis. Ferramentas de navegador ausentes, testes ignorados, servidores desatualizados ou um requisito não resolvido significam **NO-GO**, não permissão para reduzir o padrão. Adições de testes se justificam por lacunas reais; não adicionar testes é correto quando a cobertura existente é adequada.

## Levar estes hábitos adiante

- Forneça ao Copilot a issue, o motivo da alteração e limites claros.
- Revise os planos antes de aprovar trabalho autônomo.
- Examine instruções, skills e perfis gerados antes de executá-los.
- Saiba a qual cópia de trabalho, branch, servidor e revisão um resultado se refere.
- Use a menor correção justificada e atualize as evidências após alterações.
- Mantenha explícitas as instalações, ações destrutivas, compartilhamentos e merges de PR.

## Continuar aprendendo

O [workshop do aplicativo Copilot][app-workshop] alcança os resultados compartilhados por sua interface gráfica e adiciona um marco de canvas. O [workshop do VS Code][vscode-workshop] e o [workshop do agente de nuvem][cloud-workshop] exploram outras formas de trabalhar com agentes.

Use o [Awesome Copilot][awesome-copilot] para encontrar exemplos de instruções, skills e agentes personalizados. Os [exemplos de skills da Lição 5][skill-examples] incluem fluxos de contribuição, documentos de requisitos, diagramas e testes de navegador. Revise os pré-requisitos e o comportamento antes de adotar conteúdo da comunidade.

Para referência diária, consulte a [referência de comandos da CLI][cli-reference], a [documentação de skills de agente][agent-skills] e a [documentação de agentes personalizados][custom-agents]. Continue experimentando em tarefas delimitadas e compartilhe apenas material revisado por canais aprovados.

[previous-lesson]: ../9-slash-commands/
[app-workshop]: ../../app/
[vscode-workshop]: ../../vscode/
[cloud-workshop]: ../../cloud/
[skill-examples]: ../5-agent-skills/#mais-exemplos-de-skills
[awesome-copilot]: https://github.com/github/awesome-copilot
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/concepts/agents/copilot-cli/about-custom-agents
