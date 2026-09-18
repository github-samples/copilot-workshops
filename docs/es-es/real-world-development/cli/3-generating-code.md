---
title: "Ejercicio 3 - Añadir funcionalidades al proyecto con GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Como ya puedes imaginar, una de las tareas principales que realizarás con GitHub Copilot CLI es añadir funciones, capacidades y código a un proyecto. Vamos a tomar una de las incidencias de tu backlog y pedir a Copilot que nos ayude a implementarla.

## Escenario

Ha llegado el momento de completar el filtrado en el proyecto. Ya tienes la incidencia de filtrado en tu backlog y un helper base del ejercicio anterior. Vamos a hacer que Copilot recupere los detalles de la incidencia, tenga en cuenta el trabajo existente y construya la funcionalidad restante.

En este ejercicio vas a:

- utilizar el modo de planificación para generar un plan de implementación de la funcionalidad de filtrado.
- generar con Copilot el código necesario para añadir el filtrado al sitio web.

Al final de este ejercicio, habrás añadido nueva funcionalidad al proyecto.

## Utilizar el modo de planificación

Uno de los mejores usos de la IA es la planificación. Muchas veces tendrás una buena idea de lo que quieres construir, pero solo necesitas contrastar algunas ideas con algo. Las herramientas de IA pueden ayudarte a concretar tus ideas haciendo preguntas de seguimiento y analizando distintos riesgos o componentes que falten. Para apoyar este proceso, Copilot CLI ofrece un modo de planificación. Además, el tiempo que dediques a planificar ayudará a Copilot a generar código que se ajuste mejor a los requisitos establecidos.

Empezarás el proceso de creación de la nueva funcionalidad utilizando el modo de planificación de Copilot CLI.

> [!TIP]
> **Inicia una sesión de Copilot CLI**
>
> Antes de empezar los ejercicios siguientes, vuelve a tu codespace y abre un terminal (<kbd>Ctrl</kbd>+<kbd>\`</kbd> si no hay ninguno abierto). Después, inicia Copilot CLI con `--yolo` y `--enable-all-github-mcp-tools`:
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> Para retomar la sesión más reciente de este proyecto en lugar de empezar desde cero, ejecuta `copilot --yolo --enable-all-github-mcp-tools --continue`. Si Copilot CLI ya se está ejecutando desde un ejercicio anterior, envía `/clear` para empezar una conversación limpia.
>
> `--enable-all-github-mcp-tools` habilita las herramientas GitHub MCP de lectura y escritura para la sesión actual, de modo que Copilot pueda leer tu backlog y abrir pull requests durante el flujo del taller.

> [!CAUTION]
> `--yolo` habilita permisos automáticos completos (`--allow-all-tools`, `--allow-all-paths` y `--allow-all-urls`). Úsalo solo en un entorno aislado, como un Codespace o una máquina virtual, y no lo configures nunca como alias predeterminado para el desarrollo diario. Consulta [Allowing and denying tool use][allow-all-warning] para más información.

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools

1. Introduce el siguiente prompt en Copilot CLI para crear un plan basado en la incidencia de filtrado:

    ```
    /plan Retrieve the issue on the repository related to adding filtering. We already added a publishers helper in src/lib/publishers.ts, so treat that as existing work and plan the remaining updates (games filtering logic, UI, and tests).
    ```

2. Copilot puede hacer preguntas de seguimiento mientras desarrolla el plan. Cuando aparezcan, respóndelas según cómo construirías tú la funcionalidad.
3. Una vez generado el plan, revisa el esquema. Deberías ver que recomienda cambios pendientes en la capa de datos y en la interfaz, además de generar pruebas.
4. Copilot CLI te ofrecerá la posibilidad de añadir comentarios adicionales al plan. Puedes mover el cursor hasta la sección indicada y escribir tus sugerencias. Copilot incorporará esas sugerencias a una nueva versión del plan.
5. Cuando estés conforme, selecciona la opción que ofrece Copilot para empezar a trabajar en la nueva funcionalidad.

> [!NOTE]
> Como Copilot es probabilístico, el texto exacto y las opciones que se muestren variarán. Sin embargo, verás una opción para empezar a construir que dirá algo parecido a esto:
>
> `Yes, and switch to autopilot mode`.
>
> Copilot puede ofrecerte la opción de habilitar el [modo autopilot](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot), como se muestra en el ejemplo anterior. El modo autopilot permite que Copilot CLI trabaje en una tarea sin esperar tu intervención después de cada paso. Una vez que le das la instrucción inicial, Copilot CLI resuelve cada paso de forma autónoma hasta que determina que la tarea está completa. Como estamos trabajando en un entorno aislado, podemos ejecutar autopilot y permitir todas las herramientas.

6. Copilot se pondrá manos a la obra generando los archivos.

> [!NOTE]
> Es probable que esta operación tarde varios minutos. Verás a Copilot editar y crear archivos, actualizar y generar pruebas, y ejecutar todas las pruebas para comprobar que todo funciona correctamente. Es un buen momento para reflexionar sobre lo que has explorado hasta ahora o para tomarte algo.

## Revisar el código

Todo código generado por IA debe revisarse antes de fusionarse en producción. Vamos a dedicar ahora un momento a explorar los archivos que Copilot ha creado y modificado al implementar la nueva funcionalidad.

1. Usa Copilot CLI para mostrar el "diff" o los cambios de código con el siguiente comando en Copilot CLI:

    ```
    /diff
    ```

2. Observa los archivos modificados. Usa las teclas de dirección izquierda y derecha para ver los distintos archivos. Deberías ver actualizaciones en archivos como la página del listado de juegos (donde viven los nuevos controles de filtrado y el filtrado del lado del cliente) y `src/lib/games.ts`, además de pruebas como `games.test.ts`. También es posible que veas cambios en `publishers.ts` si Copilot ajusta tu helper existente para alinearlo con la implementación completa.

## Resumen y siguientes pasos

Ya has añadido la funcionalidad de filtrado al sitio web con la ayuda de Copilot CLI. En concreto:

- has utilizado el modo de planificación para generar un plan de implementación de la funcionalidad de filtrado.
- has generado con Copilot el código necesario para añadir el filtrado al sitio web.

Por supuesto, el siguiente paso es asegurarte de que funciona. Vamos a [probar tu funcionalidad con el servidor MCP de Playwright][next-lesson] antes de abrir una pull request.

## Recursos

- [Usar Copilot CLI][using-copilot-cli]
- [Acerca de Copilot CLI][about-copilot-cli]
- [Gestión del contexto en Copilot CLI][context-management]

[previous-lesson]: ../2-custom-instructions/
[next-lesson]: ../4-mcp/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
