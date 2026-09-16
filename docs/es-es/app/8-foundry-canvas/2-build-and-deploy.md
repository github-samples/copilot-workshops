---
title: "Crear e implementar el agente"
description: "Genera la estructura inicial de Backer Concierge en Canvas, inspecciónalo en local e impleméntalo y vuelve a probarlo en Foundry."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/es-es/app/8-foundry-canvas/1-project-and-model/
  label: Preparar el proyecto y el modelo
next:
  link: /copilot-workshops/es-es/app/8-foundry-canvas/3-connect-to-site/
  label: Conectar el agente al sitio
---

Este módulo convierte el proyecto, la implementación del modelo y el catálogo de [Preparar el proyecto y el modelo][previous-module] en un Backer Concierge hospedado mediante Microsoft Foundry Canvas.

Al terminar, tendrás:

- La estructura inicial de un agente con los datos del catálogo empaquetados y pruebas específicas.
- Evidencias locales para cada criterio de aceptación del catálogo y de la conversación.
- Una versión del agente implementada y probada de nuevo en Foundry.

## Escenario

Tailspin Toys necesita un asistente que pueda responder a preguntas reales sobre el catálogo, reconocer cuándo falta información y recordar los juegos mencionados en una conversación. El servicio debe ganarse esa confianza antes de formar parte del sitio de la tienda.

## Retomar el proyecto y preparar las herramientas de implementación

La inspección y la implementación del agente hospedado utilizan Azure Developer CLI a través de Canvas; se reutilizan el proyecto y el modelo de Foundry existentes.

1. Retoma el mismo repositorio de Tailspin Toys, la misma rama del worktree y la misma sesión de la incidencia **Add a Backer Concierge assistant for catalog questions** del módulo 1. Confirma que se conservan `db/catalog.json`, la suscripción registrada, el grupo de recursos dedicado, el proyecto de Foundry y la implementación del modelo. Si se eliminaron los recursos, repite primero la [configuración del proyecto y del modelo][previous-module] que corresponda; de lo contrario, no los vuelvas a crear.
2. Instala [Azure Developer CLI][install-azd] y verifica que esté instalada la versión 1.27.1 o posterior:

   ```bash
   azd version
   ```

3. Selecciona **+**, selecciona **Terminal** e inicia sesión en Azure Developer CLI; completa la autenticación en el navegador cuando se te solicite:

   ```bash
   azd auth login
   ```

4. Ejecuta `azd config show` para verificar la suscripción de Azure. Si está vacía o es incorrecta, actualízala con `azd config set defaults.subscription <subscription-id>` y vuelve a ejecutar `azd config show` para confirmar el cambio.
5. Vuelve a abrir Microsoft Foundry Canvas en esta sesión y confirma que aparecen el mismo proyecto **tailspin-toys** y la misma implementación en **Models**. Comprueba la suscripción, la región, la cuota y el coste estimado antes de cada cambio que genere costes.

> [!IMPORTANT]
> Microsoft Foundry Canvas y los agentes hospedados están en versión preliminar pública. Las llamadas locales al modelo y los recursos hospedados de Azure pueden generar costes; las [instrucciones de limpieza comunes][cleanup] también se aplican si te detienes en una implementación hospedada.

## Generar la estructura inicial de Backer Concierge

Canvas genera el código, la estructura de carpetas y el archivo `azure.yaml` de la raíz que conectan Backer Concierge con la implementación del modelo existente.

6. En la versión preliminar de **Create new hosted agents**, introduce:

   ```plaintext
   Scaffold a hosted agent named Backer Concierge in agent/backer-concierge, connected to the tailspin-toys project and the model deployment I just confirmed. Use Microsoft Agent Framework with the Responses API. Ground it in db/catalog.json and ensure it meets the acceptance criteria in this issue. Keep a single azure.yaml at the repository root with the hosted-agent service pointing to agent/backer-concierge. Make sure the deployed agent includes the catalog data it needs, and add focused tests.
   ```

   Canvas envía a Copilot la indicación y el contexto de la suscripción actual y del proyecto de Foundry. Busca ejemplos de Agent Framework + Responses API; puede aparecer una opción como **Agent with Local Tools (Responses, Agent Framework, Python)**.

   ![Generar la estructura inicial del agente Backer Concierge en Canvas](../../../_images/app-8-scaffold-backer-concierge.png)

7. Revisa los cambios de Copilot en la pestaña **Files** y compáralos con este punto de control. Los nombres de los archivos generados dentro de `src` pueden variar, pero los límites del proyecto y la ubicación de `azure.yaml` deberían coincidir:

   - El agente reside en `agent/backer-concierge`.
   - Un único archivo `azure.yaml` en la raíz del repositorio contiene un servicio con `host: azure.ai.agent`.
   - El agente que se va a implementar incluye su propia copia generada del catálogo.
   - Las pruebas específicas cubren los requisitos para que las respuestas se basen en el catálogo.
   - No se incluyen credenciales ni archivos de entorno locales.

   ```text
   tailspin-toys/
   ├── azure.yaml
   ├── agent/
   │   └── backer-concierge/
   │       └── requirements.txt
   ├── db/
   │   └── catalog.json
   └── src/
   ```

8. Comprueba en **Build current hosted agent** la conexión con el proyecto y el modelo existentes. Pide a Copilot que ejecute las pruebas específicas y corrija cualquier fallo antes de continuar con **Deploy and test**.

## Inspeccionar el agente en local

**Inspect Locally** ejecuta `azd ai agent run` en el terminal integrado de Copilot, espera a que se inicie el agente hospedado y abre Agent Inspector integrado.

9. En **Deploy and test**, selecciona **Inspect Locally** y espera a que se abra Agent Inspector.

> [!NOTE]
> La primera ejecución local puede tardar varios minutos mientras `azd` crea un entorno e instala las dependencias.

10. Si el inspector no puede conectarse, confirma que ningún otro proceso esté utilizando el puerto necesario, envía el error a Copilot y vuelve a intentarlo cuando se haya solucionado el problema.
11. Prueba una **recomendación basada en el catálogo** en Agent Inspector:

    ```text
    I love puzzle games about tracking down bugs. What should I back?
    ```

    Resultado esperado: menciona solo títulos reales del catálogo y utiliza la información correcta de cada título.

    ![Recomendación basada en el catálogo en Agent Inspector](../../../_images/app-8-grounded-recommendation.png)

12. Prueba una **pregunta trampa para detectar alucinaciones**:

    ```text
    How much has Pipeline Conquest raised so far, and how many backers does it have?
    ```

    Resultado esperado: explica que el catálogo no registra la financiación ni los patrocinadores y, después, ofrece información que sí está disponible.

13. Prueba la **presión para responder sobre juegos ajenos al catálogo**:

    ```text
    Do you have Wingspan? If not, what's the closest thing you've got?
    ```

    Resultado esperado: indica que Wingspan no está en el catálogo, no lo describe con conocimientos externos y redirige la respuesta hacia títulos reales de Tailspin.

14. Prueba una **petición imprecisa**:

    ```text
    Recommend me something good.
    ```

    Resultado esperado: hace una pregunta breve para aclarar la petición y todavía no recomienda ningún título.

15. Prueba la **exactitud de la clasificación**:

    ```text
    What are your three highest rated games?
    ```

    Resultado esperado: devuelve las tres entradas del catálogo mejor valoradas en el orden correcto y con las valoraciones correctas.

16. Prueba la **continuidad de la conversación** enviando estas indicaciones en la misma conversación:

    ```text
    Show me two highly rated strategy games.
    ```

    ```text
    Which of those has the higher rating?
    ```

    Resultado esperado: la segunda respuesta se refiere solo a los dos títulos de la primera respuesta y compara correctamente sus valoraciones del catálogo.

17. Compara cada respuesta con `db/catalog.json` y con los criterios de aceptación de la incidencia. Confirma que el agente nunca inventa juegos, editores, valoraciones, importes recaudados, cifras de patrocinadores, precios, números de jugadores, duraciones de partida ni fechas de lanzamiento. Si Agent Inspector comunica un error o una respuesta rebasa los límites de la información del catálogo, copia el resultado en el área de indicaciones de Canvas y pide a Copilot que lo corrija. Reinicia la inspección local y vuelve a ejecutar la prueba fallida después de cada cambio; después, confirma que las seis comprobaciones se superan antes de implementar.

## Implementar el agente hospedado y volver a probarlo

Canvas utiliza `azd` para implementar el agente probado. Foundry empaqueta el código fuente del servicio, resuelve las dependencias, lo compila de forma remota y lo publica en Foundry Agent Service.

18. Confirma la suscripción seleccionada, el proyecto existente, la implementación del modelo y los recursos de destino dedicados. En Canvas, en **Deploy and test**, selecciona **Deploy to Foundry**. Revisa la indicación que inserta en el chat y aprueba la implementación solo después de comprobar los destinos y el coste.

    ![Indicación Deploy to Foundry en el lienzo](../../../_images/app-8-deploy-to-foundry.png)

19. Comprueba que aparezcan una confirmación de la implementación, la versión del agente, el estado y un enlace al área de pruebas del agente en Foundry. Si la implementación falla, envía el error a Copilot y resuélvelo en el mismo proyecto antes de volver a intentarlo a través de Canvas.
20. Selecciona **Test in Foundry Portal** desde Canvas para abrir el área de pruebas del agente implementado. Vuelve a ejecutar las seis comprobaciones de aceptación de los pasos 11–16 con esta versión implementada; mantén las dos indicaciones enlazadas en una misma conversación para comprobar la continuidad. Compara las respuestas con el catálogo; si falla alguna comprobación, pide a Copilot que lo corrija, vuelve a ejecutar las pruebas locales, implementa de nuevo a través de Canvas y vuelve a probar la versión hospedada.

## Punto de control y pasos siguientes

El resultado para continuar es un agente hospedado probado; todavía no se requiere la integración con el sitio web.

21. Registra en la misma sesión de la incidencia las pruebas específicas superadas, los resultados de la inspección local, los resultados de las nuevas pruebas de la versión hospedada, la versión del agente, el estado y los datos de conexión del lado del servidor, sin registrar credenciales. Conserva el mismo repositorio de Tailspin Toys, la misma rama del worktree, la misma sesión de la incidencia, el mismo proyecto de Foundry y la misma implementación del modelo del módulo 1.
22. Continúa con [Conectar el agente al sitio][next-module] desde este mismo punto de control, o detente en la implementación hospedada y sigue las instrucciones de [Limpiar los recursos][cleanup] cuando termines. El proxy y el widget del sitio no son requisitos previos para la limpieza.

[previous-module]: ../1-project-and-model/
[next-module]: ../3-connect-to-site/
[cleanup]: ../#limpiar-los-recursos
[install-azd]: https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd
