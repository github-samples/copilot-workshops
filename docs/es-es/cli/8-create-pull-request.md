---
title: "Ejercicio 8 - Crear y combinar la PR de la funcionalidad"
description: "Revisa todo el hito de filtrado, reutiliza las pruebas de verificación actuales de QA y combina la tercera solicitud de incorporación de cambios tras CI y la revisión."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Ahora reúne el hito de filtrado en la PR 3. Mantén la rama y la copia de trabajo utilizadas en los Ejercicios 4–7. Contienen la implementación de filtrado, la habilidad quality-checks y sus scripts, el perfil de QA y las pruebas asociadas.

En este ejercicio:

- revisarás las diferencias del hito completo y las pruebas de verificación actuales de QA.
- solicitarás una PR de funcionalidad y examinarás sus comprobaciones y comentarios de revisión.
- combinarás explícitamente la PR revisada y actualizarás el `main` local.

## Escenario

El trabajo de filtrado está repartido en varios puntos de control, pero los revisores necesitan evaluar una funcionalidad completa. Tailspin Toys quiere una PR que conecte los requisitos, la implementación, las comprobaciones reutilizables y los hallazgos de QA. Prepararás esa entrega y resolverás los bloqueos antes de combinar.

Esta es una petición normal de PR con alcance limitado que utiliza las convenciones del repositorio. No requiere una habilidad de contribución.

> [!NOTE]
> Un equipo de producción podría separar una funcionalidad de la infraestructura de calidad reutilizable. Este taller las combina deliberadamente para mostrar el flujo completo en una PR de funcionalidad. Las PR anteriores de valoraciones por estrellas e instrucciones ya deberían estar combinadas en `main`, no aparecer otra vez como trabajo ajeno.

## Comprobar la preparación y las pruebas de verificación

1. Revisa el dictamen de QA y la correspondencia entre requisitos y pruebas de verificación. Un **NO-GO**, la ausencia de observaciones de navegador o una comprobación obligatoria omitida es un bloqueo que resolver antes de combinar.
2. Confirma que las cuatro comprobaciones se ejecutaron realmente mediante la habilidad quality-checks: lint, pruebas unitarias, E2E y comprobación de tipos.
3. Revisa la revisión probada y los cambios posteriores a esas comprobaciones. Reutiliza las pruebas de verificación actuales de QA solo mientras el código probado, las pruebas y los scripts de verificación no hayan cambiado. Un commit de punto de control por sí solo no invalida contenidos de archivo idénticos, pero los cambios de código sí.
4. Si cambió la implementación o alguna entrada probada, ejecuta de nuevo las comprobaciones pertinentes de la habilidad y las observaciones de navegador y actualiza las pruebas de verificación. No repitas toda la batería solo por abrir una PR cuando los resultados actuales de QA siguen siendo aplicables.
5. Examina las diferencias de toda la rama, no solo el último punto de control o los cambios sin commit.

Desde otra terminal en la misma copia de trabajo:

```bash
git status
git fetch origin
git log --oneline origin/main..HEAD
git diff --stat origin/main...HEAD
git --no-pager diff origin/main...HEAD
```

La comparación de tres puntos muestra los cambios de esta rama desde su antecesor común con `origin/main`, incluidos los puntos de control anteriores. Verifica que incluye solo el hito de filtrado previsto. Examina también los archivos nuevos; los archivos inesperados sin seguimiento o sin commit deben revisarse antes de prepararlos.

## Solicitar la PR 3

El Ejercicio 7 te devolvió a una sesión **Interactive** normal antes del punto de control. Continúa en esa sesión establecida si el perfil de QA ya no está activo y la copia de trabajo y la rama de filtrado no han cambiado. Mantén disponibles la URL de la incidencia, las aclaraciones aprobadas de planificación y el informe actual de QA, incluida la revisión probada y los resultados de las comprobaciones.

El perfil de QA prohíbe las acciones de commit y PR durante QA. Si sigue activo, vuelve a una sesión normal antes de solicitar la PR:

1. Espera a que QA esté inactivo y después introduce `/exit` en su prompt de CLI. Si CLI permanece abierto porque hay otra sesión activa, termina o conserva ese trabajo antes de volver al prompt normal y pulsar <kbd>Ctrl</kbd>+<kbd>D</kbd> para cerrar esta instancia de CLI.
2. En el prompt del shell, permanece en la misma copia de trabajo y rama de filtrado. Confirma su identidad e inicia una sesión normal nueva sin `--agent qa` ni una opción de reanudación:

   ```bash
   pwd
   git branch --show-current
   git status
   copilot
   ```

3. Confirma que estás en modo **Interactive** y el perfil de QA ya no está activo. No crees otro worktree, no cambies de rama ni reanudes la sesión de QA.

Sustituye todos los marcadores siguientes por la URL real de la incidencia, las aclaraciones aprobadas y las pruebas de verificación actuales de QA. Proporciónalos explícitamente aunque hayas permanecido en la sesión normal del Ejercicio 7; una conversación nueva no debe depender de la memoria de la sesión de QA.

```plaintext
Prepara la PR de la funcionalidad de filtrado para esta incidencia: <filtering-issue-URL>. Estos son los criterios de aceptación adicionales que aprobé durante la planificación: <pega las aclaraciones acordadas o escribe none>. Estas son las pruebas de verificación actuales de QA: <pega el informe de QA, incluida la revisión probada, las observaciones de navegador, la evaluación de cobertura, los resultados de las cuatro comprobaciones y cualquier limitación>.

Confirma la copia de trabajo y la rama de filtrado actual. Examina todas las diferencias frente a main, todos los commits de puntos de control del hito, git status, la plantilla de PR del repositorio y las pruebas de verificación de QA proporcionadas. Incluye solo la implementación de filtrado revisada, la habilidad quality-checks y los scripts incluidos, la definición del agente de QA y las pruebas asociadas.

Reutiliza los resultados de QA mientras sigan describiendo el contenido final de los archivos. Si el código, las pruebas o los scripts de verificación cambiaron después, indícalo y ejecuta las comprobaciones pertinentes mediante la habilidad y la validación de navegador afectada antes de presentarlos como actuales. No etiquetes comprobaciones fallidas, bloqueadas u omitidas como superadas.

Si hace falta, crea un commit con los cambios revisados restantes del hito, envía esta rama actual y crea una sola PR a main siguiendo las convenciones del repositorio. Incluye la incidencia y los criterios aprobados, un resumen de implementación, las pruebas añadidas o por qué no hicieron falta, las observaciones de navegador, los resultados de las cuatro comprobaciones y las limitaciones restantes. No combines, no crees otra rama, no invoques una habilidad de contribución ni empieces otra funcionalidad.
```

## Revisar la PR y CI

Abre la URL devuelta y examina **Files changed** en toda la PR. Comprueba que los scripts de la habilidad y el perfil de QA están incluidos y que no se han colado credenciales, configuración local de MCP, archivos ajenos, informes generados o instalaciones de dependencias.

Utiliza la pestaña **Checks** de la PR o ejecuta estos comandos en la terminal de la rama de funcionalidad:

```bash
gh pr view
gh pr diff
gh pr checks --watch
```

Examina `.github/workflows/` de tu repositorio en lugar de suponer que una insignia verde cubre todos los tipos de verificación. El flujo actual **Run tests** de Tailspin ejecuta lint, comprobaciones de tipos, pruebas unitarias de Vitest y pruebas E2E de Playwright contra el sitio estático compilado. No sustituye las observaciones directas del navegador mediante MCP del informe de QA. La compilación Astro y las comprobaciones de enlaces del sitio del taller validan otro repositorio.

Si una comprobación falla, examina sus registros y resuelve la causa. Una corrección específica debe revisarse y verificarse de nuevo en la revisión actualizada antes de enviar cambios. Si `main` cambia y la resolución de un conflicto modifica la funcionalidad, actualiza también las pruebas de verificación afectadas. Espera cualquier revisión humana obligatoria; la aprobación del propio agente no anula la protección de ramas.

## Combinar y actualizar el main local

Cuando la PR cumpla todos los requisitos de revisión y comprobación, elige explícitamente **Merge pull request** en GitHub y confirma la combinación. Verifica que la PR 3 está **Merged**.

Sal de la sesión de CLI con `/exit`. Con el árbol de trabajo limpio, actualiza la copia local:

```bash
git status
git switch main
git pull --ff-only
```

## Resumen y pasos siguientes

No hace falta una rama nueva para el siguiente ejercicio. Has combinado exactamente tres PR del taller: valoraciones por estrellas; instrucciones y una demostración; y filtrado con la habilidad de calidad, el perfil de QA y las pruebas.

Continúa con el [Ejercicio 9 - Explorar comandos de barra y opciones de CLI][next-lesson] para recorrer de forma acotada los controles de CLI, no para realizar otra tarea de implementación.

[previous-lesson]: ../7-qa-agent/
[next-lesson]: ../9-slash-commands/
