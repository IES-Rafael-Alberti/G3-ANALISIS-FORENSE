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

Durante el proceso de la investigación y a partir de los registros de conversaciones en WhatsApp y Telegram suministrados, se han encontrado un conjunto de vestigios que sugieren que Atalus y Camilo planificaron, tras informarse previamente, utilizar un dispositivo Rubber Ducky en el ordenador de Lassandra en el instituto. 

Según la información recabada de la imagen proporcionada de la cámara IP, se puede ver a un sujeto encapuchado introducir un dispositivo USB en el ordenador antes mencionado. Tras revisar y analizar este equipo, se revela la presencia de malware en el mismo bajo la categoría Keylogger. Este tipo de programas buscan el objetivo de registrar las pulsaciones del teclado de un ordenador, para ser recogidas por el atacante.

Además, se ha examinado el historial del navegador del SmartPhone de Atalus, en el que se puede ver búsquedas relacionadas con el uso y adquisición de un Rubber Ducky, la descarga de Telegram o la cuenta de instagram de Lassandra. 

Estos acontecimientos se relacionan y ordenan en una línea de tiempo incluida en este mismo documento.

# Introducción

En este documento se detallan los hallazgos encontrados a través del análisis de las adquisiciones dadas de las copias de seguridad de Whatsapp, Telegram, Google Database y las imagenes del Rubber Ducky, del disco duro del ordenador utilizado por la alumna Lassandra y de la cámara IP. 

Se incluyen además una serie de anexos que hace referencia a los hallazgos que se han encontrado, la cadena de custodia y los hashes sobre la integridad de las adquisiciones que se nos ha suministrado.

También incluye la metodología utilizada y una línea temporal de los hallazgos encontrados que nos permite con mayor certeza y claridad el incidente.

# Objetivos

Los objetivos que se persiguen cumplir en este informe son los siguientes:

- Construir una línea de tiempo que clarifique y contextualicen los eventos acontecidos
- Conseguir vestigios que indiquen acoso a la estudiante Lassandra Cordalis en aplicaciones de chat.
- Comprobar si Atalus Grasstem está involucrado en un posible _defacement_ (modificación sin consentimiento del perfil de la víctima). 

# Alcance

El alcance de este informe se limita a las siguientes fuentes de evidencia digital, organizadas según su origen o propietario:

### General
- Imagen de memoria de una tarjeta SD perteneciente a una cámara IP de una de las Aulas.

### Lassandra Cordalis (Víctima)
- Imagen del disco duro del PC de clase
- Copia de seguridad de su teléfono móvil (ADB - Android Debug Bridge): **Xiaomi Redmi Note 11** 
- Extracto de una copia de seguridad del servidor de google.
- Extracto de sus conversaciones de WhatsApp
- Extracto de sus conversaciones de Telegram

### Atalus Grasstem (Principal sospechoso)
- Extracto de sus conversaciones de WhatsApp
- Copia de seguridad de su teléfono móvil (ADB - Android Debug Bridge): X25
- Extracción de copia seguridad del servidor de google.

### Camillo Richbald
- Copia de seguridad de su teléfono móvil (ADB - Android Debug Bridge): Xiaomi Redmi Note 11
- Extracción de copia de seguridad de WhatsApp
- Extracción copia de seguridad del servidor Google

Cada uno de estas fuentes será analizadas con las herramientas pertinentes en su totalidad sin restricciones.

# Metodología

A continuación indicamos la metodología utilizada para el proceso:

1. Identificación de hallazgos o vestigios.

En primer lugar comenzamos por identificar los elementos que puedan tener hallazgos o vestigios de forma digital documentandolos:
- Dispositivos fisico.
- Redes y conexiones a internet.
- Software.
- Datos en la nube.
  
2. Adquisición.

Planificamos la adquisición para encontras las distintas fuentes a través de un orden de recogida basandonos en los siguientes criterios.

- Su valor probable: La fuente de datos que mas hallazgos o con mayor calidad podrían contener.
- Volatilidad:
  i. Registros, caché
  ii. Tablas de enrutamientos, caché ARP, tabla de procesos, estadística del núcleo y memoria.
  iii. Sistemas de archivos temporales.
  iv. Disco duro
  v. Datos de registro remoto, logs del sistema y monitorización del sistema.
  vi. Configuración física y topología de la red.
  vii. documentos y archivos físicos.
- Cantidad de esfuerzo requerido.

3. Presentación.

En esta fase el objetivo es mantener la integridad de los hallazgos, para ello se deben aplicar una serie de medidas como:

- Evitar exposición a campos magnéticos y otras interferencias.
- Almacenar el hallazgo, precintarlo y sellarlo en los soportes adecuados.
- Utilizar el material adecuado como indumentaria de protección para evitar daños por descargas electroestáticas entre otros.

4. documentación.

En esta fase se documentará el procedimiento completo de forma detallada y concisa que sigue una línea temporal (fecha, hora, ubicación...).

Se documentarán todos los procesos llevados acabo:

- Tácticas de adquisición
- Tipos de hardware o software
- Configuraciones
- Herramientas utilizadas

Es crucial detallar un registro de todas las personas que han tenido acceso a los hallazgos, es decir, mantener la cadena de custodia para demostrar que los hallazgos no han sido modificadas. La cadena de custodia debería de componerse de:

- Nombre de la persona que manejó la evidencia
- Fecha
- Propósito de cada manipulación

5. Análisis.

En esta fase se llevarán a cabo una serie de procesos y tareas que intentarán dar respuesta a preguntas relacionadas con el evento que se está investigando. Esto incluye:

- Revisar la hora de la BIOS del dispositivos
- Recuperar ficheros borrados
- Analizar los metadatos
- Analizar los registros de red
- Estudiar las particiones y sistemas de ficheros.
- Analizar el sistema operativo
- Estudiar la seguridad implementada en el sistema
- Analizar los registros de autenticación

6. Presentación.

En esta fase se escribirá un informe pericial con toda la información obtenida a lo largo del proceso de análisis. Este informe debe escribirse en un lenguaje entendible para un público no técnico y tener una estructura uniforme. El informe debe incluir la documentación de la cadena de custodia y al finalizar el informe será remitido al organismo solicitante.

**Herramientas usadas**

| Nombre de la herramienta | Distribuidor | Versión        |
|--------------------------|--------------|----------------|
| FTK Imager               | AccessData   | 4.7.1.2        |
| DB Browser for SQLite    |     -        | 3.12.2         | 
| Android Backup Procesor  |  Nelenkov    |  -             |

# Investigación

[...]

## Timeline

[...]

# Conclusiones

[...]

# Anexos

- [Anexo 1 - Integridad de los datos y testigos](https://github.com/IES-Rafael-Alberti/G3-ANALISIS-FORENSE/blob/main/AF-P07-G3/Anexos/Anexo%201%20-%20Integridad%20de%20los%20datos%20y%20testigos.xlsx)
- [Anexo 2 - Registro de cadena de custodia](https://github.com/IES-Rafael-Alberti/G3-ANALISIS-FORENSE/blob/main/AF-P07-G3/Anexos/Anexo%202%20-%20Registro%20de%20cadena%20de%20custodia.xlsx)
- [Anexo 3 - Índice de hallazgos](https://github.com/IES-Rafael-Alberti/G3-ANALISIS-FORENSE/blob/main/AF-P07-G3/Anexos/Anexo%202%20-%20Registro%20de%20cadena%20de%20custodia.xlsx)
