---
title: "Ejercicio 4 - Crear el filtrado con Plan y Autopilot"
description: "Acuerda los requisitos de filtrado, aprueba un plan de implementación, valida el código y guarda un punto de control en la rama de la funcionalidad."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Ahora crea la funcionalidad más amplia: permitir que los usuarios filtren juegos por categoría y editor. Planificarás antes de programar, autorizarás explícitamente **Autopilot**, revisarás y probarás la implementación y guardarás un punto de control. Este ejercicio no crea la habilidad, el agente de QA ni la PR de la funcionalidad.

En este ejercicio:

- leerás la incidencia de filtrado y aclararás los requisitos ambiguos en modo Plan.
- aprobarás explícitamente una implementación acotada con Autopilot.
- revisarás las diferencias y los resultados de las cuatro comprobaciones y guardarás un punto de control.

## Escenario

El catálogo de Tailspin Toys está creciendo y sus visitantes necesitan acotar los juegos por categoría y editor. La incidencia del backlog describe la funcionalidad, pero hay que acordar detalles como la combinación de categorías antes de programar. Utilizarás el modo Plan para resolver esas decisiones y después autorizarás una implementación acotada con Autopilot.

## Iniciar el hito de filtrado

Confirma que las PR 1 y 2 están combinadas. En la terminal del repositorio del participante:

```bash
git status
git switch main
git pull --ff-only
git switch -c add-game-filtering
copilot --enable-all-github-mcp-tools
```

Continúa solo con un árbol de trabajo limpio y una actualización correcta desde `main`. Los Ejercicios 4–8 utilizan esta misma rama y copia de trabajo. Los commits de puntos de control posteriores añadirán la habilidad y el perfil de QA; no crees una rama por ejercicio.

## Recuperar la incidencia real

Busca **Allow users to filter games by category and publisher** en la pestaña **Issues** del repositorio y copia su URL. No supongas que el nombre de archivo de la plantilla o un número de incidencia identifica la incidencia en tu copia.

La incidencia actual exige:

- seleccionar una o varias categorías.
- filtrar por editor y combinarlo con las categorías.
- funciones auxiliares de acceso a datos en `src/lib/` que admitan ambos filtros.
- controles accesibles con navegación por teclado, ARIA adecuado, estados de foco visibles y atributos `data-testid`.
- cobertura unitaria con Vitest de las funciones auxiliares y cobertura E2E con Playwright del comportamiento de filtrado.

Lee la incidencia actual como fuente de verdad. Conserva su URL y cualquier aclaración que apruebes para la indicación de QA del Ejercicio 7.

## Planificar antes de programar

Utiliza <kbd>Shift</kbd>+<kbd>Tab</kbd> para seleccionar el modo **Plan**, o empieza con `/plan`. Sustituye el marcador de la incidencia y envía:

```plaintext
Planifica la funcionalidad de filtrado descrita en esta incidencia: <filtering-issue-URL>. Lee la incidencia, las instrucciones del repositorio, las funciones auxiliares de acceso a datos existentes, la interfaz y las pruebas antes de proponer cambios. Toma la copia de trabajo actual como punto de partida; no supongas que ya se ha creado una función auxiliar de editores.

Cubre la selección de varias categorías, el filtrado por editor, su combinación, el soporte de acceso a datos, los controles accesibles y la cobertura unitaria/E2E. Pídeme que aclare comportamientos no especificados, como la forma de combinar varias categorías, limpiar los filtros y los resultados vacíos; registra las decisiones con el plan aprobado. Conserva la arquitectura estática de Astro en lugar de introducir una API de servidor innecesaria.

Planifica la implementación en la rama actual, incluidas las pruebas unitarias y E2E necesarias y la verificación con npm run lint, npm run test:unit, npm run test:e2e y npm run typecheck:all. Examina primero los requisitos previos y a quién pertenece el servidor; informa de los bloqueos en lugar de instalar software o detener procesos ajenos.

Incluye estos límites de ejecución en el plan: cuando lo apruebe, implementa solo la funcionalidad de filtrado y las pruebas necesarias, ejecuta las comprobaciones y después detente para que pueda revisar. No crees la habilidad quality-checks, un agente de QA ni otros recursos de ejercicios posteriores. No cambies de rama, no crees commits, no envíes cambios ni abras o combines una PR.

No edites código de la aplicación ni empieces la implementación hasta que apruebe el plan.
```

Responde a las preguntas de seguimiento. No añadas después criterios de aceptación ocultos: guarda las respuestas acordadas junto con la URL de la incidencia para que la implementación, las comprobaciones de navegador y QA utilicen los mismos requisitos.

Revisa que el plan incluya cambios en la capa de datos y la interfaz, pruebas, controles accesibles y la convención de documentación que has combinado. Confirma que incluye explícitamente las cuatro comprobaciones, la parada para revisión y las prohibiciones de crear recursos posteriores del taller, cambiar de rama, crear commits, enviar cambios y realizar operaciones de PR. Pide revisiones antes de aprobar si falta algún límite o criterio o si propone trabajo ajeno a la incidencia.

## Aprobar Autopilot explícitamente

Solo cuando el plan incluya el alcance y los límites de ejecución revisados, utiliza la opción de aprobación **Accept plan and build on autopilot**. Si tu versión utiliza otro texto, selecciona explícitamente la opción que cambia a **Autopilot** y comprueba el indicador de modo. La aprobación inicia la ejecución del plan acotado; no confíes en una indicación posterior para añadir límites cuando el trabajo ya haya empezado.

> [!CAUTION]
> Autopilot controla la continuación del trabajo, no solo los permisos de herramientas. Revisa el cuadro de diálogo de permisos antes de elegir. Los permisos completos permiten acceso a herramientas, rutas y URL; los limitados pueden bloquear acciones que requieren aprobación. Un codespace no da permiso para exponer secretos ni cambiar recursos ajenos. Resuelve deliberadamente el acceso bloqueado en lugar de tratar las comprobaciones omitidas como superadas.

Supervisa el trabajo y los resultados de los comandos. Autopilot puede detenerse en un límite de continuación o informar de un bloqueo antes de completar el plan. Revisa ese estado antes de autorizar que continúe y mantén el mismo alcance.

## Volver a Interactive y revisar

Cuando se detenga la implementación, utiliza <kbd>Shift</kbd>+<kbd>Tab</kbd> para volver al modo **Interactive** antes de enviar más indicaciones. Autopilot puede permanecer activo tras una tarea; no supongas que ha vuelto automáticamente.

Introduce `/diff` y examina todos los archivos modificados. Compara la implementación con la incidencia y las aclaraciones aprobadas:

- ¿Pueden los usuarios seleccionar varias categorías, filtrar por editor y combinarlos según lo acordado?
- ¿Las funciones auxiliares de acceso a datos admiten realmente los filtros, en lugar de cambiar solo la interfaz?
- ¿Los controles tienen etiquetas significativas, soporte de teclado, foco visible e identificadores de prueba estables?
- ¿Las pruebas verifican el comportamiento, incluidos los casos acordados de limpieza y resultados vacíos, sin debilitar las aserciones existentes?
- ¿El código sigue la convención de documentación y conserva la arquitectura estática de la aplicación?

Revisa las pruebas de ejecución de las cuatro comprobaciones npm. Aún no has creado `quality-checks`, así que estas comprobaciones se ejecutan directamente. La configuración E2E de Playwright compila y sirve una vista previa; antes de ejecutar la batería, detén solo un servidor de desarrollo que hayas iniciado tú para evitar que reutilice contenido obsoleto. Un conflicto de puerto o un navegador ausente es un bloqueo que resolver, no una razón para terminar otro proceso o afirmar que se ha superado una comprobación.

Solicita correcciones específicas si hacen falta, vuelve a ejecutar las comprobaciones afectadas y asegúrate de que la implementación final está completamente verificada. La observación directa en el navegador llega en el Ejercicio 6; tiene una finalidad distinta de esta verificación automatizada.

## Guardar el punto de control de implementación

Cuando las diferencias y los resultados sean satisfactorios, autoriza un punto de control local:

```plaintext
Revisa las diferencias actuales y los resultados de verificación. Crea un commit de punto de control que contenga solo la implementación de filtrado revisada y sus pruebas. Mantén la rama y la copia de trabajo de filtrado actuales. No envíes cambios, no abras una PR ni crees todavía la habilidad o el agente de QA.
```

## Resumen y pasos siguientes

Has acordado los requisitos de filtrado, revisado la implementación y las pruebas, y guardado un punto de control. Registra la revisión probada y conserva la URL de la incidencia y las aclaraciones aprobadas. Mantén **Interactive** y continúa en esta misma copia de trabajo con el [Ejercicio 5 - Crear y utilizar una habilidad quality-checks][next-lesson].

## Recursos

- [Modo Autopilot y permisos][autopilot] explica la continuación autónoma y cómo volver a Interactive.
- [Referencia de comandos de Copilot CLI][cli-reference] enumera los controles de modo y los comandos actuales.

[previous-lesson]: ../3-custom-instructions/
[next-lesson]: ../5-agent-skills/
[autopilot]: https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
