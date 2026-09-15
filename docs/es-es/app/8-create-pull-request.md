---
title: "Lección 8 - Crear y combinar la PR de la funcionalidad"
description: "Revisa conjuntamente el filtrado, la habilidad, el perfil QA y las pruebas, crea la PR 3 y autoriza Agent Merge explícitamente."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

La implementación del filtrado, la habilidad quality-checks, el perfil QA y las pruebas asociadas están guardados en commits de control en una sola rama. Revísalos juntos y utiliza las pruebas de verificación actuales de QA para preparar la PR 3. Ya has combinado explícitamente las PR de valoraciones por estrellas e instrucciones. Esta vez utilizarás **Agent Merge** dentro del flujo de PR, no como una funcionalidad o rama independiente.

En esta lección:

- aprenderás qué es Agent Merge y cómo automatiza el ciclo de vida de una combinación.
- examinarás la PR completa de la funcionalidad y las pruebas de verificación.
- autorizarás Agent Merge solo después de la revisión y confirmarás que la PR está combinada.

## Escenario

En los últimos módulos has explorado distintos niveles de automatización, desde crear código hasta permitir que Copilot valide directamente una interfaz de usuario. Para acelerar aún más el desarrollo, Tailspin Toys quiere averiguar si las solicitudes de incorporación de cambios que ya se han revisado y validado pueden combinarse automáticamente.

## Introducción a Agent Merge

**Agent Merge** permite automatizar el último tramo de la incorporación de una solicitud de cambios mediante la aplicación Copilot. Al habilitarlo, la sesión de la aplicación lee la solicitud y resuelve lo que la bloquea: corrige comprobaciones de CI con errores, responde a comentarios de revisión y reorganiza la base cuando es necesario. Después la combina en cuanto GitHub lo permite. Se ejecuta en segundo plano, continúa tras reiniciar la aplicación y se desactiva cuando se combina la solicitud.

Hasta ahora has seleccionado **Merge pull request** personalmente. Agent Merge puede asumir esa responsabilidad, pero su capacidad de editar código y combinar sigue necesitando tu autorización explícita. Revisa sus acciones permitidas y el trabajo antes de conceder permiso para combinar.

## Revisar el hito completo

Permanece en la sesión de filtrado de las Lecciones 4–7. Comprueba todas las diferencias de la rama frente a `main`, no solo el último punto de control: deben contener el filtrado, `.github/skills/quality-checks/SKILL.md`, los scripts incluidos, `.github/agents/qa.agent.md` y las pruebas asociadas.

Utiliza el selector de agentes para volver de **QA** al agente general de Copilot antes de solicitar commits o acciones de PR y mantén el modo **Interactive**. El trabajo del perfil QA era verificar, no publicar. Cambiar el agente seleccionado no debe cambiar la sesión, la copia de trabajo ni la rama de filtrado.

Este taller combina deliberadamente el trabajo de la funcionalidad y la infraestructura de calidad reutilizable en una sola PR. Un equipo de producción podría separarlos; aquí, los commits de control conservan pasos revisables sin ramas apiladas ni PR adicionales.

Revisa el informe QA de la Lección 7. Reutiliza sus pruebas de verificación solo si cubren la revisión final que se va a enviar, con las cuatro comprobaciones y las observaciones pertinentes del navegador completadas. Si los cambios de código, los conflictos o las correcciones de CI alteran lo que se probó, repite las comprobaciones y observaciones afectadas y actualiza las pruebas de verificación. Un informe **NO-GO** con fallos o bloqueos no autoriza la combinación.

Cuando las diferencias y las pruebas de verificación estén listas, envía:

```plaintext
Revisa todas las diferencias de la rama de filtrado frente a main, incluidas la funcionalidad de filtrado, la habilidad quality-checks y sus scripts, la definición del agente QA y las pruebas asociadas. Resume los criterios de la incidencia, las aclaraciones aprobadas y las pruebas de verificación actuales de QA. Reutiliza la verificación solo si sigue siendo válida para la revisión final; informa de pruebas de verificación desactualizadas, ausentes o con fallos antes de continuar.

Si los cambios revisados y la verificación están listos, crea un commit con los cambios aprobados restantes del hito, envía esta rama y crea una única PR de la funcionalidad destinada a main con la plantilla de PR del repositorio y la URL real de la incidencia de filtrado. Mantén el historial de puntos de control en esta rama. No utilices una habilidad de contribución, no crees otra rama o PR ni combines todavía.
```

Abre la PR en **My work** y examina **Files changed**, su descripción, las revisiones y los resultados de las comprobaciones. Examina los archivos de flujos de trabajo propios de Tailspin Toys y las comprobaciones obligatorias; no supongas que todas las comprobaciones locales u observaciones del navegador se ejecutan en CI. La compilación Astro y el comprobador de enlaces que publican el taller pertenecen a otro repositorio y no validan esta funcionalidad.

## Utilizar Agent Merge para gestionar la solicitud

Tras revisar la PR existente, configura Agent Merge en esta misma sesión. No crees una segunda PR.

1. Vuelve a la sesión de filtrado y confirma que está vinculada a la PR 3.
2. Abre el menú desplegable de acciones de PR en la esquina superior derecha. Antes de que exista una PR, está junto a **Create PR**; la etiqueta puede cambiar cuando hay una PR vinculada.
3. Selecciona **Agent merge** para habilitar Agent Merge.
4. Revisa los permisos disponibles, incluidos **Address reviews**, **Fix CI failures**, **Resolve conflicts** y **Merge pull request**. Mantén desactivado el permiso de combinación mientras haya hallazgos o verificaciones pendientes.
5. Antes de iniciarlo, envía el alcance y la autorización siguientes y después selecciona **Agent merge**:

   ```plaintext
   Gestiona esta PR de filtrado existente con Agent Merge. Resuelve los bloqueos de revisión o CI solo dentro del alcance de esta PR. No debilites las pruebas ni los requisitos y pregunta antes de realizar cambios ajenos o instalaciones. Cualquier cambio de la revisión probada exige actualizar las comprobaciones pertinentes y las pruebas de observación del navegador; no trates resultados QA anteriores como prueba de código modificado.

   No combines hasta que habilite explícitamente Merge pull request tras revisar las diferencias finales y las pruebas de verificación. No crees otra PR ni empieces la tarea del lienzo.
   ```

6. Revisa los cambios posteriores y los resultados actualizados. Cuando las diferencias finales estén aprobadas, CI y las revisiones obligatorias se hayan completado correctamente y las pruebas de QA correspondan a esa revisión, autoriza explícitamente la combinación seleccionando el menú desplegable junto a **Agent merge** y después **Merge pull request**.

   ![Menú desplegable Agent merge con las acciones permitidas al agente —Address reviews, Fix CI failures y Resolve conflicts— y una flecha que señala Merge pull request](../../_images/app-agent-merge-merge.png)

7. Confirma que GitHub muestra la PR 3 como **Merged**, no solo como combinable o en cola. Agent Merge no elude las protecciones del repositorio ni los permisos ausentes; resuelve esos bloqueos antes de continuar.

Solo después de esa combinación debes iniciar el hito del lienzo. La Lección 9 crea un worktree nuevo y actualiza su rama de sesión mediante un avance rápido hasta el último `origin/main` para que el lienzo parta de la funcionalidad completa combinada.

## Resumen y pasos siguientes

Has automatizado varias partes del proceso de desarrollo, como la generación, las pruebas y la validación de código, y ahora también el proceso de solicitud de incorporación de cambios. En concreto:

- has aprendido qué es Agent Merge y cómo automatiza el ciclo de vida de una combinación.
- has revisado todas las diferencias de filtrado, habilidad, perfil QA y pruebas como PR 3.
- has reutilizado las pruebas de QA actuales, examinado CI y autorizado Agent Merge explícitamente.

A continuación, explorarás los **lienzos**, una forma más completa de planificar y visualizar el trabajo con el agente. Continúa con la [Lección 9 - Crear un lienzo de clasificación de incidencias][next-lesson].

## Recursos

- [Gestionar incidencias y solicitudes de incorporación de cambios con la aplicación GitHub Copilot][managing-issues-prs]
- [Acerca de la aplicación GitHub Copilot][about-copilot-app]

[previous-lesson]: ../7-qa-agent/
[next-lesson]: ../9-canvases/
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app