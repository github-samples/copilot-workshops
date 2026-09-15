---
title: "Ejercicio 1 - Instalar GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

[GitHub Copilot CLI][about-copilot-cli] es un potente asistente de programación con agentes que se ejecuta en tu terminal y te permite explorar bases de código, generar código, ejecutar comandos e interactuar con herramientas externas, todo desde la línea de comandos. Te permite delegar tareas, solicitar cambios y mantener la concentración. Como imaginarás, el primer paso es instalar la herramienta. Por suerte, puedes hacerlo con herramientas que ya conoces.

En este ejercicio aprenderás a:

- instalar GitHub Copilot CLI con npm.
- autenticarte con tu cuenta de GitHub.
- verificar la instalación.

## Escenario

Tu equipo está empezando a usar agentes de IA para gestionar un backlog cada vez mayor. Copilot CLI lleva esa capacidad a la terminal, donde muchos desarrolladores ya trabajan habitualmente. Este ejercicio te ayudará a instalarlo, autenticarte y dejarlo listo para usarlo durante el resto del taller.

## Abrir un terminal en tu codespace

Antes de instalar Copilot CLI, tienes que abrir una ventana de terminal en tu codespace.

1. Vuelve a tu codespace y espera a que termine su configuración.
2. Abre una ventana de terminal pulsando <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
3. Deberías ver un panel de terminal en la parte inferior de la ventana de VS Code.

## Confirmar el entorno del participante

En la terminal del codespace, confirma que estás en tu propio repositorio Tailspin Toys, no en el repositorio de contenido del taller. Lee su `README.md` y `package.json` para conocer la configuración y los comandos de comprobación. Tailspin Toys requiere actualmente Node.js 22.13 o posterior, las dependencias del proyecto y Chromium de Playwright para las pruebas E2E.

```bash
pwd
git remote -v
node --version
gh auth status
```

GitHub CLI (`gh`) te ayudará a examinar PR y CI. Si falta autenticación, utiliza `gh auth login` y sigue sus instrucciones del navegador. Confirma que tu cuenta puede enviar ramas y crear y combinar PR en este repositorio; las directivas de la organización pueden exigir otro revisor. Resuelve los requisitos previos ausentes siguiendo las instrucciones de configuración del repositorio antes de cambiar código y revisa cualquier instalación antes de autorizarla.

CLI se ejecuta sobre la copia de trabajo desde la que lo inicias; empezar una conversación no crea automáticamente un worktree aislado. Este taller utiliza una rama por hito de PR. Primero combinarás las valoraciones por estrellas y la demostración de instrucciones, y después mantendrás la misma rama de filtrado durante los Ejercicios 4–8.

## Instalar Copilot CLI

Puedes instalar Copilot CLI mediante [npm][install-npm], [WinGet][install-winget] y [Homebrew][install-homebrew]. Como GitHub Codespaces incluye Node.js preinstalado, usarás npm para instalar Copilot CLI.

1. En el terminal, comprueba que Node.js está instalado y que cumple el requisito de versión:

   ```bash
   node --version
   ```

   Tailspin Toys requiere la versión 22.13 o posterior, aunque el requisito de CLI sea distinto. Sigue las instrucciones de configuración del repositorio del participante si tu versión es demasiado antigua.

2. Instala Copilot CLI globalmente en el codespace con npm:

   ```bash
   npm install -g @github/copilot
   ```

3. Verifica la instalación consultando la versión:

   ```bash
   copilot --version
   ```

   Deberías ver el número de versión mostrado (por ejemplo, `v1.0.XX`).

> [!NOTE]
> Si la instalación falla por un error de permisos, examina la configuración de npm o pide ayuda a la persona que dirige el taller en lugar de volver a ejecutar un comando desconocido con privilegios elevados.

## Autenticarse con GitHub

La primera vez que lo inicies, Copilot CLI te pedirá que te autentiques con tu cuenta de GitHub.

1. Inicia Copilot CLI:

   ```bash
   copilot
   ```

2. Si no has iniciado sesión todavía, verás un mensaje para autenticarte. Copilot CLI mostrará un código de dispositivo y te pedirá que visites una URL.
3. Sigue las instrucciones en pantalla:
   - Abre en el navegador la URL proporcionada
   - Introduce el código de dispositivo cuando se te solicite
   - Autoriza a Copilot CLI para acceder a tu cuenta de GitHub
4. Una vez autenticado, verás el prompt de Copilot CLI listo para aceptar tus preguntas y comandos.

> [!NOTE]
> En un codespace, es posible que ya estés autenticado a través de tu sesión de GitHub. Si Copilot CLI se inicia sin pedir autenticación, ya está todo listo.

## Confiar en el directorio y verificar que todo funciona

Ahora que estás en el prompt de Copilot CLI por primera vez, vamos a marcar como fiable este repositorio del taller y a comprobar que Copilot CLI está correctamente instalado y conectado.

1. Cuando Copilot CLI te pida que confirmes que confías en los archivos de esta carpeta, verás tres opciones:
   - **Yes, proceed**: confiar solo durante esta sesión
   - **Yes, and remember this folder for future sessions**: confiar de forma permanente
   - **No, exit (Esc)**: no permitir el acceso a los archivos
2. Para este taller, selecciona **Yes, and remember this folder for future sessions**, ya que trabajarás en este repositorio durante toda la sesión.
3. Haz a Copilot una pregunta sencilla para verificar que funciona:

   ```plaintext
   ¿Qué archivos hay en este proyecto?
   ```

4. Copilot debería explorar el repositorio y ofrecer un resumen de la estructura del proyecto.
5. Prueba el comando `/help` para ver los comandos de barra disponibles:

   ```text
   /help
   ```

6. Sal de esta sesión introduciendo el siguiente comando en el prompt de Copilot. Iniciarás una sesión nueva para el primer cambio.

   ```text
   /exit
   ```

## Comprender modos y permisos

Copilot CLI trabaja en el directorio y la rama de Git donde lo inicias. Confiar en un directorio le permite utilizar el contexto del repositorio; no equivale a aprobar todas las acciones de herramientas. Revisa las solicitudes de permiso para cambios de archivos, comandos de shell y operaciones de GitHub.

Inicia los ejercicios de código desde la raíz del repositorio del participante con:

```bash
copilot --enable-all-github-mcp-tools
```

El servidor MCP de GitHub está integrado. Esta opción expone todas sus herramientas para trabajar con incidencias y PR; la autenticación, los permisos del repositorio y las aprobaciones de herramientas siguen siendo necesarios. No autoriza un commit ni una PR por sí sola.

Utiliza <kbd>Shift</kbd>+<kbd>Tab</kbd> para alternar entre los modos estándar **Interactive**, **Plan** y **Autopilot**. Comprueba el indicador de modo antes de enviar una solicitud. Mantendrás Interactive para los primeros cambios, planificarás el filtrado antes de crearlo y volverás explícitamente a Interactive antes de crear y revisar personalizaciones.

> [!CAUTION]
> Los ajustes de modo y permisos son distintos. Autopilot continúa trabajando de forma autónoma; `--allow-all` y su alias `--yolo` conceden todos los permisos de herramientas, rutas y URL. Este taller no exige iniciar todas las sesiones con permisos ilimitados. Revisa el alcance antes de conceder acceso, incluso dentro de un codespace.

## Resumen y siguientes pasos

¡Enhorabuena! Has instalado y autenticado GitHub Copilot CLI correctamente. Has aprendido a:

- instalar Copilot CLI con npm.
- autenticarte con tu cuenta de GitHub.
- confiar en un directorio para que Copilot CLI pueda trabajar con él.
- verificar que la instalación funciona correctamente.

Ahora que Copilot CLI está instalado, realiza un cambio pequeño y revisable en el [Ejercicio 2 - Añadir valoraciones por estrellas: una mejora rápida][next-lesson].

## Recursos

- [Instalar GitHub Copilot CLI][install-copilot-cli]
- [Acerca de Copilot CLI][about-copilot-cli]
- [Usar Copilot CLI][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
