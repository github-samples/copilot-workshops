---
title: "Ejercicio 9 - Explorar comandos de barra y opciones de CLI"
description: "Examina el contexto y los controles de modelos y sesiones, revisa los destinos para compartir y explora opciones de CLI sin iniciar otra funcionalidad."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Los tres hitos de PR están completos. Ahora explora los controles de CLI que te ayudan a comprender y gestionar una sesión. Este ejercicio no implementa otra funcionalidad, no delega trabajo ni abre otra PR.

Desde la copia de trabajo actualizada del participante, inicia `copilot` en modo **Interactive**. Utiliza `/help` y la [referencia de comandos][cli-reference] para confirmar los comandos que admite tu versión instalada; la documentación actual puede describir controles más recientes que tu instalación.

## Examinar el contexto y la información de sesión

1. Envía una solicitud acotada de solo lectura:

   ```plaintext
   Resume los archivos de instrucciones del repositorio, la habilidad quality-checks y el perfil de QA. Explica cómo ayudan a verificar el filtrado. No modifiques archivos, no ejecutes comprobaciones, no delegues trabajo, no crees commits ni abras una PR.
   ```

2. Introduce `/context` para examinar el uso de la ventana de contexto. Observa cómo los mensajes, las instrucciones y las definiciones de herramientas consumen contexto.
3. Introduce `/compact` y después `/context` de nuevo. La compactación resume el historial para reducir su tamaño; una sesión corta puede mostrar pocos cambios.
4. Introduce `/session` para examinar la sesión actual y `/usage` para consultar la información de uso.

La compactación no sustituye la aportación de requisitos. Al cambiar de tarea o agente, proporciona explícitamente la URL de la incidencia, los criterios aprobados, la identidad de la copia de trabajo y las pruebas de verificación pertinentes.

`/clear` inicia una conversación nueva; no deshace archivos ni cambia de rama de Git. `/resume` abre el selector de sesiones para volver a un trabajo anterior. Explora el selector y pulsa <kbd>Esc</kbd> para salir sin reanudar otra tarea. No borres la única copia de los criterios de aceptación ni supongas que reanudar una conversación significa que su verificación anterior sigue vigente.

## Examinar modelos y modos

Introduce `/model` para examinar los modelos disponibles para tu cuenta, incluido **Auto** donde se ofrezca. Lee los detalles de selección y la información de uso; la disponibilidad y los precios de los modelos pueden cambiar. Pulsa <kbd>Esc</kbd> para salir del selector sin cambiar de modelo. Si lo cambias, confirma la selección mostrada y el alcance que aplica tu versión de CLI.

Utiliza <kbd>Shift</kbd>+<kbd>Tab</kbd> para examinar el indicador de modo al alternar entre **Interactive**, **Plan** y **Autopilot**, y vuelve después a **Interactive** sin enviar una indicación de implementación. Recuerda la diferencia:

- Plan sirve para acordar el trabajo antes de programar.
- Autopilot continúa una tarea aprobada y acotada.
- Interactive proporciona puntos deliberados de revisión y decisión.
- Los permisos controlan por separado qué acciones de herramientas están permitidas.

## Examinar opciones de línea de comandos

En otra terminal, ejecuta:

```bash
copilot --help
```

Compara estas opciones documentadas con la ayuda de tu versión instalada:

| Opción | Finalidad |
| --- | --- |
| `--model MODEL` | Elegir el modelo para una invocación; confirma primero su disponibilidad |
| `--agent AGENT` | Seleccionar un agente personalizado para una invocación |
| `-p PROMPT` | Ejecutar una indicación de forma programática y salir cuando termine |
| `--output-format json` | Emitir salida JSONL estructurada, un objeto JSON por línea |
| `--resume` | Reanudar una sesión existente |
| `--enable-all-github-mcp-tools` | Exponer el conjunto completo de herramientas MCP de GitHub integradas |

Son controles que comprender, no otra tarea que iniciar. El modo programático puede ejecutar acciones reales de herramientas; un formato de salida JSON no convierte una solicitud en solo lectura. La selección del agente sigue el flujo verificado del [Ejercicio 7][qa-lesson], no es una razón para sustituir la activación del agente personalizado por una petición al agente predeterminado para que lea el perfil. Los permisos y el acceso siguen siendo necesarios.

## Revisar antes de compartir

`/share` puede enviar el contenido de la sesión a distintos destinos. La [referencia de comandos de CLI][cli-reference] documenta `/share file [session|research] [PATH]` para exportar Markdown y `/share gist [session|research]` para publicar un gist. Sin subcomando, el comportamiento documentado actualmente crea un enlace de GitHub para compartir cuando hay una sesión iniciada y sincronizada, y recurre a una exportación Markdown en caso contrario. No ejecutes el comando sin argumentos suponiendo que solo muestra una vista previa.

Para este taller, selecciona explícitamente una exportación local de la sesión y un nombre de archivo en lugar de publicar:

```text
/share file session cli-session-review.md
```

Abre el archivo exportado en el editor y examina lo que contiene realmente. Revisa indicaciones, respuestas, salida de herramientas, rutas de archivo, datos del repositorio y cualquier credencial o información personal. No supongas que la exportación contiene todos los pasos internos ni que ha eliminado automáticamente el contenido sensible.

> [!CAUTION]
> Un gist o un enlace compartido supone divulgar información fuera del entorno. Un gist secreto no proporciona control de acceso privado: cualquiera que tenga su URL puede verlo. Confirma el destino, los destinatarios, los permisos y la directiva de tu organización antes de compartir. Si hace falta ocultar información, comparte solo el archivo revisado y depurado mediante un canal aprobado; no publiques después la sesión original.

Mantén esta exportación fuera de la PR de funcionalidad y del historial del repositorio. Tras examinarla, elimina el archivo que acabas de generar o muévelo a la ubicación local de notas aprobada. No elimines archivos ajenos.

La delegación en la nube puede crear trabajo remoto y una PR adicional, así que no ejecutes `/delegate` aquí. El [taller del agente en la nube][cloud-workshop] cubre ese flujo independiente.

## Resumen y pasos siguientes

Has examinado el contexto, el uso, los controles de modelos y modos, las opciones de línea de comandos y los destinos para compartir sin iniciar otra funcionalidad. Continúa con el [Ejercicio 10 - Repaso y próximos pasos][next-lesson] para revisar el flujo y los recursos que has creado.

[previous-lesson]: ../8-create-pull-request/
[next-lesson]: ../10-review/
[qa-lesson]: ../7-qa-agent/
[cloud-workshop]: ../../cloud/
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
