---
title: "Ejercicio 2 - Añadir valoraciones por estrellas: una mejora rápida"
description: "Muestra las valoraciones existentes de los juegos, revisa y valida el cambio y combina tu primera solicitud de incorporación de cambios."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Empieza con un cambio pequeño que puedas comprender y verificar. Tailspin Toys ya almacena el `starRating` de cada juego y lo muestra en la página de detalles. Mostrarás ese valor existente en las tarjetas de juegos, incluido un mensaje claro cuando un juego no tenga valoración.

En este ejercicio:

- solicitarás un cambio específico en una sesión Interactive de CLI.
- examinarás las diferencias y verificarás las tarjetas con y sin valoración.
- crearás un commit, abrirás y revisarás la PR 1 y la combinarás.

## Escenario

Los visitantes pueden ver las valoraciones en la página de detalles de un juego, pero no compararlas al explorar el catálogo. Tailspin Toys quiere mostrar las valoraciones existentes en las tarjetas, con un estado claro para los juegos sin valorar. Este pequeño cambio permite practicar cómo solicitar, revisar y publicar trabajo antes de abordar una funcionalidad mayor.

## Iniciar el primer hito

Desde la raíz del repositorio del participante, confirma que el árbol de trabajo está limpio, actualiza `main` y crea una rama. Si `git status` muestra cambios inesperados, resuélvelos antes de cambiar de rama; no los descartes.

```bash
git status
git switch main
git pull --ff-only
git switch -c add-star-rating
copilot --enable-all-github-mcp-tools
```

Confía en el repositorio cuando se solicite. Comprueba que estás en modo **Interactive** y utiliza `/model` para examinar los modelos disponibles o seleccionar **Auto**. Revisa las aprobaciones de herramientas a medida que aparezcan.

## Solicitar el cambio

Envía esta indicación:

```plaintext
Muestra la valoración por estrellas de cada juego en las tarjetas. El tipo Game ya incluye un campo starRating: un número sobre 5, o null cuando el juego aún no tiene valoración. Muéstralo en cada tarjeta de src/components/GameCard.astro y, cuando starRating sea null, muestra "No rating yet". Mantén el cambio pequeño y no reestructures el diseño de las tarjetas.

Examina y sigue las instrucciones del repositorio. Utiliza el modelo de datos existente; no añadas una API de valoraciones, un esquema nuevo ni una funcionalidad ajena a la tarea. Añade o actualiza las pruebas adecuadas para los casos con y sin valoración. No crees commits, no envíes cambios ni abras una solicitud de incorporación de cambios todavía.
```

Copilot debería examinar el tipo y el componente existentes antes de editar. Lee la actividad de sus herramientas además de su respuesta final. Un resumen seguro de sí mismo no demuestra que la implementación sea correcta.

## Revisar y validar

1. Introduce `/diff` y examina todos los archivos modificados en el editor o la vista de diferencias.
2. Confirma que la tarjeta utiliza el `starRating` existente, muestra un valor sobre 5 y presenta `No rating yet` para `null`. Una comprobación basada solo en si el valor se evalúa como verdadero puede tratar erróneamente un cero numérico como ausencia de valoración.
3. Comprueba que el cambio conserva el diseño de la tarjeta y proporciona a la valoración una etiqueta textual significativa en lugar de depender solo de una estrella o del color.
4. Pide a Copilot que verifique el cambio con las comprobaciones existentes:

   ```plaintext
   Examina package.json y la configuración de pruebas y ejecuta lint, comprobaciones de tipos y las pruebas unitarias o E2E existentes adecuadas para este cambio de tarjeta. Verifica tanto las valoraciones numéricas como la alternativa para null; informa de los comandos exactos y sus resultados, incluida cualquier carencia de cobertura o comprobación bloqueada. No instales nada, no cambies de rama, no crees commits, no envíes cambios ni abras una PR.
   ```

5. Revisa la salida de los comandos y los cambios de pruebas. Resuelve los fallos antes de entregar; pregunta antes de instalar requisitos previos ausentes.

Para observar la tarjeta en un navegador, abre una segunda terminal en esta misma copia de trabajo y ejecuta:

```bash
npm run dev
```

Abre el puerto reenviado en el panel **Ports** del codespace. Examina las tarjetas con valoración en la página de inicio. Si los datos iniciales actuales no contienen un ejemplo sin valoración, exige un caso de prueba automatizado con datos que cubran `null`; no afirmes haber observado una tarjeta sin valoración. Detén el servidor de desarrollo con <kbd>Ctrl</kbd>+<kbd>C</kbd> en su terminal antes de las comprobaciones E2E o de salir del ejercicio. Las pruebas automatizadas de Playwright no deben reutilizar un servidor de otra copia de trabajo.

## Crear y combinar la PR 1

Tras revisar el cambio y superar las comprobaciones, autoriza este hito por separado:

```plaintext
Revisa las diferencias actuales y los resultados de las comprobaciones. Crea un commit solo con el cambio de valoraciones por estrellas revisado y sus pruebas, envía la rama actual y crea una solicitud de incorporación de cambios a main utilizando la plantilla de PR de este repositorio, si existe. Incluye el resumen del cambio y los resultados reales de verificación. No combines la PR ni empieces otra tarea.
```

Abre la URL de la PR que se devuelve. Examina **Files changed** y los resultados de las comprobaciones, no solo el resumen del agente. Revisa las definiciones de los flujos de trabajo del repositorio Tailspin al interpretar CI; CI no sustituye tu observación en el navegador. Resuelve los fallos y vuelve a verificar el código modificado.

Cuando la PR cumpla los requisitos de revisión y comprobación del repositorio, selecciona **Merge pull request** y confirma la combinación en GitHub. Si la protección de ramas exige otro revisor, espera esa aprobación. Confirma que la PR está **Merged** antes de continuar.

Sal de la sesión de Copilot con `/exit`. En el siguiente ejercicio actualizarás el `main` local antes de crear la rama de instrucciones; no la inicies desde esta rama de funcionalidad sin combinar.

## Resumen y pasos siguientes

Has completado el primer ciclo: una indicación acotada, código revisado, pruebas de verificación y una PR combinada. A continuación, [guía a Copilot con instrucciones personalizadas][next-lesson] y demuestra una convención de documentación en una segunda PR pequeña.

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-custom-instructions/
