# Índice

1. [Resumen ejecutivo](#resumen-ejecutivo)
2. [Introducción](#introducción)
2. [Investigación teórica](#investigación-teórica)
3. [Evaluación de herramientas y métodos](#evaluación-de-herramientas-y-métodos)
   - [Métodos de extracción de vestigios](#métodos-de-extracción-de-vestigios)
   - [Herramientas para IoT](#herramientas-para-iot)
   - [Herramientas para móviles](#herramientas-para-móviles)
6. [Consideraciones legales y éticas](#consideraciones-legales-y-éticas)
8. [Anexos](#anexos)

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

## Métodos de extracción de vestigios

- **Adquisición física:** Es el método más utilizado. Consiste en realizar una réplica idéntica del original por lo que se preservan la totalidad de las evidencias potenciales. Este procedimiento presenta la ventaja de que es posible buscar elementos eliminados. Su desventaja principal es su complejidad respecto a los otros métodos y el tiempo que lleva su realización.

- **Adquisición lógica:** Consiste en realizar una copia de los objetos almacenados en el dispositivo. Para ello, se utilizan los mecanismos implementados de manera nativa por el fabricante, es decir, aquellos que son utilizados de manera habitual para sincronizar el terminal con un ordenador. de modo que se solicita la información deseada al sistema operativo del dispositivo móvil.

- **Adquisición del sistema de ficheros:** Permite obtener todos los ficheros visibles mediante el sistema de ficheros, lo que no incluye ficheros eliminados o particiones ocultas. Dependiendo del tipo de investigación puede resultar suficiente utilizar este método. Para llevarlo a cabo se aprovecha de los mecanismos integrados en el sistema operativo para realizar el copiado de los ficheros, Android Device Bridge (ADB) en el caso de Android. Mediante este método es posible recuperar cierta información eliminada ya que algunos sistemas operativos como es el caso de Android e iOS se valen de una estructura que utiliza bases de datos SQLite para almacenar gran parte de la información. Cuando se eliminan registros de los ficheros, únicamente se marcan como disponibles para sobrescritura, por lo que temporalmente siguen estando disponibles y por tanto es posible recuperarlos.

## Herramientas para IoT

Se ha investigado sobre herramientas IoT para la adquisición de evidencias pero teniendo en cuenta los artículos en internet, se ha llegado a la conclusión de que a día de hoy no existen herramientas especificas para la adquisición de evidencias forenses de IoT.

Dependiendo del tipo de dispositivo IoT se adquirirá de una manera u otra, teniendo en cuenta si el dispositivo puede conectarse a un equipo informático como un ordenador o si solo se permite de manera inalámbrica. En caso de poder conectarse a un ordenador, la adquisición de evidencias se hará vía FTK Imager o volatility.

En caso de que los dispositivos IoT no puedan conectarse directamente a un equipo informático, la adquisición se hará mediante Wireshark pudiendo obtener registros de conexiones o peticiones.

## Herramientas para móviles

En este punto se especifican una serie de herramientas Open Source y gratuitas para la adquisición de datos en dispositivos móviles.

### Android Debug Bridge (ADB)

Es una herramienta mediante la cual por comandos crea un puente entre nuestro ordenador y el teléfono móvil. Podemos traer archivos del móvil hacia nuestro ordenador gracias a ello. 

Para poder usar ADB con el dispositivo móvil, necesitamos activar la depuración USB e instalar los drivers ADB universales. Tiene una serie de comandos sencillos que permiten desde crear una shell para el dispositivo móvil como extraer o subir archivos al dispositivo móvil.

Muchas de las herramientas que se mencionarán en los siguientes puntos, utilizan o necesitan de esta herramienta instalada en nuestro ordenador. 

### AFLogical OSE - Open source Android Forensics app and framework

Esta herramienta es una apk que podemos instalar en nuestro dispositivo móvil para adquirir datos. Se debe ejecutar en el dispositivo o usando adb shell.

En el dispositivo android del que queramos hacer la adquisición, debemos abrir la aplicación y elegir los datos que deseamos etraer, simplemente tendremos que seguir las instrucciones dadas por la propia apliación. Se debe tener una tarjeta SD en el dispositivo para extraer los datos en ella.

Luego copiamos estos datos a nuestro ordenador para analizar estos datos o usamos adb pull. Los datos pueden ser registros de llamadas, contactos, aplicaciones, mensajes de texto o audiovisuales… Esta información será recuperada o bien conectada a una tarjeta en un dispositivo externo o a través del ADB.

### Andriller CE

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

### LIME- Linux Memory Extractor

Esta herramienta Open Source permite la adquisición de memoria volátil desde dispositivos basados en linux y android. Es la primera herramienta que permite captura de memoria completa en dispositivos Android. Minimiza su interacción entre el usuario y los procesos del espacio del kernel durante la adquisición lo que permite crear capturas de memorias más sólidas desde el punto de vista forense.

**Características**

- Adquisición completa de memoria de Android
- Adquisición a través de interfaz de red
- Huella mínima del proceso
- Hash de memoria volcada

### WhatsApp Xtract

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
