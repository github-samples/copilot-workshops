---
title: "Preparar un proyecto y un modelo"
description: "Exporta el catálogo de Tailspin y prueba un modelo implementado frente a los criterios de aceptación de Backer Concierge."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← Opcional: Incorporar Foundry][overview] |
|:--|

Este primer módulo prepara los datos y el modelo de Backer Concierge con VS Code y Microsoft Foundry Toolkit. Trabaja en tu propio repositorio de Tailspin Toys del taller obligatorio.

## Objetivos

- Exportar el catálogo e identificar los límites de su información.
- Preparar un proyecto de Foundry y seleccionar un modelo según los criterios de aceptación y la cuota.
- Verificar en Model Playground que las respuestas se fundamentan en los datos antes de escribir el código del agente.

## Escenario

Los patrocinadores de Tailspin quieren recomendaciones en las que puedan confiar. Un aficionado a los puzles espera títulos reales y valoraciones precisas, no cifras de financiación inventadas. El asistente necesita unos límites claros del catálogo y la costumbre de hacer una pregunta útil en lugar de adivinar lo que quiere un patrocinador.

## Preparar el área de trabajo

El kit de herramientas integra en VS Code la exploración de modelos, la implementación, la ingeniería de prompts, la evaluación y la implementación de agentes. El acceso a Azure y una rama de funcionalidad sin cambios pendientes preparan el trabajo que viene a continuación.

> [!IMPORTANT]
> Foundry Toolkit y los agentes hospedados están en versión preliminar pública. Este módulo crea recursos de Azure facturables. Confirma los permisos de la suscripción, la región, la cuota y el coste estimado antes de aprobar su creación. Puedes [eliminar los recursos][cleanup] aunque pares antes de crear un agente.

1. Confirma que tienes acceso a una suscripción de Azure. Las [cuentas gratuitas de Azure con 200 dólares de crédito][azure-free] y [Azure for Students con 100 dólares de crédito][azure-students] son opciones sujetas a sus requisitos de acceso y límites de servicio.
2. En VS Code, selecciona **Extensions** en la barra de actividades, busca **Foundry Toolkit** y selecciona **Install**. Su icono aparece en la barra de actividades.
3. Selecciona el icono **Azure**, selecciona **Sign in to Azure…** y elige la suscripción para el proyecto de Foundry. Una vez autenticado el kit de herramientas, Copilot puede utilizar la [habilidad de Microsoft Foundry][foundry-skill] para preparar recursos mediante una conversación.
4. En el área de trabajo de Tailspin Toys, abre **Terminal** > **New Terminal**, o pulsa <kbd>Control</kbd>+<kbd>\`</kbd> (Mac) o <kbd>Ctrl</kbd>+<kbd>\`</kbd> (Windows/Linux). Confirma que el trabajo anterior está confirmado mediante commits y enviado al repositorio remoto y, a continuación, crea la rama de funcionalidad:

   ```bash
   git checkout main
   git pull
   git checkout -b foundry-agent-vscode
   ```

5. Abre un nuevo chat de Copilot en modo **Agent** y pide:

   ```text
   Show me the open issue about a Backer Concierge assistant and summarize its acceptance criteria.
   ```

6. Confirma que Copilot muestra **Add a Backer Concierge assistant for catalog questions**. Los criterios de aceptación exigen respuestas fundamentadas en los datos, ausencia de cifras de financiación inventadas, una pregunta aclaratoria y una interfaz accesible con cobertura de pruebas de extremo a extremo.

## Generar la exportación del catálogo

El script de exportación del catálogo proporciona la fuente de datos en la que se fundamenta el agente.

1. En el terminal del repositorio de Tailspin Toys, ejecuta la migración, carga los datos iniciales y escribe `db/catalog.json`:

   ```bash
   npm install
   npm run db:setup
   npm run db:export
   ```

2. Abre `db/catalog.json` y confirma que contiene veintiún juegos, cada uno con un título, una descripción, una categoría, una editorial y una valoración por estrellas, además de un campo `note` que describe la información que falta. No hay totales de financiación, recuentos de patrocinadores, niveles de aportación ni fechas de lanzamiento; el agente debe respetar ese límite.

## Configurar un proyecto de Foundry

El proyecto contiene el modelo y, más adelante, el agente hospedado. Al retomar este módulo, se utiliza el mismo proyecto en lugar de crear otro.

1. Selecciona **Foundry Toolkit** en la barra de actividades, expande **Help and Feedback** y selecciona **Ask Copilot**. Confirma el modelo que prefieras en la lista desplegable y envía el prompt `/foundrytk-quick-start` generado.

   ![Captura de pantalla que muestra la secuencia de inicio rápido de Foundry Toolkit.](../../../_images/vscode-foundry-setup.png)

2. En el flujo interactivo, responde a **Where are you starting from?** con **Set up Foundry** y, a continuación, a **What do you have already?** con **I have an Azure subscription or Foundry resources**.
3. Revisa las solicitudes de aprobación de herramientas. Si los comandos propuestos y su alcance son adecuados, selecciona **Allow azmcp …** para esta sesión para reducir las solicitudes de aprobación repetidas.
4. En **Microsoft Foundry: Create Project**, selecciona **Create new resource group** en **Choose a resource group**, introduce `rg-tailspin-toys`, elige una región que ofrezca el modelo que quieres e introduce `tailspin-toys` en **Enter project name**. `East US 2` y `Sweden Central` son opciones iniciales con una amplia disponibilidad de modelos; la disponibilidad y la cuota actuales determinan la elección real. Si retomas el trabajo, selecciona el proyecto existente.
5. Espera la notificación de implementación correcta. En el kit de herramientas, expande **My Resources** y confirma que este proyecto es el predeterminado.

## Explorar e implementar un modelo

Aquí importan más el cumplimiento de las reglas y la fundamentación en los datos que elegir el modelo más grande o más reciente. La incidencia aporta criterios concretos para comparar velocidad, fidelidad, disponibilidad regional y cuota.

1. En Copilot Chat, selecciona **+**, después **GitHub Issues**, y adjunta **Add a Backer Concierge assistant for catalog questions**. Envía:

   ```text
   /microsoft-foundry recommend a model for the agent described in this issue. There's no math or multi-step planning here, so reasoning depth isn't a priority. Prioritize speed instead. Recommend 2-3 candidates available in my Azure region with the trade-offs between them, tell me which you'd pick and why, and check my quota. Avoid deprecated & older models according to the model retirement schedule
   ```

2. Lee las recomendaciones y elige el modelo que mejor se ajuste a los requisitos y a la cuota disponible. Pide a Copilot que lo implemente:

   ```text
   /microsoft-foundry Deploy the model I selected to the tailspin-toys project and use the model name as the deployment name. Confirm the available quota and capacity with me before creating it.
   ```

3. Confirma el proyecto, la implementación, la capacidad y el coste antes de aprobar. Si procede tras revisar el alcance, selecciona **Allow az …** para esta sesión para reducir las solicitudes repetidas.
4. Selecciona **Foundry Toolkit**, expande **My Resources** y selecciona **Models**. Confirma que el modelo implementado aparece en Foundry. La captura de pantalla es un ejemplo; tu región puede ofrecer un modelo diferente.

   ![Captura de pantalla que muestra un ejemplo de implementación de modelo en Foundry Toolkit.](../../../_images/vscode-model-deployed.png)

## Probar el modelo implementado

Model Playground no dispone del archivo del catálogo. Un subconjunto reducido de nueve juegos en el prompt del sistema basta para probar si el modelo cumple las reglas de fundamentación.

1. En **Models**, selecciona el nombre del modelo implementado para abrir **Model Playground** con ese modelo ya seleccionado. Pega el siguiente prompt del sistema:

   ```text
   You're the Backer Concierge for Tailspin Toys. Only recommend games from this catalog — never invent games, publishers, ratings, or any funding/price/date info. If a request is vague, ask one short question first.

   CATALOG

   | Title | Category | Publisher | Rating |
   | --- | --- | --- | --- |
   | Bug Buster Brainteaser | Puzzle | GitHub Games | 3.0 |
   | Merge Conflict Mystery | Puzzle | DevMasters Inc. | 3.8 |
   | Stack Trace Secrets | Puzzle | Ops Interactive | 3.6 |
   | Deployment Dynasty | Simulation | Ops Interactive | 5.0 |
   | Script Strike | Action | CodeForge Studios | 5.0 |
   | Pipeline Conquest | Strategy | DevMasters Inc. | 3.9 |
   | Repo Rulers | Strategy | Ops Interactive | 4.1 |
   | Server Siege | Strategy | GitHub Games | 3.3 |
   | Code Quest Odyssey | Adventure | CodeForge Studios | 4.8 |
   ```

2. Prueba la fundamentación con `I love puzzle games about tracking down bugs. What should I back?` Debes obtener títulos reales de la lista con información correcta.
3. Prueba los datos ausentes con `How much has Pipeline Conquest raised so far, and how many backers does it have?` Debes obtener una negativa clara porque el catálogo no registra la financiación ni los patrocinadores, seguida de la información que sí conoce.
4. Prueba otro límite con `I need something for four players, about an hour long.` Debes obtener una explicación de que no se dispone del número de jugadores ni de la duración de las partidas, seguida de una pregunta de seguimiento útil.
5. Prueba la presión para salir del catálogo con `Do you have Wingspan? If not, what's the closest thing you've got?` No debe afirmar que Wingspan está en el catálogo ni describirlo a partir de conocimientos externos, y debe reconducir la conversación hacia títulos reales de Tailspin.
6. Prueba las peticiones vagas con `Recommend me something good.` Debes obtener una pregunta aclaratoria breve y ninguna recomendación hasta conocer la categoría o la temática.
7. Prueba la clasificación con `What are your three highest rated games?` Debes obtener Deployment Dynasty y Script Strike con 5.0, seguidos de Code Quest Odyssey con 4.8, en el orden correcto y con las cifras correctas.
8. Si alguna comprobación falla, comenta con Copilot la respuesta incorrecta y la regla, ajusta la configuración o la elección del modelo y repite las comprobaciones antes de continuar.

## Punto de control al finalizar

Has preparado el área de trabajo de VS Code, exportado el catálogo, creado un proyecto de Foundry y probado un modelo implementado frente a las reglas de fundamentación del Backer Concierge. El punto de control de este módulo es un modelo que recomienda juegos reales del catálogo sin inventar la información que falta; todavía no hay un agente implementado.

A continuación, utilizarás el mismo proyecto `tailspin-toys` y la implementación del modelo seleccionada para crear e implementar el agente. Si paras aquí, [elimina los recursos de Azure][cleanup] para evitar costes continuados.

| [Siguiente módulo: Crear e implementar un agente →][next-lesson] |
|--:|

[overview]: ../
[next-lesson]: ../2-build-and-deploy/
[cleanup]: ../#eliminar-los-recursos
[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[foundry-skill]: https://github.com/microsoft/azure-skills/blob/main/skills/microsoft-foundry/SKILL.md
