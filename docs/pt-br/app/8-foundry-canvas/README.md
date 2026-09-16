---
title: "Opcional: Incorporar o Foundry"
slug: pt-br/app/8-foundry-canvas
description: "Crie um Backer Concierge baseado no catálogo com o Microsoft Foundry Canvas, com pontos seguros para encerrar ao longo do percurso."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/pt-br/app/9-review/
  label: Revisão e próximos passos
next:
  link: /copilot-workshops/pt-br/app/8-foundry-canvas/1-project-and-model/
  label: Preparar o projeto e o modelo
---

Este percurso opcional adiciona um **Backer Concierge** à Tailspin Toys usando o Microsoft Foundry Canvas no aplicativo GitHub Copilot. Ele começa com um experimento de modelo baseado no catálogo, avança para um agente hospedado e termina com uma integração local ao site.

## O percurso

Cada módulo termina com um ponto de verificação e um ponto seguro para encerrar. O mesmo repositório Tailspin Toys, branch do worktree, sessão vinculada à issue, projeto do Foundry e implantação de modelo são mantidos ao longo do percurso.

- [Preparar o projeto e o modelo][module-1] estabelece os limites do catálogo, cria o projeto e a implantação de modelo e verifica ambos no Canvas.
- [Criar e implantar o agente][module-2] gera a estrutura inicial do Backer Concierge, testa-o localmente e implanta e testa novamente o agente hospedado.
- [Conectar o agente ao site][module-3] adiciona um proxy local que protege as credenciais, um widget de chat acessível, testes de ponta a ponta e o Agent merge.

> [!IMPORTANT]
> O Microsoft Foundry Canvas e os agentes hospedados estão em versão prévia pública.
>
> Este percurso cria recursos do Azure que geram custos, incluindo uma implantação de modelo e, a partir do módulo 2, um agente hospedado. A assinatura, a região, a cota e o custo estimado precisam de aprovação antes da criação dos recursos. A limpeza também se aplica quando você encerra após criar apenas o projeto e o modelo.

1. Comece por [Preparar o projeto e o modelo][module-1], mantendo o trabalho no repositório Tailspin Toys, e não neste repositório de conteúdo do workshop.
2. No ponto em que escolher encerrar — projeto e modelo, implantação hospedada ou integração completa — registre o ponto de verificação do módulo e siga as instruções de limpeza compartilhadas abaixo quando terminar de experimentar. Continuar mais tarde, após a limpeza, exige restaurar os recursos excluídos e verificar novamente a configuração deles.

## Limpar seus recursos

A limpeza depende de até onde você avançou. Se você criou apenas o projeto e o modelo, não é necessário ter `azure.yaml`, um ambiente `azd` ou um agente hospedado.

> [!WARNING]
> A exclusão de recursos é destrutiva. Somente recursos dedicados a este workshop podem ser excluídos aqui. Nunca exclua um grupo de recursos compartilhado; a alternativa segura é remover os recursos do workshop individualmente, em conjunto com a pessoa responsável pelos recursos.

1. Nos respectivos terminais, interrompa todos os processos locais do Agent Inspector, da Azure Function e do servidor de desenvolvimento do Astro que você iniciou. Registre os detalhes dos pontos de verificação de que precisar antes de excluir os recursos do Azure.
2. No portal do Azure, confirme a ID da assinatura ativa, o nome exato do grupo de recursos do workshop e todos os recursos que ele contém. Verifique se o projeto do Foundry e a implantação de modelo pertencem a esta execução. Se houver dúvidas sobre a assinatura, a responsabilidade pelos recursos ou o conteúdo do grupo, interrompa a limpeza até esclarecê-las.
3. Escolha o caminho de limpeza para o ponto em que você encerrou. Se concluiu apenas o módulo 1, pule a próxima etapa e use a etapa 5; não crie `azure.yaml` nem inicialize `azd` apenas para fazer a limpeza. Se fez a implantação com o Canvas no módulo 2 ou 3, continue com a etapa 4.
4. Para uma implantação hospedada, abra um terminal no mesmo worktree da Tailspin Toys que contém o `azure.yaml` na raiz. Confirme que o ambiente `azd` selecionado aponta para a assinatura e os recursos desta execução, revise os recursos que serão excluídos e execute o comando a seguir somente quando todos os destinos forem dedicados ao seu workshop:

   ```bash
   azd down --purge
   ```

5. Se você criou apenas o projeto e o modelo, ou se o grupo de recursos dedicado ao workshop ainda existir após `azd down`, verifique novamente a assinatura, o nome do grupo e a lista completa de recursos no portal. Se todo o grupo for dedicado a esta execução e o nome for exatamente `rg-tailspin-toys`, execute o comando a seguir. Se o nome for diferente, use o nome dedicado que você verificou; se o grupo for compartilhado, não execute este comando e coordene a limpeza individual dos recursos com a pessoa responsável pelo grupo.

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

6. Verifique no portal do Azure se a exclusão foi concluída; `--no-wait` retorna antes de a exclusão terminar. Confirme que a implantação de modelo do workshop e todos os recursos de agentes hospedados foram removidos e resolva a situação de quaisquer recursos restantes do workshop que gerem custos, sem excluir recursos compartilhados.
7. Volte para [Revisão e próximos passos][core-review] quando concluir o ponto de verificação escolhido e a limpeza.

## Recursos

A documentação da Microsoft descreve o Canvas, as implantações hospedadas e suas permissões.

- [O que é o Microsoft Foundry Canvas?][foundry-canvas]
- [Implantar seu primeiro agente hospedado com o Foundry Canvas][hosted-agent-quickstart]
- [Permissões de agentes hospedados][hosted-agent-permissions]

[module-1]: ./1-project-and-model/
[module-2]: ./2-build-and-deploy/
[module-3]: ./3-connect-to-site/
[core-review]: ../9-review/
[foundry-canvas]: https://learn.microsoft.com/azure/foundry/agents/concepts/foundry-canvas
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=canvas
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
