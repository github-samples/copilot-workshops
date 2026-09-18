---
slug: es-es/cli/8-foundry-agent
title: "Opcional: incorpora Foundry"
description: "Una serie de tres módulos para preparar un modelo, crear y desplegar un agente basado en el catálogo y conectarlo a Tailspin Toys."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

Esta serie opcional usa GitHub Copilot CLI y la habilidad Microsoft Foundry para convertir el catálogo de Tailspin Toys en un asistente conversacional. Los tres módulos te llevan desde la configuración del proyecto y del modelo hasta un agente hospedado y una integración funcional con el sitio web.

En esta serie:

- prepararás un entorno de Azure y probarás un modelo con el catálogo.
- generarás la estructura de un agente Backer Concierge hospedado, lo probarás y lo desplegarás.
- conectarás el agente al sitio web mediante un proxy local del lado del servidor y un widget de chat.

## Escenario

Quienes apoyan los juegos de Tailspin Toys pueden explorarlos por categoría y editorial, pero esos filtros no ayudan a todo el mundo a encontrar su próximo juego. Algunas personas tienen preguntas como *¿Qué juegos serían adecuados para alguien a quien le encantan los juegos de palabras sobre Git?* Esas preguntas no se responden con un menú desplegable.

Tailspin Toys quiere un **Backer Concierge** que ayude a quienes apoyan sus juegos a descubrir nuevos títulos mediante una conversación. Debe recomendar juegos del catálogo de Tailspin, hacer una pregunta breve para aclarar las preferencias cuando sean vagas y recordar las recomendaciones anteriores cuando se plantee una pregunta de seguimiento.

Quienes apoyan los juegos necesitan respuestas fiables. El concierge debe usar únicamente la información del catálogo e indicar claramente cuándo un dato no está disponible, en lugar de inventar juegos, editoriales, valoraciones, importes totales de financiación, cifras de personas que los apoyan, precios, números de jugadores, duraciones de las partidas o fechas de lanzamiento.

## Elige el siguiente paso

Los módulos se apoyan unos en otros y usan el mismo repositorio de Tailspin Toys, la misma rama y el mismo proyecto de Foundry. Cada uno termina con un resultado funcional que puedes comprobar.

| Módulo | Qué harás | Resultado al terminar |
| --- | --- | --- |
| [1. Prepara el proyecto y el modelo][project-model] | Configura las herramientas, exporta el catálogo y selecciona y prueba un modelo | Un modelo desplegado que responde correctamente a preguntas sobre el catálogo |
| [2. Crea y despliega el agente][build-deploy] | Genera la estructura del agente, prueba su comportamiento y despliégalo en Foundry | Un Backer Concierge hospedado y funcional |
| [3. Conecta el agente al sitio web][connect-site] | Crea un proxy local y un widget de chat y prueba el flujo completo | Un concierge disponible en tu sitio web local |

> [!IMPORTANT]
> Los agentes hospedados de Microsoft Foundry están en versión preliminar pública.
>
> Esta serie crea recursos facturables de Azure, entre ellos un despliegue de modelo y un agente hospedado. Antes de crear recursos, debes revisar la suscripción, la región y la cuota seleccionadas, así como el coste estimado. Las [instrucciones de limpieza][cleanup] también se aplican si paras después del primer o del segundo módulo.

1. Para empezar la serie opcional, continúa con [Prepara el proyecto y el modelo][project-model]. Allí se incluyen las instrucciones de configuración.
2. Si prefieres terminar el taller principal, continúa con [Repaso y próximos pasos][review].

## Elimina los recursos

Cuando termines de experimentar en cualquiera de los puntos de comprobación, elimina los recursos de Azure para evitar costes no deseados. La limpieza elimina recursos necesarios para los módulos posteriores, por lo que tendrás que volver a crearlos si quieres continuar después.

> [!CAUTION]
> Elimina `rg-tailspin-toys` solo si está dedicado a este ejercicio y no contiene recursos que necesites conservar. Si eliminas un grupo de recursos compartido, también eliminarás recursos ajenos al ejercicio.

1. Detén cualquier agente local, función o servidor de desarrollo de Astro que hayas iniciado pulsando <kbd>Ctrl</kbd>+<kbd>C</kbd> en su terminal.
2. Sal de Copilot CLI. Si generaste la estructura del agente en el módulo 2, ejecuta lo siguiente desde la raíz del repositorio de Tailspin Toys usando el mismo entorno de `azd`:

    ```bash
    azd down --purge
    ```

3. Comprueba la suscripción seleccionada con `az account show`. Inspecciona `rg-tailspin-toys` en esa suscripción y verifica que todos los recursos restantes pertenecen a este ejercicio. Si paraste después del módulo 1, debes eliminar el proyecto de Foundry y el modelo aunque aún no hayas generado la estructura de un servicio de `azd`.
4. Si el grupo de recursos dedicado al taller sigue existiendo y solo contiene recursos que quieres eliminar, ejecuta:

    ```bash
    az group delete --name rg-tailspin-toys --yes --no-wait
    ```

5. Confirma en Azure Portal que la eliminación del grupo de recursos ha terminado. El comando con `--no-wait` devuelve el control antes de que termine la eliminación.

## Recursos

- [Complemento Azure Skills][azure-skills]
- [Usar la habilidad Microsoft Foundry en agentes de programación][foundry-skill]
- [Desplegar tu primer agente hospedado con la habilidad Microsoft Foundry][hosted-agent-quickstart]
- [Permisos de los agentes hospedados][hosted-agent-permissions]

[project-model]: 1-project-and-model/
[build-deploy]: 2-build-and-deploy/
[connect-site]: 3-connect-to-site/
[review]: ../9-review/
[cleanup]: #elimina-los-recursos
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
[foundry-skill]: https://learn.microsoft.com/azure/foundry/how-to/develop/use-microsoft-foundry-skill?tabs=copilot-cli
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=foundry-skills
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
