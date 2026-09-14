---
title: "Ejercicio 6 - Validar la funcionalidad con MCP de Playwright"
description: "Conecta un navegador mediante MCP y compara el comportamiento de filtrado observado con la incidencia y el plan aprobado."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

La implementación de filtrado y la habilidad quality-checks ya tienen verificación automatizada. Ahora proporciona a Copilot un navegador y pídele que observe directamente la funcionalidad. Este ejercicio demuestra la interacción mediante **Model Context Protocol (MCP)**, no otra ejecución completa de la batería de pruebas.

Mantén el modo **Interactive** en la misma copia de trabajo y rama de filtrado. Configurar MCP no inicia un nuevo hito de funcionalidad.

## Qué aporta MCP

[MCP][mcp-overview] conecta un agente con herramientas y contexto externos mediante servidores. El servidor MCP de GitHub integrado permite a Copilot trabajar con incidencias y PR. El [servidor MCP de Playwright][playwright-mcp] proporciona herramientas de navegador para abrir páginas, examinar elementos accesibles, navegar e interactuar con controles.

La instantánea de accesibilidad del navegador ayuda al agente a identificar controles, pero no demuestra un cumplimiento completo de accesibilidad. Compara las acciones y observaciones reales con los requisitos de la incidencia en lugar de aceptar un «parece correcto» genérico.

> [!CAUTION]
> Trata un servidor MCP como una dependencia del proyecto: revisa quién lo publica, el código fuente, los permisos y cualquier descarga de paquetes antes de activarlo. Las directivas de la organización pueden restringir los servidores que pueden ejecutarse. No incluyas credenciales en configuración versionada ni apruebes herramientas desconocidas solo para terminar el ejercicio.

## Configurar MCP de Playwright

1. En la sesión de CLI existente, introduce `/mcp` para examinar los servidores configurados. Reutiliza una configuración de Playwright que funcione en lugar de añadir una duplicada.
2. Si hace falta, introduce `/mcp add` y utiliza <kbd>Tab</kbd> para desplazarte por el formulario.
3. Establece **Server Name** en `playwright`, **Server Type** en **STDIO** (o **Local**) y **Command** en `npx @playwright/mcp@latest --headless`.
4. Establece **Tools** en `*` para este servidor de navegador revisado. Esto hace disponibles sus herramientas; no sustituye los controles de permisos de CLI.
5. Tras revisar el paquete y su comando de inicio, pulsa <kbd>Ctrl</kbd>+<kbd>S</kbd> para guardar. El registro inicia el servidor y puede descargar el paquete; aprueba esta configuración de forma deliberada y responde a las solicitudes del paquete.
6. Introduce `/mcp show playwright` y confirma que el servidor está conectado y sus herramientas de navegador están disponibles.

El navegador sin interfaz gráfica no necesita una ventana de escritorio, lo que resulta adecuado para Codespaces. El flujo interactivo de adición guarda la configuración en `~/.copilot/mcp-config.json` y hace disponible el servidor sin reiniciar CLI. Es configuración del usuario, no un archivo que incluir en la PR de la funcionalidad. La [guía de configuración de MCP][mcp-setup] documenta los campos y las fuentes de configuración.

> [!NOTE]
> Las dependencias E2E del proyecto y el navegador de MCP están relacionados, pero pueden requerir configuraciones distintas. Si falta un navegador o una dependencia del sistema, examina el error real y resuelve ese requisito previo específico con aprobación. No instales navegadores automáticamente ni supongas que un servidor conectado demuestra que puede iniciar uno.

## Iniciar la aplicación correcta

Abre otra terminal en esta misma copia de trabajo de filtrado. Confirma el directorio y la rama y después inicia la aplicación:

```bash
pwd
git branch --show-current
npm run dev
```

Lee la URL local real en la salida del servidor. En el codespace, el servidor MCP y la aplicación se ejecutan en el mismo entorno, así que utiliza esa URL local, normalmente `http://localhost:4321`, en lugar de suponer que hace falta una URL de navegador reenviada.

Si el puerto está ocupado o Astro elige otro puerto, identifica a quién pertenece el servidor antes de continuar. No reutilices un servidor desconocido ni lo termines. Utiliza la URL del proceso que acabas de iniciar y mantén esa terminal abierta durante las pruebas.

## Observar el comportamiento de filtrado

Sustituye los marcadores por la URL real de la incidencia, las aclaraciones aprobadas en el Ejercicio 4 y la URL de la aplicación:

```plaintext
Utiliza el servidor MCP de Playwright configurado para validar la funcionalidad de filtrado frente a esta incidencia: <filtering-issue-URL>. Estas son las aclaraciones aprobadas durante la planificación: <pega las aclaraciones acordadas o escribe none>. La aplicación de esta copia de trabajo se está ejecutando en <local-app-URL>. Confirma la copia de trabajo, la rama y el servidor que se prueban antes de confiar en los resultados.

Abre la página de juegos, observa el estado sin filtros, selecciona una y después varias categorías, aplica un filtro de editor y combina las selecciones de categoría y editor. Prueba la limpieza de filtros y los resultados vacíos según los criterios aprobados. Comprueba las etiquetas de los controles, el funcionamiento con teclado y el foco visible. Compara los resultados mostrados con los filtros seleccionados y los datos de origen; no deduzcas que todo funciona solo porque haya cambiado un control.

Utiliza acciones reales de las herramientas del navegador e informa de lo observado para cada criterio, marcando claramente los fallos o las pruebas de verificación ausentes. No ejecutes otra batería completa de pruebas solo por este ejercicio de navegador, no cambies código de la aplicación, no crees pruebas o personalizaciones, no cambies de rama, no crees commits, no envíes cambios ni abras una PR. Pregunta antes de instalar algo o detener otro proceso.
```

Examina las llamadas a las herramientas del navegador y el informe. ¿Copilot realmente seleccionó varias categorías y las combinó con un editor? ¿Los juegos devueltos coinciden con el comportamiento acordado? ¿El informe distingue el comportamiento observable del navegador de la cobertura de la capa de datos y las pruebas automatizadas?

Si algo falla, registra el comportamiento observado. Autoriza por separado cualquier corrección específica de la aplicación y repite las comprobaciones de navegador y automatizadas afectadas. No cambies los criterios de aceptación para que coincidan con la implementación ni cuentes pruebas de ejecución antiguas como verificación del código modificado.

## Detener el servidor propio y continuar

Detén el servidor de desarrollo con <kbd>Ctrl</kbd>+<kbd>C</kbd> en la terminal donde lo iniciaste. Mantén disponible la configuración de MCP de Playwright. El Ejercicio 7 coordinará observaciones nuevas en el navegador y comprobaciones E2E automatizadas, que no deben reutilizar un servidor de desarrollo obsoleto ni la aplicación de otra copia de trabajo.

Mantén **Interactive** antes de crear el perfil de QA. Has observado el comportamiento del navegador sin crear otra PR o rama; a continuación, [crea y utiliza un agente de QA][next-lesson] para combinar requisitos, cobertura, la habilidad y las pruebas de verificación finales.

## Recursos

- [Añadir servidores MCP a Copilot CLI][mcp-setup] documenta la configuración y administración.
- [Microsoft Playwright MCP][playwright-mcp] documenta la configuración y las herramientas del navegador.
- [Registro MCP de GitHub][mcp-registry] enumera otros servidores que evaluar.

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-overview]: https://docs.github.com/copilot/concepts/context/mcp
[mcp-setup]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
[playwright-mcp]: https://github.com/microsoft/playwright-mcp
[mcp-registry]: https://github.com/mcp
