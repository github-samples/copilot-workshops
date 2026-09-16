---
title: "Preparar el proyecto y el modelo"
description: "Exporta el catálogo de Tailspin, crea un proyecto de Foundry y una implementación de modelo, y valídalos en Canvas."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/es-es/app/8-foundry-canvas/
  label: "Opcional: Incorporar Foundry"
next:
  link: /copilot-workshops/es-es/app/8-foundry-canvas/2-build-and-deploy/
  label: Crear e implementar el agente
---

Este primer módulo prepara los datos y los recursos de Azure para Backer Concierge. Todavía no se necesita código del agente ni una implementación hospedada.

Al terminar, tendrás:

- Una exportación del catálogo con límites explícitos sobre la información en la que se pueden basar las respuestas.
- Un proyecto de Foundry y una implementación de modelo elegida según los requisitos de la funcionalidad.
- Una implementación validada en Canvas y una comprobación básica del modelo limitada al catálogo.

## Escenario

Quienes apoyan los juegos de Tailspin Toys pueden filtrarlos por categoría y editor, pero preguntas como *¿Qué juegos serían adecuados para alguien a quien le encantan los juegos de palabras sobre Git?* no se responden con un menú desplegable. Backer Concierge debe recomendar solo juegos del catálogo de Tailspin y nunca inventar juegos, editores, valoraciones, importes recaudados, cifras de patrocinadores, precios, números de jugadores, duraciones de partida ni fechas de lanzamiento. Un catálogo fiable y un modelo adecuado son la base de esas respuestas.

## Preparar las herramientas y la sesión de la incidencia

La configuración conecta la aplicación GitHub Copilot con Azure y mantiene unido todo el trabajo de la funcionalidad.

> [!IMPORTANT]
> Microsoft Foundry Canvas y los agentes hospedados están en versión preliminar pública. Este módulo crea recursos de Azure que generan costes. Antes de crear recursos, es necesario comprobar la suscripción, la región, la cuota y el coste estimado.

1. Confirma que dispones de una suscripción de Azure, como una [suscripción gratuita de Azure con 200 $ de crédito][azure-free] o [Azure for Students con 100 $ de crédito][azure-students], y de permisos para crear los recursos del taller.
2. Instala la [CLI de Azure][install-azure-cli] para tu sistema operativo y verifica la instalación con `az version`. La configuración de Azure Developer CLI se deja para el módulo del agente hospedado.
3. Abre la aplicación GitHub Copilot, abre **Customize** y selecciona **Plugins**. Busca `microsoft-foundry` y selecciona **Install** para el complemento Microsoft Foundry, que incluye Canvas y las habilidades de Foundry.

   ![Instalar el complemento Microsoft Foundry](../../../_images/app-8-install-foundry-plugin.png)

4. En **Customize**, selecciona **Plugins**, busca `azure` o selecciónalo en la lista **Featured** y, después, selecciona **Install** para el complemento Azure.
5. En la pestaña **My work**, busca y abre la incidencia titulada **Add a Backer Concierge assistant for catalog questions** en el repositorio de Tailspin Toys. Selecciona **New session** para iniciar una sesión vinculada a la incidencia en un worktree nuevo. Conserva este repositorio, esta rama del worktree y esta sesión de la incidencia durante los tres módulos.
6. Escribe `/microsoft-foundry` y, después, `/azure` para confirmar que ambas habilidades están instaladas y disponibles; no envíes ninguna indicación todavía. Si un complemento no aparece de inmediato, reinicia la aplicación, vuelve a esta misma sesión de la incidencia y compruébalo de nuevo.

## Generar la exportación del catálogo

El repositorio de ejemplo incluye un script de exportación que proporciona al agente un archivo que puede leer.

7. En esta sesión del worktree vinculada a la incidencia, sustituye la indicación predeterminada `/fix-issue` del cuadro de indicaciones por:

   ```plaintext
   Install the project dependencies, seed the database, then run the existing db:export script. Show me the command output and summarize the shape and grounding limits of db/catalog.json.
   ```

8. Revisa la salida de los comandos. Copilot debería ejecutar el equivalente a:

   ```bash
   npm install
   npm run db:setup
   npm run db:export
   ```

   ![Generar la exportación del catálogo](../../../_images/app-8-generate-catalog-export.png)

9. Abre `db/catalog.json` y confirma que contiene 21 juegos con título, descripción, categoría, editor y valoración por estrellas. Comprueba el campo `note`: el catálogo no contiene importes recaudados, cifras de patrocinadores, niveles de aportación ni fechas de lanzamiento. Considera también como no disponibles los precios, números de jugadores y duraciones de partida que falten, en lugar de rellenar los huecos con conocimientos externos. Si la exportación falla o es distinta, pide a Copilot que lo investigue y vuelva a ejecutarla antes de continuar.

   ![Exportación del catálogo abierta en la aplicación Copilot](../../../_images/app-8-view-catalog.png)

## Configurar un proyecto de Foundry y un modelo

Crear primero el proyecto y la implementación en el chat permite que Canvas se conecte solo a recursos que ya existen.

10. Selecciona **+**, selecciona **Terminal** e inicia sesión en Azure:

    ```bash
    az login
    ```

11. Confirma la suscripción, la región, la cuota y el coste estimado seleccionados antes de aprobar la creación de recursos. Comprueba en Azure Portal que `rg-tailspin-toys` esté disponible para un grupo dedicado al taller. Si ese nombre pertenece a recursos ajenos o compartidos, detente y acuerda un nombre dedicado antes de utilizar la indicación siguiente; utiliza los nombres aprobados de forma coherente durante todo el recorrido.
12. En la misma sesión de la incidencia, introduce:

    ```plaintext
    Use the Microsoft Foundry skill to create a resource group named rg-tailspin-toys and a Foundry project named tailspin-toys.
    ```

    ![Crear un proyecto de Foundry](../../../_images/app-8-foundry-project-created.png)

13. Pide a Copilot que recomiende un modelo. Los criterios de aceptación de la incidencia ya están en el contexto porque la sesión se inició desde ella:

    ```plaintext
    Use the Microsoft Foundry skill to recommend two or three current chat models in the tailspin-toys project that meet this issue's acceptance criteria. Explain the tradeoffs and wait for me to choose.
    ```

14. Confirma que Copilot carga la habilidad `microsoft-foundry` y elige un modelo disponible según sus ventajas e inconvenientes. La guía de inicio rápido de agentes hospedados de Microsoft Foundry utiliza actualmente `gpt-5.4-mini`, pero la disponibilidad y la cuota varían según la región.

    ![Seleccionar un modelo](../../../_images/app-8-select-model.png)

15. Pide a Copilot que implemente el modelo elegido y revisa el proyecto de destino y el coste antes de aprobarlo:

    ```plaintext
    Deploy the model I selected to the tailspin-toys Foundry project, using the model name as the deployment name.
    ```

> [!TIP]
> La disponibilidad de los modelos cambia con el tiempo. La opción adecuada es el modelo que Copilot confirme que está disponible en tu proyecto, no un modelo fijado de antemano en este módulo.

## Validar el modelo y realizar una comprobación básica en Canvas

Esta comprobación verifica el proyecto y el modelo antes de que exista código del agente. Una comprobación básica del modelo no sustituye las pruebas del módulo 2 que verifican que el agente hospedado se basa en el catálogo.

16. Selecciona **+**, después **Canvas** y, a continuación, **Microsoft Foundry (Preview)**.
17. Abre el menú **More options** en la esquina superior derecha de Canvas y selecciona **Sign in**.
18. Selecciona el proyecto de Foundry **tailspin-toys**. Expande **Models** y confirma que la implementación aparece con el nombre y el estado esperados.

    ![Validar el proyecto y el modelo en Canvas](../../../_images/app-8-validate-project-model.png)

19. En la misma sesión de la incidencia en la aplicación GitHub Copilot, pide a Copilot que ejecute una pequeña solicitud autenticada a la implementación del modelo que has confirmado en Canvas, utilizando la sesión local de Azure que ya tienes iniciada. Pídele que proporcione dos entradas reales de `db/catalog.json` junto con el campo `note` del catálogo, solicite una recomendación basada únicamente en ese fragmento y pregunte si el fragmento incluye precios. Comprueba que la recomendación utilice las entradas proporcionadas y que la respuesta reconozca que los precios no están disponibles. Mantén las credenciales en local o en el lado del servidor, nunca en el código del navegador ni en la salida del chat; no se necesita generar la estructura inicial de un agente.
20. Compara el título, el editor y la valoración de la respuesta con las entradas proporcionadas. Si no puedes probar la implementación, comprueba el proyecto, el estado de la implementación, el acceso y la cuota en Canvas, y envía el error a Copilot. Si inventa detalles, indica explícitamente que debe utilizar solo el fragmento y vuelve a intentarlo. Registra el resultado sin considerarlo una prueba de que el agente cumple todos los criterios de aceptación.

> [!NOTE]
> Canvas recuerda el proyecto seleccionado cuando se vuelve a abrir. Sus etapas son **Create new hosted agents** para generar la estructura inicial, **Build current hosted agent** para conectar modelos, conjuntos de herramientas, habilidades y medidas de protección, y **Deploy and test** para las ejecuciones locales y la implementación en Foundry Agent Service.

## Punto de control y pasos siguientes

El resultado para continuar es una exportación del catálogo y una implementación de modelo probada, no la estructura inicial de un agente.

21. Registra en esta sesión el repositorio de Tailspin Toys, la rama actual del worktree, la sesión vinculada a la incidencia, el identificador de la suscripción, el grupo de recursos dedicado, el proyecto de Foundry, el nombre de la implementación del modelo, el resultado de la exportación del catálogo y las evidencias de la comprobación básica. Confirma el proyecto seleccionado antes de cada cambio posterior que genere costes.
22. Continúa con [Crear e implementar el agente][next-module] en este mismo repositorio, rama del worktree, sesión de la incidencia, proyecto de Foundry e implementación del modelo; no crees otro proyecto. Si te detienes aquí, sigue las instrucciones de [Limpiar los recursos][cleanup]; en este punto no necesitas ni `azure.yaml` ni `azd`.

[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[install-azure-cli]: https://learn.microsoft.com/cli/azure/install-azure-cli
[next-module]: ../2-build-and-deploy/
[cleanup]: ../#limpiar-los-recursos
