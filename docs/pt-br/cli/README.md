---
slug: pt-br/cli
title: "CLI do GitHub Copilot"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

O **[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** coloca o GitHub Copilot no seu terminal como um assistente de programação baseado em agentes. Ele explora bases de código, gera código, executa comandos e se conecta a ferramentas externas — tudo pela linha de comando, para que você mantenha o foco sem trocar para um editor gráfico.

Após a configuração nas Lições 0–1, você concluirá nove módulos principais nas Lições 2–10. Comece com uma melhoria rápida de avaliações por estrelas, estabeleça instruções de documentação e crie a filtragem com os modos **Plan** e **Autopilot**. Depois, crie uma skill quality-checks reutilizável, valide o comportamento com o MCP do Playwright, crie um agente de QA e entregue o recurso. Termine explorando os controles da CLI e revisando o que criou.

## Lições

| Lição | Tópico | Descrição |
|----------|-------|-------------|
| [0. Pré-requisitos][ex0] | Configuração | Crie seu repositório e seu codespace |
| [1. Instalar o Copilot CLI][ex1] | Instalação | Instale e autentique o Copilot CLI |
| [2. Adicionar avaliações por estrelas: uma melhoria rápida][ex2] | Primeira alteração | Exiba avaliações existentes, valide e integre o PR 1 |
| [3. Orientar o Copilot com instruções personalizadas][ex3] | Contexto | Adicione uma convenção de documentação, demonstre-a e integre o PR 2 |
| [4. Criar a filtragem com Plan e Autopilot][ex4] | Implementação | Revise um plano, aprove o Autopilot, teste e salve um checkpoint |
| [5. Criar e usar uma skill quality-checks][ex5] | Skills | Gere, examine e execute verificações com scripts de shell incluídos |
| [6. Validar a funcionalidade com o MCP do Playwright][ex6] | Ferramentas de navegador | Observe o comportamento de filtragem em um navegador real |
| [7. Criar e usar um agente de QA][ex7] | Agentes | Audite requisitos e cobertura e reúna as evidências finais |
| [8. Criar e integrar o PR do recurso][ex8] | Entrega | Revise a filtragem e as personalizações reutilizáveis juntas no PR 3 |
| [9. Explorar comandos de barra e opções da CLI][ex9] | Controles da CLI | Examine contexto, modelos, sessões e destinos de compartilhamento |
| [10. Revisão e próximos passos][ex10] | Resumo | Revise os ativos comuns e os três marcos de PR |

## Branches e pull requests

Você integrará três pull requests: avaliações por estrelas; instruções e uma pequena demonstração; e filtragem com a skill quality-checks, o perfil de QA e os testes associados. Integre cada um dos dois primeiros PRs antes de iniciar o próximo marco a partir de `main` atualizado.

As Lições 4–8 compartilham uma branch de recurso e uma cópia de trabalho. Salve commits de checkpoint ao longo do caminho; criar a skill, configurar o MCP e selecionar QA não inicia novas branches de recurso. A Lição 9 explora os controles sem iniciar outro recurso ou PR.

## Pré-requisitos

Antes de participar deste workshop, verifique se você tem:

- [ ] Uma conta do GitHub com um plano ativo **Copilot Student, Pro, Pro+, Business ou Enterprise**
- [ ] Familiaridade básica com operações de terminal e linha de comando
- [ ] O Git instalado e configurado

> [!TIP]
> Não tem um plano pago? Estudantes verificados podem obter o GitHub Copilot gratuitamente por meio do [GitHub Education][callout-student-plan-education]. O plano **Copilot Student** inclui os recursos de agente, MCP, revisão de código e Copilot CLI usados neste workshop. Portanto, você pode concluir todos os percursos com esse plano.

> [!NOTE]
> Se você usa o Copilot Business ou o Copilot Enterprise, verifique se o administrador habilitou o Copilot CLI para uso.

## Começar

[**Comece pela Lição 0: Pré-requisitos →**][ex0]

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-cli/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-slash-commands/
[ex10]: 10-review/
[callout-student-plan-education]: https://github.com/education/students
