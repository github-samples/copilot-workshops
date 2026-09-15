---
title: "Lección 1 - Instalar la aplicación GitHub Copilot"
description: "Instala la aplicación GitHub Copilot, conecta el repositorio que has creado a partir de la plantilla, familiarízate con el espacio de trabajo y prueba un chat rápido."
authors:
  - geektrainer
lastUpdated: 2026-07-09
---

La [**aplicación GitHub Copilot**][about-copilot-app] es una aplicación de escritorio para el desarrollo dirigido por agentes. Se basa en GitHub Copilot CLI y se integra de forma nativa con GitHub, por lo que los repositorios, las ramas y las canalizaciones de CI funcionan sin configuración adicional. Está diseñada para flujos de trabajo en los que diriges varios agentes en paralelo, cada uno en su propio espacio de trabajo aislado, en lugar de realizar todo el trabajo y automatizar las tareas repetitivas por tu cuenta. Con Node.js instalado y tu copia del proyecto preparada, el siguiente paso es instalar la aplicación y conectar ese repositorio.

En esta lección:

- instalarás la aplicación GitHub Copilot e iniciarás sesión.
- añadirás el proyecto a la aplicación desde su repositorio de GitHub.
- conocerás el espacio de trabajo, incluida la lista de trabajo pendiente que la plantilla ha creado para ti.
- probarás un chat rápido para obtener información sobre la propia aplicación.

## Escenario

Tu equipo está adoptando agentes de IA para abordar una lista creciente de trabajo pendiente. La aplicación Copilot ofrece un único lugar desde el que dirigir ese trabajo: seleccionar incidencias, ejecutar agentes, revisar cambios y combinar solicitudes de incorporación de cambios. En esta lección instalarás y conectarás la aplicación, y aprenderás a iniciar una conversación sobre el proyecto.

> [!NOTE]
> Se requiere un plan de Copilot válido: Copilot Student o cualquier plan de pago (Pro, Pro+, Business o Enterprise). Si utilizas Copilot Business o Copilot Enterprise, el administrador debe habilitar la directiva **Copilot CLI** para que la aplicación funcione.

## Instalar y configurar la aplicación GitHub Copilot

Como cabe esperar, el primer paso para utilizar la aplicación GitHub Copilot es instalarla. Hay versiones disponibles para Windows, macOS y Linux. Vamos a instalar la aplicación, autenticarnos y añadir a ella nuestro repositorio de Tailspin Toys.

1. En un navegador, abre la [página de inicio de la aplicación GitHub Copilot][download-app].
2. Descarga la aplicación para tu plataforma e instálala siguiendo las instrucciones de la página.
3. Abre la aplicación después de instalarla.
4. Selecciona **Sign in to GitHub** y sigue las indicaciones para autenticarte. Si utilizas GitHub Enterprise Server, elige **Use GitHub Enterprise** e introduce la dirección del servidor cuando se solicite.
5. Después de autenticarte, se te pedirá que conectes los repositorios. Selecciona el repositorio de Tailspin Toys que acabas de crear, cuyo nombre debería ser `<YOUR_GITHUB_HANDLE>/tailspin-toys`.
6. Selecciona **Continue** para continuar con la incorporación.
7. Cuando se te pida que elijas un tema, selecciona el que más te guste y, después, selecciona **Finish**.

> [!NOTE]
> Si tu copia de Tailspin Toys no aparece automáticamente en la lista, puedes añadirla tras completar el proceso de incorporación en la aplicación. Al finalizar, la aplicación Copilot mostrará la pantalla de inicio. Desde allí, selecciona **Choose from GitHub**, busca el repositorio por su nombre (\<YOUR_GITHUB_HANDLE\>/tailspin-toys) y selecciónalo. El repositorio se añadirá a la aplicación Copilot.

## Familiarizarse con el espacio de trabajo

Con el proyecto conectado, dedica un momento a conocer el espacio de trabajo. La aplicación organiza todo en varias áreas de la barra lateral:

- **Sessions**: donde los agentes realizan su trabajo. En este taller, elige **new working tree** para que cada hito de PR tenga una copia de trabajo y una rama aisladas. Existen otras opciones de espacio de trabajo, pero no se utilizan aquí.
- **Quick chats**: conversaciones ligeras para preguntas y lluvias de ideas que no necesitan una rama ni un espacio de trabajo propios. Probarás una al final de esta lección.
- **My work**: tus incidencias y solicitudes de incorporación de cambios, disponibles mediante la **integración nativa con GitHub** de la aplicación. Desde aquí puedes examinar y filtrar incidencias y solicitudes de incorporación de cambios, comprobar el estado de CI, iniciar una sesión a partir de una incidencia y revisar solicitudes de incorporación de cambios, todo ello sin salir de la aplicación.
- **Customize**: descubre y gestiona servidores MCP, habilidades y lienzos. Lo utilizarás para configurar MCP de Playwright.
- **Automations**: tareas de agente guardadas que se ejecutan según una programación o bajo demanda. El resumen final enlaza a ellas como siguiente paso, no como otro ejercicio del taller.

### Localizar la lista de trabajo pendiente inicial

Como la aplicación se integra de forma nativa con GitHub, el trabajo pendiente del repositorio aparece directamente en ella. Cuando creaste el repositorio a partir de la plantilla, se generó una lista de incidencias. Vamos a comprobar que esté disponible.

1. Selecciona **My work** en la barra lateral.
2. Busca estas incidencias por su título en lugar de dar por hecho su número:

   - Allow users to filter games by category and publisher
   - Update our repository coding standards

3. Selecciona una incidencia para leer sus detalles. Cada incidencia también sirve como punto de partida para una sesión de agente. Más adelante iniciarás el trabajo desde estas incidencias. Las demás incidencias pendientes aportan contexto al lienzo, no son otra tarea de implementación.

> [!NOTE]
> La lista de elementos de **My work** se filtra automáticamente para mostrar solo los elementos de los repositorios que has añadido a la aplicación Copilot. Para ver elementos de trabajo de otros repositorios, añádelos a la aplicación.

## Probar un chat rápido

Una buena forma de familiarizarse con la aplicación es utilizarla para conocer la *propia aplicación*, y un **chat rápido** es la herramienta adecuada. Los chats rápidos permiten formular una pregunta o plantear ideas sin crear una rama ni un árbol de trabajo, por lo que son perfectos para una consulta rápida y desechable que no requiere una sesión.

1. En la barra lateral, selecciona **+** junto a **Quick chats** para abrir un chat nuevo.
2. Pregunta a la aplicación cómo funcionan sus sesiones:

   ```plaintext
   ¿Cómo utiliza la aplicación GitHub Copilot los worktrees?
   ```

3. Lee la respuesta en la vista de conversación. Verás que cada sesión se ejecuta en su propio árbol de trabajo de Git aislado, lo que permite ejecutar varios agentes en paralelo sin que sus cambios entren en conflicto. Puedes continuar la conversación o iniciar un chat nuevo en cualquier momento.

## Resumen y pasos siguientes

Has instalado la aplicación GitHub Copilot, conectado el proyecto y explorado el espacio de trabajo. Has aprendido a:

- instalar la aplicación e iniciar sesión en GitHub.
- añadir un proyecto desde su repositorio de GitHub.
- familiarizarte con el espacio de trabajo y localizar la lista de trabajo pendiente inicial en **My work**.
- utilizar un chat rápido para formular una pregunta breve y desechable.

## Mantener separados los hitos de PR

Combinarás cuatro PR: valoraciones por estrellas; instrucciones con una pequeña demostración; filtrado con la habilidad, el perfil QA y las pruebas; y, por último, el lienzo de clasificación de incidencias. Utiliza una rama por hito de PR. Las Lecciones 4–8 permanecen en la misma sesión, worktree y rama de filtrado, con commits de control en lugar de PR adicionales.

Un worktree nuevo de la aplicación puede partir de un estado local desactualizado. Antes de editar archivos en cada hito nuevo, obtén los cambios del repositorio y actualiza la rama de la nueva sesión mediante un avance rápido hasta el último `origin/main`. Las lecciones siguientes lo muestran explícitamente. No apiles ramas, no selecciones commits de trabajos anteriores mediante cherry-pick ni cambies una sesión de filtrado activa a otra rama.

A continuación, iniciarás tu primera sesión de agente y realizarás el primer cambio en el proyecto: mostrar una valoración por estrellas en las tarjetas de los juegos. Continúa con la [Lección 2 - Añadir valoraciones por estrellas: una mejora rápida][next-lesson].

## Recursos

- [Acerca de la aplicación GitHub Copilot][about-copilot-app]
- [Introducción a la aplicación GitHub Copilot][getting-started]
- [Trabajar con sesiones de agente en la aplicación GitHub Copilot][agent-sessions]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[download-app]: https://gh.io/app