---
title: "Módulo 1 - Prepara el proyecto y el modelo"
description: "Configura las herramientas de Azure, exporta el catálogo de Tailspin y selecciona y prueba un modelo de Foundry con GitHub Copilot CLI."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

Este es el primer módulo de [Opcional: incorpora Foundry][overview]. Prepararás las herramientas y el catálogo y, después, usarás Copilot para crear un proyecto de Foundry y probar un modelo desplegado antes de crear el agente.

En este módulo:

- instalarás las herramientas de línea de comandos de Azure y el complemento Azure Skills.
- exportarás el catálogo y planificarás el trabajo en Foundry.
- seleccionarás, desplegarás y probarás un modelo teniendo en cuenta los límites del catálogo.

## Escenario

Tailspin Toys necesita un concierge que distinga entre los datos del catálogo y la información que la empresa no proporciona. Una recomendación útil podría mencionar un juego de puzles con una buena valoración, pero no debe inventar su importe total de financiación. Antes de invertir en un asistente completo, el equipo quiere asegurarse de que el modelo elegido respeta ese límite.

## Requisitos previos y configuración

Usarás Azure para hospedar el Backer Concierge y Copilot CLI para guiar el trabajo. Primero, prepara las herramientas de línea de comandos y el complemento que permiten a Copilot trabajar con tus recursos de Azure.

> [!IMPORTANT]
> Las [instrucciones de limpieza][cleanup] cubren tanto la posibilidad de parar después de este módulo como la de terminar la serie.

1. Confirma que tienes una suscripción de Azure. Si necesitas una, las opciones disponibles incluyen una [suscripción gratuita de Azure con 200 USD de crédito][azure-free] o [Azure for Students con 100 USD de crédito][azure-students].
2. Vuelve a tu codespace de Tailspin Toys y abre un terminal.
3. Instala Azure CLI en el contenedor de desarrollo:

    ```bash
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    az version
    ```

4. Inicia sesión en Azure CLI con `az login` y comprueba que estás usando la suscripción correcta con `az account show`.
5. Instala [Azure Developer CLI][install-azd], versión 1.27.1 o posterior. Microsoft Foundry usa `azd` para probar y desplegar agentes hospedados.

    ```bash
    curl -sL https://aka.ms/install-azd.sh | bash
    azd version
    ```

6. Inicia sesión en Azure Developer CLI con `azd auth login` y comprueba que estás usando la suscripción correcta con `azd config show`.
7. Instala la extensión de Foundry para Azure Developer CLI (azd):

    ```bash
    azd ext install microsoft.foundry
    ```

8. Abre una nueva sesión de Copilot CLI en un panel lateral desde la paleta de comandos. Pulsa <kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Mac) o <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Windows/Linux) y selecciona **Chat: New Copilot CLI session to the side**.
9. Añade el marketplace de Azure Skills. Solo necesitas hacerlo la primera vez que instalas el complemento:

    ```text
    /plugin marketplace add microsoft/azure-skills
    ```

10. Instala el [complemento Azure Skills][azure-skills], que añade habilidades de Azure, Azure MCP Server y Foundry MCP Server a GitHub Copilot CLI:

    ```text
    /plugin install azure@azure-skills
    ```

11. Confirma que el complemento ha configurado el servidor MCP de Azure:

    ```text
    /mcp list
    ```

12. Si las habilidades o los servidores MCP no aparecen, prueba `/skills reload` o `/restart` y vuelve a comprobarlo.

Las habilidades enseñan a Copilot el flujo de trabajo, mientras que los servidores MCP le permiten inspeccionar tus recursos de Azure y trabajar con ellos.

## Prepara la rama de trabajo

En los ejercicios anteriores puede que hayas creado y enviado otras ramas de funcionalidades. Empezarás esta serie opcional desde una rama `main` actualizada para mantener separado el trabajo del agente.

1. En el terminal de shell, cambia a `main`, descarga los últimos cambios y crea una rama para el Backer Concierge:

    ```bash
    git checkout main
    git pull
    git checkout -b foundry-agent-cli
    ```

## Genera la exportación del catálogo

El agente necesita el catálogo en un archivo que pueda leer. El ejemplo de Tailspin Toys incluye un script de exportación probado para este fin.

1. Vuelve a Copilot CLI e introduce:

    ```text
    Install the project dependencies, seed the database, then run the existing db:export script. Show me the command output and summarize the shape and grounding limits of db/catalog.json.
    ```

    Copilot debería ejecutar el equivalente de:

    ```bash
    npm install
    npm run db:setup
    npm run db:export
    ```

    ![Resumen de la exportación del catálogo](../../../_images/cli-8-export-db-catalog.png)

2. Abre `db/catalog.json`. Confirma que contiene 21 juegos con título, descripción, categoría, editorial y valoración por estrellas. Su campo `note` indica que el catálogo no contiene importes totales de financiación, cifras de personas que apoyan los juegos, niveles de aportación ni fechas de lanzamiento. Tampoco tiene campos de precio, número de jugadores o duración de las partidas. Esas omisiones definen el límite que debe respetar el agente.

## Planifica el trabajo en Foundry

Antes de que Copilot cree recursos de Azure o añada código del agente, usarás el modo de planificación para revisar el flujo de trabajo previsto.

1. Introduce el siguiente prompt:

    ```text
    /plan Use the Microsoft Foundry Skill to plan a Backer Concierge hosted agent for this existing Tailspin Toys repository. Use a public Foundry project, Python 3.13, Microsoft Agent Framework, the Responses API, the Basic sample, and code deployment. Keep the agent in agent/backer-concierge and keep one azure.yaml at the repository root. Ground every answer in db/catalog.json, preserve conversation context, and add focused tests. Include project setup, model selection, local testing, deployment, remote invocation, estimated cost-bearing resources and cleanup.
    ```

2. Revisa el plan propuesto. Confirma que Copilot pretende usar la habilidad `microsoft-foundry` y que separa el agente hospedado de la aplicación Astro existente. Si observas algo preocupante o inesperado, solicita cambios antes de continuar.
3. Sal del modo de planificación cuando estés conforme con el enfoque.

## Configura un proyecto de Foundry y un modelo

El agente necesita un proyecto de Foundry y un modelo desplegado. Usarás la habilidad Microsoft Foundry para seleccionarlos según la disponibilidad y la cuota actuales de tu suscripción.

1. Pide a Copilot que cree el proyecto. Antes de aprobar la creación de recursos, comprueba la suscripción, la región y la cuota seleccionadas, así como el coste estimado:

    ```text
    Use the Microsoft Foundry Skill to create a public Foundry project for this project. Use the resource group rg-tailspin-toys and project name tailspin-toys.
    ```

    ![Creación de un proyecto público de Foundry](../../../_images/cli-8-create-foundry-project.png)

2. Cuando el proyecto esté listo, pide a Copilot que recomiende un modelo:

    ```text
    Use the Microsoft Foundry Skill to recommend two or three current chat models available in the tailspin-toys project for the Backer Concierge acceptance criteria in the issue titled "Add a Backer Concierge assistant for catalog questions". Prioritize low latency, instruction following, grounding fidelity, available quota, and models that aren't approaching retirement. There is no complex math or multi-step planning. Explain the tradeoffs and wait for me to choose a model from the recommended options.
    ```

    Copilot puede pedirte que selecciones un modelo entre las opciones recomendadas.

    ![Selección de un modelo entre las opciones recomendadas](../../../_images/cli-8-select-foundry-model.png)

    Continuaremos con `gpt-5.4-mini` en los pasos restantes, pero la disponibilidad y la cuota varían según la región.

3. Selecciona un modelo entre las opciones recomendadas y pide a Copilot que lo despliegue. Revisa la capacidad y el coste antes de aprobar el despliegue:

    ```text
    Deploy the model we selected to the tailspin-toys Foundry project and use the model name as the deployment name. Choose an SKU with available quota, ask me to confirm the capacity before deployment. After deployment, show me the deployment status.
    ```

    ![Despliegue del modelo seleccionado](../../../_images/cli-8-deploy-foundry-model.png)

> [!TIP]
> La disponibilidad de los modelos cambia con el tiempo. La elección adecuada es un modelo cuya disponibilidad en tu proyecto confirme Copilot, no un modelo fijado en un ejemplo.

## Prueba el modelo desplegado

Antes de crear el agente hospedado, comprobarás si el modelo sigue las reglas del Backer Concierge para fundamentar las respuestas en el catálogo. Esta prueba usa las instrucciones previstas y el contexto del catálogo, sin código ni configuración de agente.

Primero, asignarás a la cuenta con la que has iniciado sesión el rol **Foundry Project Manager**, para desarrollar el agente hospedado en el módulo 2, y el rol **Cognitive Services OpenAI User**, para realizar inferencias directamente con el modelo. Después, harás una pregunta sobre el catálogo que también solicite información que este no contiene.

1. Abre un terminal nuevo y define los valores de la cuenta, el proyecto y el usuario. Sustituye `<foundry-account-name>` por el nombre de la cuenta de Foundry que se indicó al crear el proyecto:

    ```bash
    SUBSCRIPTION_ID=$(az account show --query id --output tsv)
    USER_OBJECT_ID=$(az ad signed-in-user show --query id --output tsv)
    FOUNDRY_ACCOUNT="<foundry-account-name>"
    ACCOUNT_SCOPE=$(az cognitiveservices account show --name "$FOUNDRY_ACCOUNT" --resource-group rg-tailspin-toys --query id --output tsv)
    PROJECT_SCOPE="$ACCOUNT_SCOPE/projects/tailspin-toys"
    ```

2. Asigna el rol **Foundry Project Manager**:

    ```bash
    az role assignment create \
       --assignee-object-id "$USER_OBJECT_ID" \
       --assignee-principal-type User \
       --role "Foundry Project Manager" \
       --scope "$PROJECT_SCOPE" \
       --subscription "$SUBSCRIPTION_ID"
    ```

3. Asigna el rol **Cognitive Services OpenAI User**:

    ```bash
    az role assignment create \
       --assignee-object-id "$USER_OBJECT_ID" \
       --assignee-principal-type User \
       --role "Cognitive Services OpenAI User" \
       --scope "$ACCOUNT_SCOPE" \
       --subscription "$SUBSCRIPTION_ID"
    ```

4. Vuelve a Copilot CLI e introduce:

    ```text
    Use the Microsoft Foundry Skill to test my deployed model directly in the tailspin-toys project without creating an agent. Ground it with content from @db/catalog.json and ask: "I love puzzle games about tracking down bugs. What should I back, and how much funding has it raised?" Show me the response and useful metadata like tokens used and response time (only if you can obtain it). Do not change files or create resources.
    ```

    ![Respuesta del modelo de Foundry que recomienda un juego real del catálogo e indica que no hay datos de financiación disponibles](../../../_images/cli-8-foundry-agent-response.png)

5. Revisa la respuesta. Debe recomendar únicamente un juego real del catálogo, usar los datos correctos del catálogo y explicar que la información de financiación no está disponible. Si el modelo inventa un título, detalles del juego o un importe total de financiación, compáralo con otro modelo recomendado antes de continuar.

> [!NOTE]
> Esta prueba solo evalúa el modelo desplegado con instrucciones temporales y el contexto del catálogo. No prueba un agente. El módulo 2 repite la prueba después de generar la estructura del agente para validar su código, su empaquetado y su comportamiento conversacional.

## Resumen y siguientes pasos

Has preparado las herramientas de Azure, exportado el catálogo y probado un modelo desplegado con las reglas del Backer Concierge para fundamentar las respuestas en el catálogo. El resultado que debes comprobar al terminar este módulo es un modelo que recomiende juegos reales del catálogo sin inventar la información que falta.

A continuación, usarás el mismo repositorio, la rama `foundry-agent-cli`, la sesión de Copilot CLI, el proyecto de Foundry y el despliegue del modelo seleccionado para [crear y desplegar el agente][next-lesson]. Si vas a parar aquí, [elimina los recursos de Azure][cleanup] para evitar que sigan generando costes.

[overview]: ../
[next-lesson]: ../2-build-and-deploy/
[cleanup]: ../#elimina-los-recursos
[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[install-azd]: https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
