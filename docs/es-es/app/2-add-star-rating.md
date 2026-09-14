---
title: "Lección 2 - Añadir valoraciones por estrellas: una mejora rápida"
description: "Inicia tu primera sesión de agente en la aplicación GitHub Copilot, realiza un pequeño cambio en las tarjetas de los juegos y combínalo como tu primera solicitud de incorporación de cambios."
authors:
  - geektrainer
lastUpdated: 2026-07-09
---

En la lección anterior recorriste el espacio de trabajo y utilizaste un chat rápido. Ahora es el momento de iniciar una **sesión de agente** y realizar el primer cambio en el proyecto. Será un cambio pequeño: los juegos ya tienen una valoración por estrellas en sus datos, pero las tarjetas de la página de inicio todavía no la muestran. Pedirás al agente que la muestre, revisarás el cambio y lo combinarás como tu primera solicitud de incorporación de cambios.

En esta lección:

- iniciarás una sesión de agente y aprenderás cómo se estructura.
- pedirás al agente que realice un cambio pequeño y específico en el proyecto.
- revisarás el cambio en la vista de diferencias del espacio de trabajo.
- ejecutarás la aplicación en local para confirmar el cambio en el navegador.
- abrirás y combinarás tu primera solicitud de incorporación de cambios.

## Escenario

Cada juego de Tailspin Toys puede tener una valoración por estrellas, que ya aparece en la página de detalles del juego. Sin embargo, las tarjetas de los juegos de la página de inicio solo muestran el título, la categoría, el editor y la descripción. Como ejercicio inicial, pedirás al agente que muestre la valoración existente en cada tarjeta. Es un cambio pequeño y autocontenido, perfecto para tu primera sesión.

## Anatomía de una sesión

Una **sesión** es una conversación con un agente. En este taller eliges **new working tree**, lo que proporciona a la sesión una copia de trabajo y una rama dedicadas. Así se aísla cada hito de PR sin una rama distinta para cada lección. Las sesiones aparecen en la barra lateral agrupadas por repositorio; selecciona cualquiera de ellas para cambiar de sesión.

Dentro de una sesión verás tres elementos: la **conversación** con el agente, la **actividad de las herramientas** del agente mientras explora y edita archivos, y la lista de **archivos modificados** con sus diferencias.

## Iniciar una sesión y solicitar el cambio

Vamos a iniciar una sesión nueva para comenzar a explorar el proyecto e implementar la funcionalidad. En una [lección anterior][prior-lesson] añadiste el proyecto desde su repositorio de GitHub. Crearemos una sesión nueva para ese repositorio y solicitaremos el cambio.

1. Vuelve a la aplicación GitHub Copilot o ábrela.
2. Selecciona **Home screen**.
3. Comprueba que `tailspin-toys` esté seleccionado como repositorio.

   ![Cuadro de indicaciones de la aplicación GitHub Copilot con el selector de repositorio establecido en tailspin-toys y el selector de modelo debajo](../../_images/app-2-start-session.png)

4. Elige **new working tree** y el modo **Interactive** debajo del cuadro de indicaciones. Utiliza la indicación siguiente para solicitar el cambio:

   ```plaintext
   Antes de editar, identifica esta copia de trabajo y su rama, confirma que es un worktree nuevo y limpio, obtén los cambios de origin y actualiza la rama de esta sesión mediante un avance rápido hasta origin/main. Confirma que HEAD coincide con origin/main. Detente y explica el motivo si hay cambios pendientes, divergencias o no se puede actualizar; no restablezcas ni descartes trabajo.

   Muestra la valoración por estrellas de cada juego en las tarjetas. El tipo Game ya incluye un campo starRating: un número sobre 5, o null cuando el juego aún no tiene valoración. Muéstralo en cada tarjeta de src/components/GameCard.astro y, cuando starRating sea null, muestra "No rating yet". Mantén el cambio pequeño y no reestructures el diseño de las tarjetas ni cambies el modelo de datos.

   Sigue las instrucciones del repositorio, añade o actualiza las pruebas adecuadas y ejecuta las comprobaciones npm existentes pertinentes. Examina los requisitos previos y pregunta antes de instalar cualquier cosa. Informa de los archivos modificados y los resultados de las comprobaciones y después detente para que los revise. No crees commits, no envíes cambios, no abras una solicitud de incorporación de cambios ni implementes otra funcionalidad.
   ```

> [!NOTE]
> Observa que la indicación contiene el nombre del archivo que Copilot debe actualizar. Aunque no es necesario especificar los archivos que Copilot debe incluir en su trabajo, orientarlo ayuda a que genere el código con rapidez y reduzca el uso de tokens.

5. Pulsa <kbd>Enter</kbd> para enviar la indicación a Copilot.

La aplicación Copilot comienza por crear un árbol de trabajo nuevo, una copia aislada del proyecto. Después explora el proyecto, localiza los archivos que debe actualizar para añadir la funcionalidad y crea el código necesario. Ya has añadido una nueva funcionalidad con la aplicación Copilot.

## Revisar las diferencias

Todos los cambios generados por IA deben revisarse antes de combinarlos, incluso los más pequeños. Vamos a explorar los cambios directamente en la aplicación Copilot.

1. En la esquina superior derecha de la aplicación, selecciona **Toggle review panel**. Se abrirá la pantalla de diferencias con todos los cambios pendientes realizados por Copilot.

   ![Barra de herramientas superior de la aplicación GitHub Copilot con una flecha que señala el botón Toggle review panel situado a la derecha de Create PR](../../_images/app-2-review-panel.png)

2. Deberías observar código añadido a `GameCard.astro`, el archivo principal que se utiliza para mostrar los detalles de los juegos. Debería ser similar al siguiente: un pequeño bloque que representa la valoración cuando existe y muestra "No rating yet" cuando `starRating` es `null`:

   ```astro
   {game.starRating !== null ? (
       <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-amber-900/60 text-amber-300" data-testid="game-rating">
           ★ {game.starRating} / 5
       </span>
   ) : (
       <span class="text-xs font-medium text-slate-500" data-testid="game-rating-empty">
           No rating yet
       </span>
   )}
   ```

> [!NOTE]
> Como Copilot, al igual que todas las herramientas de IA generativa, es probabilístico y no determinista, el código exacto puede variar respecto al ejemplo anterior. No obstante, debería ser relativamente parecido.

## Comprobar los cambios

Revisa los resultados de las comprobaciones automatizadas del agente antes de abrir un navegador. Confirma que las pruebas cubren un `starRating` numérico y la alternativa para `null`, mediante los scripts npm existentes del proyecto en lugar de una habilidad que aún no existe. Un requisito previo ausente o una comprobación omitida no cuentan como superados.

Después examina la aplicación manualmente desde la terminal integrada de la sesión. Identifica el worktree antes de iniciar el servidor y no reutilices un servidor de otra copia de trabajo.

1. En el panel de revisión situado a la derecha de la aplicación Copilot, selecciona **Terminal**. Si no aparece el botón **Terminal**, selecciona **+** (con la etiqueta **Open in panel**) y, después, **Terminal**.

   ![Botón Terminal del panel de revisión de la aplicación GitHub Copilot](../../_images/app-terminal-screenshot.png)

2. Introduce el comando siguiente en la ventana de terminal para iniciar el servidor de desarrollo de la aplicación web:

   ```shell
   npm run dev
   ```

3. Cuando se inicie el servidor, lo que solo tardará un momento, abre una ventana del navegador.
4. Abre la URL local que muestra el servidor, normalmente `http://localhost:4321`. Si el puerto está ocupado, identifica a quién pertenece en lugar de detener un proceso ajeno.
5. Confirma que las tarjetas de juegos valorados muestran su puntuación sobre cinco. Si hay datos sin valoración, confirma que aparece **No rating yet**; de lo contrario, verifica el caso null mediante la prueba automatizada en lugar de afirmar que lo has observado.
6. Vuelve a la ventana de terminal.
7. Pulsa <kbd>Control</kbd>+<kbd>C</kbd> (Mac) o <kbd>Ctrl</kbd>+<kbd>C</kbd> (Windows/Linux) para detener el servidor de desarrollo que has iniciado.

## Abrir y combinar tu primera solicitud de incorporación de cambios

El cambio tiene buen aspecto; ha llegado el momento de entregar la PR 1. Primero autoriza el commit y la PR por separado de la implementación:

```plaintext
Revisa todas las diferencias del cambio de valoraciones por estrellas y sus pruebas, resume la verificación y crea un commit con los cambios revisados en la rama de esta sesión. Envía la rama y crea una solicitud de incorporación de cambios destinada a main con la plantilla de PR del repositorio. No la combines.
```

1. Abre el enlace de la PR creada en la sesión. Si la aplicación muestra una confirmación **Create PR**, selecciónala para aprobar la solicitud en lugar de crear una segunda PR.
2. Si se solicita, selecciona **Sign in with your browser** y sigue las indicaciones para autenticarte.
3. Copilot comenzará a crear la solicitud de incorporación de cambios.

Una vez creada la PR, examina todas sus diferencias y las comprobaciones en **My work**. Lee los resultados de los flujos de trabajo del repositorio del participante; espera a que se completen las comprobaciones y revisiones obligatorias y resuelve los fallos antes de combinar. **Ready to merge** no sustituye la revisión del cambio ni las pruebas de verificación locales.

4. Selecciona la burbuja **PR** situada justo encima del chat para abrir la solicitud en el panel de revisión. Puedes revisarla aquí según sea necesario.
5. Cuando esté lista, selecciona **Ready to merge**.
6. Selecciona **Merge pull request** en el nuevo cuadro de diálogo para combinar la solicitud.

Confirma que la PR 1 se ha combinado en `main` antes de continuar. Combinar cambios en el repositorio del participante no despliega por sí solo un sitio web. La siguiente lección inicia un worktree nuevo y lo actualiza desde `origin/main` para que incluya esta PR.

## Resumen y pasos siguientes

Has iniciado tu primera sesión de agente y publicado tu primer cambio. En concreto:

- has iniciado una sesión de agente y aprendido cómo se estructuran las sesiones.
- has indicado al agente que realice un cambio pequeño y específico en las tarjetas de los juegos.
- has revisado el cambio en la vista de diferencias del espacio de trabajo.
- has ejecutado la aplicación en local para confirmar la valoración por estrellas en el navegador.
- has abierto la PR 1, revisado sus comprobaciones y autorizado explícitamente su combinación.

A continuación, utilizarás la aplicación para añadir al repositorio un estándar de instrucciones personalizadas a partir de una de las incidencias de la lista de trabajo pendiente. Continúa con la [Lección 3 - Guiar a Copilot con instrucciones personalizadas][next-lesson].

## Recursos

- [Trabajar con sesiones de agente en la aplicación GitHub Copilot][agent-sessions]
- [Acerca de la aplicación GitHub Copilot][about-copilot-app]
- [Gestionar incidencias y solicitudes de incorporación de cambios con la aplicación GitHub Copilot][managing-issues-prs]

[prior-lesson]: ../1-install-copilot-app/#instalar-y-configurar-la-aplicación-github-copilot
[previous-lesson]: ../1-install-copilot-app/
[next-lesson]: ../3-custom-instructions/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests