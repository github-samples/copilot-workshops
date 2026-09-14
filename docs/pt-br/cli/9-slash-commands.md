---
title: "Lição 9 - Explorar comandos de barra e opções da CLI"
description: "Examine contexto e controles de modelo e sessão, revise destinos de compartilhamento e explore opções da CLI sem iniciar outro recurso."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Os três marcos de PR estão completos. Agora explore os controles da CLI que ajudam a entender e gerenciar uma sessão. Esta lição não implementa outro recurso, não delega trabalho nem abre outro PR.

Na cópia de trabalho atualizada do participante, inicie `copilot` no modo **Interactive**. Use `/help` e a [referência de comandos][cli-reference] para confirmar quais comandos a versão instalada suporta; a documentação atual pode descrever controles mais novos do que a sua instalação.

## Examinar contexto e informações da sessão

1. Envie uma solicitação delimitada, somente de leitura:

   ```plaintext
   Resuma os arquivos de instruções do repositório, a skill quality-checks e o perfil de QA. Explique como eles apoiam a verificação da filtragem. Não modifique arquivos, não execute verificações, não delegue trabalho, não faça commit nem abra um PR.
   ```

2. Digite `/context` para examinar o uso da janela de contexto. Observe como mensagens, instruções e definições de ferramentas consomem contexto.
3. Digite `/compact` e depois `/context` novamente. A compactação resume o histórico para reduzir seu tamanho; uma sessão curta pode mostrar pouca mudança.
4. Digite `/session` para examinar a sessão atual e `/usage` para consultar informações de uso.

A compactação não substitui o fornecimento de requisitos. Ao mudar de tarefa ou agente, forneça explicitamente a URL da issue, os critérios aprovados, a identidade da cópia de trabalho e as evidências relevantes.

`/clear` inicia uma conversa nova; não desfaz arquivos nem muda de branch Git. `/resume` abre o seletor de sessões para retornar a trabalhos anteriores. Explore o seletor e pressione <kbd>Esc</kbd> para sair sem retomar outra tarefa. Não apague a única cópia dos critérios de aceitação nem presuma que retomar uma conversa significa que sua verificação antiga ainda está atualizada.

## Examinar modelos e modos

Digite `/model` para examinar os modelos disponíveis para sua conta, incluindo **Auto** onde for oferecido. Leia os detalhes de seleção e as informações de uso; a disponibilidade e os preços dos modelos podem mudar. Pressione <kbd>Esc</kbd> para sair do seletor sem mudar o modelo. Se você o alterar, confirme a seleção exibida e o escopo que sua versão da CLI aplica.

Use <kbd>Shift</kbd>+<kbd>Tab</kbd> para examinar o indicador de modo ao alternar entre **Interactive**, **Plan** e **Autopilot** e volte a **Interactive** sem enviar um prompt de implementação. Lembre-se da distinção:

- Plan serve para acordar o trabalho antes de programar.
- Autopilot continua uma tarefa aprovada e delimitada.
- Interactive oferece pontos deliberados de revisão e decisão.
- As permissões controlam separadamente quais ações de ferramentas são permitidas.

## Examinar opções de linha de comando

Em outro terminal, execute:

```bash
copilot --help
```

Compare estas opções documentadas com a ajuda da versão instalada:

| Opção | Finalidade |
| --- | --- |
| `--model MODEL` | Escolher o modelo para uma invocação; confirme a disponibilidade primeiro |
| `--agent AGENT` | Selecionar um agente personalizado para uma invocação |
| `-p PROMPT` | Executar um prompt programaticamente e sair quando ele terminar |
| `--output-format json` | Emitir saída JSONL estruturada, um objeto JSON por linha |
| `--resume` | Retomar uma sessão existente |
| `--enable-all-github-mcp-tools` | Expor o conjunto completo de ferramentas MCP do GitHub integradas |

São controles para entender, não outra tarefa para iniciar. O modo programático pode executar ações reais de ferramentas; um formato de saída JSON não torna uma solicitação somente de leitura. A seleção de agente segue o fluxo verificado da [Lição 7][qa-lesson], não é motivo para substituir a ativação do agente personalizado por um pedido ao agente padrão para ler o perfil. As permissões e o acesso continuam se aplicando.

## Revisar antes de compartilhar

`/share` pode enviar o conteúdo da sessão a diferentes destinos. A [referência de comandos da CLI][cli-reference] documenta `/share file [session|research] [PATH]` para exportação Markdown e `/share gist [session|research]` para publicar gists. Sem subcomando, o comportamento documentado atualmente cria um link compartilhável do GitHub quando você está conectado e sincronizado e recorre à exportação Markdown caso contrário. Não execute o comando sem argumentos presumindo que ele apenas exibe uma prévia.

Neste workshop, selecione explicitamente uma exportação local da sessão e um nome de arquivo em vez de publicar:

```text
/share file session cli-session-review.md
```

Abra o arquivo exportado no editor e examine o que ele realmente contém. Revise prompts, respostas, saída de ferramentas, caminhos de arquivos, dados do repositório e quaisquer credenciais ou informações pessoais. Não presuma que a exportação contém todos os passos internos ou que removeu automaticamente o conteúdo sensível.

> [!CAUTION]
> Um gist ou link compartilhado é uma divulgação externa. Um gist secreto não é controle de acesso privado: qualquer pessoa com sua URL pode vê-lo. Confirme o destino, os destinatários, as permissões e a política da organização antes de compartilhar. Se precisar ocultar informações, compartilhe apenas o arquivo revisado e sanitizado por um canal aprovado; não publique a sessão original depois.

Mantenha essa exportação fora do PR do recurso e do histórico do repositório. Após examiná-la, remova o arquivo que acabou de gerar ou mova-o para seu local aprovado de notas locais. Não remova arquivos não relacionados.

A delegação para a nuvem pode criar trabalho remoto e um PR adicional, então não execute `/delegate` aqui. O [workshop do agente de nuvem][cloud-workshop] cobre esse fluxo separado.

## Resumo e próximos passos

Você examinou contexto, uso, controles de modelos e modos, opções de linha de comando e destinos de compartilhamento sem iniciar outro recurso. Continue na [Lição 10 - Revisão e próximos passos][next-lesson] para revisar o fluxo e os ativos que criou.

[previous-lesson]: ../8-create-pull-request/
[next-lesson]: ../10-review/
[qa-lesson]: ../7-qa-agent/
[cloud-workshop]: ../../cloud/
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
