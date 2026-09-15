---
title: "Lección 5 - Crear y utilizar una habilidad quality-checks"
description: "Pide a Copilot que cree comprobaciones de calidad reutilizables con scripts de shell incluidos, examina la habilidad y ejecútala en la rama de filtrado."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

La funcionalidad de filtrado está implementada y comprobada con los comandos npm existentes. Ahora reunirás esas comprobaciones en una **habilidad de agente** reutilizable. Mantén la misma sesión y rama de filtrado durante las Lecciones 4–8; esta lección no crea una solicitud de incorporación de cambios.

En esta lección:

- volverás al modo **Interactive** antes de crear personalizaciones.
- pedirás a Copilot que cree `quality-checks` y después se detenga para que la examines.
- ejecutarás las cuatro comprobaciones mediante los scripts incluidos y demostrarás que un argumento que indica un único archivo de pruebas selecciona solo ese archivo.
- guardarás un punto de control de la habilidad junto con la funcionalidad de filtrado.

## Escenario

Tailspin Toys necesita las mismas comprobaciones de calidad cada vez que cambia el filtrado. En lugar de explicar los comandos y requisitos previos en cada conversación, el equipo quiere una habilidad reutilizable. La crearás, examinarás sus scripts y verificarás que otra solicitud puede ejecutar las comprobaciones correctamente.

## Instrucciones, scripts y recursos

Las habilidades reúnen instrucciones de tareas reutilizables, scripts ejecutables y recursos de apoyo que un agente carga cuando los necesita. Los agentes personalizados definen roles especializados, instrucciones y herramientas disponibles. Son complementarios: un agente personalizado puede ejecutar scripts, incluidos los de una habilidad.

Una habilidad del repositorio reside en `.github/skills/<skill-name>/SKILL.md`, con `name` y `description` en el frontmatter e instrucciones en Markdown. Los scripts y otros recursos se encuentran junto a ese archivo. Pedirás a Copilot que genere `.github/skills/quality-checks/SKILL.md` y sus scripts incluidos, en lugar de copiar una solución preparada. La [especificación de Agent Skills][skill-spec] describe el formato.

Copilot utiliza la descripción de una habilidad descubierta para decidir cuándo cargarla. No supongas que una habilidad nueva se descubre inmediatamente en una sesión ya abierta; la sección de ejecución incluye una alternativa de lectura explícita. Un formato portable no elimina los requisitos previos del shell o del proyecto.

## Crear la habilidad

Vuelve a poner la sesión de filtrado en modo **Interactive** mediante el selector de modo antes de enviar la indicación. Mantén la copia de trabajo y la rama actuales. Si empezaste con una plantilla antigua que ya contiene esta habilidad, examínala y amplíala en lugar de sobrescribir tus personalizaciones.

```plaintext
Crea .github/skills/quality-checks/SKILL.md y cuatro scripts envoltorio para npm run lint, npm run test:unit, npm run test:e2e y npm run typecheck:all. Lee primero package.json, README, la configuración de pruebas y las instrucciones del repositorio.

Detecta este entorno. Crea SOLO scripts Bash .sh para macOS/Linux/WSL O scripts PowerShell .ps1 para Windows nativo; pregunta si no está claro. No crees ambos. Limita los scripts envoltorio a resolver la raíz del repositorio desde su propia ubicación, verificar que allí está el package.json de este proyecto e invocar npm. Si la raíz no es válida, falla con un mensaje claro. Admite cualquier directorio de trabajo y rutas con espacios. Conserva la salida y los códigos de salida de los fallos, incluidos los fallos de comandos nativos en PowerShell. Inserta el separador -- de npm exactamente una vez; quienes invoquen los scripts deben pasar directamente los argumentos de la herramienta, sin otro --. No gestiones puertos ni procesos.

Incluye en SKILL.md un frontmatter con name y description, instrucciones para ejecutar los cuatro scripts envoltorio, requisitos previos, resolución de problemas y ejemplos portables que incluyan un archivo existente de pruebas unitarias. Todos los ejemplos de Bash deben invocar bash explícitamente; nunca eludas la directiva de ejecución de PowerShell. Explica la reutilización de servidores de Playwright: detén solo los servidores que hayas iniciado realmente; en caso contrario, pregunta.

Crea únicamente la habilidad y los scripts necesarios. No ejecutes comprobaciones ni sondeos, no instales nada, no cambies código de la aplicación, no crees commits ni abras una PR. Detente para que pueda revisar los archivos.
```

## Examinar la habilidad

1. Abre **Changes** para revisar los archivos generados. También puedes utilizar **+**, **File** en el panel de revisión y después buscar `SKILL.md` o los nombres de los scripts.
2. Comprueba que `name` y `description` describen la habilidad y cuándo se aplica. Lee las instrucciones, no solo los metadatos.
3. Confirma que la secuencia de ejecución invoca realmente los scripts incluidos bajo `.github/skills/quality-checks/` para lint, pruebas unitarias, E2E y comprobación de tipos.
4. Examina en cada script envoltorio la resolución de la raíz relativa al script y la comprobación explícita de que el directorio calculado contiene el `package.json` previsto para esta copia de trabajo. Que un comando termine correctamente porque npm busca en directorios superiores no demuestra que la raíz sea correcta. Comprueba las rutas entre comillas, el reenvío de argumentos, la salida visible y los códigos de salida ante fallos; PowerShell debe propagar los fallos nativos de npm.
5. Comprueba el ejemplo documentado de un único archivo de pruebas unitarias. El script envoltorio inserta el separador `--` de npm, por lo que quienes lo invoquen pasan directamente los argumentos de la herramienta de destino sin otro separador. Mantén las instrucciones reutilizables sin rutas absolutas de la copia de trabajo específicas de una máquina. Pide a Copilot que corrija las carencias antes de ejecutar nada.
6. Limita los scripts a validar la raíz y el manifiesto y a ejecutar las comprobaciones npm existentes. Las decisiones sobre puertos y procesos corresponden a SKILL.md, no a código de gestión de procesos en shell. Confirma que solo se pueden detener servidores que el agente haya iniciado realmente; que coincidan el directorio de trabajo o el nombre del proceso no demuestra a quién pertenece. Los archivos entregados deben contener solo la habilidad, los scripts envoltorio necesarios y cualquier archivo auxiliar compartido que haga falta, sin archivos temporales de sondeo o depuración.

> [!NOTE]
> Tailspin Toys requiere actualmente Node.js 22.13 o posterior, las dependencias del proyecto y Chromium de Playwright para las comprobaciones E2E. Confirma los requisitos previos en README y `package.json` de tu copia de trabajo. Los requisitos previos ausentes o una directiva de ejecución de PowerShell que bloquee la ejecución necesitan una solución aprobada, no una instalación automática, una elusión de la directiva ni un cambio silencioso a npm directo.

## Ejecutar la habilidad

Confirma que el servidor de desarrollo de la lección anterior se ha detenido. Playwright compila y sirve una vista previa para E2E, pero su configuración local puede reutilizar un servidor en el puerto `4321`. Un servidor de otra copia de trabajo no proporciona pruebas de verificación válidas para tu funcionalidad.

Si la aplicación ofrece `/quality-checks`, selecciónalo para invocar explícitamente la habilidad descubierta e incluye la solicitud siguiente. Si no se ha descubierto, envía la misma solicitud directamente en esta sesión; leer la habilidad es una alternativa admitida en este ejercicio.

```plaintext
Lee .github/skills/quality-checks/SKILL.md y sigue sus instrucciones para validar la funcionalidad de filtrado en esta copia de trabajo. Primero examina el código de cada script envoltorio para verificar que calcula el directorio que contiene el package.json previsto para esta copia de trabajo y falla de forma explícita si la raíz no es válida, en lugar de depender de que npm descubra paquetes en directorios superiores. No muevas, renombres, elimines ni modifiques archivos del repositorio para simular fallos. Ejecuta realmente los scripts incluidos para lint, pruebas unitarias, pruebas de un extremo a otro y comprobaciones de tipos. Ejecuta también el ejemplo documentado de un único archivo de pruebas unitarias, pasando directamente los argumentos de la herramienta de destino porque el script envoltorio se encarga del separador -- de npm. Verifica en los resultados del ejecutor de pruebas que SOLO se ha ejecutado el archivo indicado e informa de su nombre y del número de archivos de prueba ejecutados. Mostrar los argumentos o devolver el código de salida 0 no demuestra por sí solo que la selección sea correcta.

Informa de cada invocación de script y su resultado, incluidos fallos, comprobaciones omitidas o requisitos previos ausentes. No sustituyas silenciosamente un script inutilizable de la habilidad por comandos npm directos. Identifica la copia de trabajo y el servidor que se prueban, detén solo los servidores que hayas iniciado y pregunta antes de instalar algo o detener otro proceso. No cambies código de la aplicación, no cambies de rama, no crees commits, no envíes cambios ni abras una solicitud de incorporación de cambios.
```

Examina las llamadas a herramientas y su salida. Los cuatro scripts deben ejecutarse realmente; una descripción de las comprobaciones o una comprobación omitida no equivale a superarlas. Para el ejemplo de un único archivo, compara el nombre de archivo solicitado con los resultados reales por archivo del ejecutor y el número comunicado: solo debe ejecutarse ese archivo. Mostrar los argumentos o devolver el código de salida 0 es insuficiente si también se ejecutaron otros archivos. Un fallo aporta información útil: corrige la habilidad o resuelve el bloqueo de configuración con aprobación y después repite las comprobaciones afectadas. No detengas procesos ajenos ni fuerces la resolución de un conflicto de puerto.

## Guardar un punto de control

Cuando hayas revisado la habilidad y sus resultados, autoriza un punto de control local:

```plaintext
Revisa las diferencias actuales y crea un commit de punto de control solo para los archivos de la habilidad quality-checks. Mantén la rama de filtrado existente. No envíes cambios ni crees una solicitud de incorporación de cambios.
```

## Resumen y pasos siguientes

Has creado, examinado y ejecutado una habilidad quality-checks reutilizable, incluido su ejemplo de prueba de un solo archivo. Los archivos de la habilidad acompañarán al filtrado, al perfil de QA y a las pruebas asociadas en la PR de funcionalidad de la Lección 8. Continúa en esta misma sesión con la [Lección 6 - Validar la funcionalidad con MCP de Playwright][next-lesson].

## Ejemplos adicionales de habilidades

Estos ejemplos de la comunidad son referencias, no tareas adicionales. Revisa sus requisitos previos y su comportamiento antes de adoptarlos:

- [Flujo de contribución: `make-repo-contribution`][contribution-example].
- [Documentos de requisitos: `prd`][prd-example].
- [Diagramas y un script de exportación incluido: `drawio`][drawio-example].
- [Pruebas de navegador: `webapp-testing`][browser-example].

El ejemplo de contribución original se llama `make-repo-contribution`; las plantillas antiguas de Tailspin utilizaban otro nombre, `make-contribution`. Este taller no depende de ninguna de esas habilidades de contribución.

[previous-lesson]: ../4-build-filtering/
[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
