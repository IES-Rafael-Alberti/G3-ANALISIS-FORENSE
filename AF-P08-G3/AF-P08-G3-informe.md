# Índice

1. [Resumen ejecutivo](#resumen-ejecutivo)
2. [Introducción](#introducción)
3. [Objetivos](#objetivos)
4. [Alcance](#alcance)
5. [Metodología](#metodología)
6. [Investigación](#investigación)  
   6.1 [Timeline](#timeline)
7. [Conclusiones](#conclusiones)
8. [Anexos](#anexos)

# Resumen ejecutivo

En este informe se presentan los resultados del análisis forense realizado por Netmancer Inc. sobre diversas fuentes de datos relacionadas con Lassandra Cordalis, Atalus Grasstem y Camillo Richbald. Se examinaron copias de seguridad de los servidores de Google, conversaciones de WhatsApp, copias de seguridad ADB, copias de seguridad del servidor de Instagram, conversaciones de Telegram y imágenes del disco del equipo de Lassandra en el instituto, incluyendo la imagen de la tarjeta SD de la cámara IP Imou.

Durante el proceso de la investigación y a partir de los registros de conversaciones en WhatsApp y Telegram proporcionados, se encontraron indicios que sugieren que Atalus y Camillo planearon, tras informarse previamente, manipular el ordenador de Lassandra en el instituto. Se observó en el historial del navegador del SmartPhone de Atalus búsquedas relacionadas con el uso y adquisición de un dispositivo Rubber Ducky, así como la descarga de Telegram y la cuenta de Instagram de Lassandra.

La imagen proporcionada de la cámara IP muestra a un sujeto manipulando el ordenador mencionado. Tras revisar y analizar este equipo, se confirmó la presencia de malware categorizado como Keylogger, un programa diseñado para registrar las pulsaciones del teclado. Además, se detectó un inicio de sesión desde un dispositivo Android 9, coincidiendo con el user agent de Atalus, mientras que el dispositivo de Lassandra es un Android 11.

Se resalta la importancia de prestar atención a la línea de tiempo detallada en este mismo documento, donde se ordenan y relacionan los eventos mencionados.

# Introducción

En este documento se detallan los hallazgos encontrados a través del análisis de las adquisiciones dadas de las copias de seguridad de Whatsapp, Telegram, Google Database y las imagenes del Rubber Ducky, del disco duro del ordenador utilizado por la alumna Lassandra y de la cámara IP. 

Se incluyen además una serie de anexos que hace referencia a los hallazgos que se han encontrado, la cadena de custodia y los hashes sobre la integridad de las adquisiciones que se nos ha suministrado.

También incluye la metodología utilizada y una línea temporal de los hallazgos encontrados que nos permite con mayor certeza y claridad el incidente.

# Investigación teórica

Los objetivos que se persiguen cumplir en este informe son los siguientes:

- Construir una línea de tiempo que clarifique y contextualicen los eventos acontecidos
- Conseguir vestigios que indiquen acoso a la estudiante Lassandra Cordalis en aplicaciones de chat.
- Comprobar si Atalus Grasstem está involucrado en un posible _defacement_ (modificación sin consentimiento del perfil de la víctima). 

# Evaluación de herramientas y métodos

El alcance de este informe se limita a las siguientes fuentes de evidencia digital, organizadas según su origen o propietario:


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

# Conclusiones


# Referencias

- Induruwa, A. (2009). 'Mobile phone forensics: an overview of technical and legal aspects', *Int. J. Electronic Security and Digital Forensics*, Vol. 2, No. 2, pp.169–181.

- Sedky, M. (2020). The Forensic Swing of Things: The Current Legal and Technical Challenges of IoT Forensics. Staffordshire University.
