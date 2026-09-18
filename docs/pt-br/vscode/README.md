---
slug: pt-br/vscode
title: "VS Code"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

O **[GitHub Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)** no VS Code traz o GitHub Copilot para o editor de código que você já usa. Trabalhando no Visual Studio Code (e no GitHub Codespaces), você conduzirá o Copilot Chat no modo de agente, conectará ferramentas externas por meio do MCP e contará com agentes personalizados — tudo sem sair do IDE, onde o Copilot tem uma visão completa dos arquivos, do terminal e dos problemas.

Você começará adicionando instruções personalizadas e observando o Copilot segui-las; depois, usará o modo de agente para criar uma funcionalidade de filtragem que abrange a interface, a camada de dados e os testes. Em seguida, conectará o servidor MCP do Playwright e deixará o Copilot controlar um navegador para testar a funcionalidade antes de abrir um pull request. Por fim, revisará e usará um agente personalizado para o trabalho de acessibilidade e, então, monitorará, orientará e iterará sobre as alterações do Copilot — tudo sem sair do editor.

## Exercícios

| Exercício | Tema | Descrição |
|----------|-------|-------------|
| [0. Pré-requisitos][ex0] | Configuração | Crie seu repositório e seu codespace |
| [1. Instruções personalizadas][ex1] | Contexto | Adicione e verifique instruções personalizadas no VS Code |
| [2. Modo de agente][ex2] | Geração de código | Crie uma funcionalidade de filtragem com o modo de agente |
| [3. MCP com Playwright][ex3] | Ferramentas externas | Teste a funcionalidade em um navegador com o servidor MCP do Playwright |
| [4. Agentes personalizados][ex4] | Agentes especializados | Revise e use agentes personalizados |
| [5. Gerenciamento de agentes][ex5] | Monitoramento | Monitore e oriente sessões de agentes |
| [6. Iteração][ex6] | Revisão | Revise o trabalho do Copilot localmente e escolha os próximos passos |
| [Opcional: Incorporar o Foundry][foundry-toolkit] | Agentes de IA | Prepare um modelo, implante um agente e conecte-o ao site em três módulos com o VS Code e o Foundry Toolkit |

## Pré-requisitos

Antes de participar deste workshop, certifique-se de ter:

- [ ] Uma conta do GitHub com um plano **Copilot Student, Pro, Pro+, Business ou Enterprise** ativo
- [ ] Acesso ao GitHub Codespaces

> [!TIP]
> Não tem um plano pago? Estudantes verificados podem obter o GitHub Copilot gratuitamente por meio do [GitHub Education][callout-student-plan-education]. O plano **Copilot Student** inclui os recursos de agente, MCP, revisão de código e Copilot CLI usados neste workshop — portanto, você pode concluir todas as trilhas com ele.

[callout-student-plan-education]: https://github.com/education/students
## Primeiros passos

**[Comece pelo Exercício 0: Pré-requisitos →][ex0]**

[ex0]: 0-prerequisites/
[ex1]: 1-custom-instructions/
[ex2]: 2-agent-mode/
[ex3]: 3-mcp/
[ex4]: 4-custom-agents/
[ex5]: 5-managing-agents/
[ex6]: 6-iterating/
[foundry-toolkit]: 7-foundry-toolkit/
