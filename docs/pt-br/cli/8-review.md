---
title: "Lição 8 - Revisão e próximos passos"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Ao longo das últimas lições, você explorou alguns dos casos de uso mais comuns do GitHub Copilot CLI, incluindo:

- interagir com o GitHub e outros servidores MCP.
- usar arquivos de instruções para orientar a geração de código.
- implementar skills para adicionar ferramentas ao conjunto de recursos do Copilot CLI.
- chamar agentes personalizados para tarefas avançadas e mais complexas.
- usar comandos de barra para gerenciar sua sessão e, opcionalmente, voltar ao agente de nuvem por meio de `/delegate`.

Vamos falar sobre alguns comandos de barra, boas práticas e próximos passos.

## Comandos de barra

O Copilot CLI oferece uma série de comandos de barra para interação, inclusive aqueles que permitem configurá-lo ou ver o que acontece nos bastidores. Você já usou `/clear` para iniciar um novo chat, limpando o contexto atual, e `/mcp` para inspecionar e gerenciar servidores MCP. Alguns outros que podem ser úteis são:

| Comando | Descrição |
| ------------------ | ------------------------------------------------------------- |
| `/add-dir` | Adicionar um diretório à lista de confiança do Copilot |
| `/clear`, `/new` | Limpar o histórico da conversa e começar de novo |
| `/compact` | Resumir o histórico da conversa para reduzir o uso da janela de contexto |
| `/context` | Mostrar o uso de tokens da janela de contexto e sua visualização |
| `/diff` | Revisar as alterações feitas no diretório atual |
| `/model` | Selecionar o modelo de IA a usar (Claude Sonnet, GPT-5 etc.) |
| `/plan <prompt>` | Criar um plano de implementação antes de programar |
| `/review <prompt>` | Executar o agente de revisão de código para analisar alterações |
| `/delegate` | Delegar a tarefa ao agente de nuvem do Copilot para processamento assíncrono |
| `/session` | Mostrar informações da sessão e um resumo do workspace |
| `/share` | Compartilhar a sessão em um arquivo markdown ou em uma GitHub gist |
| `/skills` | Gerenciar skills para ampliar recursos |
| `/usage` | Exibir métricas e estatísticas de uso da sessão |

> [!TIP]
> Use `/help` para ver a lista completa de comandos disponíveis e atalhos de teclado.

## Boas práticas

Ao usar qualquer ferramenta de IA, a infraestrutura por trás dela influencia a qualidade do que você recebe. Arquivos de instruções robustos, agentes personalizados e skills de agente fazem parte dessa base — e você explorou cada um deles neste workshop. O [awesome-copilot][awesome-copilot] é uma boa fonte de modelos, e o próprio Copilot pode gerar essas estruturas para você como ponto de partida.

O contexto continua sendo tão importante quanto a infraestrutura. Descrever com clareza *o que* você quer criar, *por que* e *como* muda significativamente a saída. Se alguma informação puder ajudar o Copilot, forneça-a.

## Próximos passos

A melhor forma de melhorar suas habilidades com qualquer ferramenta é continuar usando essa ferramenta. Use-a em código de produção, em projetos pessoais, naquele pequeno aplicativo em que você pensa há anos mas nunca parou para criar. Compartilhe seus aprendizados com a equipe e aprenda com ela. E, como sempre, explore a documentação.

Se quiser explorar mais do ecossistema do GitHub Copilot, confira o [percurso do VS Code](../../vscode/) ou o [percurso do agente de nuvem](../../cloud/).

## Recursos

- [Sobre o Copilot CLI][about-copilot-cli]
- [Usar o Copilot CLI][using-copilot-cli]
- [Repositório Awesome Copilot][awesome-copilot]
- [Guia de instruções personalizadas][repo-instructions]
- [Documentação de Agent Skills][agent-skills]
- [Documentação de agentes personalizados][custom-agents]
- [Especificação do MCP][mcp-spec]

[previous-lesson]: ../7-slash-commands/
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[awesome-copilot]: https://github.com/github/awesome-copilot
[repo-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[mcp-spec]: https://modelcontextprotocol.io/
