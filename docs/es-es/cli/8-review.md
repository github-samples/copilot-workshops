---
title: "Ejercicio 8 - Repaso y próximos pasos"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

En los últimos ejercicios, has explorado algunos de los casos de uso más habituales de GitHub Copilot CLI, entre ellos:

- interactuar con GitHub y otros servidores MCP.
- usar archivos de instrucciones para orientar la generación de código.
- implementar habilidades para añadir herramientas al conjunto de herramientas de Copilot CLI.
- invocar agentes personalizados para tareas avanzadas y más complejas.
- usar comandos de barra para gestionar tu sesión y, opcionalmente, volver a conectar con cloud agent mediante `/delegate`.

Vamos a hablar de algunos comandos de barra, buenas prácticas y próximos pasos.

## Comandos de barra

Copilot CLI tiene una serie de comandos de barra disponibles para interactuar con él, incluidos algunos que te permiten configurarlo o ver qué está ocurriendo entre bastidores. Ya has usado `/clear` para iniciar un chat nuevo que borra el contexto actual, y `/mcp` para inspeccionar y gestionar servidores MCP. Algunos adicionales que pueden resultarte útiles son:

| Comando | Descripción |
| ------------------ | ------------------------------------------------------------- |
| `/add-dir` | Añadir un directorio a la lista de confianza de Copilot |
| `/clear`, `/new` | Borrar el historial de la conversación y empezar de cero |
| `/compact` | Resumir el historial de la conversación para reducir el uso de la ventana de contexto |
| `/context` | Mostrar el uso de tokens de la ventana de contexto y su visualización |
| `/diff` | Revisar los cambios realizados en el directorio actual |
| `/model` | Seleccionar el modelo de IA que se va a usar (Claude Sonnet, GPT-5, etc.) |
| `/plan <prompt>` | Crear un plan de implementación antes de programar |
| `/review <prompt>` | Ejecutar el agente de revisión de código para analizar los cambios |
| `/delegate` | Delegar la tarea en Copilot cloud agent para procesamiento asíncrono |
| `/session` | Mostrar la información de la sesión y el resumen del espacio de trabajo |
| `/share` | Compartir la sesión en un archivo Markdown o un GitHub gist |
| `/skills` | Gestionar habilidades para ampliar las capacidades |
| `/usage` | Mostrar métricas y estadísticas de uso de la sesión |

> [!TIP]
> Usa `/help` para ver la lista completa de comandos disponibles y de atajos de teclado.

## Buenas prácticas

Cuando usas una herramienta de IA, la infraestructura subyacente determina en gran medida la calidad de lo que obtienes. Unos archivos de instrucciones sólidos, agentes personalizados y habilidades de agente robustas forman parte de ello, y en este taller has explorado cada uno de esos elementos. [awesome-copilot][awesome-copilot] es una buena fuente de plantillas, y el propio Copilot puede generarlas como punto de partida.

El contexto sigue importando tanto como la infraestructura. Describir claramente *qué* quieres que se construya, *por qué* y *cómo* cambia de forma significativa el resultado. Si una información puede ayudar a Copilot, compártela.

## Próximos pasos

La mejor forma de mejorar tus habilidades con cualquier herramienta es seguir usándola. Úsala para código de producción, para proyectos personales, para esa pequeña aplicación en la que llevas años pensando pero que nunca llegabas a construir. Comparte lo que aprendas con tu equipo y aprende también de él. Y, como siempre, explora la documentación.

Si quieres explorar más del ecosistema de GitHub Copilot, consulta el [recorrido de VS Code](../../vscode/) o el [recorrido de Cloud agent](../../cloud/).

## Recursos

- [Acerca de Copilot CLI][about-copilot-cli]
- [Usar Copilot CLI][using-copilot-cli]
- [Repositorio Awesome Copilot][awesome-copilot]
- [Guía de instrucciones personalizadas][repo-instructions]
- [Documentación de las habilidades de agente][agent-skills]
- [Documentación de agentes personalizados][custom-agents]
- [Especificación de MCP][mcp-spec]

[previous-lesson]: ../7-slash-commands/
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[awesome-copilot]: https://github.com/github/awesome-copilot
[repo-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[mcp-spec]: https://modelcontextprotocol.io/
