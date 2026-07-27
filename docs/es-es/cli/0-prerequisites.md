---
title: "Ejercicio 0: Requisitos previos"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Antes de empezar los ejercicios de Copilot CLI, tienes que dejarlo todo preparado. Crearás tu propia copia del repositorio Tailspin Toys y pondrás en marcha un [codespace][codespaces], cuyo terminal integrado usarás para instalar y ejecutar Copilot CLI en el siguiente ejercicio.

## Configurar el repositorio del laboratorio

Para crear una copia del repositorio para el código que vas a crear, generarás una instancia a partir de la [plantilla][template-repository]. La nueva instancia contendrá todos los archivos necesarios para el laboratorio y la usarás a medida que avances por los ejercicios.

1. En una nueva ventana del navegador, ve al repositorio de GitHub de este laboratorio: `https://github.com/github-samples/tailspin-toys`.
2. Crea tu propia copia del repositorio seleccionando el botón **Use this template** en la página del repositorio del laboratorio. Después, selecciona **Create a new repository**.

    ![Captura del botón Use this template](../../_images/ex0-use-template.png)

3. Si estás realizando el taller como parte de un evento dirigido por GitHub o Microsoft, sigue las instrucciones proporcionadas por el personal mentor. En caso contrario, puedes crear el nuevo repositorio en una organización en la que tengas acceso a GitHub Copilot.

    ![Captura de la configuración de la plantilla del repositorio](../../_images/ex0-repository-settings.png)

4. Anota la ruta del repositorio que has creado (**nombre-de-organización-o-usuario/nombre-del-repositorio**), ya que la consultarás más adelante en el laboratorio.

> [!NOTE]
> **Tu backlog está listo**
>
> Cuando creas tu repositorio a partir de la plantilla, se crea automáticamente un backlog de incidencias de GitHub para ti. Trabajarás con esas incidencias durante todo el taller; no tienes que crear ninguna por tu cuenta.

## Crear un codespace

Ahora usarás un codespace para completar los ejercicios del laboratorio.

[GitHub Codespaces][codespaces] es un entorno de desarrollo en la nube que te permite escribir, ejecutar y depurar código directamente en el navegador. Proporciona un IDE con todas las funciones y compatibilidad con varios lenguajes de programación, extensiones y herramientas.

1. Ve a tu repositorio recién creado.
2. Selecciona el botón verde **Code**.

    ![Botón Code](../../_images/ex0-code-button.png)

3. Selecciona la pestaña **Codespaces** y, a continuación, selecciona el botón **+** para crear un Codespace nuevo.

    ![Crear un codespace nuevo](../../_images/ex0-create-codespace.png)

La creación del codespace tardará varios minutos, aunque sigue siendo mucho más rápida que instalar manualmente todos los servicios. Dicho esto, puedes aprovechar este tiempo para explorar otras funciones de GitHub Copilot, a las que prestaremos atención a continuación.

> [!CAUTION]
> Volverás al codespace en un ejercicio posterior. De momento, déjalo abierto en una pestaña del navegador.

> [!NOTE]
> Este taller está diseñado para ejecutarse dentro de un codespace o de un [contenedor de desarrollo][dev-containers] local. Ambos garantizan que el entorno tenga instalados todos los requisitos previos necesarios para disfrutar de una experiencia fluida. Si prefieres ejecutarlo en local, abre el repositorio clonado en VS Code y selecciona **Reopen in Container** cuando se te solicite; VS Code compilará el mismo contenedor de desarrollo que usa el codespace.

[codespaces]: https://github.com/features/codespaces
[dev-containers]: https://code.visualstudio.com/docs/devcontainers/containers

## Resumen

¡Enhorabuena! Has creado una copia del repositorio del laboratorio. También has iniciado el proceso de creación de tu codespace, que usarás cuando empieces a trabajar con Copilot CLI.

## Siguiente paso

Vamos a instalar Copilot CLI y a autenticarlo con tu cuenta de GitHub. Continúa con el [Ejercicio 1 - Instalar GitHub Copilot CLI][next-lesson].

## Recursos

- [Información general de GitHub Codespaces][codespaces]
- [Crear un repositorio a partir de una plantilla][template-repository]
- [Primeros pasos con Codespaces][codespaces-quickstart]

[template-repository]: https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository
[codespaces-quickstart]: https://docs.github.com/codespaces/getting-started/quickstart
[next-lesson]: ../1-install-copilot-cli/
