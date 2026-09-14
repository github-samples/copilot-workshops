---
title: "Lição 10 - Revisão e próximos passos"
description: "Recapitule os nove módulos principais do aplicativo, os quatro marcos de PR e o fluxo reutilizável de qualidade e explore outros recursos."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Nas últimas lições, você levou um recurso da ideia ao merge com o aplicativo GitHub Copilot. Nesse processo, você:

- conectou um repositório e conheceu o espaço de trabalho do aplicativo e o backlog criado pelo modelo.
- iniciou sessões a partir de uma tarefa direta e de issues e usou os modos Plan e Autopilot para controlar como o agente trabalha.
- orientou o agente com instruções personalizadas e depois pediu que ele criasse uma skill reutilizável com scripts de shell que você revisou e executou para lint, testes de unidade, testes de ponta a ponta e verificações de tipos.
- testou o trabalho com o servidor MCP do Playwright em um navegador real.
- criou e selecionou um agente personalizado QA para avaliar requisitos, cobertura, resultados dos scripts da skill e evidências do navegador.
- colaborou com o agente em um canvas compartilhado.
- fez o merge explicitamente dos primeiros PRs por conta própria e depois autorizou o **Agent Merge** nos fluxos de PR do recurso e do canvas.

As Lições 0–1 de configuração levaram aos nove módulos principais, as Lições 2–10. Reserve um momento para revisar os artefatos e os próximos passos; este encerramento não inicia outra tarefa prática.

## O que você entregou

O workshop tem quatro marcos de PR, cada um em sua própria branch a partir de `main` atualizado:

1. **Avaliações por estrelas:** exibir o `starRating` existente e um estado explícito sem avaliação nos cards dos jogos.
2. **Instruções e demonstração:** adicionar a convenção de documentação e verificar seu efeito em uma pequena alteração real de código.
3. **Filtragem e fluxo de qualidade:** implementar a issue, criar a skill `quality-checks` com scripts de shell e o perfil QA e incluir os testes associados.
4. **Canvas de triagem salvo no repositório:** compartilhar um quadro que adiciona contexto de issues sem implementar automaticamente outro recurso.

As Lições 4–8 usaram a mesma sessão, worktree e branch de filtragem. Os commits de checkpoint preservaram o progresso dentro do PR 3; skills, configuração MCP e QA não precisaram de branches de recurso separadas. Cada marco posterior começou apenas depois do merge do PR anterior e da atualização da branch da nova sessão a partir de `origin/main`.

## Diferentes tipos de verificação

Os primeiros recursos usaram as verificações npm existentes. A filtragem acrescentou sua inspeção manual no navegador. A skill tornou as quatro verificações repetíveis por meio de scripts incluídos, o MCP acrescentou observações diretas do agente no navegador e o QA combinou requisitos e cobertura com a verificação final. O PR reutilizou evidências de QA apenas enquanto elas se aplicavam à revisão enviada.

Os testes adicionados devem cobrir lacunas reais; uma execução de QA que não precisa de testes novos pode estar correta. Ferramentas ausentes, verificações ignoradas e falhas são bloqueios visíveis, não aprovações. Revise código e evidências antes de autorizar o merge e atualize as evidências afetadas após alterações.

## Boas práticas

Ao usar qualquer ferramenta de IA, a infraestrutura ao redor dela influencia a qualidade dos resultados. Você criou instruções, uma skill e um perfil QA neste workshop; revise-os e reutilize-os entre sessões. Agentes personalizados definem papéis especializados e instruções, com ferramentas disponíveis conforme a configuração e as permissões do ambiente; skills reúnem instruções reutilizáveis para tarefas, scripts executáveis e recursos de apoio carregados sob demanda. Um agente personalizado também pode executar scripts, incluindo os que fazem parte de uma skill. Confirme a execução real dos scripts e a seleção do agente personalizado em vez de confiar em uma descrição convincente.

Associe o **modo e o modelo** à tarefa. Use **Plan** para analisar uma abordagem antes de desenvolver, **Interactive** para acompanhar alterações específicas e **Autopilot** somente para tarefas isoladas e com escopo bem definido. Escolha um modelo mais rápido para edições rotineiras e um modelo mais avançado, com maior esforço de raciocínio, para trabalhos complexos.

O contexto continua tão importante quanto a infraestrutura. Descrever claramente *o que* você quer criar, *por que* e *como* muda significativamente o resultado. Os chats rápidos são ótimos para definir o escopo de uma ideia antes de transformá-la em uma sessão completa.

## Mais recursos para explorar

Você percorreu o fluxo de trabalho principal. Veja outros recursos que valem a pena conhecer:

- **Quick chats** para perguntas rápidas e descartáveis que não exigem uma sessão completa.
- [**Automações**][using-automations] para tarefas recorrentes ou sob demanda, como resumir trabalhos recentes. Revise a agenda, as permissões e o escopo antes de adotar uma; criar uma automação é um próximo passo, não parte deste workshop.
- **Rubber duck** para analisar um problema e receber feedback relevante antes de começar a desenvolver.
- [**Agentes personalizados**][custom-agents] para empacotar uma função, suas ferramentas e instruções para trabalhos especializados e repetíveis.
- [`/chronicle`][chronicle] para gerar uma narrativa do que aconteceu em uma sessão.
- [Bring your own key (BYOK)][byok] para usar modelos do seu próprio provedor, incluindo modelos locais por meio de Ollama, Foundry Local ou LM Studio.
- [Sandboxes na nuvem][sandboxes] para executar sessões em um ambiente isolado hospedado pelo GitHub.
- [Deep links][deep-links] para abrir o aplicativo diretamente em um repositório, uma sessão ou um prompt.

## Próximos passos

A melhor maneira de melhorar com qualquer ferramenta é continuar usando-a. Use-a em código de produção, em projetos pessoais ou naquele pequeno aplicativo que você planeja criar há anos. Compartilhe o que aprendeu com sua equipe e aprenda com as experiências dela. E, como sempre, explore a documentação.

Para conhecer melhor o ecossistema do GitHub Copilot, confira o [percurso do VS Code][vscode-harness], o [percurso do Copilot CLI][cli-harness] ou o [percurso do agente de nuvem][cloud-harness].

## Recursos

- [Sobre o aplicativo GitHub Copilot][about-copilot-app]
- [Introdução ao aplicativo GitHub Copilot][getting-started]
- [Personalizar o aplicativo GitHub Copilot][customize]
- [Usar automações][using-automations]
- [Trabalhar com extensões de canvas][canvas-docs]
- [Sobre sandboxes locais e na nuvem][sandboxes]

[previous-lesson]: ../9-canvases/
[vscode-harness]: ../../vscode/
[cli-harness]: ../../cli/
[cloud-harness]: ../../cloud/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[customize]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[using-automations]: https://docs.github.com/copilot/how-tos/github-copilot-app/using-automations
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
[chronicle]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle
[custom-agents]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[byok]: https://docs.github.com/copilot/how-tos/github-copilot-app/use-byok-models
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links