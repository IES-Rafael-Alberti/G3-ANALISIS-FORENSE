# Índice

1. [Resumen ejecutivo](#resumen-ejecutivo)
2. [Introducción](#introduccion)
3. [Objetivos](#objetivos)
4. [Alcance](#alcance)
5. [Objetivos](#objetivos)
6. [Metodología](#metodología)
7. [Investigación](#investigación)
8. [Conclusiones](#conclusiones)
9. [Anexos](#anexos)

## Resumen ejecutivo

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

## Conclusiones

## Anexos

[- Anexo 1 - Integridad de los datos y testigos](https://github.com/IES-Rafael-Alberti/G3-ANALISIS-FORENSE/blob/main/AF-P03-G3/Anexos/Anexo%201%20-%20Integridad%20de%20los%20datos%20y%20testigos.ods)<br>
[- Anexo 2 - Registro de cadena de custodia](https://github.com/IES-Rafael-Alberti/G3-ANALISIS-FORENSE/blob/main/AF-P03-G3/Anexos/Anexo%202-%20Registro%20de%20cadena%20de%20custodia.ods)<br>
[- Anexo 3 - Índice de hallazgos]()
