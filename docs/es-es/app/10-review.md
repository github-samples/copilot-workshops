---
title: "Lección 10 - Repaso y pasos siguientes"
description: "Repasa los nueve módulos principales de la aplicación, los cuatro hitos de PR y el flujo de calidad reutilizable, y explora otros recursos."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Durante las últimas lecciones, has llevado una funcionalidad desde la idea hasta la combinación mediante la aplicación GitHub Copilot. Entre otras cosas, has aprendido a:

- conectar un repositorio y familiarizarte con el espacio de trabajo de la aplicación y la lista de trabajo pendiente inicial.
- iniciar sesiones desde una tarea directa y desde incidencias, y utilizar los modos Plan y Autopilot para controlar cómo trabaja el agente.
- orientar al agente con instrucciones personalizadas y después pedirle que cree una habilidad reutilizable con scripts de shell que has revisado y ejecutado para el linter, las pruebas unitarias, las pruebas de un extremo a otro y las comprobaciones de tipos.
- probar el trabajo con el servidor MCP de Playwright en un navegador real.
- crear y seleccionar un agente personalizado QA para evaluar requisitos, cobertura, resultados de scripts de la habilidad y pruebas de observación del navegador.
- colaborar con el agente en un lienzo compartido.
- combinar explícitamente las primeras PR personalmente y después autorizar **Agent Merge** dentro de los flujos de PR de la funcionalidad y el lienzo.

Las Lecciones 0–1 de configuración dieron paso a nueve módulos principales, las Lecciones 2–10. Dedica un momento a repasar los recursos creados y cómo continuar; este resumen no inicia otra tarea práctica.

## Qué has entregado

El taller tiene cuatro hitos de PR, cada uno en su propia rama a partir de `main` actualizado:

1. **Valoraciones por estrellas:** mostrar el `starRating` existente y un estado explícito sin valoración en las tarjetas de juegos.
2. **Instrucciones y demostración:** añadir la convención de documentación y verificar su efecto en un pequeño cambio de código real.
3. **Filtrado y flujo de calidad:** implementar la incidencia, crear la habilidad `quality-checks` con scripts de shell y el perfil QA e incluir las pruebas asociadas.
4. **Lienzo de clasificación guardado en el repositorio:** compartir un tablero que añada contexto de incidencias sin implementar automáticamente otra funcionalidad.

Las Lecciones 4–8 utilizaron la misma sesión, worktree y rama de filtrado. Los commits de control conservaron el progreso dentro de la PR 3; las habilidades, la configuración MCP y QA no necesitaron ramas de funcionalidad independientes. Cada hito posterior comenzó solo después de combinar la PR anterior y actualizar la rama de la nueva sesión desde `origin/main`.

## Distintos tipos de verificación

Las primeras funcionalidades utilizaron las comprobaciones npm existentes. El filtrado añadió tu inspección manual en el navegador. La habilidad hizo repetibles las cuatro comprobaciones mediante scripts incluidos, MCP añadió observaciones directas del agente en el navegador y QA combinó requisitos y cobertura con la verificación final. La PR reutilizó las pruebas de QA solo mientras correspondían a la revisión enviada.

Las pruebas añadidas deben cubrir carencias reales; una ejecución QA que no necesita pruebas nuevas puede ser correcta. Las herramientas ausentes, las comprobaciones omitidas y los fallos son bloqueos visibles, no resultados satisfactorios. Revisa el código y las pruebas de verificación antes de autorizar la combinación y actualiza las afectadas después de los cambios.

## Procedimientos recomendados

Al utilizar cualquier herramienta de IA, la infraestructura que la rodea determina la calidad de los resultados. En este taller has creado instrucciones, una habilidad y un perfil QA; revísalos y reutilízalos entre sesiones. Los agentes personalizados definen roles especializados e instrucciones, con herramientas disponibles según la configuración y los permisos del entorno; las habilidades agrupan instrucciones reutilizables para tareas, scripts ejecutables y recursos de apoyo que se cargan bajo demanda. Un agente personalizado también puede ejecutar scripts, incluidos los que forman parte de una habilidad. Confirma la ejecución real de los scripts y la selección del agente personalizado en lugar de confiar en una descripción convincente.

Adapta el **modo y el modelo** a la tarea. Utiliza **Plan** para razonar sobre un enfoque antes de desarrollar, **Interactive** para mantener el control durante cambios concretos y **Autopilot** solo para tareas aisladas y bien delimitadas. Elige un modelo más rápido para las modificaciones rutinarias y otro más capaz, con mayor esfuerzo de razonamiento, para el trabajo complejo.

El contexto sigue siendo tan importante como la infraestructura. Describir con claridad *qué* quieres crear, *por qué* y *cómo* cambia sustancialmente el resultado. Los chats rápidos son un buen lugar para delimitar una idea antes de dedicarle una sesión completa.

## Más opciones para explorar

Ya conoces el flujo de trabajo principal. Estas son algunas funcionalidades adicionales que merece la pena explorar:

- **Quick chats** para preguntas rápidas y desechables que no necesitan una sesión completa.
- [**Automatizaciones**][using-automations] para tareas recurrentes o bajo demanda, como resumir el trabajo reciente. Revisa la programación, los permisos y el alcance antes de adoptar una; crear una automatización es un siguiente paso, no parte de este taller.
- **Rubber duck** para razonar sobre un problema y obtener comentarios pertinentes antes de desarrollar.
- [**Agentes personalizados**][custom-agents] para encapsular un rol, sus herramientas y sus instrucciones con el fin de realizar trabajo especializado y repetible.
- [`/chronicle`][chronicle] para generar una narración de lo sucedido en una sesión.
- [Usar tu propia clave (BYOK)][byok] para utilizar modelos de tu propio proveedor, incluidos modelos locales mediante Ollama, Foundry Local o LM Studio.
- [Entornos aislados en la nube][sandboxes] para ejecutar sesiones en un entorno aislado hospedado en GitHub.
- [Vínculos profundos][deep-links] para abrir la aplicación directamente en un repositorio, una sesión o una indicación.

## Pasos siguientes

La mejor forma de mejorar con cualquier herramienta es seguir utilizándola. Úsala para código de producción, proyectos personales o esa pequeña aplicación que llevas años pensando en crear. Comparte lo que aprendas con el equipo y aprende de sus experiencias. Y, como siempre, consulta la documentación.

Para explorar más elementos del ecosistema de GitHub Copilot, consulta el [recorrido de VS Code][vscode-harness], el [recorrido de Copilot CLI][cli-harness] o el [recorrido del agente en la nube][cloud-harness].

## Recursos

- [Acerca de la aplicación GitHub Copilot][about-copilot-app]
- [Introducción a la aplicación GitHub Copilot][getting-started]
- [Personalizar la aplicación GitHub Copilot][customize]
- [Utilizar automatizaciones][using-automations]
- [Trabajar con extensiones de lienzo][canvas-docs]
- [Acerca de los entornos aislados locales y en la nube][sandboxes]

[previous-lesson]: ../9-canvases/
[vscode-harness]: ../../vscode/
[cli-harness]: ../../cli/
[cloud-harness]: ../../cloud/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[customize]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[using-automations]: https://docs.github.com/copilot/how-tos/github-copilot-app/using-automations
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
[chronicle]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle
[custom-agents]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[byok]: https://docs.github.com/copilot/how-tos/github-copilot-app/use-byok-models
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links