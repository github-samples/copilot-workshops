---
title: "Ejercicio 6 - Agentes personalizados con GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

## ¿Qué son los agentes personalizados?

Los [agentes personalizados][custom-agents-concept] de GitHub Copilot te permiten crear asistentes de IA especializados y adaptados a tareas o dominios concretos dentro de tu flujo de desarrollo. Al definir agentes mediante archivos Markdown en la carpeta `.github/agents` de tu repositorio, puedes proporcionar a Copilot instrucciones enfocadas, buenas prácticas, patrones de desarrollo y conocimiento específico del dominio para orientarlo y que realice ciertos tipos de trabajo con mayor eficacia. Los equipos pueden codificar su experiencia en agentes reutilizables: un agente de accesibilidad que aplique el cumplimiento de [WCAG][wcag], un agente de seguridad que siga prácticas de desarrollo seguro o un agente de pruebas que mantenga patrones de prueba coherentes.

Los agentes personalizados se definen mediante archivos Markdown en la carpeta `.github/agents` de tu proyecto, o globalmente en `~/.copilot/agents`. Cada archivo tiene frontmatter YAML con al menos `name` y `description`, seguido de un prompt en Markdown que define el comportamiento, la especialización y las instrucciones del agente.

### Agentes personalizados frente a habilidades de agente

Existe cierta superposición lógica entre los agentes personalizados y las [habilidades de agente][agent-skills-concept]. Ambos se definen principalmente mediante archivos Markdown y explican a una IA cómo realizar operaciones. La forma más clara de diferenciarlos es esta: un **agente personalizado** es quien trabaja y las **habilidades** son herramientas.

Los agentes personalizados tienen su propia ventana de contexto y están pensados para orquestar habilidades, e incluso otros agentes, como parte de su trabajo. En este laboratorio, el agente personalizado de accesibilidad revisa y actualiza el sitio según las directrices de accesibilidad; como parte de ese trabajo podría invocar habilidades como una habilidad de flujo de trabajo de pull requests o una que ejecute y gestione pruebas.

> [!NOTE]
> No existe una única forma "correcta" de crear un agente personalizado. Como ocurre con todo en IA, conviene probar e iterar para descubrir qué funciona mejor en tus entornos y escenarios.

[custom-agents-concept]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[agent-skills-concept]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/

## Escenario

Muchas aplicaciones web no logran ser accesibles para todos los usuarios, y el sitio web en el que estás trabajando no es una excepción. Usarás un agente personalizado para identificar y corregir carencias de accesibilidad.

Tailspin Toys se compromete a garantizar que su plataforma de crowdfunding sea accesible para todos los usuarios, independientemente de sus capacidades visuales o preferencias. Comentarios recientes de usuarios han señalado que algunas personas encuentran el tema oscuro actual difícil de leer debido al contraste insuficiente entre el texto y los colores de fondo. Para responder a este problema de accesibilidad, el equipo de diseño ha solicitado implementar un modo de alto contraste que los usuarios puedan activar y desactivar.

Como la accesibilidad es crítica, quieres asegurarte de que esto se implemente lo antes posible. Vas a utilizar un agente personalizado para generar la funcionalidad.

En este ejercicio vas a:

- explorar los agentes personalizados.
- habilitar un agente personalizado y asignarle una tarea con Copilot CLI.

## Revisar el agente personalizado de accesibilidad

Ya se ha creado para ti un agente personalizado de accesibilidad. Vamos a revisar su contenido para entender cómo orientará a Copilot.

1. Abre `.github/agents/accessibility.md`.
2. Fíjate en el frontmatter YAML con los campos `name` y `description`.

> [!CAUTION]
> El frontmatter con `name` y `description` es obligatorio para los agentes personalizados.

3. A continuación, revisa las secciones siguientes, que destacan:
   - responsabilidades principales al generar código para un sitio web accesible.
   - buenas prácticas de accesibilidad.
   - ejemplos de código para HTML, CSS y JavaScript.
   - una lista de errores y problemas habituales.

## Usar un agente personalizado en Copilot CLI

Puedes iniciar un agente personalizado en Copilot CLI con el comando `/agent`. Vamos a realizar una revisión de accesibilidad de nuestro sitio web.

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

1. Muestra la lista de agentes escribiendo `/agent` en la ventana de prompt de Copilot CLI y seleccionando <kbd>Enter</kbd>.
2. Selecciona **Accessibility agent** en la lista de agentes disponibles.
3. Usa el siguiente prompt para pedir al agente de accesibilidad que realice una revisión y genere correcciones para el elemento del backlog relacionado con accesibilidad:

    ```
    Perform an accessibility review of the site. Pull the related issue down from the repository for details. Implement a high-contrast mode toggle that persists the user's preference across page reloads. Ensure there are e2e tests for any updates made to the project. Then create a PR with the updates.
    ```

4. Copilot se pondrá a trabajar en la tarea. Empezará recuperando la incidencia, después realizará la revisión, generará las actualizaciones y, por último, creará la PR. También deberías observar que, al crear la PR, utiliza la habilidad centrada en PR del proyecto.

> [!NOTE]
> Es probable que este proceso tarde unos minutos. Es un buen momento para reflexionar sobre todo lo que has aprendido, tomar algo o adelantarte al siguiente módulo, donde se comentan algunos comandos adicionales disponibles en Copilot CLI.

## Resumen y siguientes pasos

Esta lección ha explorado los [agentes personalizados][custom-agents] de GitHub Copilot, asistentes de IA especializados adaptados a tareas y dominios concretos. Con los agentes personalizados puedes codificar la experiencia y los estándares de tu equipo en agentes reutilizables que orienten a Copilot para realizar determinados tipos de trabajo con mayor eficacia.

Has explorado estos conceptos:

- cómo se definen los agentes personalizados.
- cómo usar un agente personalizado en Copilot CLI.

Ahora vamos a explorar [algunos comandos de barra][next-lesson] para aprender algunos trucos adicionales con Copilot CLI.

## Recursos

- [Agentes personalizados][custom-agents]
- [Crear agentes personalizados para un repositorio][creating-custom-agents]
- [Agentes personalizados en awesome-copilot][awesome-copilot-agents]
- [Prepararse para usar agentes personalizados en tu organización][org-custom-agents]
- [Prepararse para usar agentes personalizados en tu empresa][enterprise-custom-agents]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-slash-commands/
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[creating-custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents
[awesome-copilot-agents]: https://github.com/github/awesome-copilot/tree/main/agents
[org-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
[enterprise-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
