# Metodología RFC 3227

## Descripción

La metodología RFC 3227, titulada como “Directrices para la Recopilación y Archivado de Evidencia” (*Guidelines for Evidence Collection and Archiving*) es una guía creada con el propósito de proporcionar un conjunto de pautas y recomendaciones orientadas al uso por parte de administradores de sistemas y profesionales de seguridad. Este abanico de directrices buscan ofrecer una manera estructurada y detallada de recopilar y preservar evidencias informáticas relacionadas con eventos de seguridad, tales como intrusiones de la política de seguridad de un sistema. Además, este documento presenta las mejores prácticas que permiten determinar la volatilidad de los datos, ofrece los conocimientos para saber priorizar las evidencias que recolectar y como desarrollar la recolección y definir cómo almacenar y documentar los datos.

<br/>

## Fases de la Metodología

### Introducción

Como parte introductoria del documento, comienza definiendo "incidente de seguridad" como un evento en el que se viola la política de seguridad de un sistema, subrayando que la recopilación adecuada de evidencia es fundamental para identificar a los atacantes y presentar las pruebas en procesos legales. 

Además de esto, se incentiva a los administradores de sistemas a hacer uso de las pautas establecidas en el documento, a fin de usarlas como base para desarrollar procedimientos de recopilación de evidencia más específicos y concretos. 

Finalmente, se hace referencia a las convenciones de palabras clave usadas en el documento.

### Principios Rectores durante la Recopilación de Evidencia

En esta sección se establecen las pautas generales para la recolección de evidencia durante un incidente de seguridad. En estas se establece la necesidad de adherirse a la política de seguridad del sitio y colaborar con el personal, a fin de manejar el incidente correctamente. 

Luego de esto, comienza con las normas establecidas para el proceso de recopilación de evidencia, en el que se dicta lo siguiente:

- Capturar una imagen precisa del sistema
- Minimizar cambios en los datos durante la recopilación
- Eliminar vías externas que puedan alterar la evidencia
- Dar prioridad a la recopilación sobre el análisis cuando se enfrenten a elecciones
- Implementar procedimientos que sean factibles y probados, preferiblemente automatizados
- Adoptar un enfoque metódico para recopilar evidencia de dispositivos siguiendo las pautas establecidas en los procedimientos de recopilación
- Proceder desde lo más volátil a lo menos volátil, siguiendo el "Orden de Volatilidad" recomendado

Además se hace hincapié en la importancia de mantener notas con fechas y horas, registrando también la diferencia entre la hora del sistema y la hora universal (UTC) en las marcas de tiempo. Otros puntos importantes que se subrayan son las cosas a evitar, como apagar el sistema antes de completar la recopilación de evidencia o confiar en programas del sistema para la recopilación.

El orden de volatilidad anteriormente descrito queda de la siguiente manera:

1. Registros, caché
2. Tabla de enrutamiento, caché ARP, tabla de procesos, estadísticas del núcleo y memoria
3. Sistemas de archivos temporales
4. Disco duro
5. Datos de registro remoto y monitorización relevantes para el sistema en cuestión
6. Configuración física y topología de la red
7. Medios de archivo

### Procedimiento de Recolección

La fase de recolección de evidencia es presentada como un proceso meticuloso, el cual debe seguir los principios siguientes, siendo el primero la transparencia de los métodos utilizados durante la recolección, dado que deben ser reproducibles. Los demás principios son los siguientes:

- Ubicar la evidencia, enumerando los sitemas involucrados en el incidente
- Determinar lo que es relevante y admisible
- Para cada sistema, seguir el orden de volatilidad
- Eliminar posibles fuentes de cambio externas
- Recopilar evidencia siguiendo el orden de volatilidad
- Registrar la diferencia entre el reloj del sistema y UTC
- Documentar cada paso
- No olvidar a las personas involucradas

Este apartado también incide en considerar generar checksums y firmas criptográficas para la evidencia recopilada, ya que esto facilita preservar una cadena de evidencia fuerte, siendo muy importante no alterar las pruebas durante este proceso.

### Procedimiento de Archivado

Para lograr un correcto almacenamiento de la evidencia, es crucial registrar una cadena de custodia de manera exhaustiva, lo que incluye:

- Dónde, cuándo y quién descubrió y recopiló la evidencia
- Dónde, cuándo y quién manejó o examinó la evidencia
- Quién tuvo custodia de la evidencia, durante cuánto tiempo y cómo se almacenó
- Cómo se realizó la transferencia de custodia, incluyendo números de envío, en caso de cambio

La evidencia debe archivarse en medioscomunes, además de restringirse el acceso a la misma, documentándolo, a fin de prevenir accesos no autorizados.

### Herramientas que necesitarás

Con el fin de llevar a cabo la recolección de evidencia y análisis forense, esta sección recomienda una lista de herramientas preparadas para dicho fin. Entre estas herramientas se deben incluir:

- Un programa para examinar procesos, como 'ps'
- Programas para examinar el estado del sistema, como 'showrev', 'ifconfig', 'netstat' y 'arp'
- Un programa para realizar copias de bits a bits, como 'dd' o 'SafeBack'
- Programas para generar checksums y firmas, como 'sha1sum', 'dd' habilitado para checksum, 'SafeBack' o 'pgp'
- Programas para generar imágenes de núcleo y examinarlas, como 'gcore' y 'gdb'
- Scripts para automatizar la recolección de evidencia, como el "The Coroner's Toolkit" 

Es necesario que sus herramientas sean completamente autónomas y no dependan de librerías externas en el medio de sólo lectura, ya que en algunos casos, las herramientas pueden no revelar la totalidad de la información del sistema, debido a la capacidad de los rootkits actuales de ocultarse en módulos de kernel cargables.

### Referencias

Sección de referencias utilizadas en la confección de esta metodología