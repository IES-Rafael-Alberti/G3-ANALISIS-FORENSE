# Índice

1. [Resumen ejecutivo](#resumen-ejecutivo)
2. [Introducción](#introducción)
3. [Investigación teórica](#investigación-teórica)
4. [Evaluación de herramientas y métodos](#evaluación-de-herramientas-y-métodos)
   - [Métodos de extracción de vestigios](#métodos-de-extracción-de-vestigios)
   - [Herramientas para IoT](#herramientas-para-iot)
   - [Herramientas para móviles](#herramientas-para-móviles)
5. [Consideraciones legales y éticas](#consideraciones-legales-y-éticas)
6. [Anexos](#anexos)

# Resumen ejecutivo

En el documento se aportan diferentes perspectivas del análisis forense de smartphones y dispositivos IoT. Se discuten varios métodos de adquisición de datos, incluyendo la adquisición física, la adquisición lógica y la adquisición del sistema de ficheros.

Durante el proceso de investigación, se termina concluyendo que no existen herramientas específicas para la adquisición de evidencias forenses de IoT, lo cual si uno para a pensarlo es lógico teniendo en cuenta la gran variabilidad en la arquitectura y hardware de este tipo de dispositivo. Aún no habiendo herramientas específicas, debido a la sólida naturaleza general y compatible de herramientas como FTK Imager o Wireshark podemos valernos de ellas para conseguir resultados válidos a la hora de trabajar con estos dispositivos. 

En cuanto a la adquisición de datos en dispositivos móviles y smartphones, se describen varias herramientas como Android Debug Bridge (ADB), AFLogical OSE, Andriller CE, LIME- Linux Memory Extractor y WhatsApp Xtract. Para la práctica de la adquisición realizada para este mismo informe, se utilizaron ADB para realizar una captura de todas las aplicaciones, datos de las aplicaciones y del sistema.

Se abordan también las consideraciones legales y éticas de las adquisiciones forenses. Se hace referencia al Reglamento General de Protección de Datos (GDPR), a la guía de la ACPO entre otras. Se destaca la importancia de la transparencia en el proceso de recopilación de datos y se discuten las implicaciones éticas de la aplicación de modelos de Machine Learning para procesar y detectar patrones en los datos de un usuario.

En resumen, el documento proporciona una visión general de las metodologías, herramientas, una pequeña práctica de adquisición de un smartphone y consideraciones éticas y legales en el análisis forense de smartphones y dispositivos IoT.

# Introducción

En este documento se realiza una investigación acerca del proceso de análisis forense en smartphones y dispositivos IoT. 

Se discuten y exponen distintos aspectos como metodologías para realizar adquisiciones, herramientas comunes que se utilizan, tipos y variantes de adquisición, añadiendo también comentarios y ciertas referencias sobre los aspectos legales y éticos del análisis forense en este tipo de dispositivos.

# Investigación teórica

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

## Métodos de extracción de vestigios

- **Adquisición física:** Es el método más utilizado. Consiste en realizar una réplica idéntica del original por lo que se preservan la totalidad de las evidencias potenciales. Este procedimiento presenta la ventaja de que es posible buscar elementos eliminados. Su desventaja principal es su complejidad respecto a los otros métodos y el tiempo que lleva su realización.

- **Adquisición lógica:** Consiste en realizar una copia de los objetos almacenados en el dispositivo. Para ello, se utilizan los mecanismos implementados de manera nativa por el fabricante, es decir, aquellos que son utilizados de manera habitual para sincronizar el terminal con un ordenador. de modo que se solicita la información deseada al sistema operativo del dispositivo móvil.

- **Adquisición del sistema de ficheros:** Permite obtener todos los ficheros visibles mediante el sistema de ficheros, lo que no incluye ficheros eliminados o particiones ocultas. Dependiendo del tipo de investigación puede resultar suficiente utilizar este método. Para llevarlo a cabo se aprovecha de los mecanismos integrados en el sistema operativo para realizar el copiado de los ficheros, Android Device Bridge (ADB) en el caso de Android. Mediante este método es posible recuperar cierta información eliminada ya que algunos sistemas operativos como es el caso de Android e iOS se valen de una estructura que utiliza bases de datos SQLite para almacenar gran parte de la información. Cuando se eliminan registros de los ficheros, únicamente se marcan como disponibles para sobrescritura, por lo que temporalmente siguen estando disponibles y por tanto es posible recuperarlos.

### Herramientas para IoT

Se ha investigado sobre herramientas IoT para la adquisición de evidencias pero teniendo en cuenta los artículos en internet, se ha llegado a la conclusión de que a día de hoy no existen herramientas especificas para la adquisición de evidencias forenses de IoT.

Dependiendo del tipo de dispositivo IoT se adquirirá de una manera u otra, teniendo en cuenta si el dispositivo puede conectarse a un equipo informático como un ordenador o si solo se permite de manera inalámbrica. En caso de poder conectarse a un ordenador, la adquisición de evidencias se hará vía FTK Imager o volatility.

En caso de que los dispositivos IoT no puedan conectarse directamente a un equipo informático, la adquisición se hará mediante Wireshark pudiendo obtener registros de conexiones o peticiones.

### Herramientas para móviles

En este punto se especifican una serie de herramientas Open Source y gratuitas para la adquisición de datos en dispositivos móviles.

#### Android Debug Bridge (ADB)

Es una herramienta mediante la cual por comandos crea un puente entre nuestro ordenador y el teléfono móvil. Podemos traer archivos del móvil hacia nuestro ordenador gracias a ello. 

Para poder usar ADB con el dispositivo móvil, necesitamos activar la depuración USB e instalar los drivers ADB universales. Tiene una serie de comandos sencillos que permiten desde crear una shell para el dispositivo móvil como extraer o subir archivos al dispositivo móvil.

Muchas de las herramientas que se mencionarán en los siguientes puntos, utilizan o necesitan de esta herramienta instalada en nuestro ordenador. 

#### AFLogical OSE - Open source Android Forensics app and framework

Esta herramienta es una apk que podemos instalar en nuestro dispositivo móvil para adquirir datos. Se debe ejecutar en el dispositivo o usando adb shell.

En el dispositivo android del que queramos hacer la adquisición, debemos abrir la aplicación y elegir los datos que deseamos etraer, simplemente tendremos que seguir las instrucciones dadas por la propia apliación. Se debe tener una tarjeta SD en el dispositivo para extraer los datos en ella.

Luego copiamos estos datos a nuestro ordenador para analizar estos datos o usamos adb pull. Los datos pueden ser registros de llamadas, contactos, aplicaciones, mensajes de texto o audiovisuales… Esta información será recuperada o bien conectada a una tarjeta en un dispositivo externo o a través del ADB.

#### Andriller CE

Andriller CE es una herramienta para la adquisición de dispositivos móviles. Realiza adquisiciones no destructivas, solidas y de solo lectura desde dispositivos Android. Contiene decodificadores personalizados para datos de bases de datos de android para decodificar comunicaciones. Las extraciones y los decodificadors producen informes en formatos HTML y Excel.

**Características:**

- Extracción y decodificación de datos automatizada
- Extracción de datos de dispositivos no rooteados mediante Android Backup (versiones de Android 4.x, soporte variado/limitado)
- Extracción de datos con permisos de root: demonio ADB raíz, modo de recuperación CWM o binario SU (Superusuario)
- Análisis y decodificación de datos para estructura de carpetas, archivos Tarball (de copias de seguridad de nanddroid) y copia de seguridad de Android ( archivos backup.ab )
- Selección de decodificadores de bases de datos individuales para aplicaciones de Android Descifrado de bases de datos archivadas cifradas de WhatsApp (.crypt a .crypt12, debe tener el archivo de clave correcto )
- Cracking de pantalla de bloqueo para patrón, PIN y contraseña.
- Descomprimiendo los archivos de copia de seguridad de Android
- Captura de pantalla de la pantalla de un dispositivo

#### LIME- Linux Memory Extractor

Esta herramienta Open Source permite la adquisición de memoria volátil desde dispositivos basados en linux y android. Es la primera herramienta que permite captura de memoria completa en dispositivos Android. Minimiza su interacción entre el usuario y los procesos del espacio del kernel durante la adquisición lo que permite crear capturas de memorias más sólidas desde el punto de vista forense.

**Características**

- Adquisición completa de memoria de Android
- Adquisición a través de interfaz de red
- Huella mínima del proceso
- Hash de memoria volcada

#### WhatsApp Xtract

Es una herramienta que permite extraer del dispositivo móvil todas las conversaciones en el ordenador. Esta aplicación de Windows trabaja con archivos .bat utilizandolo con la ruta "/sdcard/WhatsApp/Databases/msgstore.db.crypt" desde la cual tendremos que ejecutar la herramienta. Requiere tener instalado Active Python.

# Evaluación de herramientas y métodos

# Consideraciones legales y éticas

En el aspecto legal y ético de las adquisiciones forenses de los dispositivos IoT y móviles debe considerarse que, para la extensión de su uso y presencia en nuestras vidas, existe una falta de reglas universales y regulaciones aplicables a los mismos debido al vertiginoso ritmo de avance en las nuevas tecnologías y al contrantes con el inherente ritmo más pausado que la elaboración de leyes y reglamentos requiere.

Aún así, existen regulaciones y marcos legales, de los cuáles principalmente se utiliza el Reglamento General de Protección de Datos (GDPR en adelante), ya que los datos adquiridos tanto en un dispositivo IoT como un dispositivo móvil pueden ir en contra de la privacidad de los usuarios, es por ello que las organizaciones que custodian estos datos deben asegurarse de que solo personas autorizadas tienen acceso a los mismos (Sedky, M. 2020). 

En nuestra búsqueda de información una guía elaborada por la ACPO (*Association of Chief Police Officers*, una asociación de policías perteneciente a Reino Unido) aparece múltiples veces y básicamente es una recopilación de buenas prácticas a la hora de realizar adquisiciones forenses que aconsejan usar a todos los profesionales forenses digitales.

Debido a que pueden existir distintos requerimentos legales en donde un crimen sea perseguido y/o cometido, aparecen desafíos legales a la hora de establecer marcos generales. Sin embargo, existen organizaciones como la previamente mencionada ACPO, el Instituto Nacional de Estándares y Tecnología (NIST) o el Subgrupo G8, el cual es un grupo informal conformado por las mayores democracias industriales del mundo como son Canada, Francia, Italia, Japón, Rusia, Reino Unido y Estados Unidos (Induruwa, A. 2009). Este último tiene como objetivo el otorgar a otros países herramientas y ayuda para llevar a cabo una competencia con el "*High-tech crime*", entre su trabajo se pueden destacar medidas como las siguientes (Induruwa, A. 2009): 

- Negociación de principios ampliamente aceptados y plan de acción para combatir el delito de alta tecnología, posteriormente adoptado por los Ministros de Justicia y Asuntos Internos del G8, respaldado por los Jefes de Estado del G8 y reconocido por otros foros internacionales.
- Varios documentos de mejores prácticas, incluyendo guías para la seguridad de las redes informáticas, solicitudes internacionales de asistencia, redacción legislativa y rastreo de comunicaciones en red a través de las fronteras.
- Evaluaciones de amenazas e impacto a la aplicación de la ley de nuevas tecnologías inalámbricas, cifrado, virus, gusanos y otro código malicioso.

Según la información recaba en el artículo de Sedky, M. 2020, los usuarios tienen derecho a acceder a sus datos personales en todo momento y a que el proceso de sus datos por parte de los analistas forenses sea transparente, incluyendo aspectos sobre cómo se lleva a cabo la recopilación, el uso, divulgación y almacenamiento de su información personal. la responsabilidad en el tratamiento de estos datos recae principalmente en el investigador forense, que en caso de incumplir alguna ley de protección de datos puede enfrentar grandes multas. 

Con el aspecto ético podemos destacar la reciente aplicación de modelos de Machine Learning para procesar y detectar patrones en los datos de un usuario, llegando a crear perfiles de individuos a través del procesamiento probabilístico de sus datos personales. Esto puede llevar implicaciones éticas serias como por ejemplo que se elaboren estádisticas o gráficos de información acerca del comportamiento de un individuo y se le muestre a un juez como prueba en un juicio: El desconocimiento del funcionamiento de las tecnologías de Machine Learning o IA pueden llevar a una toma de conclusiones muy sesgada e inválida.

# Referencias

- Induruwa, A. (2009). 'Mobile phone forensics: an overview of technical and legal aspects', *Int. J. Electronic Security and Digital Forensics*, Vol. 2, No. 2, pp.169–181.

- Sedky, M. (2020). The Forensic Swing of Things: The Current Legal and Technical Challenges of IoT Forensics. Staffordshire University.

- Asier, M. (23/02/2016) Herramientas para realizar análisis forenses a dispositivos móviles.Recuperado de [https://www.incibe.es/incibe-cert/blog/herramientas-para-realizar-analisis-forenses-dispositivos-moviles](https://www.incibe.es/incibe-cert/blog/herramientas-para-realizar-analisis-forenses-dispositivos-moviles)

- Nowsecure (s.f.) Herramienta android-forensics. Recuperado de [https://github.com/nowsecure/android-forensics](https://github.com/nowsecure/android-forensics)

- Den4uk (s.f.) Herramienta andriller. Recuperado de [https://github.com/den4uk/andriller](https://github.com/den4uk/andriller)

- Eduardo, S. (01/10/2018) Herramientas para análisis forenses a dispositivos móviles. Recuperado de [https://peritos-informaticos.com/blog/herramientas-analisis-forense-moviles/](https://peritos-informaticos.com/blog/herramientas-analisis-forense-moviles/)

- Ricardo, A. (09/04/2024) ADB en Android: qué es y para qué puedes utilizarlo. Recuperado de [https://www.xatakandroid.com/tutoriales/adb-android-que-puedes-utilizarlo](https://www.xatakandroid.com/tutoriales/adb-android-que-puedes-utilizarlo)

- 504ensicsLabs (s.f.) Herramienta LiME ~ Linux Memory Extractor. Recuperado de [https://github.com/504ensicsLabs/LiME](https://github.com/504ensicsLabs/LiME)

- Ideal Gente (11/04/2015) Como guardar conversaciones WhatsApp en el ordenador para leerlas cuando quieras. Recuperado de [https://www.ideal.es/sociedad/201504/11/como-guardar-conversaciones-whatsapp-20150410170133.html](https://www.ideal.es/sociedad/201504/11/como-guardar-conversaciones-whatsapp-20150410170133.html)

- Metodologías para el Análisis Forense de IoT. Recuperado de https://publicaciones.sadio.org.ar/index.php/JAIIO/article/download/295/242#:~:text=Metodologías para el Análisis Forense de IoT&text=El proceso forense incluye seis,y Presentación de la Evidencia.

- Propuesta de una guía de actuación forense para entornos de internet de las cosas (IoT). Recuperado de [https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S1405-55462022000100441](https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S1405-55462022000100441)

- Universitat Politècnica de València - Definición de una metodología para el análisis informático
forense en entornos IoT. Recuperado de https://riunet.upv.es/bitstream/handle/10251/186198/Sorribas - Definicion de una metodologia para el analisis informatico forense en entornos IoT.pdf?sequence=1&isAllowed=y

- Universitat Oberta de Catalunya - Análisis Forense de dispositivos móviles iOS y Android. Recuperado de [https://openaccess.uoc.edu/bitstream/10609/45641/6/malvarezmuTFG0116memoria.pdf](https://openaccess.uoc.edu/bitstream/10609/45641/6/malvarezmuTFG0116memoria.pdf)