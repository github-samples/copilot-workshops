---
title: "Ejercicio 7 - Crear y utilizar un agente de QA"
description: "Crea un perfil de QA que parta de los requisitos y combine cobertura de pruebas, la habilidad quality-checks y observaciones directas del navegador."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Has ejecutado comprobaciones repetibles y explorado el filtrado mediante MCP de Playwright. Ahora crea un **agente personalizado de QA** para reunir los requisitos, la cobertura y las observaciones del navegador. Mantén la sesión, la copia de trabajo y la rama de filtrado; la PR de funcionalidad llegará en el Ejercicio 8.

En este ejercicio:

- crearás y examinarás un perfil de QA que parte de los requisitos.
- seleccionarás el perfil y revisarás la cobertura, los resultados de las comprobaciones y las pruebas de verificación del navegador.
- volverás al agente normal y guardarás un punto de control del perfil con las pruebas cuya incorporación esté justificada.

## Escenario

Tailspin Toys se prepara para publicar el filtrado. Que las pruebas pasen no basta para saber si se cubren todos los requisitos acordados. El equipo necesita una revisión centrada en comparar la incidencia con la implementación, identificar carencias y explicar si la funcionalidad está lista para revisión. El perfil de QA guiará esa evaluación sin sustituir el criterio humano.

## Crear el perfil de QA

Mantén el modo **Interactive**. Un perfil define el rol y las instrucciones de un especialista; una habilidad reúne instrucciones de tareas reutilizables, scripts y recursos. El agente de QA utilizará tu habilidad y las herramientas MCP configuradas en lugar de sustituirlas.

Envía esta indicación y después examina la definición antes de ejecutarla:

```plaintext
Crea un agente personalizado de QA reutilizable en .github/agents/qa.agent.md. Primero examina las instrucciones del repositorio, package.json, la configuración de pruebas y .github/skills/quality-checks/SKILL.md. Proporciona al perfil un frontmatter YAML válido con name establecido en QA y una description que explique cuándo utilizarlo. No fijes un modelo ni añadas una lista tools; hereda las herramientas y los permisos disponibles del entorno. Crea solo la definición del agente y después detente para que pueda examinarla antes de ejecutarlo.

En las instrucciones del agente, exige que toda tarea de QA parta de la incidencia y de los criterios de aceptación aprobados que proporcione el usuario. Trata estos requisitos como fuente de verdad, no la implementación. Pregunta cuando falten requisitos o sean ambiguos. Examina la funcionalidad y las pruebas existentes y relaciona cada criterio con la cobertura automatizada adecuada y el comportamiento observable.

Exige validación directa en el navegador mediante el servidor MCP de Playwright configurado y la ejecución de lint, pruebas unitarias, pruebas de un extremo a otro y comprobaciones de tipos mediante la habilidad quality-checks existente y sus scripts incluidos. Lee la habilidad explícitamente si no se ha descubierto automáticamente. Informa de la ausencia de habilidades, herramientas MCP, requisitos previos o acceso como bloqueos; no sustituyas silenciosamente el flujo por otro ni etiquetes comprobaciones omitidas como superadas. Identifica la copia de trabajo y el servidor que se prueban, evita reutilizar el servidor de otro worktree, detén solo los servidores que haya iniciado el agente y pregunta antes de cualquier instalación o de detener otro proceso.

Permite que el agente de QA añada las pruebas mínimas necesarias para carencias reales de cobertura, siguiendo las instrucciones del repositorio; no añadir pruebas es válido cuando la cobertura ya es adecuada. No debilites aserciones, no desactives pruebas fallidas, no cambies los criterios de aceptación para ajustarlos al código ni modifiques código de la aplicación sin mi aprobación. Tras los cambios, repite las comprobaciones afectadas y completa la verificación final de la revisión resultante. Exige un informe conciso que relacione los criterios con las pruebas de verificación y el estado superado/fallido/bloqueado, enumere las pruebas añadidas o explique por qué no hicieron falta, comunique los resultados de las cuatro comprobaciones e identifique los defectos sin resolver. GO exige todas las comprobaciones y pruebas de verificación obligatorias; de lo contrario, informa de NO-GO y su motivo. No cambies de rama, no crees commits, no envíes cambios, no abras ni combines PR y no crees agentes o habilidades adicionales durante QA.
```

## Examinar el perfil

Abre `.github/agents/qa.agent.md` en el editor y examina las diferencias. `description` es obligatorio; este ejercicio también proporciona `QA` como `name` legible. Confirma que no se ha fijado un `model` ni inventado una lista de herramientas. Omitir `tools` hereda las herramientas disponibles; no elude los permisos del entorno. Los perfiles de producción pueden restringir las herramientas deliberadamente.

Confirma que las instrucciones parten de los requisitos, exigen actividad real del navegador mediante MCP y scripts de la habilidad, permiten solo adiciones de pruebas justificadas e informan de los bloqueos con veracidad. Ni un perfil especializado ni una habilidad requieren una ventana de contexto independiente o la orquestación de otros agentes.

## Ejecutar QA frente a la incidencia

La indicación de ejecución es para el agente personalizado **QA** seleccionado, no para el agente predeterminado que lee un perfil. Inicia una conversación nueva de CLI en la misma copia de trabajo para cargar el perfil nuevo sin crear otra rama de funcionalidad.

1. Conserva la URL de la incidencia de filtrado y las aclaraciones aprobadas. Espera a que termine el agente actual y después introduce `/exit` para volver a la terminal.
2. Confirma que sigues en el directorio del repositorio de filtrado y en la misma rama con `git branch --show-current` y `git status --short`. No cambies de rama ni crees un worktree.
3. Inicia CLI con el perfil del repositorio:

   ```shell
   copilot --agent qa
   ```

4. Verifica que CLI identifica a **QA** como agente seleccionado antes de ejecutarlo. La [referencia de comandos de CLI][cli-reference] documenta `--agent`; escribir o leer el perfil no constituye por sí solo su activación. Si la selección falla o el agente no puede acceder a las herramientas MCP de Playwright configuradas y a la habilidad, detente y resuelve ese bloqueo con la persona que dirige el taller.

Sustituye ambos marcadores por la URL real de la incidencia de filtrado y las aclaraciones aprobadas en el Ejercicio 4, o por `none` si la incidencia está completa. No dependas de la memoria del agente anterior.

```plaintext
Verifica la funcionalidad de filtrado frente a esta incidencia: <filtering-issue-URL>. Estos son los criterios de aceptación adicionales que aprobé durante la planificación: <pega las aclaraciones acordadas o escribe none>.

Valida el comportamiento con el servidor MCP de Playwright, examina la cobertura de pruebas, añade pruebas solo para carencias de cobertura y ejecuta la validación mediante la habilidad quality-checks. Informa de las pruebas de verificación, los resultados de las comprobaciones y los bloqueos. No cambies código de la aplicación sin mi aprobación, no crees un commit ni abras una solicitud de incorporación de cambios.
```

## Revisar las pruebas de verificación

Contrasta el informe con la incidencia: cada criterio necesita cobertura automatizada adecuada y comportamiento observable. Examina la actividad real de las herramientas MCP de Playwright, la identidad de la copia de trabajo y del servidor y los resultados de los cuatro scripts de la habilidad. Las comprobaciones de navegador y E2E automatizadas no deben reutilizar un servidor obsoleto ni otra copia de trabajo.

Revisa las pruebas añadidas: deben cubrir carencias reales sin debilitar las aserciones. No añadir pruebas es correcto cuando la cobertura es adecuada. Un dictamen **NO-GO** por bloqueo o fallo es un resultado válido, no permiso para omitir pruebas de verificación.

Si QA identifica un defecto de la aplicación, aprueba por separado una corrección específica y repite las comprobaciones y observaciones de navegador afectadas en la revisión resultante. La ausencia de requisitos previos o herramientas necesita una resolución explícita. No trates las pruebas de verificación anteriores como demostración del código modificado.

## Guardar un punto de control

Cuando QA haya terminado, conserva su informe con la URL de la incidencia, las aclaraciones aprobadas, la revisión probada, las observaciones de navegador y los resultados de las comprobaciones. Introduce `/exit` y después inicia `copilot` sin `--agent` desde el mismo directorio y rama para volver a una conversación normal. Proporciona ese contexto de nuevo; la conversación nueva no hereda las pruebas de verificación de la conversación de QA.

Cuando hayas revisado el perfil, los cambios de pruebas y las pruebas de verificación resultantes, envía la solicitud siguiente al agente normal:

```plaintext
Revisa las diferencias actuales y crea un commit de punto de control para la definición del agente de QA y los cambios de pruebas aprobados. Mantén la rama de filtrado existente. No envíes cambios ni abras una solicitud de incorporación de cambios.
```

## Resumen y pasos siguientes

Has creado y seleccionado un perfil de QA, revisado sus pruebas de verificación y guardado el perfil con las pruebas justificadas. Conserva los hallazgos pendientes; un veredicto fallido o bloqueado no autoriza la combinación. Continúa con el [Ejercicio 8 - Crear y combinar la PR de la funcionalidad][next-lesson] con la funcionalidad de filtrado, la habilidad, el perfil de QA, las pruebas y las pruebas de verificación actuales.

[previous-lesson]: ../6-mcp-playwright/
[next-lesson]: ../8-create-pull-request/
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
