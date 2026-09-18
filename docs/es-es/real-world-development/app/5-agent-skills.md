---
title: "Lección 5 - Personalizar y utilizar una habilidad quality-checks"
description: "Explora la habilidad quality-checks existente, personaliza el formato de su informe y utilízala para validar el filtrado."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Escribir código implica mucho más que limitarse a escribirlo. Hemos podido validar manualmente que funciona y hemos utilizado archivos de instrucciones para garantizar que sigue nuestros estándares. Pero ¿qué ocurre con las pruebas, lint y el resto de las tareas de integración continua (CI)?

Para este tipo de tareas, las **habilidades de agente** son la mejor opción. Las habilidades ayudan a Copilot a comprender cómo ejecutar correctamente operaciones como estas.

En esta lección:

- explorarás la habilidad `quality-checks` existente y sus scripts incluidos.
- personalizarás el formato de sus resultados.
- ejecutarás la habilidad y revisarás su salida.

## Escenario

Tailspin Toys dispone de un conjunto de pruebas unitarias y de un extremo a otro que siempre deben ejecutarse antes de crear cualquier solicitud de incorporación de cambios (PR). Como cabe esperar, es importante garantizar que se ejecuten de forma correcta y coherente. El equipo ya ha creado una habilidad de agente para ejecutar estas pruebas, pero quiere mejorar la salida para facilitar su lectura.

## Instrucciones, scripts y recursos

Las habilidades de agente reúnen instrucciones de tareas reutilizables, scripts ejecutables y recursos de apoyo que un agente carga cuando los necesita. En esencia, son una carpeta con el nombre de la habilidad y un archivo Markdown llamado `SKILL.md`. Este archivo contiene frontmatter con un nombre y una descripción que definen la habilidad, una introducción sobre lo que hace e indicaciones sobre cuándo debe invocarse. La carpeta también puede contener subcarpetas con scripts y otros recursos que utilizará la habilidad.

> [!NOTE]
> Una habilidad no necesita carpetas ni archivos adicionales. En nuestro ejemplo, la habilidad ejecutará comandos `npm` para iniciar las pruebas y los linters, así que no necesitamos archivos auxiliares.

Las habilidades pueden residir en la carpeta `.github/skills` de un proyecto para convertirse en un recurso del repositorio que el resto del equipo pueda compartir y reutilizar, o en la carpeta raíz de Copilot, que suele ser `~/.copilot/skills`.

## Explorar la habilidad

1. Si todavía no tienes abierto un lienzo **Files**, selecciona **+** en el panel de revisión y, después, **File**.
2. Busca `.github/skills/quality-checks/SKILL.md`.
3. Lee `name` y `description` al principio. Observa que la descripción ayuda a Copilot a comprender cuándo debe invocar la habilidad.
4. Lee las instrucciones y observa cómo orientan a Copilot durante el proceso de pruebas y lint.

## Ejecutar la habilidad antes de realizar un cambio

Las habilidades se pueden invocar directamente mediante un comando con barra diagonal (`/`) o con lenguaje natural. La descripción destaca que la habilidad debe utilizarse cuando se solicite ejecutar pruebas o lint. Ejecutemos la habilidad pidiendo a Copilot que ejecute las pruebas.

1. Selecciona el modo **Interactive** en el menú desplegable para confirmar que Copilot lo utiliza.
2. Utiliza la indicación siguiente para pedir a Copilot que ejecute las pruebas y el linter, lo que invocará la habilidad:

    ```plaintext
    Run the tests and linters.
    ```

3. Observa el informe final.

## Personalizar el informe

Queremos un informe mejor que muestre las pruebas ejecutadas, las tasas de éxito y error y cuánto han tardado. Actualicemos la habilidad para que Copilot genere ese informe.

1. Vuelve al lienzo **Files**.
2. Si aún no está abierto, abre `.github/skills/quality-checks/SKILL.md`.
3. Busca al final del archivo el encabezado **Results output formatting**.
4. Justo debajo, añade lo siguiente para que los resultados se muestren según nuestras especificaciones:

    ```markdown
    Upon completion of all tests, generate a report that provides a quick overview of both success and failure of the tests, and how long they took to ran. In particular, we need sections for:

    - Unit tests, total number of tests, number succeeded, number failed, a percentage thereof, and the amount of time testing took.
    - End to end tests, total number of tests, number succeeded, number failed, a percentage thereof, and the amount of time testing took.
    - Linting, number of lines scanned, number of violations, and the percentage of lines of code that meet the linting requirements.
    ```

El archivo se guardará automáticamente.

## Ejecutar la habilidad actualizada

Una vez realizado el cambio, veamos cómo funciona. Utilizaremos exactamente la misma indicación que antes.

1. Selecciona el modo **Interactive** en el menú desplegable para confirmar que Copilot lo utiliza.
2. Utiliza la indicación siguiente para pedir a Copilot que ejecute las pruebas y el linter, lo que invocará la habilidad:

    ```plaintext
    Run the tests and linters.
    ```

3. Observa el informe final.

## Resumen y pasos siguientes

Has personalizado y utilizado una habilidad de agente existente. En esta lección:

- has explorado la habilidad `quality-checks` y sus scripts incluidos.
- has personalizado el formato de sus resultados.
- has ejecutado la habilidad y revisado su salida.

Este cambio acompañará al filtrado en la PR de la funcionalidad. A continuación, permitirás que Copilot interactúe directamente con el sitio [mediante el servidor MCP de Playwright][next-lesson].

## Más ejemplos de habilidades

Estos ejemplos de la comunidad son referencias, no tareas adicionales. Revisa sus requisitos previos y su comportamiento antes de adoptarlos:

- [Especificación de Agent Skills][skill-spec].
- [Flujo de contribución: `make-repo-contribution`][contribution-example].
- [Documentos de requisitos: `prd`][prd-example].
- [Diagramas y un script de exportación incluido: `drawio`][drawio-example].
- [Pruebas de navegador: `webapp-testing`][browser-example].

El ejemplo de contribución original se llama `make-repo-contribution`; las plantillas antiguas de Tailspin utilizaban otro nombre, `make-contribution`. Este taller no depende de ninguna de esas habilidades de contribución.

[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
