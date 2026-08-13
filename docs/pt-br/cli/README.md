---
slug: pt-br/cli
title: "CLI do GitHub Copilot"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

O **[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** coloca o GitHub Copilot no seu terminal como um assistente de programação baseado em agentes. Ele explora bases de código, gera código, executa comandos e se conecta a ferramentas externas — tudo pela linha de comando, para que você mantenha o foco sem trocar para um editor gráfico.

Ao longo destas lições, você instalará e autenticará o Copilot CLI, depois fornecerá contexto do projeto com instruções personalizadas antes de usar o modo plan para gerar um recurso de forma deliberada. Você conectará o servidor MCP do Playwright para testar esse recurso em um navegador real e, em seguida, ampliará o Copilot com skills de agente reutilizáveis e agentes personalizados. Por fim, você explorará comandos de barra para gerenciar contexto, modelos e compartilhamento, e concluirá com uma revisão do que criou.

## Lições

| Lição | Tópico | Descrição |
|----------|-------|-------------|
| [0. Pré-requisitos][ex0] | Configuração | Crie seu repositório e seu codespace |
| [1. Instalar o Copilot CLI][ex1] | Instalação | Instale e autentique o Copilot CLI |
| [2. Instruções personalizadas][ex2] | Contexto | Adicione uma instrução e veja como o Copilot CLI a segue |
| [3. Geração de código][ex3] | Geração de código | Use o modo plan e gere recursos |
| [4. Testar com o MCP do Playwright][ex4] | Ferramentas externas | Adicione o servidor MCP do Playwright e teste seu recurso em um navegador |
| [5. Skills de agente][ex5] | Skills | Aprimore o Copilot com skills especializadas |
| [6. Agentes personalizados][ex6] | Agentes | Revise e use agentes personalizados |
| [7. Comandos de barra][ex7] | Recursos da CLI | Explore contexto, modelos, compartilhamento e a delegação opcional para o agente de nuvem |
| [8. Revisão][ex8] | Resumo | Revise os principais conceitos e os próximos passos |

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
[ex2]: 2-custom-instructions/
[ex3]: 3-generating-code/
[ex4]: 4-mcp/
[ex5]: 5-agent-skills/
[ex6]: 6-custom-agents/
[ex7]: 7-slash-commands/
[ex8]: 8-review/
[callout-student-plan-education]: https://github.com/education/students
