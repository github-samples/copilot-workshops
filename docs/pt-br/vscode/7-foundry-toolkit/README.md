---
slug: pt-br/vscode/7-foundry-toolkit
title: "Opcional: Incorporar o Foundry"
description: "Crie um Backer Concierge fundamentado no catálogo com o VS Code e o Microsoft Foundry Toolkit em três módulos focados."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← Lição anterior: Iterar sobre o trabalho do GitHub Copilot][previous-lesson] |
|:--|

A trilha obrigatória do VS Code está concluída após o Exercício 6. Esta extensão opcional usa o GitHub Copilot Chat e o Microsoft Foundry Toolkit no VS Code para transformar o catálogo da Tailspin em um Backer Concierge, implantá-lo como agente hospedado e conectá-lo ao site por meio de um proxy local.

## Cenário

Os apoiadores fazem perguntas que os filtros não conseguem responder: qual jogo combina com alguém que adora trocadilhos com git, ou o que torna um jogo de quebra-cabeça mais adequado do que outro? A Tailspin Toys precisa de um assistente que recomende títulos reais do catálogo, faça uma pergunta de esclarecimento quando necessário e conquiste a confiança ao admitir quando os números de financiamento ou outros fatos não estão disponíveis.

## Módulos

Cada módulo termina com uma etapa funcional concluída. O mesmo repositório do participante, a mesma branch de funcionalidade e o mesmo projeto do Foundry são usados nos três módulos; o projeto não é recriado entre eles.

| Módulo | Marco de conclusão |
|--------|-----------------------|
| [1. Preparar um projeto e um modelo][module-1] | Catálogo exportado e modelo implantado testado em relação às regras de fundamentação |
| [2. Criar e implantar um agente][module-2] | Agente local depurado e agente hospedado testado |
| [3. Conectar o agente ao site][module-3] | Proxy local e widget acessível testados de ponta a ponta |

> [!IMPORTANT]
> O Microsoft Foundry Toolkit e os agentes hospedados estão em versão prévia pública. Estes módulos criam recursos do Azure sujeitos a cobrança, incluindo uma implantação de modelo e um agente hospedado. Permissões da assinatura, disponibilidade regional, cota e custo podem limitar a participação.

## Antes de começar

A extensão usa como base o seu repositório da Tailspin Toys, não o repositório de documentação do workshop.

1. Confirme que o trabalho obrigatório do workshop foi salvo, registrado em commits e enviado ao repositório remoto antes de iniciar a funcionalidade opcional.
2. Comece por [Preparar um projeto e um modelo][module-1]. Se estiver retomando o trabalho, reabra o repositório do Tailspin Toys na branch `foundry-agent-vscode` e confirme que o projeto `tailspin-toys` e a respectiva implantação do modelo ainda existem em **Foundry Toolkit** > **My Resources**.
3. Ao parar após qualquer módulo, siga [Limpar os recursos][cleanup], a menos que decida manter os recursos para o próximo módulo e aceite os custos contínuos.

## Limpar os recursos

Quando terminar de experimentar em qualquer marco de conclusão, remova os recursos do Azure para evitar custos indesejados. A limpeza remove recursos necessários para os módulos seguintes, portanto continuar depois exige recriá-los.

> [!WARNING]
> Só exclua `rg-tailspin-toys` se ele for exclusivo deste exercício e não contiver recursos que você queira manter. Excluir um grupo de recursos compartilhado removeria também recursos não relacionados.
>
> Se você aprovou outro nome de grupo de recursos no módulo 1, substitua `rg-tailspin-toys` por esse nome em todos os comandos a seguir.

1. Pare, no respectivo terminal, qualquer sessão de depuração do Agent Inspector, host do Azure Functions ou servidor de desenvolvimento do Astro que você tenha iniciado.
2. Se você implantou o agente hospedado no módulo 2, abra um terminal no diretório do agente gerado que contém `azure.yaml`, selecione o mesmo ambiente `azd` e execute:

   ```bash
   azd down --purge
   ```

3. Verifique a assinatura selecionada e se o grupo de recursos do workshop ainda existe:

   ```bash
   az account show --output table
   az group exists --name rg-tailspin-toys
   ```

   Se o comando retornar `false`, a limpeza está concluída. Se retornar `true`, inspecione os recursos do grupo:

   ```bash
   az resource list --resource-group rg-tailspin-toys --output table
   ```

   Verifique se todos os recursos restantes pertencem a este exercício. Se você parou após o módulo 1, o projeto e o modelo do Foundry ainda precisam de limpeza, mesmo que você não tenha implantado um serviço `azd`.

4. Se o grupo de recursos exclusivo do workshop ainda existir e contiver apenas recursos que você pretende remover, execute:

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

5. Como `--no-wait` retorna antes de a exclusão terminar, execute novamente o comando a seguir até que ele retorne `false`:

   ```bash
   az group exists --name rg-tailspin-toys
   ```

## Recursos

- [Foundry Toolkit para Visual Studio Code][foundry-toolkit]
- [Visão geral da extensão de agentes do Microsoft Foundry][foundry-extension]

| [Próximo módulo: Preparar um projeto e um modelo →][module-1] |
|--:|

[previous-lesson]: ../6-iterating/
[module-1]: 1-project-and-model/
[module-2]: 2-build-and-deploy/
[module-3]: 3-connect-to-site/
[cleanup]: #limpar-os-recursos
[foundry-toolkit]: https://code.visualstudio.com/docs/intelligentapps/overview
[foundry-extension]: https://learn.microsoft.com/azure/developer/azure-developer-cli/extensions/azure-ai-foundry-extension
