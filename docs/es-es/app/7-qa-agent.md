---
title: "Lección 7 - Crear y utilizar un agente de QA"
description: "Crea un perfil de QA que parta de los requisitos y combine cobertura de pruebas, la habilidad quality-checks y observaciones directas del navegador."
authors:
  - geektrainer
lastUpdated: 2026-09-14
---

En las lecciones anteriores, creaste una habilidad quality-checks y diste a Copilot acceso a un navegador mediante MCP de Playwright. Ahora reúne esas capacidades con un **agente personalizado de QA** que revise la funcionalidad de filtrado frente a sus requisitos.

En esta lección:

- comprenderás cómo trabaja un agente personalizado con instrucciones, habilidades y herramientas MCP.
- crearás y examinarás un perfil de QA reutilizable.
- seleccionarás el agente de QA y revisarás sus conclusiones frente a la incidencia de filtrado.
- guardarás el perfil y las pruebas justificadas para la PR de la funcionalidad.

## Escenario

Tailspin Toys se prepara para publicar el filtrado por categoría y editor. Las comprobaciones automatizadas y la exploración en el navegador han aportado información útil al equipo, pero superar las pruebas no demuestra por sí solo que se cubran todos los requisitos acordados. Antes de abrir la PR, el equipo quiere revisar de forma específica qué se pidió, qué se implementó y qué sigue pendiente.

Crearás un agente de QA que parta de la incidencia y de las decisiones de planificación aprobadas, examine la cobertura y utilice la habilidad y las herramientas del navegador para reunir pruebas de verificación. Su función es identificar carencias y explicar si la funcionalidad está lista para revisión, no aprobar su propio trabajo ni combinar la PR.

## ¿Qué es un agente personalizado?

Un agente personalizado es un rol especializado reutilizable definido en un perfil Markdown. Sus instrucciones orientan cómo aborda Copilot una tarea; al seleccionar el perfil, aplicas ese rol a la conversación. En este taller, definirás el rol en `.github/agents/qa.agent.md` y lo seleccionarás en la aplicación.

Las personalizaciones que has creado tienen funciones distintas. Las instrucciones del repositorio describen los estándares del equipo. La habilidad quality-checks reúne comprobaciones repetibles. MCP de Playwright proporciona herramientas de navegador. El perfil de QA indica a Copilot cómo usar esas capacidades para evaluar requisitos e informar de sus conclusiones. No las sustituye ni requiere otra sesión de agente.

## Crear el perfil de QA

Continúa en la sesión de filtrado de la Lección 6, manteniendo el mismo worktree y rama. Confirma que la sesión está en modo **Interactive**, que la habilidad quality-checks está presente y que MCP de Playwright está disponible. La PR de la funcionalidad llegará en la Lección 8; esta lección añade un perfil y, solo cuando sea necesario, pruebas.

Envía la siguiente indicación al agente habitual de Copilot. Examinarás el archivo resultante antes de seleccionar QA:

```plaintext
Crea un agente personalizado de QA reutilizable en .github/agents/qa.agent.md. Primero examina las instrucciones del repositorio, package.json, la configuración de pruebas y .github/skills/quality-checks/SKILL.md. Proporciona al perfil un frontmatter YAML válido con name establecido en QA y una description que explique cuándo utilizarlo. No fijes un modelo ni añadas una lista tools; hereda las herramientas y los permisos disponibles del entorno. Crea solo la definición del agente y después detente para que pueda examinarla antes de ejecutarlo.

En las instrucciones del agente, exige que toda tarea de QA parta de la incidencia y de los criterios de aceptación aprobados que proporcione el usuario. Trata estos requisitos como fuente de verdad, no la implementación. Pregunta cuando falten requisitos o sean ambiguos. Examina la funcionalidad y las pruebas existentes y relaciona cada criterio con la cobertura automatizada adecuada y el comportamiento observable.

Exige validación directa en el navegador mediante el servidor MCP de Playwright configurado y la ejecución de lint, pruebas unitarias, pruebas de un extremo a otro y comprobaciones de tipos mediante la habilidad quality-checks existente y sus scripts incluidos. Lee la habilidad explícitamente si no se ha descubierto automáticamente. Informa de la ausencia de habilidades, herramientas MCP, requisitos previos o acceso como bloqueos; no sustituyas silenciosamente el flujo por otro ni etiquetes comprobaciones omitidas como superadas. Identifica la copia de trabajo y el servidor que se prueban, evita reutilizar el servidor de otro worktree, detén solo los servidores que haya iniciado el agente y pregunta antes de cualquier instalación o de detener otro proceso.

Permite que el agente de QA añada las pruebas mínimas necesarias para carencias reales de cobertura, siguiendo las instrucciones del repositorio; no añadir pruebas es válido cuando la cobertura ya es adecuada. No debilites aserciones, no desactives pruebas fallidas, no cambies los criterios de aceptación para ajustarlos al código ni modifiques código de la aplicación sin mi aprobación. Tras los cambios, repite las comprobaciones afectadas y completa la verificación final de la revisión resultante. Exige un informe conciso que relacione los criterios con las pruebas de verificación y el estado superado/fallido/bloqueado, enumere las pruebas añadidas o explique por qué no hicieron falta, comunique los resultados de las cuatro comprobaciones e identifique los defectos sin resolver. GO exige todas las comprobaciones y pruebas de verificación obligatorias; de lo contrario, informa de NO-GO y su motivo. No cambies de rama, no crees commits, no envíes cambios, no abras ni combines PR y no crees agentes o habilidades adicionales durante QA.
```

## Examinar el perfil

1. Abre **Changes** y selecciona `.github/agents/qa.agent.md`. También puedes encontrarlo en el panel de revisión de archivos.
2. Lee el frontmatter. `description` es obligatorio y `name: QA` permite reconocer el perfil en el selector. Deja `model` y `tools` sin especificar en este ejercicio para usar el modelo seleccionado y las herramientas disponibles; los permisos habituales siguen vigentes.
3. Lee las instrucciones como una lista de revisión: ¿parten de los requisitos, utilizan la habilidad y las herramientas del navegador, añaden pruebas solo para carencias reales y distinguen los fallos de las comprobaciones bloqueadas?
4. Pide a Copilot que corrija las carencias antes de seleccionar el perfil. Confirma que ha creado la definición sin iniciar QA ni cambiar la aplicación.

> [!NOTE]
> Un perfil especializado orienta el comportamiento; no garantiza un resultado correcto. Debes seguir examinando la actividad de las herramientas, los cambios en las pruebas y el informe del agente.

## Ejecutar QA frente a la incidencia

La indicación de ejecución es para el agente personalizado **QA** seleccionado, no para el agente predeterminado que lee un perfil. Mantén la misma copia de trabajo y rama de filtrado.

1. En la sesión actual, abre el selector de agentes del cuadro de la indicación o introduce `/agent`, como describe la [documentación de personalización de la aplicación][customize-app].
2. Selecciona **QA** y verifica que la aplicación identifica visiblemente a **QA** como agente activo antes de enviar la indicación de ejecución.
3. Si **QA** no aparece o no puedes confirmar que está activo, detente y pregunta a la persona que dirige el taller, conservando este worktree y rama. No crees otra sesión de funcionalidad, no inventes una secuencia de recarga ni sustituyas este paso por una solicitud al agente predeterminado para que lea `qa.agent.md`.

El selector documentado está disponible durante una sesión, pero el descubrimiento de un perfil de repositorio recién creado puede depender de la versión de la aplicación. No trates la creación del archivo como prueba de activación.

Sustituye ambos marcadores por la URL real de la incidencia de filtrado y las aclaraciones aprobadas en la Lección 4, o por `none` si la incidencia está completa. No dependas de la memoria del agente anterior.

```plaintext
Verifica la funcionalidad de filtrado frente a esta incidencia: <filtering-issue-URL>. Estos son los criterios de aceptación adicionales que aprobé durante la planificación: <pega las aclaraciones acordadas o escribe none>.

Valida el comportamiento con el servidor MCP de Playwright, examina la cobertura de pruebas, añade pruebas solo para carencias de cobertura y ejecuta la validación mediante la habilidad quality-checks. Informa de las pruebas de verificación, los resultados de las comprobaciones y los bloqueos. No cambies código de la aplicación sin mi aprobación, no crees un commit ni abras una solicitud de incorporación de cambios.
```

## Revisar las pruebas de verificación

Lee el informe junto con la incidencia de filtrado y las aclaraciones aprobadas:

1. Comprueba que cada criterio se relaciona con pruebas adecuadas y comportamiento observable. Por ejemplo, combinar categorías y un editor exige verificar los juegos devueltos, no solo si responden los controles.
2. Examina la actividad real de las herramientas MCP de Playwright y confirma que el servidor probado pertenece a esta copia de trabajo. Las comprobaciones de navegador y E2E automatizadas no deben reutilizar un servidor obsoleto ni otra copia de trabajo.
3. Revisa los resultados de lint, pruebas unitarias, pruebas E2E y comprobaciones de tipos. Las cuatro deben ejecutarse mediante los scripts de la habilidad quality-checks; resumir comandos previstos no equivale a ejecutarlos.
4. Abre **Changes** para examinar las pruebas añadidas y compararlas con las carencias del informe.

Revisa las pruebas añadidas: deben cubrir carencias reales sin debilitar las aserciones. No añadir pruebas es correcto cuando la cobertura es adecuada. Un dictamen **NO-GO** por bloqueo o fallo es un resultado válido, no permiso para omitir pruebas de verificación.

Si QA identifica un defecto de la aplicación, aprueba por separado una corrección específica y repite las comprobaciones y observaciones de navegador afectadas en la revisión resultante. La ausencia de requisitos previos o herramientas necesita una resolución explícita. No trates las pruebas de verificación anteriores como demostración del código modificado.

## Guardar un punto de control

La función de QA es verificar, así que vuelve al agente habitual antes de solicitar un commit:

1. Conserva el informe de QA, la URL de la incidencia, las aclaraciones aprobadas y la revisión probada para la lección sobre la PR.
2. En la misma sesión, utiliza el selector de agentes para volver al agente habitual de Copilot y confirma que **QA** ya no está seleccionado.
3. Mantén el mismo worktree y rama. Si no encuentras la opción del agente habitual, pregunta a la persona que dirige el taller en lugar de iniciar otra sesión de funcionalidad o enviar instrucciones de commit a QA.

Cuando hayas revisado el perfil, los cambios de pruebas y las pruebas de verificación resultantes, envía la solicitud de punto de control al agente habitual con ese contexto de QA:

```plaintext
Revisa las diferencias actuales y crea un commit de punto de control para la definición del agente de QA y los cambios de pruebas aprobados. Mantén la rama de filtrado existente. No envíes cambios ni abras una solicitud de incorporación de cambios.
```

## Resumen y pasos siguientes

Has añadido un rol especializado reutilizable al flujo de trabajo y revisado su trabajo. En esta lección:

- creaste y examinaste un perfil de QA que parte de los requisitos.
- lo seleccionaste para evaluar la cobertura y reunir pruebas de verificación mediante la habilidad y MCP de Playwright.
- revisaste las conclusiones y guardaste el perfil con los cambios de pruebas justificados en la rama de filtrado.

Ya tienes los elementos para revisar la funcionalidad: la implementación, la habilidad, el perfil de QA, las pruebas y el informe de verificación. Conserva los hallazgos pendientes; un resultado fallido o bloqueado no autoriza la combinación. Continúa con la [Lección 8 - Crear y combinar la PR de la funcionalidad][next-lesson] para revisar el hito completo y utilizar Agent Merge.

## Recursos

- [Personalizar la aplicación GitHub Copilot, incluida la selección de agentes personalizados][customize-app]

[previous-lesson]: ../6-mcp-playwright/
[next-lesson]: ../8-create-pull-request/
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
