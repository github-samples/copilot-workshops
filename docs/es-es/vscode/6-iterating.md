---
title: "Ejercicio 6 - Iterar sobre el trabajo de GitHub Copilot"
authors:
  - geektrainer
lastUpdated: 2026-06-30
next: false
---

| [← Lección anterior: Supervisar y gestionar agentes][previous-lesson] |
| :-- |

## Revisar el trabajo

A lo largo de esta práctica has trabajado con GitHub Copilot en varias tareas centradas en mejorar la experiencia de usuario. Has utilizado el modo agente para añadir filtros en el cliente y el servidor, el servidor MCP de Playwright para probar manualmente ese trabajo en un navegador y, después, un agente personalizado para implementar funciones de accesibilidad —controles de alto contraste y modo claro—, y has dirigido la sesión sobre la marcha para ampliar el trabajo. Ahora toca publicar ese trabajo local y revisarlo como lo haría tu equipo.

### Escenario

Los fundamentos del diseño de software y DevOps no cambian con la incorporación de la IA generativa. Sigue siendo necesario un ciclo de revisión real de todo lo que produce Copilot. Teniendo esto en cuenta, vamos a enviar los cambios de accesibilidad desde el codespace, abrir una solicitud de incorporación de cambios y examinar las diferencias antes de involucrar al resto del equipo.
## Publicar las funciones de accesibilidad

Los controles de alto contraste y modo claro que has implementado con el agente personalizado de accesibilidad en el [ejercicio 4][exercise-4] y el [ejercicio 5][exercise-5] están en el codespace como cambios confirmados mediante commits. Vamos a enviarlos a una rama y a abrir una solicitud de incorporación de cambios para que el resto del equipo pueda revisarlos.

1. Vuelve al codespace.
2. Abre la vista **Source Control** en VS Code.
3. Confirma que los cambios de accesibilidad están confirmados mediante commits. Si tienes cambios sin confirmar del ejercicio 5, añádelos al área de preparación y crea un commit ahora con un mensaje descriptivo como `Add high-contrast and light-mode toggles`.
4. Publica la rama seleccionando **Publish Branch** (o utiliza el menú **...** → **Push**).
5. VS Code te ofrecerá abrir la nueva rama en github.com. Acepta la propuesta o ve a tu repositorio manualmente y selecciona **Compare & pull request** en el aviso de la rama.
6. Establece un título claro (por ejemplo, `Add high-contrast and light-mode toggles`) y una descripción breve que resuma qué se ha hecho y por qué.
7. Selecciona **Create pull request**.
8. Una vez abierta la PR, selecciona la pestaña **Files changed** para revisar todo el trabajo. Presta especial atención a:
   - Los componentes de la interfaz que permiten alternar entre modos.
   - El uso del almacenamiento local para conservar las preferencias del usuario.
   - Los cambios de CSS o de estilos para los modos de alto contraste y claro.
   - Los atributos de accesibilidad (etiquetas ARIA, navegación por teclado, etc.).
   - Cualquier código JavaScript/TypeScript que gestione el cambio de modo.

9. Vuelve a la pestaña **Conversation**.
10. Si hay flujos de trabajo pendientes de aprobación, selecciona **Approve and run workflows**.

    ![Aprobar y ejecutar flujos de trabajo con Approve and run workflows](../../_images/shared-approve-workflows.png)
11. Espera a que terminen los flujos de trabajo. Si todo va bien, deberían completarse correctamente.

> [!TIP]
> ¿Quieres una segunda opinión sobre el trabajo de accesibilidad? Menciona a `@copilot` en un comentario de la PR con una petición como «revisa esta PR para detectar otros problemas de WCAG» o «sugiere mejoras en la navegación por teclado». Copilot iniciará una nueva sesión para atender el comentario.

## Ejercicio opcional: seguir explorando localmente

Trabajar de forma iterativa con un agente en el IDE es una habilidad, y la única forma de desarrollarla es repetir. Algunas ideas para próximas sesiones que puedes realizar desde VS Code:

- Añadir un formulario de interés para patrocinadores en la página de detalles del juego.
- Implementar la paginación en la página de la lista de juegos.
- Añadir validación de entradas y gestión de errores a las funciones auxiliares de acceso a datos en `src/lib/`.
- Ampliar el alcance del agente de accesibilidad; por ejemplo, auditar el orden del foco del teclado en todo el sitio.

## Resumen

¡Enhorabuena! Has completado el itinerario de VS Code. A lo largo de esta práctica:

- **Has utilizado Playwright MCP para probar manualmente la funcionalidad.** Has añadido el servidor MCP de Playwright y dejado que Copilot maneje un navegador para verificar la funcionalidad de filtrado antes de abrir una solicitud de incorporación de cambios.
- **Has dirigido el modo agente en cambios coordinados en todas las capas.** Has añadido una funcionalidad de filtrado que ha afectado al cliente, al servidor y a las pruebas en una sola sesión.
- **Has utilizado un agente personalizado.** Has seleccionado el agente personalizado centrado en la accesibilidad en el selector de agentes y observado cómo implementaba el modo de alto contraste en el repositorio.
- **Has gestionado y dirigido una sesión de agente.** Has revisado los cambios propuestos en el propio editor, aceptado los que querías y ampliado la sesión con una petición posterior para el modo claro.
- **Has cerrado el ciclo con una solicitud de incorporación de cambios.** Has publicado el trabajo local y lo has revisado de principio a fin como lo haría tu equipo.

## Revisión y siguientes pasos

Aquí termina el itinerario obligatorio de VS Code. Puedes parar aquí con el taller completo.

Si quieres ampliar tu perspectiva sobre las capacidades de los agentes de Copilot, los otros itinerarios cubren escenarios relacionados a través de distintas interfaces:

- 💻 **[Itinerario de CLI](../../cli/)**: realiza flujos similares desde el terminal con Copilot CLI: modo plan, habilidades de agente, agentes personalizados y comandos de barra como `/share`, `/context` y `/delegate`.
- ☁️ **[Itinerario del agente en la nube](../../cloud/)**: céntrate en asignar incidencias al agente en la nube, supervisar sesiones a través de la página de agentes e iterar de forma asíncrona sobre solicitudes de incorporación de cambios.

También puedes seguir ampliando lo que has empezado aquí. [awesome-copilot][awesome-copilot] es una gran fuente de archivos de instrucciones, agentes personalizados y habilidades que puedes adaptar a tus propios proyectos.

Como ampliación opcional, [Opcional: Incorporar Foundry][exercise-7] utiliza VS Code y Microsoft Foundry Toolkit para preparar un modelo, implementar un Backer Concierge y conectarlo al sitio.

## Recursos

- [GitHub Copilot][github-copilot]
- [Copilot Chat en VS Code][copilot-chat-vscode]
- [Uso del modo agente][agent-mode]

---

| [← Lección anterior: Gestionar agentes][previous-lesson] |
|:--|

[previous-lesson]: ../5-managing-agents/
[exercise-4]: ../4-custom-agents/
[exercise-5]: ../5-managing-agents/
[exercise-7]: ../7-foundry-toolkit/
[github-copilot]: https://github.com/features/copilot
[copilot-chat-vscode]: https://code.visualstudio.com/docs/copilot/chat/copilot-chat
[agent-mode]: https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode
[awesome-copilot]: https://github.com/github/awesome-copilot
