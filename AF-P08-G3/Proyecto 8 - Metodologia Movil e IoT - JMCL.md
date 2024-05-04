# Metodologías de Adquisición aplicables a dispositivos móviles e IoT

## Metodología de Adquisición aplicable a dispositivos móviles

La adquisición de evidencias digitales, especialmente en dispositivos móviles, es un proceso meticuloso que requiere atención al detalle para preservar la integridad de la información. Aunque los sistemas operativos marcan los archivos eliminados como disponibles, no los borran completamente, lo que permite su recuperación con herramientas forenses. Para garantizar la trazabilidad y el borrado seguro de datos, se siguen protocolos específicos, incluyendo la copia bit a bit.

Factores Clave en la Adquisición de Evidencias:

- **Características del Dispositivo:** La identificación se realiza a través de características visibles y bases de datos, utilizando información como el IMEI y el ESN para determinar el fabricante y el modelo.
- **Modo Depuración USB:** Utilizado principalmente por desarrolladores, permite el acceso al sistema para la copia bit a bit a través de ADB, especialmente si el dispositivo tiene permisos de Root o Jailbreak.
- **Niveles de Extracción de Datos:**
    - ***Extracción Manual:*** Implica la visualización y grabación de la pantalla, limitada a la información visible actualmente en el dispositivo.
    - ***Extracción Física:*** Consiste en crear una imagen completa del dispositivo para análisis forense, utilizando comandos como dd en Linux para asegurar la copia y el borrado seguro. Este método permite buscar elementos eliminados, pero presenta una clara complejidad frente a a los otros métodos de adquisición y toma un mayor tiempo en su realización.
    - ***Extracción Lógica:*** Se realiza conectando el dispositivo a una estación de trabajo y utilizando comandos para enviar la información. Contrariamente al método anterior, es más sencillo de realizar, pero no permite el acceso a la misma cantidad de información.
    - ***Extracción del sistema de ficheros:*** Este método de adquisición de sistema de archivos permite obtener todos los archivos visibles en el sistema, excluyendo los eliminados o las particiones ocultas. Se aprovecha de los mecanismos integrados en el sistema operativo, como Android Device Bridge (ADB) en Android, para copiar los archivos.
    - ***Hex Dumping y JTAG:*** Acceso directo a la memoria flash para análisis y decodificación de datos.
    - ***Chip-Off:*** Consiste en extraer físicamente el chip de memoria del dispositivo y crear una imagen binaria de su contenido.
    - ***Micro read:*** Técnica avanzada que implica la extracción física del chip de memoria y la captura de cambios a nivel microscópico.

Cada método tiene sus propias ventajas y desafíos, y la elección depende de la situación específica y los recursos disponibles. Es fundamental aplicar funciones hash como MD5 o SHA-1 para mantener la integridad de los datos y realizar el análisis a partir de copias para evitar dañar el dispositivo original. La entrega de la imagen original al juzgado y la posibilidad de un contra-peritaje son pasos finales cruciales en el proceso de adquisición de evidencias digitales.

## Metodología de Adquisición aplicable a dispositivos IoT

La etapa de preservación, identificación y preprocesamiento en la metodología forense para dispositivos IoT busca identificar las fuentes de evidencia, lo cual puede ser desafiante debido a la diversidad de dispositivos y la gran cantidad de datos que generan. Se propone abordar esta identificación en dos niveles, en el primero se buscará la identificación de patrones anómalos, mientras que en el segundo nos centraremos en los agentes identificados.

### Fase 1

Utiliza inteligencia artificial (IA), específicamente algoritmos de Machine Learning. Estos algoritmos pueden reconocer patrones y comportamientos anómalos, lo que ayuda a determinar los agentes involucrados en un incidente. Además, la aplicación de la inteligencia artificial puede redundar en nuestro beneficio, proporcionando efectividad, precisión y reducción de costes, respecto a la realización manual de esta misma labor. Dentro del Machine Learning se distinguen cuatro grupos principales: supervisados, semi-supervisados, por refuerzo y no supervisados.

- **Supervisados:** Utilizan datos etiquetados para predecir nuevos eventos. Ejemplos incluyen árboles de decisión, regresión logística, SVM, Naive Bayes y Redes Neuronales.
- **Semi-supervisados:** Usan tanto datos etiquetados como no etiquetados en el entrenamiento.
- **Por refuerzo:** Basan su funcionamiento en prueba y error, penalizando comportamientos no deseados y recompensando los correctos.
- **No supervisados:** Realizan predicciones sin datos etiquetados, como K-means, DBSCAN, One-Class SVM e Isolation Forests.

Se selecciona el algoritmo de Isolation Forests debido a su capacidad para trabajar con grandes volúmenes de datos de manera no supervisada y su eficiencia en la detección de anomalías. Este algoritmo mejora la capacidad de manejar la heterogeneidad y gran cantidad de datos presentes en los dispositivos IoT, además de ofrecer una buena precisión de predicción y tiempos de ejecución óptimos en comparación con otros algoritmos evaluados.

Hemos de remarcar la necesidad de identificar la Infraestructura IoT, lo que implica observar el entorno para detectar objetos relevantes, especialmente la infraestructura de red y servicios en las cuatro capas del modelo IoT. Se identifican los servicios en la nube consumidos, así como los recursos distribuidos bajo responsabilidad del usuario.

### Fase 2

La metodología propuesta introduce un nivel adicional que utiliza inteligencia artificial para identificar fuentes de evidencia en sistemas IoT, con el fin de detectar anomalías que puedan constituir evidencias para apoyar o refutar la hipótesis de un incidente. Se recomienda el uso de algoritmos de Machine Learning supervisados, como los basados en árboles de decisión, por su capacidad explicativa y facilidad de entrenamiento. Estos algoritmos procesarán datos previamente analizados y etiquetados.

En esta fase, se llevarán a cabo cuatro actividades principales:

- **Detección de la Infraestructura:** Identificación de los componentes del entorno IoT, ajustando la infraestructura inicialmente concebida.
- **Extracción y Adquisición de Objetos:** Se sigue un protocolo estricto que asegura la trazabilidad de la evidencia, con tareas técnicas adecuadas para la preservación y transporte.
- **Validación y Resguardo:** Incluye la creación de imágenes forenses, su encriptación y registro seguro.
- **Supervisión del Transporte:** Se cuida la entrega de evidencias a terceros, asegurando el cumplimiento de los criterios de resguardo y preservación.

Es crucial considerar si la adquisición de datos será en vivo, lo que permite acceder a datos en memoria o en tránsito pero con una extracción más complicada, o post-mortem, que facilita un análisis más profundo de los datos apagados. También es importante definir si se trabajará con una granularidad detallada o general de los datos.

- ***Post-Mortem:*** Este permite un análisis más profundo de los datos.
- ***Análisis en vivo:*** Esta clase de análisis brindan la oportunidad de acceder a los datos en memoria, tanto en tránsito como los no cifrados. 

La privacidad y protección de datos deben respetarse de acuerdo con la legislación local y del Cloud. En España, esto implica cumplir con la Ley Orgánica 3/2018 y el RGPD en Europa. Aspectos clave incluyen el deber de confidencialidad, la transparencia y el tratamiento adecuado de los datos.

En la investigación forense digital, es esencial obtener consentimiento para el uso de datos, implementar medidas de seguridad para proteger los datos y mantener la transparencia durante la investigación. Para mitigar los Data Leaks, se sugiere verificar las comunicaciones de dispositivos IoT contra bases de datos de IoC para identificar posibles compromisos.

Finalmente, la normativa ISO/IEC 27037 establece que las evidencias deben ser recolectadas de manera no intrusiva, que el proceso debe ser auditable y que las técnicas utilizadas deben ser reproducibles y defensibles. Este enfoque subraya la importancia de un manejo cuidadoso de la privacidad y la legalidad en la adquisición de evidencias en investigaciones forenses digitales.

## Diferencias entre ambos

Las metodologías forenses de adquisición en dispositivos móviles e IoT tienen diferencias clave debido a la naturaleza de los dispositivos y los datos que manejan. Algunas de las más importantes son las siguientes:

- En dispositivos móviles, la adquisición de datos volátiles puede ser más sencilla debido a la presencia de interfaces de usuario y sistemas operativos estánda, sin embargo, en los dispositivos IoT la adquisición de datos volátiles puede ser más desafiante debido a la diversidad de dispositivos y la falta de interfaces estándar.
- La adquisición en dispositivos móviles es generalmente más directa, mientras que en IoT puede ser más compleja debido a la variedad de tecnologías y la necesidad de considerar la interconectividad de los dispositivos.
- Los dispositivos móviles suelen tener metadatos y registros detallados de las actividades del usuario, mientras que los dispositivos IoT pueden no tener metadatos tan ricos o pueden presentar desafíos como diferencias horarias en los registros.

Además, debemos remarcar los siguientes aspectos clave de ambos tipos de dispositivos. Los dispositivos móviles suelen presentar las siguientes características:

- Los dispositivos móviles suelen tener una gran capacidad de almacenamiento interno y externo, lo que permite almacenar una amplia variedad de datos personales y aplicaciones.
- Operan con sistemas operativos conocidos como Android o iOS, lo que facilita el uso de herramientas forenses estándar para la adquisición de datos.
- Poseen interfaces de usuario que permiten la interacción directa, lo que puede simplificar la extracción de datos.
- Sus metodologías de extracción incluyen adquisición manual, física, adquisición lógica y adquisición del sistema de ficheros, con herramientas y técnicas bien establecidas.

Como veremos a continuación, los dispositivos IoT presentan características muy diferentes:

- Los dispositivos IoT pueden variar desde sensores simples hasta electrodomésticos inteligentes, cada uno con diferentes capacidades de almacenamiento y procesamiento.
- Pueden operar con una variedad de sistemas operativos, muchos de los cuales son específicos del fabricante o del dispositivo, lo que puede complicar la adquisición de datos.
- Esta clase de dispositivos suelen estar diseñados para conectarse y comunicarse con otros dispositivos, lo que puede requerir un enfoque de adquisición que tenga en cuenta la red de dispositivos interconectados.
- Muchos dispositivos IoT carecen de una interfaz de usuario tradicional, lo que puede requerir métodos indirectos para la adquisición de datos.

## Referencias

- https://riunet.upv.es/bitstream/handle/10251/186198/Sorribas%20-%20Definicion%20de%20una%20metodologia%20para%20el%20analisis%20informatico%20forense%20en%20entornos%20IoT.pdf?sequence=1&isAllowed=y
- https://publicaciones.sadio.org.ar/index.php/JAIIO/article/download/295/242#:~:text=Metodolog%C3%ADas%20para%20el%20An%C3%A1lisis%20Forense%20de%20IoT&text=El%20proceso%20forense%20incluye%20seis,y%20Presentaci%C3%B3n%20de%20la%20Evidencia.
- https://www.incibe.es/incibe-cert/blog/herramientas-para-realizar-analisis-forenses-dispositivos-moviles
- https://openaccess.uoc.edu/bitstream/10609/45641/6/malvarezmuTFG0116memoria.pdf
- https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S1405-55462022000100441