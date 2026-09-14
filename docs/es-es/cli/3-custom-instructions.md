---
title: "Ejercicio 3 - Guiar a Copilot con instrucciones personalizadas"
description: "Añade una convención de documentación específica, demuéstrala en código existente y combina la segunda solicitud de incorporación de cambios."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

El contexto ayuda a Copilot a comprender no solo *qué* crear, sino *cómo* espera tu equipo que se escriba el código. Añadirás una convención de documentación específica, observarás su efecto en código real y combinarás las instrucciones y la demostración juntas como PR 2.

En este ejercicio:

- explorarás instrucciones generales del repositorio y limitadas por ruta.
- añadirás un estándar de documentación sin implementar el filtrado antes de tiempo.
- demostrarás el estándar en una pequeña función auxiliar o un componente existente.
- validarás y combinarás el hito de instrucciones.

## Explorar las instrucciones

El repositorio ya contiene dos tipos útiles de instrucciones:

- `.github/copilot-instructions.md` proporciona contexto general del repositorio, como la pila tecnológica, la estructura y las prácticas habituales.
- `.github/instructions/*.instructions.md` proporciona directrices de alcance limitado. Un patrón glob `applyTo` en el frontmatter identifica los archivos a los que se aplican.

Abre estos archivos en el editor:

1. Lee `.github/copilot-instructions.md` y localiza los estándares actuales de programación y verificación.
2. Explora `.github/instructions/`, incluidas las directrices de Astro, capa de datos y pruebas.
3. En `unit-tests.instructions.md`, examina el patrón `applyTo` y las convenciones de pruebas.
4. En `drizzle.instructions.md`, examina los patrones de acceso a datos y las referencias a ejemplos.

Mantén concisas las instrucciones generales, coloca los detalles específicos de archivo en el archivo de instrucciones pertinente y evita copias contradictorias de la misma regla. La [referencia de compatibilidad de instrucciones de GitHub][instruction-support] explica qué formatos admite cada entorno.

> [!NOTE]
> Las instrucciones influyen en la generación; no garantizan el cumplimiento. Tu revisión comprobará tanto el texto de las instrucciones como su efecto en el código. Si Copilot ya produce buenos comentarios, el objetivo es hacer explícita y repetible la convención, no forzar un fallo para comparar un antes y un después.

## Partir de la PR 1 combinada

Confirma que la PR de valoraciones por estrellas está combinada. Desde la terminal del repositorio del participante, inicia el siguiente hito a partir de `main` actualizado:

```bash
git status
git switch main
git pull --ff-only
git switch -c update-custom-instructions
copilot --enable-all-github-mcp-tools
```

Si el árbol de trabajo no está limpio o falla la actualización, resuelve ese estado antes de continuar. Mantén el modo **Interactive**.

En la pestaña **Issues** del repositorio, busca **Update our repository coding standards** y copia su URL real. La incidencia proporciona el contexto más amplio: explicar la intención, documentar funciones exportadas de la capa de datos y contratos de componentes y mantener los comentarios actualizados. Este ejercicio aborda una parte acotada de la documentación, no una refactorización de todo el repositorio ni una promesa de cumplir todos los criterios de la incidencia.

## Añadir la convención de documentación

Sustituye el marcador por la URL real de la incidencia y envía:

```plaintext
Lee esta incidencia de estándares de programación como contexto: <coding-standards-issue-URL>. Examina las instrucciones generales y de alcance limitado existentes. Añade una convención de documentación específica: explica la intención en lugar de repetir el código, documenta las funciones exportadas de db/ y src/lib/ con TSDoc/JSDoc que cubra propósito, parámetros y valores de retorno, documenta los contratos de Props de los componentes reutilizables de Astro y mantén los comentarios actualizados cuando cambie el código relacionado.

Coloca cada regla en el archivo de instrucciones existente adecuado y evita duplicaciones o contradicciones. Conserva los estándares de formato y lint existentes; enlaza o resume la convención de documentación en README donde corresponda. Limita este cambio al estándar de documentación, no a una migración de herramientas de formato ni a una reescritura de todo el repositorio. No crees una habilidad o un agente, no implementes el filtrado, no crees commits, no envíes cambios ni abras una PR. Detente para que pueda examinar las instrucciones antes de la demostración.
```

Examina las diferencias. La convención debe fomentar comentarios útiles, no exigir una cabecera genérica en todos los archivos ni comentarios que repitan código evidente. Pide correcciones antes de continuar.

## Demostrar la convención en código real

Elige una pequeña función auxiliar exportada o un componente reutilizable existente tras examinar el repositorio. No tiene que ser una función auxiliar de editores, y no se exige que `src/lib/publishers.ts` ya exista.

Envía:

```plaintext
Con las instrucciones actualizadas, selecciona una pequeña función auxiliar exportada o un componente reutilizable de Astro existente que se beneficie de una documentación más clara. Aplica la convención directamente a ese archivo sin cambiar el comportamiento en ejecución ni añadir filtrado. Explica qué instrucción ha guiado el cambio y detente antes de crear un commit o abrir una PR.
```

Abre el archivo real modificado. En una función auxiliar, comprueba que los comentarios describen correctamente sus parámetros, el valor de retorno y cualquier argumento de base de datos inyectado. En un componente, comprueba que su contrato de `Props` está documentado. Confirma que la explicación coincide con el código en lugar de limitarte a buscar un bloque de comentarios.

> [!TIP]
> Un fragmento ilustrativo en el chat no es la demostración: examina un cambio real del repositorio. Si el código elegido ya cumple la convención, elige otro objetivo pequeño existente donde la mejora esté justificada en lugar de añadir comentarios redundantes.

## Validar y combinar la PR 2

Pide a Copilot que valide los cambios revisados:

```plaintext
Revisa los cambios de instrucciones y la pequeña demostración de documentación. Confirma que el comportamiento en ejecución no ha cambiado. Examina package.json, ejecuta npm run lint y npm run typecheck:all y ejecuta las pruebas existentes afectadas cuando el cambio de código lo justifique. Informa de los comandos exactos y sus resultados. No instales nada, no crees una habilidad, no crees commits, no envíes cambios ni abras una PR todavía.
```

Resuelve los fallos y examina las diferencias finales. Después autoriza el hito:

```plaintext
Crea un commit solo con las instrucciones de documentación revisadas, la actualización directamente relacionada de README y la pequeña demostración de código. Envía la rama actual y crea una PR a main siguiendo la plantilla de PR del repositorio. Incluye los resultados de verificación y referencia la incidencia de estándares de programación como contribución parcial; no utilices una palabra clave de cierre salvo que se cumplan realmente todos los criterios de la incidencia. No combines ni empieces el filtrado.
```

Abre la URL de la PR, examina **Files changed** y revisa CI. Cuando se superen todas las comprobaciones y revisiones obligatorias, combina en GitHub y confirma que la PR 2 está **Merged**. Sal de la sesión de CLI con `/exit`. No inicies el siguiente hito hasta que esta PR esté combinada.

## Resumen y pasos siguientes

La convención de documentación y una demostración real ya están en `main`. A continuación, [crearás el filtrado con Plan y Autopilot][next-lesson] en una rama nueva basada en ese estado combinado.

## Recursos

- [Añadir instrucciones personalizadas al repositorio][repository-instructions] explica las directrices generales y limitadas por ruta.
- [Awesome Copilot][awesome-copilot] ofrece ejemplos para revisar y adaptar, no para adoptar a ciegas.

[previous-lesson]: ../2-add-star-rating/
[next-lesson]: ../4-build-filtering/
[instruction-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[repository-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[awesome-copilot]: https://github.com/github/awesome-copilot
