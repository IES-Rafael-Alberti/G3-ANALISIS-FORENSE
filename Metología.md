# Desarrollo de una Metodología para la correcta aplicación del Análisis Digital Forense

Desarrollo de una metodología sólida destinada a la aplicación correcta y eficiente del análisis forense, así como de evidencias electrónicas

## Adquisición de evidencia digital

Cuando se proceda a extraer una evidencia, este proceso debe arrojar siempre resultado similares y verificables, independientemente de quién realice la susodicha recolección de pruebas. Una vez entendido este principio, se ha de **planificar el proceso de adquisición de evidencias**, siendo esto verdaderamente importante debido la posibilidad de encontrar múltiples fuentes de evidencia. Si se da este caso, es imperativo acudir a un plan bien organizado con el fin de priorizar unas fuentes sobre otras, estableciendo el orden en el que los datos deberían adquirirse. Factores importantes a tener en cuenta para la priorización incluyen los siguientes:

- **Valor probable.** Basándonos en la experiencia del analista, así como en su comprensión de la situación, este debería ser capaz de estimar el valor relativo probable de cada fuente potencial de datos.
- **Volatilidad.** El término Volatilidad hace referencia a los datos en un sistema activo que se pierden tras el apagado de un ordenador, o pasado un tiempo, aunque también podría producirse esta pérdida de datos debido a ciertas acciones llevadas a cabo en el sistema. Por esto mismo será de crucial importancia establecer un orden en la prioridad de obtención de evidencias, primando siempre los datos más volátiles sobre los menos.
- **Cantidad de esfuerzo requerido.** La cantidad de esfuerzo necesario para obtener diversas fuentes de datos puede variar ampliamente, dado que el esfuerzo no sólo incluye el tiempo invertido por los analistas, sino también los costos asociados con los equipos y servicios. Por ejemplo, adquirir datos del router de una red requeriría menos esfuerzo que obtener datos de un proveedor de servicios de Internet (ISP). En resumen, la dificultad y costo de adquirir datos pueden variar según la fuente de información.

Para llevar a cabo el **proceso de adquisición** o captura forense de las evidencias se debe incluir, según los casos: 

- Clonado forense. 
- Realización de imágenes completas o lógicas de la información de interés.

Los dispositivos que identifiquemos se encontrarán bien encendidos o apagados, y así deben permanecer, tomando un curso de acción distinto para cada una de ambas situaciones:

- *Encendido:* Se debe mantener la batería cargada y sin manipular, evitando tocar la pantalla táctil. Además, es necesario aislar el dispositivo de la red, usando los medios que se crean convenientes, como colocarlo en una Jaula Faraday, encendiendo un inhibidor de señal cerca del dispositivo o configurando el mismo en modo avión, evitando de este modo el intento de conexión de terceros. 
- *Apagado:* El dispositivo se mantendrá de ese modo, para así poder trabajar correctamente, evitando la sobreescritura. Luego se extraerá la batería y memorias externas.

Para la correcta labor de adquisición de evidencias, existen una serie de normas a tener seriamente en cuenta, dada la facilidad para destruir inadvertidamente las pruebas:

- No detenerse hasta completar la obtención de pruebas. El atacante pudo haber alterado el inicio, scripts o servicios, para así destruir la evidencia de apagado
- Tener cautela con los programas presentes en el sistema
- No ejecutar programas que modifiquen el tiempo de acceso de todos los archivos del sistema
- Cuando se trabaje con una red de dispositivos, se ha de tener en cuenta la posibilidad de activar un “interruptor de hombre muerto”, que es un sistema de detección de fallos con la capacidad potencial de eliminar cualquier actividad maliciosa. Esto puede suceder al desconectar la red o filtrar el tráfico
- Si es confrontado con la situación en la que deba elegir entre la recolección y el análisis, realice primero la recolección de evidencias y luego lleve a cabo el análisis

Una vez obtenida una imagen de la evidencia digital, se deberá verificar el hash, con el fin de autenticar y preservar la **integridad de los datos**. Se deberá corroborar también que dichos datos tengan el formato apropiado, fechas y horas consistentes, y que fue posible extraer toda la información.

Para resumir el apartado, tenemos el siguiente orden a seguir a la hora de llevar a cabo la adquisición de evidencias:
1. Planificación del proceso de adquisición.
2. Adquisición de datos.
3. Verificación de la integridad de los datos.

### Orden de Volatilidad

Como se explica en el punto anterior, durante el proceso de recolección de evidencias, siempre se debe proceder de lo volátil a lo menos volátil. A continuación, se muestra un ejemplo de orden de volatilidad para un sistema típico:

1. Registros, caché
2. Tabla de enrutamiento, caché ARP, tabla de procesos, estadísticas del núcleo y memoria
3. Sistemas de archivos temporales
4. Disco duro
5. Datos de registro remoto y monitorización relevantes para el sistema en cuestión
6. Configuración física y topología de la red
7. Medios de archivo

## Preservación y almacenamiento de evidencia

La correcta preservación y almacenamiento de la evidencia original recolectada asegura que éstas mantengan en todo momento su validez y confiabilidad, garantizando también que los estudios forenses llevados a cabo sobre las pruebas recabadas sean reproducibles por cualquier entorno de análisis forense o laboratorio designado para su análisis.

A fin de lograr este propósito, se deben tener en cuenta firmemente los principios siguientes a la hora de interactuar con las evidencias electrónicas:

- Necesidad de poseer protocolos detallados con el fin de garantizar la integridad de las pruebas objeto del estudio forense, contra la manipulación intencionada o “tampering”, las descargas electrostáticas, los campos magnéticos o la conexión accidental a redes inalámbricas.
- Los técnicos encargados de la primera respuesta sobre el estudio deberán hacer énfasis en almacenar las mismas de forma adecuada, a fin de preservar la integridad de las pruebas tanto como evitar la contaminación de evidencias externas al ámbito tecnológico tales como huellas, restos orgánicos o partículas diversas.
- El uso de una indumentaria adecuada por parte del personal técnico es imperativo, a fin de prevenir las descargas electrostáticas, así como de igual forma debe evitarse la utilización de equipos que emitan señales de radiofrecuencia, dado que estas podrían interferir con la escena de interés. Esto puede en ocasiones llevar a la necesidad de utilizar soportes aislados para prevenir interferencias externas en los datos originales.

Además de estos principios de actuación, el personal técnico encargado de salvaguardar las evidencias electrónicas debería seguir las pautas siguientes:

- Todas las evidencias encontradas deben precintarse y sellarse en soportes adecuados, poniendo atención a los dispositivos que requieran ser alimentados por una fuente de energía externa
- Todas las evidencias 