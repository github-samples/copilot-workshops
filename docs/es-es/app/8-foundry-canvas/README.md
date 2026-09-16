---
title: "Opcional: Incorporar Foundry"
slug: es-es/app/8-foundry-canvas
description: "Crea un Backer Concierge basado en el catálogo con Microsoft Foundry Canvas, con puntos seguros para detenerte durante el recorrido."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/es-es/app/9-review/
  label: Repaso y pasos siguientes
next:
  link: /copilot-workshops/es-es/app/8-foundry-canvas/1-project-and-model/
  label: Preparar el proyecto y el modelo
---

Este recorrido opcional añade un **Backer Concierge** a Tailspin Toys mediante Microsoft Foundry Canvas en la aplicación GitHub Copilot. Parte de un experimento con un modelo basado en el catálogo, continúa con un agente hospedado y termina con una integración local en el sitio web.

## El recorrido

Cada módulo termina con un punto de control y un punto seguro para detenerte. Durante todo el recorrido se mantienen el mismo repositorio de Tailspin Toys, la misma rama del worktree, la misma sesión vinculada a la incidencia, el mismo proyecto de Foundry y la misma implementación del modelo.

- [Preparar el proyecto y el modelo][module-1] establece los límites del catálogo, crea el proyecto y la implementación del modelo, y los comprueba en Canvas.
- [Crear e implementar el agente][module-2] genera la estructura inicial de Backer Concierge, lo prueba en local, e implementa y vuelve a probar el agente hospedado.
- [Conectar el agente al sitio][module-3] añade un proxy local que protege las credenciales, un widget de chat accesible, pruebas de extremo a extremo y Agent merge.

> [!IMPORTANT]
> Microsoft Foundry Canvas y los agentes hospedados están en versión preliminar pública.
>
> Este recorrido crea recursos de Azure que generan costes, incluida una implementación de modelo y, a partir del módulo 2, un agente hospedado. Antes de crear recursos, es necesario aprobar la suscripción, la región, la cuota y el coste estimado. La limpieza también se aplica si te detienes tras crear únicamente el proyecto y el modelo.

1. Empieza por [Preparar el proyecto y el modelo][module-1] y realiza el trabajo en el repositorio de Tailspin Toys, no en este repositorio de contenido del taller.
2. En el punto en el que decidas detenerte —proyecto y modelo, implementación hospedada o integración completa—, registra el punto de control del módulo y sigue las instrucciones de limpieza comunes que aparecen a continuación cuando termines de experimentar. Para continuar más adelante después de la limpieza, tendrás que restaurar los recursos eliminados y volver a comprobar su configuración.

## Limpiar los recursos

La limpieza depende de hasta dónde hayas llegado. Si solo has creado el proyecto y el modelo, no necesitas `azure.yaml`, un entorno de `azd` ni un agente hospedado.

> [!WARNING]
> La eliminación de recursos es destructiva. En este taller solo se pueden eliminar recursos dedicados exclusivamente a él. Nunca se debe eliminar un grupo de recursos compartido; la alternativa segura es eliminar los recursos del taller de forma individual junto con el propietario de los recursos.

1. Detén desde sus terminales los procesos locales de Agent Inspector, Azure Function y el servidor de desarrollo de Astro que hayas iniciado. Registra los datos del punto de control que necesites antes de eliminar recursos de Azure.
2. En Azure Portal, confirma el identificador de la suscripción activa, el nombre exacto del grupo de recursos del taller y todos los recursos que contiene. Comprueba que el proyecto de Foundry y la implementación del modelo pertenecen a esta ejecución del taller. Si no tienes clara la suscripción, la propiedad o el contenido, detén la limpieza hasta aclararlos.
3. Elige la opción de limpieza correspondiente al punto en el que te hayas detenido. Si solo has completado el módulo 1, omite el paso siguiente y utiliza el paso 5; no crees `azure.yaml` ni inicialices `azd` solo para realizar la limpieza. Si has realizado una implementación con Canvas en el módulo 2 o 3, continúa con el paso 4.
4. Para una implementación hospedada, abre un terminal en el mismo worktree de Tailspin Toys que contiene el archivo `azure.yaml` en la raíz. Confirma que el entorno de `azd` seleccionado apunta a la suscripción y los recursos de esta ejecución, revisa los recursos que se van a eliminar y ejecuta lo siguiente solo cuando todos los destinos estén dedicados al taller:

   ```bash
   azd down --purge
   ```

5. Si solo has creado el proyecto y el modelo, o si el grupo de recursos dedicado al taller sigue existiendo después de `azd down`, vuelve a comprobar en el portal la suscripción, el nombre del grupo y la lista completa de recursos. Si todo el grupo está dedicado a esta ejecución y su nombre es exactamente `rg-tailspin-toys`, ejecuta lo siguiente. Si el nombre es distinto, utiliza el nombre dedicado que hayas verificado; si el grupo es compartido, no ejecutes este comando y coordina la limpieza individual de recursos con su propietario.

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

6. Verifica en Azure Portal que la eliminación finalice; `--no-wait` devuelve el control antes de que termine. Confirma que se han eliminado la implementación del modelo del taller y todos los recursos del agente hospedado, y ocúpate de los recursos restantes del taller que generen costes sin eliminar recursos compartidos.
7. Vuelve a [Repaso y pasos siguientes][core-review] cuando hayas completado el punto de control elegido y la limpieza.

## Recursos

La documentación de Microsoft describe Canvas, las implementaciones hospedadas y sus permisos.

- [¿Qué es Microsoft Foundry Canvas?][foundry-canvas]
- [Implementar el primer agente hospedado con Foundry Canvas][hosted-agent-quickstart]
- [Permisos de los agentes hospedados][hosted-agent-permissions]

[module-1]: ./1-project-and-model/
[module-2]: ./2-build-and-deploy/
[module-3]: ./3-connect-to-site/
[core-review]: ../9-review/
[foundry-canvas]: https://learn.microsoft.com/azure/foundry/agents/concepts/foundry-canvas
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=canvas
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
