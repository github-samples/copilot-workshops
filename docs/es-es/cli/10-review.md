---
title: "Ejercicio 10 - Repaso y próximos pasos"
description: "Repasa el flujo de desarrollo compartido, los recursos reutilizables y los tres hitos de solicitudes de incorporación de cambios de CLI."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Has utilizado Copilot CLI para pasar de un cambio pequeño a una funcionalidad planificada con verificación reutilizable. La configuración de los Ejercicios 0–1 preparó tu entorno; los nueve módulos principales de los Ejercicios 2–10 enseñaron un flujo completo de desarrollo.

## Repasar los tres hitos de PR

| Hito | Resultado combinado | Hábito de revisión |
| --- | --- | --- |
| PR 1: valoraciones por estrellas | El `starRating` existente se muestra en las tarjetas de juegos, incluido `No rating yet` para `null` | Mantener el cambio acotado y verificar ambos casos |
| PR 2: instrucciones personalizadas | Una convención de documentación específica y una pequeña demostración en código real | Comprobar que las instrucciones mejoran código real, no solo ejemplos del chat |
| PR 3: filtrado y verificación | Filtrado, la habilidad quality-checks, el perfil de QA y las pruebas asociadas | Revisar todos los puntos de control, las pruebas de verificación actuales de QA y CI antes de combinar |

Las dos primeras PR se combinaron antes de iniciar el siguiente hito desde `main` actualizado. Los Ejercicios 4–8 compartieron una rama y una copia de trabajo. Los commits de puntos de control conservaron el progreso sin crear una PR por módulo. El ejercicio de controles no inició otra funcionalidad o PR.

## Repasar los recursos compartidos

Son los mismos resultados principales que los del [taller de la aplicación Copilot][app-workshop], alcanzados mediante una interfaz de terminal:

- **Las instrucciones del repositorio** explican el contexto y los estándares del proyecto; las instrucciones limitadas por ruta añaden detalles para los archivos pertinentes.
- **La implementación de filtrado y las pruebas** satisfacen la incidencia y las aclaraciones que aprobaste durante la planificación.
- **La habilidad quality-checks** reúne instrucciones reutilizables y scripts reales de shell que ejecutan las cuatro comprobaciones del proyecto.
- **La configuración de MCP de Playwright** proporciona herramientas de navegador para observación directa. En este flujo de CLI reside en la configuración del usuario, no en la PR de funcionalidad.
- **El agente personalizado de QA** define un rol reutilizable que parte de requisitos, comprueba cobertura, utiliza la habilidad y las herramientas de navegador e informa de resultados veraces.
- **La PR y las pruebas de verificación** conectan los cambios revisados con los resultados de pruebas, las observaciones de navegador, las limitaciones y CI.

Una habilidad es más que una lista de comandos y un perfil es más que un nombre de archivo. Has examinado los recursos generados, confirmado su ejecución real y seleccionado el agente personalizado antes de confiar en su informe.

## Distinguir las finalidades de validación

La planificación aclaró los requisitos antes de la implementación. Autopilot ejecutó ese plan acotado; volver a Interactive restableció puntos deliberados de revisión antes de crear personalizaciones.

La implementación utilizó las comprobaciones npm existentes antes de que existiera una habilidad. El ejercicio de la habilidad demostró que sus scripts incluidos y el reenvío de argumentos funcionaban. MCP demostró interacción directa con el navegador en lugar de repetir una batería completa. QA combinó criterios, cobertura, observaciones de navegador y las cuatro comprobaciones mediante la habilidad. La PR reutilizó resultados actuales de QA mientras CI comprobaba la revisión enviada.

Los fallos y bloqueos son resultados útiles. La ausencia de herramientas de navegador, las pruebas omitidas, los servidores obsoletos o un requisito sin resolver significan **NO-GO**, no permiso para rebajar el estándar. Añadir pruebas se justifica por carencias reales; no añadir ninguna es correcto cuando la cobertura existente es adecuada.

## Mantener estos hábitos

- Proporciona a Copilot la incidencia, el motivo del cambio y límites claros.
- Revisa los planes antes de aprobar trabajo autónomo.
- Examina instrucciones, habilidades y perfiles generados antes de ejecutarlos.
- Identifica la copia de trabajo, la rama, el servidor y la revisión a los que corresponde un resultado.
- Aplica la corrección más pequeña justificada y actualiza las pruebas de verificación tras los cambios.
- Mantén explícitas las instalaciones, las acciones destructivas, el uso compartido y las combinaciones de PR.

## Seguir aprendiendo

El [taller de la aplicación Copilot][app-workshop] alcanza los resultados compartidos mediante su interfaz gráfica y añade un hito de lienzo. El [taller de VS Code][vscode-workshop] y el [taller del agente en la nube][cloud-workshop] exploran otras formas de trabajar con agentes.

Utiliza [Awesome Copilot][awesome-copilot] para encontrar ejemplos de instrucciones, habilidades y agentes personalizados. Los [ejemplos de habilidades del Ejercicio 5][skill-examples] incluyen flujos de contribución, documentos de requisitos, diagramas y pruebas de navegador. Revisa los requisitos previos y el comportamiento antes de adoptar contenido de la comunidad.

Como referencia cotidiana, consulta la [referencia de comandos de CLI][cli-reference], la [documentación de habilidades de agente][agent-skills] y la [documentación de agentes personalizados][custom-agents]. Sigue experimentando con tareas acotadas y comparte solo material revisado mediante canales aprobados.

[previous-lesson]: ../9-slash-commands/
[app-workshop]: ../../app/
[vscode-workshop]: ../../vscode/
[cloud-workshop]: ../../cloud/
[skill-examples]: ../5-agent-skills/#ejemplos-adicionales-de-habilidades
[awesome-copilot]: https://github.com/github/awesome-copilot
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/concepts/agents/copilot-cli/about-custom-agents
