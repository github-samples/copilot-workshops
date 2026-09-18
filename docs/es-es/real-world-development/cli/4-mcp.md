---
title: "Ejercicio 4 - Probar tu funcionalidad con el servidor MCP de Playwright"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Acabas de generar la funcionalidad de filtrado con Copilot CLI. Antes de abrir una pull request, deberías confirmar que funciona en el navegador. En lugar de recorrer la aplicación manualmente, conectarás el **servidor MCP de Playwright** y dejarás que Copilot controle un navegador real para probar la funcionalidad por ti.

En este ejercicio vas a:

- comprender qué es Model Context Protocol (MCP) y cómo amplían los servidores MCP las capacidades de Copilot CLI.
- añadir el servidor MCP de Playwright a Copilot CLI.
- pedir a Copilot que lo use para probar manualmente tu funcionalidad de filtrado en un navegador.

## ¿Qué es Model Context Protocol (MCP)?

[Model Context Protocol (MCP)](https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/) proporciona a los agentes de IA una forma de comunicarse con herramientas y servicios externos. Al usar MCP, los agentes de IA pueden comunicarse con herramientas y servicios externos en tiempo real. Esto les permite acceder a información actualizada (mediante recursos) y realizar acciones en tu nombre (mediante herramientas).

Se accede a estas herramientas y recursos a través de un servidor MCP, que actúa como puente entre el agente de IA y las herramientas y servicios externos. El servidor MCP se encarga de gestionar la comunicación entre el agente de IA y las herramientas externas (como API existentes o herramientas locales como paquetes de NPM). Cada servidor MCP representa un conjunto distinto de herramientas y recursos a los que el agente de IA puede acceder.

Algunos servidores MCP populares ya existentes son:

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**: este servidor proporciona acceso a un conjunto de API para gestionar tus repositorios de GitHub. Permite al agente de IA realizar acciones como crear repositorios nuevos, actualizar los existentes y gestionar incidencias y pull requests.
- **[Playwright MCP Server](https://github.com/microsoft/playwright-mcp)**: este servidor proporciona capacidades de automatización del navegador mediante Playwright. Permite al agente de IA realizar acciones como navegar por páginas web, rellenar formularios y seleccionar botones.

Hay muchos otros servidores MCP disponibles que proporcionan acceso a distintas herramientas y recursos. GitHub aloja un [registro de MCP](https://github.com/mcp) para mejorar la visibilidad y las contribuciones al ecosistema.

> [!CAUTION]
> En términos de seguridad, trata los servidores MCP como tratarías cualquier otra dependencia de tu proyecto. Antes de usar un servidor MCP, revisa cuidadosamente su código fuente, verifica el publicador y valora las implicaciones de seguridad. Usa solo servidores MCP en los que confíes y ten cuidado al conceder acceso a recursos u operaciones sensibles.

> [!NOTE]
> El [servidor GitHub MCP][github-mcp-server] está **integrado** en Copilot CLI: ya está disponible sin ninguna configuración, y así es como Copilot ha estado leyendo y escribiendo en tu repositorio durante todo el taller. En este ejercicio añadirás un *segundo* servidor, Playwright, para darle a Copilot un navegador.

## Añadir el servidor MCP de Playwright

La forma más rápida de añadir un servidor es el comando interactivo `/mcp add`. Registrarás el [servidor MCP de Playwright][playwright-mcp-server], que proporciona a Copilot un navegador que puede controlar.

> [!TIP]
> **Inicia una sesión de Copilot CLI**
>
> Antes de empezar los ejercicios siguientes, vuelve a tu codespace y abre un terminal (<kbd>Ctrl</kbd>+<kbd>\`</kbd> si no hay ninguno abierto). Después, inicia Copilot CLI con `--yolo` y `--enable-all-github-mcp-tools`:
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> Para retomar la sesión más reciente de este proyecto en lugar de empezar desde cero, ejecuta `copilot --yolo --enable-all-github-mcp-tools --continue`. Si Copilot CLI ya se está ejecutando desde un ejercicio anterior, envía `/clear` para empezar una conversación limpia.
>
> `--enable-all-github-mcp-tools` habilita las herramientas GitHub MCP de lectura y escritura para la sesión actual, de modo que Copilot pueda leer tu backlog y abrir pull requests durante el flujo del taller.

> [!CAUTION]
> `--yolo` habilita permisos automáticos completos (`--allow-all-tools`, `--allow-all-paths` y `--allow-all-urls`). Úsalo solo en un entorno aislado, como un Codespace o una máquina virtual, y no lo configures nunca como alias predeterminado para el desarrollo diario. Consulta [Allowing and denying tool use][allow-all-warning] para más información.

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools

1. En tu sesión de Copilot CLI, introduce:

    ```text
    /mcp add
    ```

2. Aparecerá un formulario de configuración. Usa <kbd>Tab</kbd> para desplazarte por los campos y complétalo de esta forma:

    - **Server Name**: `playwright`
    - **Server Type**: selecciona **Local** (también aparece como **STDIO**)
    - **Command**: `npx @playwright/mcp@latest --headless`
    - **Tools**: déjalo en `*` para permitir todas las herramientas del servidor

3. Pulsa <kbd>Ctrl</kbd>+<kbd>S</kbd> para guardar. El servidor se añade y queda disponible de inmediato; no hace falta reiniciar nada.

La opción `--headless` indica a Playwright que ejecute el navegador sin una ventana visible, lo que es necesario dentro de un codespace donde no hay un escritorio para mostrarlo. Internamente, esto escribe el servidor en tu archivo `~/.copilot/mcp-config.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "type": "local",
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--headless"],
      "tools": ["*"]
    }
  }
}
```

4. Confirma que el servidor está registrado y activo mostrando la lista de servidores MCP:

    ```text
    /mcp show
    ```

5. Deberías ver `playwright` en la lista junto con el servidor `github` integrado.

> [!NOTE]
> El proyecto Tailspin Toys ya usa Playwright para sus pruebas end-to-end, así que normalmente el navegador que Playwright necesita ya está instalado. Si Copilot informa más adelante de que falta un navegador, pídele que ejecute `npx playwright install chromium` y vuelve a intentarlo.

## Iniciar el sitio web

El servidor MCP de Playwright necesita una aplicación en ejecución sobre la que probar. Inicia el servidor de desarrollo de Astro en un terminal **independiente** para que siga ejecutándose mientras trabajas en Copilot CLI.

1. Abre un terminal nuevo en tu codespace pulsando <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
2. Inicia el sitio web:

    ```bash
    npm run dev
    ```

3. Deja este terminal en ejecución. Cuando veas el banner `Astro server: http://localhost:4321`, la aplicación estará lista.

## Probar la funcionalidad de filtrado

Vuelve a tu sesión de Copilot CLI y pídele a Copilot que pruebe la funcionalidad.

El [servidor MCP de Playwright][playwright-mcp-server] le da a Copilot un navegador real que puede controlar. En lugar de que tengas que recorrer manualmente la aplicación para comprobar tu trabajo, el agente puede abrir una página, navegar, aplicar filtros y devolverte el resultado, para luego resumirte lo que ha visto. Es la forma más rápida de confirmar que una funcionalidad se comporta como esperas sin salir de la conversación.

Internamente, el servidor MCP de Playwright trabaja a partir del [árbol de accesibilidad][playwright-mcp-server] de la página, en lugar de usar capturas de pantalla. Eso significa que el agente razona sobre elementos estructurados y etiquetados (botones, enlaces, elementos de lista) de la misma forma que lo hace la tecnología de asistencia, así que una comprobación funcional rápida también sirve como verificación básica de accesibilidad.

Con el servidor conectado y la aplicación en ejecución, pídele a Copilot que ejercite la funcionalidad de filtrado que acabas de crear:

```text
Using the Playwright MCP server, open a browser to the running app at http://localhost:4321 and verify the new game filtering feature:

1. Go to the games page and note how many games are listed.
2. Apply a category filter and confirm the list updates to only show games in that category.
3. Clear it, then apply a publisher filter and confirm the list updates to that publisher.
4. Combine a category and a publisher filter and confirm the results respect both.

Report what you observe at each step, and call out anything that does not behave as expected.
```

Copilot iniciará un navegador a través del servidor MCP de Playwright, recorrerá cada paso y te informará de lo que ha encontrado. Lee su resumen comparándolo con los criterios de aceptación de la incidencia. Si algo no parece correcto, haz preguntas de seguimiento o pídele que vuelva a corregir el código antes de abrir una pull request.

> [!NOTE]
> La aplicación debe estar ejecutándose en `http://localhost:4321` para esta prueba. Si has detenido el servidor de desarrollo, vuelve a iniciarlo antes de enviar el prompt. La primera vez que Copilot use el servidor MCP de Playwright puede que necesite descargar un navegador; si informa de que falta uno, pídele que ejecute `npx playwright install chromium` y vuelve a intentarlo.

[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp

## Resumen y siguientes pasos

¡Enhorabuena! Has usado el servidor MCP de Playwright para probar manualmente tu funcionalidad con Copilot CLI. En resumen:

- has aprendido qué es Model Context Protocol (MCP) y cómo amplían los servidores MCP las capacidades de Copilot CLI.
- has añadido el servidor MCP de Playwright con `/mcp add`.
- has pedido a Copilot que controle un navegador y verifique tu funcionalidad de filtrado antes de publicarla.

Ahora que has confirmado que la funcionalidad funciona, puedes continuar con el siguiente ejercicio, en el que [abrirás una pull request con la ayuda de una habilidad de agente][next-lesson].

## Recursos

- [¿Qué demonios es MCP y por qué todo el mundo habla de ello?][mcp-blog-post]
- [Servidor MCP de Playwright de Microsoft][playwright-mcp-server]
- [Añadir servidores MCP para Copilot CLI][cli-add-mcp]
- [Servidor MCP de GitHub][github-mcp-server]

[previous-lesson]: ../3-generating-code/
[next-lesson]: ../5-agent-skills/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[github-mcp-server]: https://github.com/github/github-mcp-server
[cli-add-mcp]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
