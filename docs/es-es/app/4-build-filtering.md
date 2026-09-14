---
title: "Lección 4 - Crear el filtrado con Plan y Autopilot"
description: "Planifica el filtrado desde su incidencia, aprueba Autopilot explícitamente, valida con las comprobaciones npm existentes y una visita manual al navegador, y guarda un punto de control."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Has combinado las valoraciones por estrellas y el estándar de documentación con su demostración en código. Ahora crea la funcionalidad de filtrado. Este es el inicio de un hito de PR más amplio: mantén esta misma sesión, worktree y rama durante las Lecciones 4–8.

En esta lección:

- partirás de `main` actualizado y leerás la incidencia real de filtrado.
- resolverás los requisitos en modo **Plan** antes de aprobar explícitamente **Autopilot**.
- revisarás el filtrado y las pruebas y después ejecutarás las cuatro comprobaciones npm existentes.
- visitarás la funcionalidad manualmente en un navegador y guardarás un punto de control.

La habilidad, la validación MCP, el perfil QA y la PR de la funcionalidad llegarán en módulos posteriores. No los crees durante este paso de implementación.

## Modos de sesión

El selector de modo situado debajo de la indicación controla la autonomía del agente:

- **Interactive** te mantiene al tanto mientras el agente trabaja y solicita información.
- **Plan** prepara un plan para revisarlo antes de la implementación.
- **Autopilot** implementa e itera de forma autónoma dentro del alcance y los permisos aprobados.

Planifica primero, aprueba de forma explícita y vuelve a Interactive antes de crear personalizaciones reutilizables.

## Partir de main actualizado

Confirma que la PR 1 y la PR 2 están combinadas en GitHub. Crea un worktree nuevo para el filtrado en lugar de continuar en cualquiera de las ramas anteriores.

1. Selecciona **My work** y busca **Allow users to filter games by category and publisher** por su título. Ábrela y copia su URL real; los números de incidencia varían entre repositorios.
2. Selecciona **New session** y elige **new working tree**. Mantén el modo **Interactive** para actualizar el estado inicial.

   ![Vista de una incidencia en la aplicación GitHub Copilot con una flecha que señala el botón New session](../../_images/app-new-session-from-issue.png)

3. Envía esta solicitud de preparación antes de planificar o editar:

   ```plaintext
   Prepara esta nueva sesión de filtrado sin implementar nada. Identifica la copia de trabajo y la rama, confirma que el worktree está limpio, obtén los cambios de origin y actualiza la rama de esta sesión mediante un avance rápido hasta origin/main. Confirma que HEAD coincide con origin/main e incluye las PR combinadas de valoraciones por estrellas y estándares de programación.

   Detente y explica el motivo si hay cambios pendientes, divergencias o falta cualquiera de las combinaciones. No restablezcas ni descartes trabajo, no cambies de rama, no crees otra rama ni edites archivos de la aplicación. Informa de la revisión de partida.
   ```

4. Comprueba el estado inicial comunicado. Obtener los cambios no actualiza por sí solo el worktree: la rama de la sesión actual debe avanzar mediante un avance rápido y su `HEAD` debe coincidir con el `origin/main` obtenido antes de empezar a trabajar.

## Planificar la funcionalidad de filtrado

Cambia el selector de modo a **Plan**. Sustituye el marcador de posición de la incidencia por la URL que has copiado.

```plaintext
Planifica la funcionalidad de filtrado a partir de esta incidencia: <filtering-issue-URL>. Lee todos sus criterios de aceptación y las instrucciones del repositorio y después examina la aplicación estática de Astro actual, sus funciones auxiliares de acceso a datos y sus pruebas existentes. No implementes nada todavía.

Cubre la selección de varias categorías, el filtrado por editor, la combinación de categorías y editor, las funciones auxiliares de acceso a datos adecuadas, los controles accesibles y la cobertura unitaria y de un extremo a otro que exige la incidencia. Pregúntame para resolver comportamientos no especificados, como la combinación de varias categorías, el borrado de filtros y los resultados vacíos, en lugar de inventar requisitos sin decirlo. No introduzcas una API de servidor a menos que los requisitos y la arquitectura existente lo justifiquen.

Propón un plan de implementación y verificación acotado que siga la convención de documentación del repositorio y añada o actualice las pruebas unitarias y de un extremo a otro necesarias. Tras confirmar los comandos en package.json, planifica la ejecución de npm run lint, npm run test:unit, npm run test:e2e y npm run typecheck:all con las herramientas existentes del proyecto. Registra la URL de la incidencia y mis aclaraciones aprobadas en el plan para que pueda reutilizarlas en QA.

Incluye estas medidas de seguridad de ejecución en el plan antes de que lo apruebe: identifica la copia de trabajo y el servidor que se prueban; examina los requisitos previos antes de ejecutar las comprobaciones; pregunta antes de instalar software, dependencias o navegadores; no reutilices el servidor de otro worktree; detén solo los servidores que hayas iniciado; e informa de otros conflictos de puerto en lugar de detener procesos ajenos. Los requisitos previos ausentes y las comprobaciones omitidas deben comunicarse como bloqueos, no como comprobaciones superadas.

Incluye este límite de implementación en el plan: después de que apruebe explícitamente Autopilot, implementa solo la funcionalidad de filtrado acordada y sus pruebas en este mismo worktree y rama, ejecuta las cuatro comprobaciones, informa de la implementación y de todos los resultados, incluidos fallos o bloqueos, y después detente para que revise el trabajo y lo compruebe manualmente en el navegador. No crees habilidades ni agentes personalizados, no configures MCP, no cambies de rama, no crees commits, no envíes cambios ni abras una PR durante la implementación. La comprobación manual del navegador y el commit de punto de control tendrán lugar después, bajo mis instrucciones por separado.

Por ahora, mantén el modo Plan y detente con el plan para que lo revise. No implementes, no crees habilidades ni agentes personalizados, no configures MCP, no cambies de rama, no crees commits, no envíes cambios ni abras una PR.
```

Responde a las preguntas aclaratorias y revisa el plan frente a la incidencia. Busca los cambios de acceso a datos, los controles accesibles y las pruebas, en lugar de aceptar una implementación solo de interfaz. Guarda la URL real de la incidencia y las aclaraciones aprobadas del plan para las Lecciones 6 y 7; utiliza `none` cuando no hagan falta criterios adicionales.

Antes de aprobar, confirma que el propio plan contiene las cuatro comprobaciones, la convención de documentación, las medidas de seguridad sobre requisitos previos y servidores, el requisito de mantener el mismo worktree y rama y la parada tras la implementación y la verificación. Debe prohibir las habilidades, agentes y configuración MCP posteriores, los commits, los envíos de cambios y las PR durante la implementación. Si falta algún límite, solicita un plan revisado mientras sigues en modo **Plan** y examina la revisión antes de aprobar.

## Aprobar Autopilot explícitamente

Solo cuando el plan revisado contenga tus requisitos y todos los límites de ejecución, selecciona **Approve and implement with autopilot** en los controles de aprobación del plan, o la opción explícita de Autopilot equivalente de tu versión. Confirma que el indicador de modo muestra **Autopilot**.

La aprobación puede iniciar la ejecución inmediatamente. Por tanto, todo el alcance de implementación, las reglas de seguridad y los límites de parada deben estar en el plan revisado antes de aprobar; no confíes en añadirlos mediante un mensaje posterior cuando la ejecución ya haya empezado.

Autopilot puede escribir código y pruebas e iterar sobre los fallos, pero este permiso no autoriza a completar módulos posteriores del taller. La falta de un requisito previo es un bloqueo que debe resolverse con aprobación, no una comprobación superada.

## Revisar y verificar la implementación

1. Abre **Changes** y examina la implementación del filtrado y las pruebas.
2. Compara el resultado con la incidencia y las aclaraciones aprobadas, incluidas las combinaciones de varias categorías y editores. Comprueba que las funciones auxiliares nuevas o modificadas siguen el estándar de documentación de la Lección 3.
3. Examina la salida real de los comandos de las cuatro comprobaciones npm. Ahora se ejecutan directamente porque aún no has creado la habilidad quality-checks.
4. Resuelve los fallos y repite las comprobaciones afectadas antes de aceptar la implementación. La configuración E2E de Playwright compila y sirve una vista previa y puede reutilizar un servidor local; asegúrate de que el servidor probado pertenece a este worktree, no a una lección anterior.

## Comprobar la funcionalidad manualmente

Vuelve al modo **Interactive** antes de la revisión manual y mantenlo para la Lección 5.

1. Abre **Terminal** en el panel de revisión de esta sesión. Si es necesario, selecciona **+** y después **Terminal**.
2. Confirma que la terminal está en el worktree de filtrado y ejecuta:

   ```shell
   npm run dev
   ```

3. Abre en el navegador la URL que muestra este servidor, normalmente `http://localhost:4321`. Si el puerto está ocupado, identifica a quién pertenece en lugar de detener un proceso ajeno o suponer que el servidor existente contiene tus cambios.
4. Prueba la selección de categorías, la selección de editor y su combinación según el comportamiento aprobado. Comprueba el acceso mediante teclado y el comportamiento acordado de borrado de filtros y resultados vacíos.
5. Si algo falla, solicita una corrección específica, revisa las diferencias, repite las comprobaciones automatizadas afectadas y las comprobaciones pertinentes del navegador.
6. Vuelve a la terminal y pulsa <kbd>Control</kbd>+<kbd>C</kbd> (Mac) o <kbd>Ctrl</kbd>+<kbd>C</kbd> (Windows/Linux) para detener el servidor que has iniciado. Confirma que se ha detenido antes de la ejecución E2E del siguiente módulo.

Esta es tu observación manual en el navegador. La observación en el navegador dirigida por el agente mediante MCP llegará en la Lección 6.

## Guardar un punto de control

Tras revisar los cambios y la verificación, autoriza un commit local:

```plaintext
Revisa las diferencias actuales y crea un commit de control para la implementación del filtrado y sus pruebas. Mantén esta misma rama y worktree de filtrado. No crees habilidades ni agentes, no configures MCP, no envíes cambios ni abras una solicitud de incorporación de cambios.
```

Este punto de control forma parte de la PR 3, no de una PR independiente. Mantén el modo **Interactive** en la misma sesión para la [Lección 5 - Crear y utilizar una habilidad quality-checks][next-lesson].

## Recursos

- [Trabajar con sesiones de agente en la aplicación GitHub Copilot][agent-sessions]
- [Acerca de los entornos aislados locales y en la nube para GitHub Copilot][sandboxes]

[previous-lesson]: ../3-custom-instructions/
[next-lesson]: ../5-agent-skills/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
