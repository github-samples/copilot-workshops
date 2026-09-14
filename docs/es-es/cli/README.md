---
slug: es-es/cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

**[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** incorpora GitHub Copilot a tu terminal como asistente de programación con agentes. Explora bases de código, genera código, ejecuta comandos y se conecta a herramientas externas, todo desde la línea de comandos, para que puedas mantener el flujo sin cambiar a un editor gráfico.

Tras la configuración de los Ejercicios 0–1, completarás nueve módulos principales en los Ejercicios 2–10. Empieza con una mejora rápida de valoraciones por estrellas, establece instrucciones de documentación y crea el filtrado con los modos **Plan** y **Autopilot**. Después crea una habilidad quality-checks reutilizable, valida el comportamiento con MCP de Playwright, crea un agente de QA y entrega la funcionalidad. Termina explorando los controles de CLI y repasando lo que has creado.

## Ejercicios

| Ejercicio | Tema | Descripción |
|----------|-------|-------------|
| [0. Requisitos previos][ex0] | Configuración | Crea tu repositorio y tu codespace |
| [1. Instalación de Copilot CLI][ex1] | Instalación | Instala y autentica Copilot CLI |
| [2. Añadir valoraciones por estrellas: una mejora rápida][ex2] | Primer cambio | Muestra las valoraciones existentes, valida y combina la PR 1 |
| [3. Guiar a Copilot con instrucciones personalizadas][ex3] | Contexto | Añade una convención de documentación, demuéstrala y combina la PR 2 |
| [4. Crear el filtrado con Plan y Autopilot][ex4] | Implementación | Revisa un plan, aprueba Autopilot, prueba y guarda un punto de control |
| [5. Crear y utilizar una habilidad quality-checks][ex5] | Habilidades | Genera, examina y ejecuta comprobaciones con scripts de shell incluidos |
| [6. Validar la funcionalidad con MCP de Playwright][ex6] | Herramientas de navegador | Observa el comportamiento del filtrado en un navegador real |
| [7. Crear y utilizar un agente de QA][ex7] | Agentes | Audita requisitos y cobertura y reúne las pruebas de verificación finales |
| [8. Crear y combinar la PR de la funcionalidad][ex8] | Entrega | Revisa el filtrado y las personalizaciones reutilizables juntos en la PR 3 |
| [9. Explorar comandos de barra y opciones de CLI][ex9] | Controles de CLI | Examina contexto, modelos, sesiones y destinos para compartir |
| [10. Repaso y próximos pasos][ex10] | Resumen | Repasa los recursos comunes y los tres hitos de PR |

## Ramas y solicitudes de incorporación de cambios

Combinarás tres solicitudes de incorporación de cambios: valoraciones por estrellas; instrucciones y una pequeña demostración; y filtrado con la habilidad quality-checks, el perfil de QA y las pruebas asociadas. Combina cada una de las dos primeras PR antes de iniciar el siguiente hito desde `main` actualizado.

Los Ejercicios 4–8 comparten una rama de funcionalidad y una copia de trabajo. Guarda commits de puntos de control durante el proceso; crear la habilidad, configurar MCP y seleccionar QA no inicia nuevas ramas de funcionalidad. El Ejercicio 9 explora los controles sin iniciar otra funcionalidad o PR.

## Requisitos previos

Antes de asistir a este taller, asegúrate de tener:

- [ ] Una cuenta de GitHub con un plan activo de **Copilot Student, Pro, Pro+, Business o Enterprise**
- [ ] Conocimientos básicos de operaciones de terminal/línea de comandos
- [ ] Git instalado y configurado

> [!TIP]
> ¿No tienes un plan de pago? Los estudiantes verificados pueden obtener GitHub Copilot gratis a través de [GitHub Education][callout-student-plan-education]. El plan **Copilot Student** incluye las funciones de agente, MCP, revisión de código y Copilot CLI que utiliza este taller, así que puedes completar con él todos los recorridos.

[callout-student-plan-education]: https://github.com/education/students

> [!NOTE]
> Si usas Copilot Business o Copilot Enterprise, asegúrate de que tu administrador haya habilitado Copilot CLI.

## Primeros pasos

**[Empieza con el ejercicio 0: Requisitos previos →][ex0]**

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-cli/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-slash-commands/
[ex10]: 10-review/
