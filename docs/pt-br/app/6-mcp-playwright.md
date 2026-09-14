---
title: "Lição 6 - Validar a funcionalidade com o MCP do Playwright"
description: "Configure o MCP do Playwright pelo Customize e observe a filtragem no navegador, no worktree existente do recurso."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Na lição anterior, você reuniu e executou as verificações do projeto por meio da skill quality-checks. Agora dê ao agente acesso a um navegador para observar diretamente a interface de filtragem. Permaneça na mesma sessão, worktree e branch de filtragem. Esta lição acrescenta evidências do navegador, não outro recurso, uma nova execução de toda a suíte de testes ou um PR.

Nesta lição, você vai:

- entender o que é o Model Context Protocol (MCP) e como o aplicativo GitHub Copilot o utiliza.
- adicionar o servidor MCP do Playwright pelo **Customize**.
- pedir ao agente que controle um navegador e explore o recurso de filtragem.

## Cenário

Embora os testes de unidade e de ponta a ponta sejam importantes, validar atualizações na interface exige interagir com ela. Você quer permitir que o Copilot use o site em desenvolvimento como uma pessoa usuária faria, automatizando ainda mais o processo de alteração e aumentando a confiança de que as atualizações se comportam conforme o esperado.

## O que é o Model Context Protocol (MCP)?

O [Model Context Protocol (MCP)][mcp-blog-post] oferece aos agentes de IA uma forma de se comunicar com ferramentas e serviços externos em tempo real. Isso permite que eles acessem informações atualizadas, usando recursos, e realizem ações em seu nome, usando ferramentas.

Essas ferramentas e esses recursos são acessados por meio de um servidor MCP, que funciona como uma ponte entre o agente de IA e as ferramentas e os serviços externos. O servidor MCP é responsável por gerenciar essa comunicação, seja com APIs existentes ou com ferramentas locais, como pacotes NPM. Cada servidor MCP representa um conjunto diferente de ferramentas e recursos que o agente de IA pode acessar.

Alguns servidores MCP conhecidos são:

- [**GitHub MCP Server**](https://github.com/github/github-mcp-server): oferece acesso a um conjunto de APIs para gerenciar repositórios do GitHub. Ele permite que o agente de IA realize ações como criar repositórios, atualizar repositórios existentes e gerenciar issues e pull requests.
- [**Playwright MCP Server**][playwright-mcp-server]: oferece recursos de automação de navegador usando o Playwright. Ele permite que o agente de IA realize ações como acessar páginas Web, preencher formulários e selecionar botões.

Há muitos outros servidores MCP que fornecem acesso a diferentes ferramentas e recursos. O GitHub mantém um [registro de MCP](https://github.com/mcp) para facilitar a descoberta e as contribuições ao ecossistema.

> [!CAUTION]
> Trate os servidores MCP como qualquer outra dependência do projeto. Antes de usar um servidor MCP, revise cuidadosamente o código-fonte, verifique quem o publicou e considere as implicações de segurança. Use apenas servidores MCP confiáveis e tenha cuidado ao conceder acesso a recursos ou operações confidenciais.

## Adicionar o servidor MCP do Playwright

A [documentação atual de personalização do aplicativo][customize-app] usa **Customize** na barra lateral para descobrir e gerenciar MCP. Servidores MCP configurados para seus repositórios ou para o Copilot CLI já podem estar disponíveis no aplicativo; examine os servidores instalados antes de adicionar um duplicado.

1. Selecione **Customize** na barra lateral.
2. Selecione **MCP** e verifique em **Installed** se já existe um servidor Playwright.
3. Se necessário, encontre **Playwright** entre os servidores disponíveis ou use o fluxo de servidor personalizado documentado pelo publicador.
4. Revise o publicador, a configuração e as solicitações de instalação antes de aprová-las. Siga as instruções para adicionar o servidor; políticas da organização ou pré-requisitos ausentes podem bloquear a configuração.
5. Volte à sessão de filtragem existente e mantenha o modo **Interactive**. Confirme que as ferramentas de navegador do MCP do Playwright estão disponíveis antes de solicitar a validação. Não crie um novo worktree do recurso como solução alternativa de configuração.

Se a configuração falhar, resolva o problema de configuração ou permissão em vez de aceitar uma afirmação de que o agente navegou sem ferramentas. A visibilidade do navegador depende da configuração do servidor; a atividade real das ferramentas e as observações são as evidências.

## Pedir ao Copilot que explore o recurso com o Playwright

Use a URL real da issue e os esclarecimentos aprovados salvos na Lição 4. Pare qualquer servidor de desenvolvimento manual das lições anteriores antes de o agente iniciar o próprio servidor. Ele deve identificar a cópia de trabalho e o servidor em teste.

1. Use o prompt a seguir para pedir ao Copilot que valide a nova funcionalidade:

   ```plaintext
   Use o servidor MCP do Playwright configurado para observar o recurso de filtragem conforme esta issue: <filtering-issue-URL>. Estes são meus esclarecimentos de planejamento aprovados: <cole os esclarecimentos acordados ou escreva none>. Permaneça neste worktree e branch de filtragem.

   Identifique a cópia de trabalho, inicie seu servidor de desenvolvimento e use ferramentas reais de navegador para exercitar a seleção de várias categorias, a filtragem por distribuidora, a filtragem combinada, os controles acessíveis e qualquer comportamento acordado de limpeza de filtros ou resultados vazios. Relate observações em relação aos critérios, incluindo falhas ou verificações bloqueadas. Não afirme comportamentos que não observou.

   Esta etapa é uma observação no navegador, não outra execução automatizada completa de testes. Não altere código da aplicação, testes, skills ou perfis de agente, não faça commit, push nem crie um PR. Relate ferramentas MCP ou pré-requisitos ausentes como bloqueios e pergunte antes de instalar qualquer coisa. Não reutilize o servidor de outra cópia de trabalho nem interrompa processos não relacionados. Ao terminar, pare apenas o servidor que você iniciou.
   ```

Examine as chamadas de ferramentas MCP do Playwright, a URL em teste e as observações relatadas do navegador. Uma narrativa baseada apenas no código-fonte ou em resultados E2E anteriores não demonstra o uso de MCP.

2. Compare o resumo com a issue e os esclarecimentos aprovados. Se houver um defeito, autorize uma correção específica separadamente, revise o diff alterado e repita as verificações automatizadas e observações do navegador relevantes. Evidências anteriores à correção não comprovam a revisão resultante.
3. Confirme que o agente parou o próprio servidor. Mantenha esta sessão de filtragem aberta e permaneça no modo **Interactive** antes de criar o perfil QA na Lição 7.

Esta etapa estabelece observação direta, não substitui a cobertura automatizada. Falhas ou observações bloqueadas permanecem visíveis para o QA.

## Resumo e próximos passos

Parabéns! Você usou o servidor MCP do Playwright para explorar o recurso em um navegador real a partir do aplicativo GitHub Copilot. Recapitulando, você:

- aprendeu o que é o Model Context Protocol (MCP) e como o aplicativo disponibiliza ferramentas MCP.
- configurou o servidor MCP do Playwright pelo **Customize**.
- pediu ao agente que controlasse um navegador e explorasse o recurso de filtragem.

Em seguida, reúna os requisitos, as observações do navegador, a cobertura e a skill em um perfil especializado. Continue nesta mesma sessão para a [Lição 7 - Criar e usar um agente QA][next-lesson]. Não crie o PR do recurso ainda.

## Recursos

- [O que é MCP e por que todos estão falando sobre ele?][mcp-blog-post]
- [Servidor MCP do Microsoft Playwright][playwright-mcp-server]
- [Configurar servidores MCP no aplicativo GitHub Copilot][customize-app]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app