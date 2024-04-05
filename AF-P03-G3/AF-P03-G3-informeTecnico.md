# Índice

1. [Resumen ejecutivo](#resumen-ejecutivo)
2. [Introducción](#introducción)
3. [Objetivos](#objetivos)
4. [Alcance](#alcance)
5. [Objetivos](#objetivos)
6. [Metodología](#metodología)
7. [Investigación](#investigación)

   7.1 [Timeline](#timeline)
8. [Conclusiones](#conclusiones)
9. [Anexos](#anexos)

## Resumen ejecutivo

En el presente informe se detallan los hechos acontecidos entre el **20 y el 22 de Febrero de 2023**, en los cuáles se investiga la actividad del empleado **_Richard Eduardo Wagner_** en las semanas previas a su despido a partir de una imagen de disco suministrada por InnovaTech Solutions. 

A partir de la imagen suministrada, se ha encontrado una serie de vestigios que indican que _**Richard Eduardo Wagner**_ mantuvo conversaciones con lo que parecen dos personas externas a InnovaTech Solutions, una a la que se refiere como "_Tom_" y otra la que se refiere como "_Phy_", con las cuáles expresaba descontento con su situación actual como empleado,hay vestigios que indican que comparte archivos de metadatos que parecen pertenecer al proyecto "_Social Query_" de InnovaTech Solutions.

Se encuentran vestigios de que Richard lleva acabo una serie de acciones planeadas y comunicaciones con estos agentes, y que a cambio estas personas ofrecen una serie de compensaciones, entre ellas una supuesta transacción de Bitcoin, que se ha intentado ratificar, y de la que no hay registro de que se haya producido en la fecha indicada.

Según una serie de correos electrónicos encontrados y su historial de búsquedas online, Richard planeaba su salida de la empresa, un intercambio de información que se ha comprobado perteneciente a la empresa a cambio de dinero (_a través de bitcoin, previamente mencionada_) y la toma de unas vacaciones a Las Palmas de Gran Canaria. El usuario Richard también comparte un enlace con un archivo subido a Google Drive el cual no se ha podido determinar su contenido. 

Además se encuentran indicios de actividad no relacionada con su trabajo en su historial de búsqueda, como visitas a webs de periódicos deportivo o sitios de streaming de películas online en horario laboral que podría justificar un despido procedente.

Estos acontecimientos se relacionan y ordenan en una línea de tiempo incluida en este mismo documento.

## Introducción

En este documento se presentan los hallazgos encontrados en la investigación y análisis de la imagen proporiconada. Incluimos anexos que hacen referencia a los hallazgos mencionados, a la cadena de custodia realizada y un documento generado sobre la integridad de la imagen proporcionada con sus valores hashes comprobados. También mencionamos la metodología y las herramientas utilizadas en el proceso de investigación.

## Objetivos

Aclarar las acciones del empleado llamado Richard en las semanas previas a su salida de la empresa.

## Alcance

Loss datos del disco duro a partir del cual se creó la imagen, el usuario de Richard, recuperación y análisis de archivos que se encuentran en la imagen, correos electrónicos del usuario Richard y el historial del navegador utilizado por el propio usuario teniendo en cuenta sus búsquedas en internet y marcadores.

## Metodología y herramientas

A continuación indicamos la metodología utilizada para el proceso:

1. Identificación de hallazgos o vestigios.

En primer lugar comenzamos por identificar los elementos que puedan tener hallazgos o vestigios de forma digital documentandolos:
- Dipositivos fisico.
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

| Nombre de la herramienta | Empresa      | Versión        |
|--------------------------|--------------|----------------|
| Windows Registry Recovery| MiTeC        | 1.6.1.0        |
| Event Log Explorer       | FSPro Labs   | 5.5 (Build 5.5.0.5011) |
| AccessData® FTK® Imager  | Exterro      | 4.7.1.2        |
| DB Browser for Sqlite    | Sqlitebrowser| 3.12.2         |
| SysTools MBOX Viewer     | Systool      | 4.0            |

## Investigación

### Timeline

![timeline](./img/timeline.png)

Utilizando FTK Imager se ha extraído los registros SYSTEM, SAM y SOFTWARE para su análisis. Estos registros se encuentran en `C:\Windows\System32\config` y se han analizado en busca de vestigios de que el usuario Richard existe en la imagen proporcionada y si se ha introducido un dispositivo USB con sus características y el punto de montaje recibido.

Analizando el registro `System\ControlSet001\Enum\USBSTOR`se ha encontrado que se ha conectado un USB con el número de serie 002618525C8EF0B0E87D2853& marcado con un recruadro rojo y con un Device Class ID llamado Ven_Kingston Prod_DataTraveler_3.0 Rev_ como podemos ver en la siguiente captura marcado con un recrado amarillo.

![usbstorg](./img/usbstorg.png)

En el propio registro se ha utilizado el id disk del USB encontrado para compararlo con el id disk que se encuentra en el registro `System\MountedDevices` para saber que punto de montaje recibió el dispositivo USB al momento de su conexión indicandonos que fue la letra E: la recibida.

![usbid](./img/usbid.png)

Teniendo en cuenta que tenemos la letra E: se ha analizado el registro `SOFTWARE\Microsoft\Windows Search\VolumeInfoCache\` para comprobar el nombre del dispositivo. El nombre del volumen es Mantemento.

![usbname](./img/usbname.png)

Después de encontrar las características del dispositivo USB se ha utilizado la herramienta Event Log Explorer para analizar los logs extraidos con FTK Imager de la ruta `C:\Windows\System32\winevt\logs`. El log analizado es Microsoft-Windows-DeviceSetupManager%4Admin.ectx y se ha encontrado un evento de id 112 que indica en su descripción que un dispositivo DataTraveler 3.0 que concuerda con el dispositivo encontrado en el reigstro SYSTEM con fecha de utilización en el día 20 de Febrero de 2023 a las 21:09:5 horas de la noche. 

El dispositivo estuvo trabajando durante 791 milisegundos.

![eventusb](./img/eventusb.png)

## Conclusiones

## Anexos

[- Anexo 1 - Integridad de los datos y testigos](https://github.com/IES-Rafael-Alberti/G3-ANALISIS-FORENSE/blob/main/AF-P03-G3/Anexos/Anexo%201%20-%20Integridad%20de%20los%20datos%20y%20testigos.ods)<br>
[- Anexo 2 - Registro de cadena de custodia](https://github.com/IES-Rafael-Alberti/G3-ANALISIS-FORENSE/blob/main/AF-P03-G3/Anexos/Anexo%202-%20Registro%20de%20cadena%20de%20custodia.ods)<br>
[- Anexo 3 - Índice de hallazgos]()
