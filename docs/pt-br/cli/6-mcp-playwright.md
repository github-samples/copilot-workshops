---
title: "Lição 6 - Validar a funcionalidade com o MCP do Playwright"
description: "Conecte um navegador via MCP e compare o comportamento observado da filtragem com a issue e o plano aprovado."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Sua implementação de filtragem e a skill quality-checks já têm verificação automatizada. Agora dê um navegador ao Copilot e peça que observe a funcionalidade diretamente. Esta lição demonstra a interação por **Model Context Protocol (MCP)**, não outra execução completa da suíte de testes.

Permaneça no modo **Interactive** na mesma cópia de trabalho e branch de filtragem. A configuração do MCP não inicia um novo marco de recurso.

Nesta lição, você vai:

- conectar o MCP do Playwright e confirmar que suas ferramentas de navegador estão disponíveis.
- comparar o comportamento real da filtragem com a issue e os critérios aprovados.
- revisar as observações e parar o servidor de desenvolvimento que iniciou.

## Cenário

As verificações automatizadas passaram, mas a Tailspin Toys também precisa de evidências da experiência dos visitantes. Você dará ao Copilot ferramentas de navegador para exercitar os filtros e comparar os jogos exibidos com o comportamento acordado, em vez de considerar que um controle que responde prova que a filtragem funciona.

## O que o MCP acrescenta

O [MCP][mcp-overview] conecta um agente a ferramentas e contexto externos por meio de servidores. O servidor MCP do GitHub integrado permite ao Copilot trabalhar com issues e PRs. O [servidor MCP do Playwright][playwright-mcp] fornece ferramentas de navegador para abrir páginas, examinar elementos acessíveis, navegar e interagir com controles.

O snapshot de acessibilidade do navegador ajuda o agente a identificar controles, mas não comprova conformidade completa de acessibilidade. Compare ações e observações reais com os requisitos da issue em vez de aceitar um “parece bom” genérico.

> [!CAUTION]
> Trate um servidor MCP como uma dependência do projeto: revise o publicador, o código-fonte, as permissões e qualquer download de pacote antes de habilitá-lo. Políticas da organização podem restringir quais servidores podem executar. Não coloque credenciais em configurações versionadas nem aprove ferramentas desconhecidas apenas para concluir a lição.

## Configurar o MCP do Playwright

1. Na sessão existente da CLI, digite `/mcp` para examinar os servidores configurados. Reutilize uma configuração funcional do Playwright em vez de adicionar uma duplicada.
2. Se necessário, digite `/mcp add` e use <kbd>Tab</kbd> para percorrer o formulário.
3. Defina **Server Name** como `playwright`, **Server Type** como **STDIO** (ou **Local**) e **Command** como `npx @playwright/mcp@latest --headless`.
4. Defina **Tools** como `*` para este servidor de navegador revisado. Isso disponibiliza suas ferramentas; não substitui os controles de permissão da CLI.
5. Depois de revisar o pacote e seu comando de inicialização, pressione <kbd>Ctrl</kbd>+<kbd>S</kbd> para salvar. O registro inicia o servidor e pode baixar o pacote; aprove essa configuração deliberadamente e responda a qualquer solicitação do pacote.
6. Digite `/mcp show playwright` e confirme que o servidor está conectado e suas ferramentas de navegador estão disponíveis.

O navegador headless não precisa de uma janela de desktop, o que é adequado ao Codespaces. O fluxo interativo de adição salva a configuração em `~/.copilot/mcp-config.json` e disponibiliza o servidor sem reiniciar a CLI. Essa é uma configuração do usuário, não um arquivo para incluir no PR do recurso. O [guia de configuração do MCP][mcp-setup] documenta os campos e as fontes de configuração.

> [!NOTE]
> As dependências E2E do projeto e o navegador do MCP estão relacionados, mas podem exigir configurações diferentes. Se faltar um navegador ou uma dependência do sistema, examine o erro real e resolva o pré-requisito específico com aprovação. Não instale navegadores automaticamente nem presuma que um servidor conectado comprova que ele pode iniciar um.

## Iniciar a aplicação correta

Abra outro terminal nesta mesma cópia de trabalho de filtragem. Confirme o diretório e a branch e depois inicie a aplicação:

```bash
pwd
git branch --show-current
npm run dev
```

Leia a URL local real na saída do servidor. No codespace, o servidor MCP e a aplicação executam no mesmo ambiente, então use essa URL local, normalmente `http://localhost:4321`, em vez de presumir que uma URL de navegador encaminhada seja necessária.

Se a porta estiver ocupada ou o Astro escolher outra porta, identifique a quem pertence o servidor antes de continuar. Não reutilize um servidor desconhecido nem o encerre. Use a URL do processo que você acabou de iniciar e mantenha esse terminal aberto durante os testes.

## Observar o comportamento de filtragem

Substitua os marcadores pela URL real da issue, os esclarecimentos aprovados na Lição 4 e a URL da aplicação:

```plaintext
Use o servidor MCP do Playwright configurado para validar o recurso de filtragem em relação a esta issue: <filtering-issue-URL>. Estes são os esclarecimentos aprovados durante o planejamento: <cole os esclarecimentos acordados ou escreva none>. A aplicação desta cópia de trabalho está executando em <local-app-URL>. Confirme a cópia de trabalho, a branch e o servidor em teste antes de confiar nos resultados.

Abra a página de jogos, observe o estado sem filtros, selecione uma e depois múltiplas categorias, aplique um filtro de distribuidora e combine as seleções de categoria e distribuidora. Exercite a limpeza e os resultados vazios conforme os critérios aprovados. Verifique os rótulos dos controles, a operação por teclado e o foco visível. Compare os resultados exibidos com os filtros selecionados e os dados de origem; não deduza sucesso apenas porque um controle mudou.

Use ações reais das ferramentas de navegador e relate o que observou para cada critério, marcando claramente falhas ou evidências ausentes. Não execute outra suíte completa de testes apenas por esta lição de navegador, não altere código da aplicação, não crie testes ou personalizações, não mude de branch, não faça commit, push nem abra um PR. Pergunte antes de instalar algo ou parar outro processo.
```

Examine as chamadas de ferramentas do navegador e o relatório. O Copilot realmente selecionou múltiplas categorias e as combinou com uma distribuidora? Os jogos retornados correspondem ao comportamento acordado? O relatório distingue o comportamento observável no navegador da cobertura da camada de dados e dos testes automatizados?

Se algo falhar, registre o comportamento observado. Autorize separadamente qualquer correção específica da aplicação e depois repita as verificações de navegador e automatizadas afetadas. Não altere os critérios de aceitação para corresponder à implementação nem conte evidências antigas como verificação de código alterado.

## Parar o próprio servidor e continuar

Pare o servidor de desenvolvimento com <kbd>Ctrl</kbd>+<kbd>C</kbd> no terminal em que o iniciou. Mantenha a configuração do MCP do Playwright disponível. A Lição 7 coordenará novas observações no navegador e verificações E2E automatizadas, que não devem reutilizar um servidor de desenvolvimento desatualizado nem a aplicação de outra cópia de trabalho.

## Resumo e próximos passos

Permaneça em **Interactive** antes de criar o perfil de QA. Você observou o comportamento no navegador sem criar outro PR ou branch; em seguida, [crie e use um agente de QA][next-lesson] para combinar requisitos, cobertura, a skill e as evidências finais.

## Recursos

- [Adicionar servidores MCP ao Copilot CLI][mcp-setup] documenta configuração e gerenciamento.
- [Microsoft Playwright MCP][playwright-mcp] documenta a configuração e as ferramentas de navegador.
- [Registro MCP do GitHub][mcp-registry] lista outros servidores para avaliar.

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-overview]: https://docs.github.com/copilot/concepts/context/mcp
[mcp-setup]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
[playwright-mcp]: https://github.com/microsoft/playwright-mcp
[mcp-registry]: https://github.com/mcp
