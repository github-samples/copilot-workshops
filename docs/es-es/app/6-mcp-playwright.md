---
title: "Lección 6 - Validar la funcionalidad con MCP de Playwright"
description: "Configura MCP de Playwright mediante Customize y observa el filtrado en un navegador desde el worktree existente de la funcionalidad."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

En la lección anterior agrupaste y ejecutaste las comprobaciones del proyecto mediante tu habilidad quality-checks. Ahora da al agente acceso a un navegador para que pueda observar directamente la interfaz de filtrado. Permanece en la misma sesión, worktree y rama de filtrado. Esta lección aporta pruebas de observación en el navegador, no otra funcionalidad, una nueva ejecución de todo el conjunto de pruebas ni una PR.

En esta lección:

- comprenderás qué es Model Context Protocol (MCP) y cómo lo utiliza la aplicación GitHub Copilot.
- añadirás el servidor MCP de Playwright mediante **Customize**.
- pedirás al agente que controle un navegador y explore la funcionalidad de filtrado.

## Escenario

Aunque las pruebas unitarias y de un extremo a otro son importantes, validar las actualizaciones de la interfaz de usuario requiere interactuar con ella. Quieres que Copilot pueda utilizar el sitio web en el que trabajas como lo haría un usuario para automatizar aún más los cambios y aumentar la confianza en que las actualizaciones funcionan según lo previsto.

## ¿Qué es Model Context Protocol (MCP)?

[Model Context Protocol (MCP)][mcp-blog-post] proporciona a los agentes de IA una forma de comunicarse con herramientas y servicios externos. Mediante MCP, los agentes de IA pueden comunicarse con ellos en tiempo real. Esto les permite acceder a información actualizada mediante recursos y realizar acciones en tu nombre mediante herramientas.

Se accede a estas herramientas y recursos a través de un servidor MCP, que actúa como puente entre el agente de IA y las herramientas y servicios externos. El servidor MCP gestiona la comunicación entre el agente de IA y las herramientas externas, como API existentes o herramientas locales, por ejemplo, paquetes NPM. Cada servidor MCP representa un conjunto diferente de herramientas y recursos a los que puede acceder el agente de IA.

Dos servidores MCP populares son:

- [**GitHub MCP Server**](https://github.com/github/github-mcp-server): proporciona acceso a un conjunto de API para gestionar repositorios de GitHub. Permite al agente de IA realizar acciones como crear repositorios, actualizar los existentes y gestionar incidencias y solicitudes de incorporación de cambios.
- [**Playwright MCP Server**][playwright-mcp-server]: proporciona capacidades de automatización del navegador mediante Playwright. Permite al agente de IA realizar acciones como visitar páginas web, completar formularios y seleccionar botones.

Hay muchos otros servidores MCP que proporcionan acceso a distintas herramientas y recursos. GitHub aloja un [registro de MCP](https://github.com/mcp) para facilitar su descubrimiento y las contribuciones al ecosistema.

> [!CAUTION]
> Trata los servidores MCP como cualquier otra dependencia del proyecto. Antes de utilizar uno, revisa atentamente su código fuente, verifica el editor y considera las implicaciones de seguridad. Utiliza únicamente servidores MCP de confianza y ten cuidado al conceder acceso a recursos u operaciones confidenciales.

## Añadir el servidor MCP de Playwright

La [documentación actual de personalización de la aplicación][customize-app] utiliza **Customize** en la barra lateral para descubrir y gestionar MCP. Los servidores MCP configurados para tus repositorios o Copilot CLI pueden estar ya disponibles en la aplicación; examina los servidores instalados antes de añadir un duplicado.

1. Selecciona **Customize** en la barra lateral.
2. Selecciona **MCP** y comprueba en **Installed** si ya existe un servidor de Playwright.
3. Si es necesario, busca **Playwright** entre los servidores disponibles o utiliza el procedimiento de servidor personalizado documentado por el editor.
4. Revisa el editor, la configuración y cualquier solicitud de instalación antes de aprobarla. Sigue las indicaciones para añadir el servidor; las directivas de la organización o la falta de requisitos previos pueden bloquear la configuración.
5. Vuelve a la sesión de filtrado existente y mantén el modo **Interactive**. Confirma que las herramientas de navegador de MCP de Playwright están disponibles antes de solicitar la validación. No crees un worktree nuevo de la funcionalidad para solucionar problemas de configuración.

Si la configuración falla, resuelve el problema de configuración o permisos en lugar de aceptar una afirmación de que el agente ha navegado sin herramientas. La visibilidad del navegador depende de la configuración del servidor; la actividad real de las herramientas y las observaciones son las pruebas.

## Pedir a Copilot que explore la funcionalidad mediante Playwright

Utiliza la URL real de la incidencia y las aclaraciones aprobadas que guardaste en la Lección 4. Detén cualquier servidor de desarrollo manual de lecciones anteriores antes de que el agente inicie el suyo. Debe identificar la copia de trabajo y el servidor que está probando.

1. Utiliza la indicación siguiente para pedir a Copilot que valide la nueva funcionalidad:

   ```plaintext
   Utiliza el servidor MCP de Playwright configurado para observar la funcionalidad de filtrado según esta incidencia: <filtering-issue-URL>. Estas son mis aclaraciones de planificación aprobadas: <pega las aclaraciones acordadas o escribe none>. Permanece en este worktree y rama de filtrado.

   Identifica la copia de trabajo, inicia su servidor de desarrollo y utiliza herramientas reales de navegador para probar la selección de varias categorías, el filtrado por editor, el filtrado combinado, los controles accesibles y cualquier comportamiento acordado de borrado de filtros o resultados vacíos. Informa de las observaciones frente a los criterios, incluidos fallos o comprobaciones bloqueadas. No afirmes comportamientos que no hayas observado.

   Este paso es una observación en el navegador, no otra ejecución automatizada completa de pruebas. No cambies código de la aplicación, pruebas, habilidades ni perfiles de agente, no crees commits, no envíes cambios ni crees una PR. Informa como bloqueadas las herramientas MCP o los requisitos previos ausentes y pregunta antes de instalar cualquier cosa. No reutilices el servidor de otra copia de trabajo ni detengas procesos ajenos. Al terminar, detén solo el servidor que hayas iniciado.
   ```

Examina las llamadas a herramientas MCP de Playwright, la URL probada y las observaciones comunicadas del navegador. Un relato basado solo en el código fuente o en resultados E2E anteriores no demuestra el uso de MCP.

2. Compara el resumen con la incidencia y las aclaraciones aprobadas. Si hay un defecto, autoriza por separado una corrección específica, revisa las diferencias y repite las comprobaciones automatizadas y observaciones del navegador pertinentes. Las pruebas anteriores a la corrección no demuestran la revisión resultante.
3. Confirma que el agente ha detenido su propio servidor. Mantén abierta esta sesión de filtrado y permanece en modo **Interactive** antes de crear el perfil QA en la Lección 7.

Esta etapa aporta observación directa, no sustituye la cobertura automatizada. Los fallos y las observaciones bloqueadas siguen siendo visibles para QA.

## Resumen y pasos siguientes

Has utilizado el servidor MCP de Playwright para explorar la funcionalidad en un navegador real desde la aplicación GitHub Copilot. En resumen:

- has aprendido qué es Model Context Protocol (MCP) y cómo la aplicación pone a disposición las herramientas MCP.
- has configurado el servidor MCP de Playwright mediante **Customize**.
- has pedido al agente que controle un navegador y explore la funcionalidad de filtrado.

A continuación, reúne los requisitos, las observaciones del navegador, la cobertura y la habilidad en un perfil especializado. Continúa en esta misma sesión con la [Lección 7 - Crear y utilizar un agente QA][next-lesson]. No crees todavía la PR de la funcionalidad.

## Recursos

- [¿Qué es MCP y por qué todo el mundo habla de él?][mcp-blog-post]
- [Servidor MCP de Playwright de Microsoft][playwright-mcp-server]
- [Configurar servidores MCP en la aplicación GitHub Copilot][customize-app]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app