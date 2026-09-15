---
title: "Lección 9 - Crear un lienzo de clasificación de incidencias"
description: "Crea y revisa un lienzo de clasificación guardado en el repositorio, combina la PR 4 y vuelve a abrirlo para añadir contexto de incidencias sin iniciar otra funcionalidad."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Hasta ahora has dirigido a los agentes mediante el chat. Sin embargo, gran parte del trabajo no reside en una conversación, sino en un tablero, un documento o una lista de comprobación. Los **lienzos** ofrecen al agente y a ti una superficie compartida para ese tipo de trabajo, directamente en la aplicación. En esta lección crearás un lienzo sencillo para planificar y realizar el seguimiento de la lista de trabajo pendiente que has estado abordando.

En esta lección:

- comprenderás qué es un lienzo y cuándo utilizarlo.
- crearás un lienzo compartido con un tablero Kanban para clasificar la lista de trabajo pendiente.
- guardarás el lienzo en el repositorio y lo combinarás para el equipo.
- volverás a abrir el lienzo y añadirás contexto de incidencias sin implementar otra funcionalidad.

## Escenario

Examinar una lista de incidencias puede resultar abrumador. Los desarrolladores de Tailspin Toys quieren una herramienta para clasificarlas y añadir sus detalles al contexto de una sesión. Añadir contexto no autoriza a implementar una incidencia; este ejercicio termina con un tablero reutilizable, no con una quinta PR.

## ¿Qué es un lienzo?

Un [lienzo][canvas-docs] es una superficie interactiva y compartida para un recurso de trabajo, como un plan, un tablero de clasificación, una lista de comprobación de versiones, un panel o un documento. Aunque el chat resulta adecuado para describir intenciones y razonar sobre ambigüedades, la mayor parte del trabajo se realiza en una *superficie*. Los lienzos permiten colaborar con el agente directamente sobre ella.

Los lienzos son **bidireccionales**: el agente puede actualizar el lienzo mientras trabaja y tú puedes editar la misma superficie. Cuando creas un lienzo, el agente lo genera a partir de la indicación y el flujo de trabajo, y puedes pedirle que añada, elimine o revise capacidades a medida que avanzas. Una vez creado, el lienzo se abre en el panel derecho de la aplicación.

Algunos ejemplos habituales son:

- **Lienzos de Markdown** para planificar el día y priorizar incidencias y solicitudes de incorporación de cambios.
- **Tableros Kanban con agentes** en los que las personas y los agentes añaden tarjetas y desplazan el trabajo entre columnas.
- **Tableros de clasificación de incidencias** que resumen las incidencias principales y los temas recurrentes de un repositorio.

## ¿Por qué utilizar un lienzo?

Utiliza un lienzo cuando una tarea requiera estructura, iteración y verificación, y un chat no sea suficiente. Un lienzo permite:

- basar el trabajo del agente en un recurso real que se adapte al flujo de trabajo.
- orientar o corregir el trabajo directamente en la superficie compartida y, después, permitir que el agente continúe a partir de los cambios.
- inspeccionar el progreso como cambios visibles en un recurso, no solo como respuestas del chat.

## Crear un lienzo para realizar el seguimiento del trabajo

Confirma que la PR 3 se ha combinado. Las valoraciones por estrellas, el estándar de documentación, la funcionalidad de filtrado, la habilidad de calidad y el perfil QA deben estar en `main` antes de empezar el lienzo. Utiliza una sesión nueva y una rama para este último hito de PR.

1. Vuelve a la aplicación GitHub Copilot o ábrela.
2. Selecciona **Home screen**.
3. Comprueba que `tailspin-toys` esté seleccionado como repositorio.
4. Elige **new working tree** y el modo **Interactive**. Envía esta solicitud de estado inicial antes de crear archivos:

   ```plaintext
   Prepara esta nueva sesión de lienzo sin implementar nada. Confirma que es un worktree nuevo y limpio, obtén los cambios de origin y actualiza la rama de la sesión actual mediante un avance rápido hasta origin/main. Informa de la copia de trabajo, la rama y las revisiones coincidentes de HEAD y origin/main. Verifica que la PR de filtrado está combinada y que están presentes la funcionalidad de filtrado, la habilidad quality-checks y el perfil QA.

   Detente si hay cambios pendientes, divergencias o falta la combinación anterior. No restablezcas, no descartes trabajo, no cambies de rama ni crees otra rama. Detente después de comunicar el estado inicial.
   ```

5. Comprueba el informe del estado inicial y solicita el lienzo guardado en el repositorio:

   ```plaintext
   Crea un lienzo Kanban básico de clasificación de incidencias guardado en este repositorio mediante el flujo de extensiones de lienzo compatible con la aplicación. Guarda su definición en .github/extensions/ para que el equipo pueda reutilizarlo. Examina las extensiones existentes y consérvalas; no sobrescribas el explorador de base de datos incluido.

   Lee las incidencias abiertas actuales. Destaca las tres con más probabilidades de necesitar atención y muestra las demás debajo. Incluye en cada incidencia destacada su título, un resumen del contenido, la URL y una justificación de su prioridad. Trata la clasificación como sugerencia, no como instrucción para modificar incidencias.

   Proporciona en cada tarjeta una acción Add to current context que adjunte los detalles de la incidencia solo a esta sesión. No debe iniciar la implementación, crear sesiones o ramas, cambiar el estado de la incidencia ni crear PR. Mantén el alcance del lienzo acotado y hazlo accesible mediante teclado.

   Muéstrame los archivos generados y abre el lienzo para revisarlo. No cambies el código de la aplicación, no crees commits, no envíes cambios ni crees una PR. Pregunta antes de instalar cualquier cosa o añadir dependencias.
   ```

Copilot crea los archivos del lienzo y abre la superficie compartida. Revisa la extensión generada antes de confiar en sus acciones; es contenido ejecutable del repositorio, no solo una imagen.

> [!NOTE]
> Si la primera versión necesita mejoras, solicita cambios específicos dentro del alcance de clasificación de incidencias. No conviertas este ejercicio en la implementación de una incidencia pendiente.

## Revisar y probar el lienzo

1. Abre **Changes** y confirma que la definición del lienzo se guarda en el repositorio bajo `.github/extensions/`, no solo para tu usuario o sesión. Comprueba que las extensiones existentes y los archivos de la aplicación no han cambiado.
2. Compara el tablero con las incidencias abiertas reales y evalúa las explicaciones de la clasificación.
3. Comprueba que las tarjetas y los controles se leen bien y se pueden utilizar con teclado.
4. Selecciona **Add to current context** en una incidencia y confirma que solo sus detalles se añaden a la conversación. No debe iniciarse ninguna implementación ni cambio de estado de la incidencia.
5. Revisa las correcciones y pide a Copilot que ejecute la validación existente aplicable a los archivos modificados. Registra resultados y bloqueos, en lugar de suponer que una superficie interactiva funciona correctamente solo porque se ha abierto.

## Guardar el lienzo y combinarlo con el repositorio

El lienzo ya es un recurso del repositorio. Crea un commit y envía solo el trabajo revisado del lienzo como PR 4:

1. En la misma sesión, envía:

   ```plaintext
   Revisa las diferencias del lienzo de clasificación guardado en el repositorio y sus pruebas de validación. Crea un commit con los archivos del lienzo aprobados en la rama de esta sesión, envíala y crea una única PR destinada a main con la plantilla de PR del repositorio. Describe el comportamiento del lienzo y cómo hemos verificado que añadir una incidencia solo añade contexto. No combines todavía ni implementes una incidencia pendiente.
   ```

2. Revisa todas las diferencias y comprobaciones de la PR en **My work**. Confirma que contiene el lienzo, no trabajo de la aplicación ajeno a la tarea.
3. En la misma sesión del lienzo, abre el menú desplegable de acciones de PR y selecciona **Agent merge**. Revisa sus acciones permitidas y mantén **Merge pull request** desactivado hasta aprobar el resultado final.
4. Define el alcance antes de iniciar Agent Merge:

   ```plaintext
   Gestiona esta PR de lienzo existente con Agent Merge. Resuelve solo los bloqueos de revisión y CI dentro del alcance; pregunta antes de realizar cambios ajenos o instalaciones. Si cambia el lienzo, repite la validación afectada y actualiza las pruebas de verificación. No combines hasta que habilite explícitamente Merge pull request tras la revisión. No implementes incidencias pendientes ni crees otra PR.
   ```

5. Selecciona **Agent merge** y revisa los cambios posteriores. Examina las comprobaciones reales de CI del repositorio del participante y resuelve los fallos; CI no sustituye las pruebas de uso del lienzo.

6. Cuando las diferencias finales y las pruebas de verificación actuales estén aprobadas y se hayan superado las comprobaciones y revisiones obligatorias, autoriza explícitamente a Agent Merge a combinar seleccionando su menú desplegable y después **Merge pull request**.

   ![Menú desplegable Agent merge con las acciones permitidas al agente —Address reviews, Fix CI failures y Resolve conflicts— y una flecha que señala Merge pull request](../../_images/app-agent-merge-merge.png)

7. Confirma que GitHub muestra la PR 4 como **Merged** antes de continuar.

Ya has creado un lienzo compartido para el equipo.

## Volver a abrir el lienzo sin iniciar otra funcionalidad

Vuelve a abrir el lienzo guardado en el repositorio en la misma sesión del lienzo después de combinar su PR. Es un paso de inspección, no otra rama ni otro hito de PR.

1. Vuelve a la sesión del lienzo, mantén el modo **Interactive** y cierra el panel del lienzo si sigue abierto.
2. Envía:

   ```plaintext
   Vuelve a abrir el lienzo de clasificación de incidencias del repositorio en esta misma sesión. Añadiré una incidencia al contexto solo para examinar sus detalles. No edites archivos, no implementes la incidencia, no cambies su estado, no crees otra sesión o rama, no crees commits, no envíes cambios ni abras una PR.
   ```

3. Confirma que el lienzo guardado se abre de nuevo sin regenerar su definición.
4. Selecciona **Add to current context** en una de las incidencias que más te interese.
5. Confirma que los detalles de la incidencia seleccionada aparecen en el contexto sin iniciar la implementación. Detente aquí: el taller tiene cuatro hitos de PR, no cinco.

Has utilizado un lienzo creado por ti para agilizar el proceso de desarrollo.

## Resumen y pasos siguientes

Has creado una superficie compartida en la que puedes colaborar con el agente. En concreto:

- has aprendido qué son los lienzos y cuándo utilizarlos.
- has creado con el agente un lienzo compartido con un tablero Kanban para clasificar incidencias.
- has guardado y combinado el lienzo con el repositorio mediante Agent Merge.
- has vuelto a abrir el lienzo combinado y añadido contexto de incidencias sin iniciar otra funcionalidad.

Con la lista de trabajo pendiente organizada, da un paso atrás para revisar todo lo que has creado y descubrir cómo continuar. Continúa con la [Lección 10 - Repaso y pasos siguientes][next-lesson].

## Recursos

- [Trabajar con extensiones de lienzo en la aplicación GitHub Copilot][canvas-docs]
- [Lienzos en Awesome Copilot][awesome-copilot-canvases]
- [Acerca de la aplicación GitHub Copilot][about-copilot-app]

[previous-lesson]: ../8-create-pull-request/
[next-lesson]: ../10-review/
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[awesome-copilot-canvases]: https://awesome-copilot.github.com/extensions/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app