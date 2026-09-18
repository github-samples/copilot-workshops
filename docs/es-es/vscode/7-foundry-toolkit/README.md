---
slug: es-es/vscode/7-foundry-toolkit
title: "Opcional: Incorporar Foundry"
description: "Crea un Backer Concierge basado en el catálogo con VS Code y Microsoft Foundry Toolkit en tres módulos específicos."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← Lección anterior: Iterar sobre el trabajo de GitHub Copilot][previous-lesson] |
|:--|

El itinerario obligatorio de VS Code termina con el ejercicio 6. Esta ampliación opcional utiliza GitHub Copilot Chat y Microsoft Foundry Toolkit en VS Code para convertir el catálogo de Tailspin en un Backer Concierge, implementarlo como agente hospedado y conectarlo al sitio a través de un proxy local.

## Escenario

Los patrocinadores hacen preguntas que los filtros no pueden responder: ¿qué juego encaja con alguien a quien le encantan los juegos de palabras sobre git, o qué hace que un juego de puzles sea más adecuado que otro? Tailspin Toys necesita un asistente que recomiende títulos reales del catálogo, haga una pregunta aclaratoria cuando sea necesario y se gane la confianza de los usuarios al reconocer que las cifras de financiación u otros datos no están disponibles.

## Módulos

Cada módulo termina con un resultado funcional. Se mantienen el mismo repositorio del participante, la misma rama de funcionalidad y el mismo proyecto de Foundry durante los tres módulos; el proyecto no se vuelve a crear entre módulos.

| Módulo | Resultado al finalizar |
|--------|-----------------------|
| [1. Preparar un proyecto y un modelo][module-1] | Catálogo exportado y modelo implementado probado frente a las reglas de fundamentación |
| [2. Crear e implementar un agente][module-2] | Agente local depurado y agente hospedado probado |
| [3. Conectar el agente al sitio][module-3] | Proxy local y widget accesible probados de extremo a extremo |

> [!IMPORTANT]
> Microsoft Foundry Toolkit y los agentes hospedados están en versión preliminar pública. Estos módulos crean recursos de Azure facturables, incluidos una implementación de modelo y un agente hospedado. Los permisos de la suscripción, la disponibilidad regional, la cuota y el coste pueden limitar la participación.

## Antes de empezar

La ampliación parte de tu repositorio de Tailspin Toys, no del repositorio de documentación del taller.

1. Confirma que el trabajo obligatorio del taller está guardado, confirmado mediante un commit y enviado al repositorio remoto antes de empezar la funcionalidad opcional.
2. Empieza por [Preparar un proyecto y un modelo][module-1]. Si retomas el trabajo, vuelve a abrir tu repositorio de Tailspin Toys en la rama `foundry-agent-vscode` y confirma que el proyecto `tailspin-toys` y su implementación del modelo siguen existiendo en **Foundry Toolkit** > **My Resources**.
3. Si paras después de cualquier módulo, sigue las indicaciones de [Eliminar los recursos][cleanup], salvo que decidas conservarlos para el siguiente módulo y aceptes los costes continuados.

## Eliminar los recursos

Cuando termines de experimentar en cualquier punto de control, elimina los recursos de Azure para evitar costes no deseados. La eliminación afecta a recursos que necesitan los módulos posteriores, por lo que continuar después exige volver a crearlos.

> [!WARNING]
> Elimina `rg-tailspin-toys` solo si está dedicado a este ejercicio y no contiene recursos que quieras conservar. Al eliminar un grupo de recursos compartido, se eliminarían también recursos ajenos al taller.
>
> Si aprobaste otro nombre de grupo de recursos en el módulo 1, sustituye `rg-tailspin-toys` por ese nombre en todos los comandos siguientes.

1. Detén en su terminal cualquier sesión de depuración de Agent Inspector, host de Azure Functions o servidor de desarrollo de Astro que hayas iniciado.
2. Si implementaste el agente hospedado en el módulo 2, abre un terminal en el directorio del agente generado que contiene `azure.yaml`, selecciona el mismo entorno de `azd` y ejecuta:

   ```bash
   azd down --purge
   ```

3. Comprueba la suscripción seleccionada y si el grupo de recursos del taller sigue existiendo:

   ```bash
   az account show --output table
   az group exists --name rg-tailspin-toys
   ```

   Si el comando devuelve `false`, la eliminación ha terminado. Si devuelve `true`, inspecciona los recursos del grupo:

   ```bash
   az resource list --resource-group rg-tailspin-toys --output table
   ```

   Verifica que todos los recursos restantes pertenecen a este ejercicio. Si paraste después del módulo 1, el proyecto y el modelo de Foundry todavía deben eliminarse aunque no hayas implementado un servicio de `azd`.

4. Si el grupo de recursos dedicado al taller sigue existiendo y solo contiene recursos que quieres eliminar, ejecuta:

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

5. Como `--no-wait` devuelve el control antes de que termine la eliminación, vuelve a ejecutar el siguiente comando hasta que devuelva `false`:

   ```bash
   az group exists --name rg-tailspin-toys
   ```

## Recursos

- [Foundry Toolkit para Visual Studio Code][foundry-toolkit]
- [Información general de la extensión de agentes de Microsoft Foundry][foundry-extension]

| [Siguiente módulo: Preparar un proyecto y un modelo →][module-1] |
|--:|

[previous-lesson]: ../6-iterating/
[module-1]: 1-project-and-model/
[module-2]: 2-build-and-deploy/
[module-3]: 3-connect-to-site/
[cleanup]: #eliminar-los-recursos
[foundry-toolkit]: https://code.visualstudio.com/docs/intelligentapps/overview
[foundry-extension]: https://learn.microsoft.com/azure/developer/azure-developer-cli/extensions/azure-ai-foundry-extension
