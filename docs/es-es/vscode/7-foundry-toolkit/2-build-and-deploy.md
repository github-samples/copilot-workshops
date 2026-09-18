---
title: "Crear e implementar un agente"
description: "Genera la estructura de Backer Concierge y depúralo en VS Code; después, impleméntalo y pruébalo como agente hospedado de Foundry."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← Módulo anterior: Preparar un proyecto y un modelo][previous-lesson] |
|:--|

Este módulo utiliza el catálogo y el modelo probado de [Preparar un proyecto y un modelo][previous-lesson]. Microsoft Foundry Toolkit y su agente personalizado **AIAgentExpert** guían la creación local y la implementación hospedada en VS Code.

## Objetivos

- Generar la estructura de un agente fundamentado en el catálogo dentro del área de trabajo existente de Tailspin Toys.
- Depurar el comportamiento local con Agent Inspector.
- Implementar en el proyecto de Foundry existente y verificar el agente hospedado.

## Escenario

Una recomendación fiable debe seguir siéndolo más allá de una sola conversación. Tailspin Toys necesita que el asistente respete los límites del catálogo cuando los patrocinadores hagan preguntas vagas o insistan en obtener datos de financiación no disponibles. Un asistente hospedado debe comportarse con la misma fiabilidad que uno probado en privado.

## Retomar el área de trabajo

El agente utiliza la implementación del modelo existente; no hay que crear un nuevo proyecto de Foundry.

1. Abre el mismo repositorio de Tailspin Toys en VS Code en `foundry-agent-vscode`. Confirma que existe `db/catalog.json` y que el proyecto `tailspin-toys` y la implementación del modelo probado están visibles en **Foundry Toolkit** > **My Resources**.
2. Confirma que se ha completado el [punto de control anterior][previous-lesson]. Si se eliminaron los recursos, vuelve a completar la preparación del proyecto y del modelo antes de continuar.
3. Instala Azure Developer CLI (`azd`) si todavía no está disponible. La implementación de agentes hospedados la utiliza; elige únicamente el comando correspondiente a tu sistema operativo:

   ```bash
   # macOS / Linux
   curl -fsSL https://aka.ms/install-azd.sh | bash

   # Windows (PowerShell)
   winget install microsoft.azd
   ```

4. Inicia sesión en la suscripción utilizada para el proyecto existente:

   ```bash
   azd auth login
   ```

> [!IMPORTANT]
> Los agentes hospedados y Foundry Toolkit están en versión preliminar pública. La implementación crea recursos facturables. Confirma la suscripción, los permisos, la región, la cuota y el coste estimado antes de aprobar comandos.

## Crear y depurar el agente

El kit de herramientas genera la estructura de código en el repositorio actual y abre un chat especializado de Copilot. Agent Inspector permite ver las solicitudes locales, los eventos y las llamadas a herramientas antes de la implementación.

1. Selecciona **Foundry Toolkit**, expande **Developer Tools**, expande **+ Build** y selecciona **+ Create Agent**. En **Create Agent**, selecciona **Code an agent with Copilot**.

   ![Captura de pantalla que muestra la página de creación de agentes.](../../../_images/vscode-create-agent.png)

2. En el nuevo chat, confirma que se cambia a **AIAgentExpert**. Sustituye el prompt generado por el prompt personalizado y envíalo:

   ```text
   /foundrytk-quick-start Create a backer concierge AI agent called 'Backer Concierge'. The agent should use the model I deployed to answer catalog questions and recommend games grounded strictly in db/catalog.json. Review the acceptance criteria in the issue titled 'Add a Backer Concierge assistant for catalog questions' and ensure the agent meets them. Generate the code into agent/backer-concierge in the current workspace and ask me if anything is unclear.
   ```

3. Revisa el código generado en `agent/backer-concierge`. Confirma que el catálogo está incluido en el agente que se puede implementar, que las pruebas específicas pasan y que no se incluirán credenciales ni archivos de entorno locales en los commits.
4. Selecciona **Run and Debug** en la barra de actividades e inicia el depurador con <kbd>F5</kbd>. Confirma que **Agent Inspector** se carga y se conecta al servidor del agente.
5. Reutiliza los seis prompts de [Probar el modelo implementado][model-tests]. Comprueba las respuestas con el archivo `db/catalog.json` completo, en lugar de suponer que la clasificación del subconjunto de nueve juegos coincide con la del catálogo completo.
6. Alterna entre **Input & Output**, **Events** y **Tools** para inspeccionar los datos de las solicitudes y respuestas, los eventos de sesión y las llamadas a herramientas. Si el comportamiento incumple los criterios de aceptación, pide a Copilot que lo corrija y vuelve a ejecutar las pruebas específicas y las comprobaciones de Inspector antes de implementar.

   ![Captura de pantalla que muestra el flujo de depuración local del agente.](../../../_images/vscode-agent-debug.png)

## Implementar y probar el agente hospedado

La transferencia **Go production** empaqueta el agente existente para Foundry. No convierte el posterior proxy del sitio en un servicio público listo para producción.

1. En el chat de Copilot de creación del agente, selecciona **Go production**, sustituye el prompt predeterminado por el siguiente y envíalo:

   ```text
   /foundrytk-quick-start Review this agent for deployment readiness, run its tests, then deploy it to my existing tailspin-toys Foundry project. Show me the deployment status and test the deployed agent.
   ```

   ![Captura de pantalla que muestra las opciones de transferencia del agente AIAgentExpert.](../../../_images/vscode-go-production-handoff.png)

2. Revisa el chat y el terminal para comprobar los parámetros y las solicitudes de aprobación de comandos. Confirma que la implementación tiene como destino el proyecto `tailspin-toys` existente y revisa los recursos facturables antes de aprobar.
3. Si Copilot ofrece un conjunto de evaluaciones, puedes aceptarlo y completarlo como comprobación adicional.
4. Selecciona **Foundry Toolkit**, expande **My Resources** y selecciona **Agents**. En la pestaña **Agents**, cambia a **Hosted Agent**.

   ![Captura de pantalla que muestra el agente hospedado implementado.](../../../_images/vscode-agent-deployed.png)

5. Selecciona el nombre del agente y confirma que el estado de implementación es **Running**. Cambia a **Playground** y repite las comprobaciones de fundamentación, datos ausentes, peticiones fuera del catálogo, peticiones vagas y clasificación con el catálogo implementado.

   ![Captura de pantalla que muestra una respuesta del agente hospedado implementado.](../../../_images/vscode-agent-response.png)

6. Si la implementación o las respuestas fallan, inspecciona con Copilot el estado notificado y los registros, corrige el fallo en el proyecto existente y repite las comprobaciones. No continúes con una implementación sin verificar.

## Punto de control al finalizar

Has generado la estructura del Backer Concierge, depurado su fundamentación en el catálogo con Agent Inspector, lo has implementado en Foundry mediante el traspaso **Go production** y has vuelto a probar la versión hospedada en el Playground. El punto de control de este módulo es un agente hospedado en ejecución que respeta el catálogo sin inventar la información que falta.

A continuación, utilizarás el mismo proyecto `tailspin-toys`, la implementación del modelo y el agente hospedado para conectar el agente al sitio. Si paras aquí, [elimina los recursos de Azure][cleanup] para evitar costes continuados.

| [Siguiente módulo: Conectar el agente al sitio →][next-lesson] |
|--:|

[previous-lesson]: ../1-project-and-model/
[model-tests]: ../1-project-and-model/#probar-el-modelo-implementado
[next-lesson]: ../3-connect-to-site/
[cleanup]: ../#eliminar-los-recursos
