---
slug: es-es
title: "Manos a la obra con los agentes de GitHub Copilot"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Las recientes ampliaciones de las capacidades de GitHub Copilot ofrecen a los desarrolladores herramientas potentes para todo el ciclo de vida del desarrollo de software (SDLC). Estas capacidades incluyen trabajar con incidencias y solicitudes de incorporación de cambios en GitHub, interactuar con servicios externos y, por supuesto, crear código. En este laboratorio se exploran estas funciones mediante casos de uso reales y consejos para aprovechar al máximo las herramientas.

> [!CAUTION]
> Como GitHub Copilot es probabilístico y no determinista, el código exacto, los archivos modificados y otros elementos pueden variar. Por este motivo, es posible que observes pequeñas diferencias entre las capturas de pantalla y los fragmentos de código del laboratorio y lo que tú ves. Es algo normal y forma parte de trabajar con este tipo de herramientas.
>
> Si algo parece no funcionar o no se ejecuta correctamente, ¡pide ayuda a un mentor!

## Elige tu entorno

GitHub Copilot te acompaña allí donde trabajes. Elige el entorno que se ajuste a tu forma de desarrollar y completa sus ejercicios con el trabajo pendiente compartido de Tailspin Toys. Cada entorno comienza con su propia configuración para que puedas empezar directamente con el que elijas.

### 🖥️ [VS Code](vscode/)

GitHub Copilot dentro de **Visual Studio Code** y GitHub Codespaces. Trabaja con el modo agente de Copilot Chat, servidores MCP y agentes personalizados sin salir del editor que ya utilizas. Es ideal si quieres integrar la asistencia de IA directamente en el IDE.

### 💻 [Copilot CLI](cli/)

**GitHub Copilot CLI** es un asistente basado en agentes que se ejecuta en el terminal. Tras la configuración, sigue nueve módulos principales: entrega una mejora rápida de valoraciones por estrellas, establece instrucciones, planifica y crea el filtrado, crea una habilidad quality-checks, valida mediante MCP de Playwright, crea un agente QA y combina la funcionalidad. Termina con los controles de CLI y un resumen. El flujo tiene tres hitos de solicitudes de incorporación de cambios.

### 🤖 [Copilot App](app/)

La **aplicación GitHub Copilot** es una aplicación de escritorio basada en Copilot CLI. Sigue la misma configuración y los nueve módulos principales del flujo de valoraciones por estrellas, instrucciones, filtrado, habilidad, MCP, QA y PR de la funcionalidad, mediante las sesiones aisladas de la aplicación y **Agent Merge**. Crea y combina un lienzo guardado en el repositorio como cuarto hito de solicitudes de incorporación de cambios y termina con el resumen.

### ☁️ [Copilot Cloud Agent](cloud/)

El **agente de Copilot en la nube** es un compañero de programación asíncrono que trabaja en segundo plano en las incidencias de GitHub. Asígnale trabajo, guíalo con agentes personalizados, supervisa el progreso desde el panel de agentes y revisa las solicitudes de incorporación de cambios que abre.

## Escenario

Acabas de incorporarte como desarrollador a Tailspin Toys, una empresa ficticia que ofrece financiación colectiva para juegos de mesa de temática tecnológica: ¡un mercado enorme! El trabajo pendiente del equipo ya está registrado como incidencias de GitHub para que puedas comenzar. Incluye tanto funcionalidades, como el filtrado y la paginación, como mejoras de calidad, como la accesibilidad y los estándares de programación. Trabajarás de forma iterativa para completar las tareas mientras exploras el sitio y las capacidades de Copilot.

## Primeros pasos

Elige uno de los entornos anteriores para empezar. Cada uno comienza con la configuración necesaria para que puedas ponerte manos a la obra.