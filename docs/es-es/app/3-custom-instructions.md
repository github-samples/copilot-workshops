---
title: "Lección 3 - Guiar a Copilot con instrucciones personalizadas"
description: "Añade un estándar de documentación, demuéstralo en una pequeña función auxiliar o un componente existente y combina ambos como segunda solicitud de incorporación de cambios."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

El contexto es fundamental al trabajar con IA generativa. Si una tarea debe realizarse de una forma concreta o Copilot necesita conocer información de fondo, conviene que ese contexto esté disponible. Una de las herramientas más potentes para proporcionarlo son los [archivos de instrucciones][instruction-files], que describen no solo *qué* código quieres, sino también *cómo* debe estructurarse. En esta lección añadirás un estándar de documentación al repositorio y lo harás como realizarás la mayor parte del trabajo a partir de ahora: comenzarás desde una incidencia de la lista de trabajo pendiente y dejarás que el agente realice el cambio.

En esta lección:

- explorarás cómo llegan al agente las instrucciones del repositorio y los archivos de instrucciones limitados por ruta.
- iniciarás una sesión desde la incidencia sobre instrucciones de la lista de trabajo pendiente.
- pedirás al agente que añada un estándar de documentación específico a los archivos de instrucciones adecuados del repositorio.
- demostrarás el estándar con un pequeño cambio de código real, lo validarás y combinarás la PR 2.

## Escenario

Como cualquier buen equipo de desarrollo, Tailspin Toys dispone de directrices y requisitos para las prácticas de desarrollo. Entre ellos se incluyen:

- Los comentarios deben explicar la intención y las decisiones no evidentes, en lugar de repetir lo que hace el código.
- Las funciones exportadas de `db/` y `src/lib/` deben documentar su propósito, parámetros y valores de retorno mediante TSDoc/JSDoc, incluido un argumento `db` inyectable cuando exista.
- Los componentes reutilizables de Astro deben documentar sus contratos de `Props`, y los comentarios deben mantenerse actualizados cuando cambie el código relacionado.
- Deben conservarse las directrices existentes de formato y lint.

Mediante los archivos de instrucciones, garantizarás que Copilot disponga de la información adecuada para realizar las tareas conforme a estas prácticas.

## Archivos de instrucciones

Las instrucciones personalizadas permiten proporcionar contexto y preferencias a Copilot para que comprenda mejor el estilo y los requisitos de programación. Esta potente funcionalidad ayuda a orientar a Copilot para obtener sugerencias y fragmentos de código más pertinentes. Puedes especificar las convenciones de programación, las bibliotecas e incluso los tipos de comentarios que prefieres incluir en el código. También puedes crear instrucciones para todo el repositorio o para tipos de archivo concretos, con contexto específico para una tarea.

El proyecto utiliza dos tipos de archivos de instrucciones:

- `.github/copilot-instructions.md`, un único archivo de instrucciones que se envía a Copilot con **cada** solicitud del repositorio. Debe contener información del proyecto que sea pertinente para la mayoría de las solicitudes de chat o CLI enviadas a Copilot, como la pila tecnológica, una descripción general de lo que se está creando, procedimientos recomendados y otras directrices globales.
- Los archivos `.github/instructions/*.instructions.md` se pueden crear para tareas o tipos de archivo concretos. Puedes utilizarlos para proporcionar directrices para lenguajes específicos, como TypeScript o Astro, o para tareas como crear un componente de interfaz de usuario o un nuevo conjunto de pruebas unitarias.

> [!NOTE]
> Los demás formatos de instrucciones y su compatibilidad varían según el entorno. Consulta la [referencia de compatibilidad de instrucciones personalizadas][custom-instructions-support] antes de depender de un formato concreto.

### Procedimientos recomendados para gestionar archivos de instrucciones

Una explicación completa sobre la creación de archivos de instrucciones queda fuera del alcance del taller. No obstante, los ejemplos del proyecto de muestra presentan un enfoque representativo. En términos generales:

- Mantén las instrucciones de `copilot-instructions.md` centradas en directrices de ámbito de proyecto, como una descripción de lo que se está creando, la estructura del proyecto y los estándares globales de programación.
- Utiliza archivos `*.instructions.md` para proporcionar instrucciones específicas para tipos de archivo, como pruebas unitarias, componentes de Astro o la capa de datos, o para tareas concretas.
- Utiliza lenguaje natural. Redacta directrices claras. Proporciona ejemplos de cómo debe y no debe ser el código.

No existe una única forma de crear archivos de instrucciones, del mismo modo que no existe una única forma de utilizar la IA. La experimentación te permitirá descubrir qué funciona mejor para tu proyecto.

> [!TIP]
> Todos los proyectos que utilicen GitHub Copilot deberían disponer de una colección sólida de archivos de instrucciones. Al explorar los de este proyecto, observarás que hay archivos de instrucciones para muchos tipos de archivos de código.
>
> ¿Buscas plantillas o un punto de partida? Explora [Awesome Copilot][awesome-copilot], un repositorio repleto de archivos de instrucciones, agentes personalizados y otros recursos.

## Explorar los archivos de instrucciones personalizadas del proyecto

Dedica un momento a leer los archivos de instrucciones incluidos en este repositorio: hay un archivo principal `copilot-instructions.md` y una colección de archivos `*.instructions.md` para distintas tareas. Ábrelos en el editor o en la interfaz web de GitHub.

1. Si el panel de revisión aún no está visible, selecciona **Toggle review panel** en la esquina superior derecha para abrirlo.

   ![Barra de herramientas superior de la aplicación GitHub Copilot con una flecha que señala el botón Toggle review panel situado a la derecha de Create PR](../../_images/app-2-review-panel.png)

2. Selecciona **+** para añadir un elemento nuevo al panel de revisión.
3. Selecciona **File**.
4. Busca `copilot-instructions.md`.
5. Selecciona `copilot-instructions.md` en la lista de archivos para abrirlo.
6. Explora el archivo. Observa la breve descripción del proyecto y secciones como **Agent notes**, **Code standards**, **Scripts** y **Repository Structure**. En **Code standards**, fíjate en las directrices anidadas de **GitHub Actions Workflows**. Se aplican a cualquier interacción con Copilot.
7. Selecciona **Show folder view** para abrir el navegador de carpetas.

   ![Botón Show folder view del panel de revisión con un archivo abierto en la aplicación GitHub Copilot](../../_images/app-show-folder-view.png)

8. Ve a la carpeta `.github/instructions` y explora los archivos. Observa que hay instrucciones para archivos de Astro, la capa de datos de Drizzle, pruebas y otros elementos.
9. Abre `.github/instructions/unit-tests.instructions.md`. Observa el campo `applyTo` de la parte superior: establece un patrón glob, relativo a la raíz del repositorio, que determina a qué archivos se aplican las instrucciones. En este caso, coincidirá cualquier archivo de prueba de TypeScript, por ejemplo, uno que cumpla `**/*.test.ts`.
10. Examina las instrucciones específicas para crear pruebas unitarias en este proyecto.
11. Por último, abre `.github/instructions/drizzle.instructions.md` y desplázate hasta el final. Observa los vínculos a otros archivos de instrucciones, como `unit-tests.instructions.md`, y a archivos existentes del proyecto. De este modo puedes dividir conjuntos de instrucciones grandes en archivos más pequeños y reutilizables, y señalar a Copilot ejemplos que debe seguir al generar código. Las rutas son relativas al archivo de instrucciones, no a la raíz del repositorio.

> [!NOTE]
> Compara las directrices existentes con la incidencia real de estándares de programación antes de añadir reglas. Esta lección se centra en comentarios que explican la intención, documentación de funciones exportadas de la capa de datos y contratos de `Props` de Astro, no en cabeceras obligatorias para todos los archivos ni en comentarios que repiten el código.

## Empezar desde la incidencia sobre instrucciones

Confirma que la PR 1 está combinada antes de crear esta sesión. Inicia un worktree nuevo para la PR 2; no continúes en la rama de valoraciones por estrellas. La mayor parte del trabajo comienza con una incidencia, así que utiliza la de estándares de programación para aportar los requisitos.

> [!NOTE]
> Como los archivos de instrucciones influyen mucho en el código que genera Copilot, debes asegurarte de que lo orienten con claridad. Pedir a Copilot que cree una primera versión, como harás en esta lección, es un buen enfoque, siempre que después la revises para confirmar que las actualizaciones cumplen tus requisitos.

1. Selecciona **My work** en la barra lateral.
2. Selecciona la incidencia titulada **Update our repository coding standards** para abrirla.
3. Selecciona **New session** en la esquina superior derecha, elige **new working tree** y selecciona el modo **Interactive**.

   ![Vista de una incidencia en la aplicación GitHub Copilot con una flecha que señala el botón New session de la esquina superior derecha](../../_images/app-new-session-from-issue.png)

4. Utiliza la siguiente indicación. Actualizar la rama de la nueva sesión antes de editar hace que el último `main` combinado sea el punto de partida real, aunque la copia local de la aplicación estuviera desactualizada:

   ```plaintext
   Antes de editar, identifica esta copia de trabajo y su rama, confirma que es un worktree nuevo y limpio, obtén los cambios de origin y actualiza la rama de esta sesión mediante un avance rápido hasta origin/main. Confirma que HEAD coincide con origin/main e incluye la PR de valoraciones por estrellas combinada. Detente si hay cambios pendientes, divergencias o falta esa combinación; no restablezcas, no descartes trabajo ni crees otra rama.

   Lee la incidencia "Update our repository coding standards" y las instrucciones existentes del repositorio. Añade una convención de documentación específica: explica la intención en lugar de la mecánica; documenta las funciones exportadas de db/ y src/lib/ con TSDoc/JSDoc que cubra propósito, parámetros, valores de retorno y argumentos db inyectables cuando existan; documenta los contratos de Props de los componentes reutilizables de Astro; y mantén los comentarios actualizados cuando cambie el código relacionado.

   Coloca cada regla en el archivo de instrucciones existente adecuado, sin duplicaciones ni contradicciones, y enlaza o resume el estándar actualizado en README. Conserva las directrices existentes de formato y lint. No exijas cabeceras para todos los archivos, no migres herramientas de formato, no reescribas la documentación de toda la aplicación ni implementes el filtrado. Muéstrame las diferencias de las instrucciones y después detente para que las revise. No crees una habilidad o un agente, no crees commits, no envíes cambios ni crees una PR.
   ```

Copilot realizará las actualizaciones.

## Revisar el cambio

Lee las directrices actualizadas y demuestra su efecto en un archivo real. Un fragmento propuesto por sí solo no demuestra que las instrucciones del repositorio hayan influido en un cambio de código.

1. Selecciona **Changes** en la esquina superior derecha para abrir los cambios de código.

   ![Pestañas del panel de sesión de la aplicación GitHub Copilot con una flecha que señala la pestaña Changes](../../_images/app-select-changes.png)

2. Revisa los archivos de instrucciones actualizados y la referencia en README. Confirma que las reglas coinciden con la filosofía de comentarios, la documentación de funciones exportadas y los contratos de componentes de la incidencia, sin inventar un requisito general de cabeceras de archivo.

> [!NOTE]
> Como la IA es probabilística y no determinista, el texto exacto puede variar.

3. Tras revisar las instrucciones, solicita una demostración acotada en esta misma sesión:

   ```plaintext
   Demuestra la convención de documentación actualizada en una pequeña función auxiliar exportada de TypeScript existente en db/ o src/lib/, o en un componente reutilizable de Astro. Examina el repositorio para elegir un archivo existente adecuado; no des por hecho que existe una función auxiliar de editores. Realiza una pequeña mejora de legibilidad que conserve el comportamiento y aplica las directrices pertinentes de documentación de funciones o contratos de Props. Explica las intenciones no evidentes sin añadir comentarios que se limiten a repetir el código.

   Limita el cambio a esa demostración y las pruebas directamente relacionadas. No implementes el filtrado ni crees una funcionalidad nueva. Ejecuta las comprobaciones npm existentes pertinentes, informa de lo que ha cambiado y de cómo la instrucción ha influido en el código y detente para que lo revise. Pregunta antes de instalar cualquier cosa. No crees commits, no envíes cambios ni crees una PR.
   ```

4. Revisa las diferencias reales del archivo, no solo la respuesta del chat. Comprueba que la documentación explica el comportamiento real y que la mejora de legibilidad lo conserva. Revisa los resultados pertinentes de pruebas, lint y comprobaciones de tipos; resuelve los fallos antes de continuar.

Ya has actualizado los archivos de instrucciones del proyecto y has comprobado el efecto que tendrán.

## Abrir y combinar la solicitud de incorporación de cambios

Los archivos de instrucciones pasan a ser recursos del repositorio y, por tanto, se comparten con el resto del equipo. Vamos a crear una solicitud de incorporación de cambios con nuestro trabajo, igual que haríamos con cualquier otro recurso.

Primero autoriza conjuntamente las instrucciones y la demostración revisadas:

```plaintext
Revisa todas las diferencias de las instrucciones de estándares de programación, la referencia en README y la demostración de código acotada, incluidas las pruebas relacionadas. Resume la verificación y crea un commit con estos cambios revisados en la rama de esta sesión. Envía la rama y crea una única solicitud de incorporación de cambios destinada a main, con la plantilla de PR del repositorio y un enlace a la incidencia de estándares de programación. Descríbela como contribución parcial salvo que se cumplan todos los criterios de aceptación de la incidencia; no utilices palabras clave de cierre para trabajo incompleto. No la combines.
```

1. Abre el enlace de la PR en la sesión. Si la aplicación muestra una confirmación **Create PR**, selecciónala sin crear una PR duplicada.
2. Si se solicita, selecciona **Sign in with your browser** y sigue las indicaciones para autenticarte.
3. Copilot comenzará a crear la solicitud de incorporación de cambios.

Examina todas las diferencias de la PR en **My work**, incluidos los cambios de instrucciones y código. Revisa los resultados de CI del repositorio del participante y las revisiones obligatorias. Resuelve los fallos antes de seleccionar **Ready to merge**; CI no sustituye la demostración ni tu revisión.

4. Selecciona **Ready to merge**.
5. Selecciona **Merge pull request** en el nuevo cuadro de diálogo para combinar la solicitud.

> [!NOTE]
> Confirma que la PR 2 se ha combinado en `main` antes de empezar el filtrado. Un worktree nuevo por sí solo no garantiza código actualizado: en la Lección 4 obtendrás los cambios y actualizarás la rama de la nueva sesión mediante un avance rápido hasta `origin/main`, y verificarás que ambas combinaciones anteriores están presentes antes de planificar.

## Resumen y pasos siguientes

Has explorado cómo la aplicación obtiene contexto de los archivos de instrucciones y, después, has utilizado una sesión para añadir y combinar un estándar para todo el repositorio. En concreto:

- has explorado el archivo `copilot-instructions.md` del repositorio y los archivos `*.instructions.md` limitados por ruta.
- has iniciado una sesión desde la incidencia sobre instrucciones de la lista de trabajo pendiente.
- has pedido al agente que añada reglas de documentación específicas a los archivos de instrucciones adecuados y las referencie desde README.
- has examinado el efecto del estándar en un cambio de código real, validado el resultado y combinado ambos como PR 2.

A continuación, crearás la funcionalidad de filtrado en una sesión nueva y comprobarás que sigue el estándar que acabas de combinar. Continúa con la [Lección 4 - Crear el filtrado con Plan y Autopilot][next-lesson].

## Recursos

- [Archivos de instrucciones para personalizar GitHub Copilot][instruction-files]
- [Personalizar la aplicación GitHub Copilot][customize-app]
- [Procedimientos recomendados para crear instrucciones personalizadas][instructions-best-practices]
- [Awesome Copilot: colección de archivos de instrucciones y otros recursos][awesome-copilot]

[previous-lesson]: ../2-add-star-rating/
[next-lesson]: ../4-build-filtering/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[awesome-copilot]: https://awesome-copilot.github.com/
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests