---
slug: pt-br/cli/8-foundry-agent
title: "Opcional: Incorpore o Foundry"
description: "Uma série de três módulos para preparar um modelo, criar e implantar um agente baseado no catálogo e conectá-lo ao Tailspin Toys."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

Esta série opcional usa o GitHub Copilot CLI e a skill do Microsoft Foundry para transformar o catálogo do Tailspin Toys em um assistente de conversação. Os três módulos levam você da configuração do projeto e do modelo a um agente hospedado e uma integração funcional com o site.

Nesta série, você vai:

- preparar um ambiente do Azure e testar um modelo com base no catálogo.
- gerar a estrutura, testar e implantar um agente Backer Concierge hospedado.
- conectar o agente ao site por meio de um proxy local do lado do servidor e um widget de chat.

## Cenário

Os apoiadores do Tailspin Toys podem explorar jogos por categoria e editora, mas esses filtros não ajudam todo mundo a encontrar o próximo jogo. Alguns apoiadores têm perguntas como *Quais jogos seriam indicados para quem adora trocadilhos com Git?* Essas perguntas não têm respostas em menus suspensos.

O Tailspin Toys quer um **Backer Concierge** que ajude os apoiadores a descobrir jogos por meio de uma conversa. Ele deve recomendar jogos do catálogo do Tailspin, fazer uma pergunta breve de esclarecimento quando as preferências de alguém forem vagas e lembrar as recomendações anteriores quando essa pessoa fizer uma pergunta de acompanhamento.

Os apoiadores precisam de respostas confiáveis. O concierge deve usar apenas informações do catálogo e deixar claro quando um detalhe não estiver disponível, em vez de inventar jogos, editoras, avaliações, totais arrecadados, quantidades de apoiadores, preços, números de jogadores, tempos de jogo ou datas de lançamento.

## Escolha seu próximo passo

Os módulos dão continuidade ao trabalho anterior no mesmo repositório do Tailspin Toys, na mesma branch e no mesmo projeto do Foundry. Cada um termina com um resultado funcional.

| Módulo | O que você vai fazer | Resultado ao concluir |
| --- | --- | --- |
| [1. Prepare o projeto e o modelo][project-model] | Configurar as ferramentas, exportar o catálogo e selecionar e testar um modelo | Um modelo implantado que responde corretamente a perguntas sobre o catálogo |
| [2. Crie e implante o agente][build-deploy] | Gerar a estrutura do agente, testar seu comportamento e implantá-lo no Foundry | Um Backer Concierge hospedado e funcional |
| [3. Conecte o agente ao site][connect-site] | Criar um proxy local e um widget de chat e testar o fluxo completo | Um concierge disponível no site local |

> [!IMPORTANT]
> Os agentes hospedados do Microsoft Foundry estão em versão prévia pública.
>
> Esta série cria recursos do Azure que geram custos, incluindo uma implantação de modelo e um agente hospedado. A criação de recursos exige uma revisão da assinatura, da região, da cota e do custo estimado selecionados. As [instruções de limpeza][cleanup] se aplicam mesmo se você parar após o primeiro ou o segundo módulo.

1. Para começar a série opcional, continue em [Prepare o projeto e o modelo][project-model]. As instruções de configuração estão incluídas nesse módulo.
2. Se preferir concluir o workshop principal, continue em [Revisão e próximos passos][review].

## Limpe seus recursos

Quando terminar de experimentar em qualquer etapa, remova os recursos do Azure para evitar custos indesejados. A limpeza remove recursos necessários para os módulos seguintes, portanto, será preciso recriá-los se quiser continuar depois.

> [!CAUTION]
> Exclua `rg-tailspin-toys` somente se ele for dedicado a este exercício e não contiver recursos que você precisa manter. Excluir um grupo de recursos compartilhado também removeria recursos não relacionados.

1. Pare qualquer agente local, Function ou servidor de desenvolvimento do Astro que tenha iniciado pressionando <kbd>Ctrl</kbd>+<kbd>C</kbd> no respectivo terminal.
2. Saia do Copilot CLI. Se você gerou a estrutura do agente no Módulo 2, execute o comando a seguir na raiz do repositório do Tailspin Toys usando o mesmo ambiente do `azd`:

    ```bash
    azd down --purge
    ```

3. Verifique a assinatura selecionada com `az account show`. Inspecione `rg-tailspin-toys` nessa assinatura e confirme que todos os recursos restantes pertencem a este exercício. Se você parou após o Módulo 1, o projeto do Foundry e o modelo ainda precisam de limpeza, mesmo que você não tenha gerado a estrutura de um serviço do `azd`.
4. Se o grupo de recursos dedicado ao workshop ainda existir e contiver apenas recursos que você pretende remover, execute:

    ```bash
    az group delete --name rg-tailspin-toys --yes --no-wait
    ```

5. Confirme no portal do Azure que a exclusão do grupo de recursos foi concluída. O comando com `--no-wait` retorna antes de a exclusão terminar.

## Recursos

- [Plugin Azure Skills][azure-skills]
- [Use a skill do Microsoft Foundry em agentes de programação][foundry-skill]
- [Implante seu primeiro agente hospedado com a skill do Microsoft Foundry][hosted-agent-quickstart]
- [Permissões de agentes hospedados][hosted-agent-permissions]

[project-model]: 1-project-and-model/
[build-deploy]: 2-build-and-deploy/
[connect-site]: 3-connect-to-site/
[review]: ../9-review/
[cleanup]: #limpe-seus-recursos
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
[foundry-skill]: https://learn.microsoft.com/azure/foundry/how-to/develop/use-microsoft-foundry-skill?tabs=copilot-cli
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=foundry-skills
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
