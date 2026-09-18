---
title: "Ejercicio 2 - Instrucciones personalizadas (Copilot CLI)"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

[← Lección anterior: Instalar Copilot CLI][previous-lesson] · [Siguiente lección: Generar código con CLI →][next-lesson]

El contexto es clave cuando se trabaja con IA generativa. Si una tarea debe hacerse de una forma concreta, o hay información de fondo que Copilot debería conocer, te interesa asegurarte de que ese contexto esté disponible. Tienes varias herramientas a tu disposición para ayudar a Copilot, y las exploraremos a lo largo de este taller. Vamos a empezar con los [archivos de instrucciones][instruction-files], que suelen centrarse en cómo debe estructurarse el propio código. Esto ayuda a Copilot a entender no solo *qué* código quieres, sino también *cómo* debe estructurarse.

En este ejercicio vas a:

- explorar cómo el contexto específico del proyecto, las directrices de desarrollo y los estándares de documentación llegan a Copilot a través de las instrucciones personalizadas del repositorio y de los archivos de instrucciones con ámbito de ruta;
- generar el primer bloque de datos para el filtrado (un helper de editoriales) con las instrucciones *actuales*;
- añadir un nuevo estándar general del repositorio a `.github/copilot-instructions.md`;
- ejecutar un prompt de seguimiento y ver cómo el código regenerado adopta el nuevo estándar;
- confirmar los cambios de las instrucciones y del helper para que el siguiente ejercicio pueda basarse en ellos.

> [!CAUTION]
> El código generado puede desviarse de algunos de los estándares que establezcas. Copilot no es determinista. El objetivo es observar la *tendencia* del cambio de comportamiento tras actualizar las instrucciones, no hacer que la salida coincida carácter por carácter.

## Archivos de instrucciones

### Escenario

Como cualquier buen equipo de desarrollo, Tailspin Toys tiene un conjunto de directrices y requisitos para sus prácticas de desarrollo. Entre ellos se incluyen:

- La capa de datos siempre necesita pruebas unitarias.
- La interfaz debe estar en modo oscuro y tener un aspecto moderno.
- Debe añadirse documentación al código en forma de comentarios de documentación TSDoc.
- Debe añadirse un bloque de comentarios al inicio de cada archivo para describir lo que hace.

Gracias al uso de archivos de instrucciones, te asegurarás de que Copilot disponga de la información correcta para realizar las tareas de acuerdo con las prácticas indicadas.

### Instrucciones personalizadas

Las instrucciones personalizadas te permiten proporcionar contexto y preferencias a Copilot para que entienda mejor tu estilo de desarrollo y tus requisitos. Es una función muy potente que puede ayudarte a orientar Copilot para obtener sugerencias y fragmentos de código más relevantes. Puedes indicar tus convenciones de desarrollo preferidas, bibliotecas e incluso los tipos de comentarios que te gusta incluir en el código. Puedes crear instrucciones para todo el repositorio o para tipos de archivo concretos, con el fin de aportar contexto a nivel de tarea.

Hay dos tipos de archivos de instrucciones:

- `.github/copilot-instructions.md`, un único archivo de instrucciones que se envía a Copilot en **todas** las solicitudes del repositorio. Este archivo debe contener información a nivel de proyecto, es decir, contexto relevante para la mayoría de las solicitudes que se envían a Copilot desde el chat o la CLI. Puede incluir la pila tecnológica que se usa, una visión general de lo que se está construyendo, buenas prácticas y otras directrices globales.
- Se pueden crear archivos `.github/instructions/*.instructions.md` para tareas o tipos de archivo concretos. Puedes usarlos para proporcionar directrices para lenguajes concretos (como TypeScript o Astro), o para tareas como crear un componente de interfaz o un nuevo conjunto de pruebas unitarias.

> [!NOTE]
> Cuando trabajas en tu IDE, los archivos de instrucciones solo se usan para generar código en Copilot Chat, no para las finalizaciones de código ni para las sugerencias de la siguiente edición.
>
> Copilot Chat, Copilot CLI y Copilot cloud agent usan tanto los archivos a nivel de repositorio como los archivos `*.instructions.md` (con frontmatter `applyTo`) al generar código.
>
> Además, Copilot [admite archivos de instrucciones que usan otros estándares][custom-instructions-support], incluidos los archivos AGENTS.md y CLAUDE.md.

### Buenas prácticas para gestionar archivos de instrucciones

Una conversación completa sobre cómo crear archivos de instrucciones queda fuera del alcance de este taller. Sin embargo, los ejemplos proporcionados en el proyecto de ejemplo muestran un enfoque representativo. A grandes rasgos:

- Mantén las instrucciones de `copilot-instructions.md` centradas en directrices a nivel de proyecto, como una descripción de lo que se está construyendo, la estructura del proyecto y los estándares globales de desarrollo.
- Usa archivos `*.instructions.md` para proporcionar instrucciones específicas según el tipo de archivo (pruebas unitarias, componentes Astro, capa de datos) o la tarea.
- Usa lenguaje natural. Mantén las directrices claras. Proporciona ejemplos de cómo debería verse el código, y de cómo no.

No existe una única forma de crear archivos de instrucciones, igual que no existe una única forma de usar la IA. A través de la experimentación descubrirás qué funciona mejor para tu proyecto.

> [!TIP]
> Todos los proyectos que usan GitHub Copilot deberían contar con una colección sólida de archivos de instrucciones. Al explorar los de este proyecto, puede que veas que hay archivos para muchos tipos de tareas, incluidas [actualizaciones de la interfaz][ui-instructions] y [Astro][astro-instructions].
>
> Copilot también puede ayudarte a generar archivos de instrucciones. Cada superficie lo presenta de una forma distinta (por ejemplo, **Configure Chat → Generate Agent Instructions** en VS Code, o `/init` en Copilot CLI); la lección de la superficie en la que estés lo señalará cuando sea relevante.
>
> ¿Buscas plantillas o un punto de partida? Explora [awesome-copilot][awesome-copilot], un repositorio lleno de archivos de instrucciones, agentes personalizados y otros recursos.

[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[awesome-copilot]: https://github.com/github/awesome-copilot
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support

## Explorar los archivos de instrucciones personalizadas de este proyecto

Dedica un momento a leer los archivos de instrucciones incluidos en este repositorio: hay un `copilot-instructions.md` principal y una colección de archivos `*.instructions.md` para varias tareas. Ábrelos en tu editor o en la interfaz web de GitHub.

1. Abre `.github/copilot-instructions.md`.
2. Explora el archivo y fíjate en la breve descripción del proyecto y en secciones como **Agent notes**, **Code standards**, **Scripts** y **Repository Structure**. En **Code standards**, fíjate en la guía anidada **GitHub Actions Workflows**. Se aplica a cualquier interacción que tengas con Copilot.
3. Abre la carpeta `.github/instructions` y échale un vistazo. Verás instrucciones para archivos Astro, la capa de datos de Drizzle, pruebas y mucho más.
4. Abre `.github/instructions/unit-tests.instructions.md`. Fíjate en el campo `applyTo` de la parte superior: establece un glob (relativo a la raíz del repositorio) que determina a qué archivos se aplican las instrucciones. Aquí, cualquier archivo de prueba TypeScript (por ejemplo, uno que coincida con `**/*.test.ts`) coincidirá.
5. Observa las instrucciones específicas para crear pruebas unitarias para este proyecto.
6. Por último, abre `.github/instructions/drizzle.instructions.md` y desplázate hasta el final. Fíjate en los enlaces a otros archivos de instrucciones (como `unit-tests.instructions.md`) y a archivos existentes del proyecto. Esto te permite dividir conjuntos de instrucciones más grandes en archivos más pequeños y reutilizables, y mostrar a Copilot ejemplos que seguir al generar código. (Las rutas allí son relativas al archivo de instrucciones, no a la raíz del repositorio).

> [!NOTE]
> La sección **Code formatting requirements** de `copilot-instructions.md` documenta los estándares de desarrollo del proyecto, pero todavía no exige documentación dentro del código. En los pasos siguientes, añadirás reglas para comentarios de documentación TSDoc y encabezados de comentario a nivel de archivo.

## Crear una rama

Vas a hacer cambios en el código, así que crea una rama para trabajar.

1. Desde el terminal de tu codespace, crea una rama nueva y cambia a ella:

   ```bash
   git checkout -b update-custom-instructions
   ```

2. Confirma que Copilot CLI está instalado y autenticado:

   ```bash
   copilot --version
   ```

   Si no se encuentra el comando o no has iniciado sesión, vuelve al [Ejercicio 1 - Instalar GitHub Copilot CLI](../1-install-copilot-cli/).

## Usar Copilot CLI *antes* de actualizar las instrucciones

Para ver el impacto de las instrucciones personalizadas, empieza generando código con las instrucciones actuales. Más adelante, actualizarás el archivo y ejecutarás un prompt de seguimiento.

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

1. Asegúrate de que tu sesión de Copilot CLI se está ejecutando desde la **raíz del repositorio** para que detecte automáticamente `.github/copilot-instructions.md`.
2. En el prompt de Copilot CLI, pídele que genere el helper de editoriales que usará la interfaz de filtrado:

   ```plaintext
   Create a new data-access helper at src/lib/publishers.ts to return a list of all publishers. It should return the name and id for all publishers. Do not run the tests yet.
   ```

3. Copilot CLI explorará el proyecto, propondrá un plan y escribirá el archivo en esta sesión con `--yolo`. Supervisa los cambios en la salida del terminal y luego revísalos en tu editor.
4. Abre el archivo generado `src/lib/publishers.ts` en tu editor.
5. Observa que el helper es una función tipada que recibe un cliente `db` como primer argumento y devuelve un array tipado de editoriales; esto procede de las convenciones de la capa de datos en `.github/instructions/drizzle.instructions.md` (que se aplica a `src/lib/*.ts`).
6. Observa que al código generado **le faltan** comentarios de documentación TSDoc y un encabezado de comentario a nivel de archivo.

> [!CAUTION]
> Copilot es probabilístico: existe la posibilidad de que añada comentarios de documentación incluso sin que se lo indiques. Si ocurre, no pasa nada; la mejora en la *consistencia* después de actualizar las instrucciones sigue siendo la idea importante.

## Añadir un nuevo estándar del repositorio

Como se indicó antes, `.github/copilot-instructions.md` está diseñado para proporcionar información del proyecto a Copilot. Vamos a asegurarnos de que los estándares de desarrollo del repositorio queden documentados para mejorar las sugerencias de código.

1. Vuelve a abrir `.github/copilot-instructions.md`.
2. Localiza la sección **Code formatting requirements**, que debería estar cerca de la línea 27. Observa cómo documenta los estándares de desarrollo del proyecto, pero todavía no tiene ninguna regla para la documentación dentro del código, y por eso el helper generado no incluía comentarios de documentación.
3. Añade las siguientes líneas de Markdown justo debajo de los estándares existentes para indicar a Copilot que añada encabezados de comentario a nivel de archivo y comentarios de documentación TSDoc:

   ```markdown
   - Every exported function should have a TSDoc comment describing its purpose, parameters, and return value.
   - Before imports or any code, add a comment block to the file that explains its purpose.
   ```

4. Guarda `copilot-instructions.md`.

> [!TIP]
> Como viste en la lección anterior, los archivos de instrucciones pueden crearse a nivel de repositorio (`.github/copilot-instructions.md`) para directrices globales, o como archivos `*.instructions.md` para lenguajes, tipos de archivo o tareas concretos. El archivo a nivel de repositorio es el lugar adecuado para estándares generales del proyecto, como la regla de comentarios de documentación que acabas de añadir.

## Ejecutar de nuevo el prompt y observar el cambio

Ahora que las instrucciones incluyen una regla para los comentarios de documentación, pídele a Copilot CLI que actualice el archivo de editoriales que acabas de generar. La misma directriz de estándares orientará la reescritura.

1. Envía `/clear` en tu sesión de Copilot CLI para empezar con una conversación limpia.
2. Envía el siguiente prompt:

   ```plaintext
   Update src/lib/publishers.ts to follow the latest documentation conventions in .github/copilot-instructions.md.
   ```

3. Deja que termine la edición y vuelve a abrir `src/lib/publishers.ts`.
4. Observa que el archivo ahora empieza con un bloque de comentarios similar a este:

   ```typescript
   /**
    * Helpers de acceso a datos de editoriales para la plataforma de crowdfunding de Tailspin Toys.
    * Proporciona funciones para recuperar información de editoriales desde la base de datos.
    */
   ```

5. Observa que la función generada ahora incluye un comentario de documentación TSDoc similar a este:

   ```typescript
   /**
    * Devuelve una lista de todas las editoriales con su id y su nombre.
    *
    * @param db - El cliente de base de datos de Drizzle.
    * @returns Una promesa que se resuelve en un array de objetos de editoriales.
    */
   ```

6. Mantén este archivo actualizado. Es el primer bloque de datos sobre el que trabajarás en el siguiente ejercicio.

## Confirmar y enviar este primer bloque de filtrado

1. En el terminal, verifica los archivos modificados:

   ```bash
   git status
   ```

2. Prepara el cambio de las instrucciones y el helper:

   ```bash
   git add .github/copilot-instructions.md src/lib/publishers.ts
   ```

3. Confirma los cambios:

   ```bash
   git commit -m "Add doc comment standards and publishers helper foundation"
   ```

4. Envía la rama:

   ```bash
   git push -u origin update-custom-instructions
   ```

## Resumen y siguientes pasos

Has explorado cómo Copilot toma el contexto de los archivos de instrucciones de este proyecto y después has usado Copilot CLI para:

- generar una base del helper de acceso a datos de editoriales para el filtrado con las instrucciones *existentes*;
- añadir un nuevo estándar general del repositorio a `.github/copilot-instructions.md`;
- ejecutar un prompt de seguimiento y ver cómo el código regenerado adopta el nuevo estándar;
- confirmar y enviar tanto la actualización de instrucciones como la base del helper.

A continuación, aplicarás estas instrucciones mientras implementas trabajo del backlog en el [ejercicio de generación de código][next-lesson].

## Recursos

- [Archivos de instrucciones para la personalización de GitHub Copilot][instruction-files]
- [Buenas prácticas para crear instrucciones personalizadas][instructions-best-practices]
- [5 consejos para escribir mejores instrucciones personalizadas para Copilot][copilot-instructions-five-tips]
- [Awesome Copilot: una colección de archivos de instrucciones y otros recursos][awesome-copilot]

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-generating-code/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[copilot-instructions-five-tips]: https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/
