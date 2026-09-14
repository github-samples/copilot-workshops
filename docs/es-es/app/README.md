---
slug: es-es/app
title: "Aplicación GitHub Copilot"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

La [**aplicación GitHub Copilot**](https://docs.github.com/copilot/concepts/agents/github-copilot-app) es una aplicación de escritorio basada en Copilot CLI que reúne el desarrollo dirigido por agentes en un único espacio de trabajo específico. Añade sesiones de agente en paralelo, modos de sesión intercambiables, lienzos compartidos y gestión nativa de incidencias y solicitudes de incorporación de cambios de GitHub, incluido **Agent Merge**, que guía una solicitud durante reorganizaciones de base, comentarios de revisión, correcciones de CI y la combinación.

Las Lecciones 0–1 de configuración preparan el proyecto y el espacio de trabajo de la aplicación. Los nueve módulos principales, las Lecciones 2–10, empiezan con una mejora rápida de valoraciones por estrellas y una convención de documentación demostrada en código real. Después planificarás y crearás el filtrado, crearás y ejecutarás una habilidad quality-checks con scripts de shell, observarás la funcionalidad mediante MCP de Playwright y crearás un agente personalizado QA para evaluar requisitos y cobertura. Revisarás la PR completa de la funcionalidad y autorizarás Agent Merge; después crearás y combinarás un lienzo compartido de clasificación de incidencias.

El taller tiene cuatro hitos de PR: valoraciones por estrellas; instrucciones con su demostración; filtrado con la habilidad, el perfil QA y las pruebas; y, por último, el lienzo. Empieza cada hito desde `main` actualizado, con una rama por PR en lugar de una por módulo. Las Lecciones 4–8 permanecen en la misma sesión, worktree y rama de filtrado. Volver a abrir el lienzo añade contexto de incidencias sin iniciar otra funcionalidad ni una quinta PR. Las automatizaciones se enlazan como siguiente paso, no como ejercicio adicional.

## Lecciones

| Lección | Tema | Descripción |
|--------|-------|-------------|
| [0. Requisitos previos][ex0] | Configuración | Instala Node.js y crea tu copia del proyecto Tailspin Toys |
| [1. Instalar la aplicación Copilot][ex1] | Configuración | Instala la aplicación, conecta el proyecto y familiarízate con el espacio de trabajo |
| [2. Añadir valoraciones por estrellas: una mejora rápida][ex2] | Primer cambio | Muestra las valoraciones existentes y la alternativa para null y combina la PR 1 |
| [3. Guiar a Copilot con instrucciones personalizadas][ex3] | Contexto | Añade un estándar de documentación y una demostración real y combina la PR 2 |
| [4. Crear el filtrado con Plan y Autopilot][ex4] | Implementación | Aprueba el plan, implementa y comprueba el filtrado y guarda un punto de control |
| [5. Crear y utilizar una habilidad quality-checks][ex5] | Comprobaciones repetibles | Crea, revisa y ejecuta los scripts de shell incluidos |
| [6. Validar la funcionalidad con MCP de Playwright][ex6] | Observación en el navegador | Configura MCP mediante Customize y examina el comportamiento del filtrado |
| [7. Crear y utilizar un agente QA][ex7] | Requisitos y cobertura | Selecciona un perfil especializado y reúne pruebas de verificación final |
| [8. Crear y combinar la PR de la funcionalidad][ex8] | Revisión y combinación | Revisa el filtrado, la habilidad, el perfil QA y las pruebas y autoriza Agent Merge para la PR 3 |
| [9. Crear un lienzo de clasificación de incidencias][ex9] | Colaboración | Comparte un lienzo guardado en el repositorio en la PR 4 y añade contexto de incidencias |
| [10. Repaso y pasos siguientes][ex10] | Resumen | Revisa el flujo, los recursos creados y otros materiales |

## Requisitos previos

Antes de asistir a este taller, asegúrate de disponer de:

- [ ] Una cuenta de GitHub con un plan **Copilot Student, Pro, Pro+, Business o Enterprise** activo
- [ ] Un ordenador con **macOS, Linux o Windows**
- [ ] [Git instalado][install-git] en el ordenador

> [!TIP]
> ¿No tienes un plan de pago? Los estudiantes verificados pueden obtener GitHub Copilot gratis mediante [GitHub Education][callout-student-plan-education]. El plan **Copilot Student** incluye el agente, MCP, la revisión de código y las funcionalidades de Copilot CLI que se utilizan en este taller, por lo que permite completar todos los recorridos.

> [!NOTE]
> Como la aplicación Copilot se ejecuta en tu propio equipo y no en un codespace, la [Lección 0][ex0] explica cómo instalar Node.js y crear tu copia del proyecto antes de instalar la aplicación.

> [!NOTE]
> Si utilizas Copilot Business o Copilot Enterprise, el administrador debe habilitar la directiva **Copilot CLI** para que puedas utilizar la aplicación.

## Comenzar

[**Empieza por la Lección 0: Requisitos previos →**][ex0]

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-app/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-canvases/
[ex10]: 10-review/
[install-git]: https://github.com/git-guides/install-git
[callout-student-plan-education]: https://github.com/education/students