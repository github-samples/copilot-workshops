---
slug: pt-br/app
title: "Aplicativo GitHub Copilot"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

O [**aplicativo GitHub Copilot**](https://docs.github.com/copilot/concepts/agents/github-copilot-app) é um aplicativo para desktop criado com base no Copilot CLI que reúne o desenvolvimento orientado por agentes em um espaço de trabalho único e focado. Ele oferece sessões paralelas de agentes, modos de sessão alternáveis, canvases compartilhados e gerenciamento nativo de issues e pull requests do GitHub, incluindo o **Agent Merge**, que conduz um pull request por rebases, feedback de revisão, correções de CI e merge.

As Lições 0–1 de configuração preparam o projeto e o espaço de trabalho do aplicativo. Os nove módulos principais, as Lições 2–10, começam com uma melhoria rápida de avaliações por estrelas e uma convenção de documentação demonstrada em código real. Depois, você planejará e criará a filtragem, criará e executará uma skill quality-checks com scripts de shell, observará o recurso pelo MCP do Playwright e criará um agente personalizado QA para avaliar requisitos e cobertura. Você revisará o PR completo do recurso e autorizará o Agent Merge e, depois, criará e integrará um canvas compartilhado de triagem.

O workshop tem quatro marcos de PR: avaliações por estrelas; instruções com sua demonstração; filtragem com a skill, o perfil QA e os testes; e, por fim, o canvas. Comece cada marco a partir de `main` atualizado, usando uma branch por PR em vez de uma por módulo. As Lições 4–8 permanecem na mesma sessão, worktree e branch de filtragem. Reabrir o canvas adiciona contexto de issues sem iniciar outro recurso ou um quinto PR. As automações são vinculadas como próximo passo, não como exercício adicional.

## Lições

| Lição | Tópico | Descrição |
|--------|-------|-------------|
| [0. Pré-requisitos][ex0] | Configuração | Instale o Node.js e crie sua cópia do projeto Tailspin Toys |
| [1. Instalar o aplicativo Copilot][ex1] | Configuração | Instale o aplicativo, conecte seu projeto e conheça o espaço de trabalho |
| [2. Adicionar avaliações por estrelas: uma melhoria rápida][ex2] | Primeira alteração | Exiba as avaliações existentes e a alternativa para null e integre o PR 1 |
| [3. Orientar o Copilot com instruções personalizadas][ex3] | Contexto | Adicione um padrão de documentação e uma demonstração real e integre o PR 2 |
| [4. Criar a filtragem com Plan e Autopilot][ex4] | Implementação | Aprove o plano, implemente e verifique a filtragem e salve um checkpoint |
| [5. Criar e usar uma skill quality-checks][ex5] | Verificações repetíveis | Crie, revise e execute os scripts de shell incluídos |
| [6. Validar a funcionalidade com o MCP do Playwright][ex6] | Observação no navegador | Configure MCP pelo Customize e examine o comportamento da filtragem |
| [7. Criar e usar um agente QA][ex7] | Requisitos e cobertura | Selecione um perfil especializado e reúna evidências de verificação final |
| [8. Criar e integrar o PR do recurso][ex8] | Revisão e merge | Revise a filtragem, a skill, o perfil QA e os testes e autorize o Agent Merge para o PR 3 |
| [9. Criar um canvas de triagem][ex9] | Colaboração | Compartilhe um canvas salvo no repositório no PR 4 e adicione contexto de issues |
| [10. Revisão e próximos passos][ex10] | Resumo | Revise o fluxo, os artefatos e outros recursos |

## Pré-requisitos

Antes de participar deste workshop, verifique se você tem:

- [ ] Uma conta do GitHub com um plano ativo **Copilot Student, Pro, Pro+, Business ou Enterprise**
- [ ] Um computador com **macOS, Linux ou Windows**
- [ ] O [Git instalado][install-git] no computador

> [!TIP]
> Não tem um plano pago? Estudantes verificados podem obter o GitHub Copilot gratuitamente por meio do [GitHub Education][callout-student-plan-education]. O plano **Copilot Student** inclui os recursos de agente, MCP, revisão de código e Copilot CLI usados neste workshop. Portanto, você pode concluir todos os percursos com esse plano.

> [!NOTE]
> Como o aplicativo Copilot é executado no seu computador, e não em um codespace, a [Lição 0][ex0] orienta você na instalação do Node.js e na criação da sua cópia do projeto antes da instalação do aplicativo.

> [!NOTE]
> Se você usa o Copilot Business ou o Copilot Enterprise, o administrador deve habilitar a política **Copilot CLI** para que você possa usar o aplicativo.

## Começar

[**Comece pela Lição 0: Pré-requisitos →**][ex0]

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-app/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-canvases/
[ex10]: 10-review/
[install-git]: https://github.com/git-guides/install-git
[callout-student-plan-education]: https://github.com/education/students