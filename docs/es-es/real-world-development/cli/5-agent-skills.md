---
title: "Ejercicio 5 - Usar habilidades de agente"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Desarrollar una aplicación suele implicar tareas repetibles, como generar builds, ejecutar pruebas o crear pull requests. Las **habilidades de agente** te permiten dar a Copilot, y a otros agentes de IA, directrices sobre cómo realizar esas tareas. Una habilidad es una carpeta de instrucciones, scripts y recursos que el agente puede cargar bajo demanda. [Agent Skills es un estándar abierto][agent-skills-repo] utilizado por distintos agentes, por lo que la misma habilidad puede funcionar en Copilot Chat en modo agente, Copilot cloud agent, Copilot CLI y la aplicación GitHub Copilot.

Las habilidades viven en la carpeta `.github/skills` de un proyecto, o globalmente en `~/.copilot/skills`. Cada habilidad es una carpeta que contiene un archivo `SKILL.md` con frontmatter YAML (un `name` y un `description`) seguido de las instrucciones en Markdown:

```yaml
---
name: make-contribution
description: All changes to code must follow the guidance documented in the repository. Before any issue is filed, branch is made, commits generated, or pull request (or PR) created, a search must be done to ensure the right steps are followed. Whenever asked to create an issue, commit messages, to push code, or create a PR, use this skill so everything is done correctly.
---
```

Las habilidades también pueden incluir subcarpetas con scripts, recursos y material de referencia. La estructura completa se describe en la [especificación de agent skills][agent-skills-spec].

> [!TIP]
> Las habilidades se cargan dinámicamente. El agente decide qué habilidad se aplica a partir del campo `description`; una descripción clara y específica para el escenario marca la diferencia entre una habilidad que se usa y otra que se ignora.

[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification

Vamos a ver cómo una habilidad puede garantizar que las pull requests sigan las especificaciones marcadas por nuestro equipo.

## Escenario

El equipo tiene una serie de requisitos para las pull requests (PR):

- mensajes de confirmación claros, con los archivos agrupados de forma lógica.
- todas las pruebas deben superarse antes de crear una PR.
- cada PR debe contener las siguientes secciones:
    - una descripción de por qué se hicieron los cambios.
    - una visión general de los archivos modificados.
    - fragmentos de bloques de código importantes.
    - detalles de los cambios realizados agrupados juntos.

Como el equipo usa Copilot para generar código y PR, quiere asegurarse de que las herramientas de IA sigan estos requisitos.

En este ejercicio vas a:

- explorar una habilidad existente para crear pull requests.
- aprender cómo utiliza el agente de IA las habilidades.
- crear una PR que cumpla las directrices con ayuda de la habilidad.

## Ejecutar habilidades

Las habilidades se cargan dinámicamente cuando el agente determina que son necesarias. La decisión de qué habilidades usar depende de la descripción del archivo `SKILL.md`. Por eso, es importante que las descripciones sean claras y definan el caso de uso de la habilidad.

## Explorar la habilidad de PR

Como Tailspin Toys tiene un conjunto de requisitos para crear PR, ha creado una habilidad para ayudar a las herramientas de IA a generar PR que cumplan esas directrices. Vamos a explorar la habilidad para entender qué hará.

1. Abre `.github/skills/make-contribution/SKILL.md`.
2. Fíjate en el nombre y la descripción. Observa cómo la descripción destaca el escenario en el que debe usarse, es decir, siempre que se solicite crear una pull request o confirmar código.
3. Lee la habilidad. Observa que define reglas sobre cómo deben crearse las ramas, generarse las confirmaciones y redactarse los contenidos de la pull request.

## Usar la habilidad

Como se indicó antes, Copilot CLI invoca automáticamente las habilidades. Como resultado, lo único que tienes que hacer es pedirle a Copilot que cree una PR.

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

1. Pídele a Copilot que cree una PR con el siguiente prompt:

    ```
    Can you please create a pull request for me!
    ```

2. Copilot confirmará la solicitud. Al cabo de unos instantes, verás que Copilot indica que está utilizando la habilidad **make-contribution**.

3. Después, Copilot seguirá las instrucciones de la habilidad. Empezará ejecutando las pruebas y luego creará una rama, confirmaciones y, finalmente, la PR.
4. Cuando se cree la PR, vuelve a tu repositorio y ábrela. Observa que las secciones siguen las directrices definidas en la habilidad y coinciden con los requisitos establecidos por el equipo.
5. Antes de pasar al siguiente ejercicio, restablece tu espacio de trabajo local en una rama nueva desde `main` para que el trabajo de accesibilidad quede separado de esta PR de filtrado:

    ```bash
    git checkout main
    git pull
    git checkout -b accessibility-cli
    ```

## Resumen y siguientes pasos

Con la ayuda de una habilidad de agente, has creado una PR nueva que cumple los requisitos documentados. Has hecho lo siguiente:

- explorar una habilidad existente para crear pull requests.
- aprender cómo utiliza el agente de IA las habilidades.
- crear una PR que cumple las directrices con ayuda de la habilidad.

Las habilidades son perfectas para tareas concretas, pero para operaciones más amplias conviene aprovechar los [agentes personalizados][next-lesson], que exploraremos a continuación.

## Recursos

- [Acerca de las habilidades de agente][about-agent-skills]
- [Especificación de Agent Skills][agent-skills-spec]
- [Repositorio de Agent Skills][agent-skills-repo]
- [Habilidades de agente en awesome-copilot][awesome-copilot-skills]

[previous-lesson]: ../4-mcp/
[next-lesson]: ../6-custom-agents/
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[awesome-copilot-skills]: https://github.com/github/awesome-copilot/tree/main/skills
