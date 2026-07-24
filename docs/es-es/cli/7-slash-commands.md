---
title: "Ejercicio 7 - Comandos de barra en GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Como cualquier buena herramienta de CLI, GitHub Copilot CLI incluye muchos comandos de barra para interactuar con ella. Estos comandos exponen funcionalidad avanzada, información "entre bastidores" u opciones de configuración adicionales. Ya has explorado un par de ellos con `/clear` para borrar el contexto y `/mcp` para inspeccionar los servidores MCP. Vamos a explorar otros muy potentes, entre ellos `/context`, `/model`, `/share` y `/delegate`.

## Escenario

Ya has completado los flujos principales de CLI. Ahora vamos a ver algunas capacidades adicionales: compartir sesiones, cambiar de modelo y delegar tareas en [Copilot cloud agent][about-cloud-agent].

En este ejercicio usarás:

- `/share` para crear un GitHub gist y compartir tu sesión con el equipo.
- `/context` para ver el contexto que está usando actualmente Copilot CLI.
- `/model` para explorar la lista de modelos disponibles y seleccionar uno nuevo si así lo deseas.
- `/delegate` para delegar opcionalmente una tarea al agente en la nube. Esto requiere cloud agent, disponible en Copilot Student, Pro, Pro+, Business o Enterprise, es decir, en todos los planes excepto Copilot Free.

## Compartir una sesión

Usar cualquier herramienta, incluida una herramienta de IA, es una habilidad. Trabajar en equipo y compartir lo aprendido es la mejor forma de mejorar la experiencia de todos y generar código de mayor calidad. Para ello, Copilot CLI proporciona el comando `/share`. El comando `/share` puede generar un archivo Markdown o un GitHub gist con los detalles de la sesión, incluidos los prompts utilizados y la lógica que siguió Copilot.

Vamos a crear un GitHub gist que podríamos compartir con nuestro equipo.

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

1. En la ventana de prompt de Copilot CLI, envía el siguiente comando:

    ```
    /share gist
    ```

2. En apenas unos instantes, Copilot creará un gist y mostrará el enlace.
3. Copia el texto del enlace.
4. En una pestaña nueva del navegador, pega el enlace para explorar el gist. Observa cómo el gist destaca los prompts enviados, las habilidades y los agentes utilizados, el proceso de razonamiento de Copilot e incluso el código y los resultados de los comandos ejecutados localmente.

Los gists y archivos Markdown generados por `/share` pueden usarse para documentar cómo se generó el código o para compartir con el equipo cómo se llevaron a cabo determinadas acciones que produjeron los resultados deseados con Copilot.

## Explorar el contexto de Copilot CLI

Cuando trabajas en tareas grandes o complejas, puedes llegar al límite máximo de la ventana de contexto del modelo. El tamaño exacto de la ventana variará según el modelo que se esté usando y la versión de Copilot CLI. Cuando la ventana de contexto se llena, Copilot CLI la compacta automáticamente, resumiendo la información y eliminando lo que considera irrelevante para la tarea actual. Puedes tanto ver el estado actual del contexto como compactarlo manualmente usando comandos de barra. Vamos a explorar la ventana de contexto.

1. En la ventana de prompt de Copilot CLI, envía el siguiente comando:

    ```
    /context
    ```

2. En apenas unos instantes, Copilot CLI generará una representación visual de su contexto actual:

    ![Captura de la ventana de contexto de Copilot CLI](../../_images/cli-7-context-window.png)

3. Fíjate en el modelo mostrado (que puede ser distinto del de la imagen) y en el porcentaje actual de tokens usados. El resto de la información destaca lo siguiente:

    | Título | Descripción |
    | ------------ | ------------------------------------------------------ |
    | Sistema/Herramientas | Archivos de instrucciones, contenido de archivos y definiciones de herramientas |
    | Mensajes | Historial de la conversación entre tú y Copilot |
    | Búfer | Espacio reservado por Copilot CLI para generar respuestas |
    | Espacio libre | Espacio libre restante |

4. Compacta el historial de la conversación enviando el siguiente comando de barra a Copilot CLI:

    ```
    /compact
    ```

5. Cuando termine, envía de nuevo el siguiente comando para mostrar las estadísticas actuales del contexto:

    ```
    /context
    ```

6. Observa el cambio en el contexto. Puede que no sea drástico, ya que es probable que la ventana de contexto sea relativamente pequeña en este momento.

> [!NOTE]
> Copilot CLI compactará automáticamente el contexto cuando se llene. Cuando se acerque al 100 % de capacidad, mostrará el porcentaje justo encima de la ventana de prompt. Normalmente lo compactará de forma asíncrona, lo que te permitirá seguir interactuando con Copilot mientras realiza ese trabajo. Aun así, puede bloquear una operación en curso durante varios segundos mientras lo hace.

### Buenas prácticas con el contexto

En la mayoría de las sesiones, Copilot gestionará el contexto de forma eficiente sin que tengas que darle instrucciones específicas. Sin embargo, puede haber ocasiones en las que decidas indicarle manualmente que borre o compacte el historial:

- Si vas a pasar a otra parte de la aplicación o a una tarea no relacionada, puedes usar `/clear` para empezar de nuevo y evitar confundir a Copilot con contexto antiguo que no tiene relación.
- Si te estás acercando al límite máximo de la ventana de contexto, puedes usar manualmente `/compact` para controlar cuándo ocurre.

> [!CAUTION]
> De nuevo, la mayor parte del tiempo Copilot gestionará su contexto sin interacción directa por tu parte. Si observas que Copilot está algo confundido por información antigua, o estás a punto de cambiar a una tarea no relacionada, entonces quizá te convenga usar los comandos manuales.

## Elegir tu modelo

Los distintos modelos tienen puntos fuertes diferentes y cada desarrollador tiene sus propias preferencias. Copilot CLI te permite listar y seleccionar el modelo que quieras usar.

1. Muestra la lista de modelos enviando el siguiente comando de barra a Copilot CLI:

    ```
    /model
    ```

2. Observa la lista de modelos. Junto a cada modelo aparecerán tanto su nombre como el modificador de coste por solicitud.
3. Si quieres, selecciona un modelo nuevo. O bien selecciona <kbd>Esc</kbd> para salir de la lista de modelos.

> [!CAUTION]
> La selección de modelo persiste en Copilot CLI.

## Delegar en cloud agent (opcional)

Hay ocasiones en las que quieres seguir trabajando en tu terminal, pero delegar una tarea de mayor duración en Copilot cloud agent. El comando `/delegate` envía la sesión actual de Copilot CLI a GitHub.com, donde cloud agent la retoma, trabaja de forma asíncrona y abre una pull request cuando termina.

> [!NOTE]
> `/delegate` requiere cloud agent, disponible en Copilot Student, Pro, Pro+, Business o Enterprise, es decir, en todos los planes excepto Copilot Free. Si no tienes acceso, lee esta sección y omite los pasos prácticos.

1. Borra primero la sesión actual para no delegar el contexto acumulado del taller:

    ```
    /clear
    ```

2. Envía un prompt pequeño y bien delimitado. Por ejemplo, podrías delegar la paginación de objetivo ampliado de tu backlog:

    ```
    Implement pagination on the game list page so it shows a fixed number of games per page with Previous and Next controls, and add tests.
    ```

3. Envía el siguiente comando de barra para delegar la sesión al agente en la nube y confirma el prompt que quieres delegar:

    ```
    /delegate
    ```

4. Abre [Copilot agents](https://github.com/copilot/agents) en un navegador para supervisar el progreso.
5. No necesitas esperar a que la pull request termine en este recorrido; puedes volver más tarde. Si quieres profundizar en la gestión del trabajo asíncrono con agentes, continúa con el [recorrido de Cloud agent](../../cloud/).

## Resumen y siguientes pasos

Usar comandos de barra en Copilot CLI te permite configurarlo, compartir sesiones y obtener información interna sobre cómo está trabajando Copilot. En esta lección has usado o explorado:

- `/share` para crear un GitHub gist y compartir tu sesión con el equipo.
- `/context` para ver el contexto que está usando actualmente Copilot CLI.
- `/model` para explorar la lista de modelos disponibles y seleccionar uno nuevo si así lo deseas.
- `/delegate` como puente opcional hacia cloud agent.

Por supuesto, hay más comandos de barra disponibles y mucho más por explorar con Copilot CLI. Vamos a cerrar este recorrido [repasando lo que hemos aprendido][next-lesson] y viendo algunos próximos pasos para seguir aprendiendo.

## Recursos

- [Usar Copilot CLI][using-copilot-cli]
- [Acerca de Copilot CLI][about-copilot-cli]
- [Gestión del contexto en Copilot CLI][context-management]
- [Compartir sesiones con Copilot CLI][share-sessions]
- [Seleccionar modelos en Copilot CLI][selecting-models]

[previous-lesson]: ../6-custom-agents/
[next-lesson]: ../8-review/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[about-cloud-agent]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
[share-sessions]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#share-sessions
[selecting-models]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#select-an-llm
