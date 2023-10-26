---
marp: true
theme: default
_class: lead
paginate: true
backgroundColor: #fff
color: white
backgroundImage: url('./img/background6.jpg')
---

<style type="text/css">
    img {
  	    background-color: transparent!important;
        width: 100%;
        max-height: 300px
    }

    .ciclo {
        background: red;
        width: 50% !important;
        margin-left: 20%
    }

</style>

![bg left:30% 50%](./img/imago-iesra-1.png)

# Análisis Forense

# **Proyecto 1 - Nuestra Metodología**
## Grupo 3

Raúl Ladrón de Guevara García
Juan Manuel Cumbrera López
Sergio Guerrero Merlo
Christian Romero Oliva


---

# **Introducción**

- Necesidad de seguir normas y estándares forenses.
- Investigación de normativas.
- Creación de una metodología específica.



---

# **Investigación de Normas y Estándares Forenses**

Normativas investigadas

- Norma UNE 71505/2013 (Sistemas de gestión de evidencias electrónicas)
- Norma UNE 71506/2013 (Análisis forense de las evidencias electrónicas)
- ISO 27037
- Metodología RFC 3227
- Metodología NIST


---

# **Por qué usar una norma o estándar forense**


- Establecer un marco de referencia.

- Garantizar un nivel de integridad y fiabilidad

- Mejorar la calidad y consistencia

- Aumentar la credibilidad

- Facilitar la colaboración y comunicación

---


## **Norma UNE 71505/2013 (Sistemas de gestión de evidencias electrónicas)**

Esta norma se centra garantizar los principios de la información de las evidencias electrónicas o digitales estableciendo un ciclo de vida de las mismas.

<div class="container">
    <img class="ciclo" src="img/ciclo.png">
</div>

---

## **Principios**

**Confidencialidad:** Se refiere a la protección de la información para que solo las personas autorizadas puedan acceder a ella.

**Autenticación e integridad:** Garantiza que la evidencia es auténtica, es decir, que proviene de la fuente que se afirma y que no ha sido modificada de ninguna manera.

**Disponibilidad y completitud:** Asegura que la información esté disponible cuando sea necesaria y que esté completa, es decir, que incluya todos los datos.

**Calidad y gestión:** Se refiere a la necesidad de mantener estándares de calidad en la recopilación, almacenamiento y uso de la información. También implica una gestión de los datos, lo que incluye su actualización y eliminación en el momento adecuado.

---

## **Ciclo de vida de las evidencias**

**Generación:** En este primer paso es donde se crean los datos. 

**Almacenamiento:** Una vez generados los datos, se almacenan en algún tipo de medio de almacenamiento. 

**Transmisión:** Los datos a menudo necesitan ser enviados de un lugar a otro. 

**Recuperación:** Extraer datos de los medios de almacenamiento y exportarlos para su análisis.

**Tratamiento:** Los datos extraídos se procesan para obtener información útil.

**Comunicación:** Los resultados del análisis de la evidencias se comunican a las partes pertinentes.

---

## **Norma UNE 71506/2013 (Análisis forense de las evidencias electrónicas)**

El objetivo de esta norma es definir el proceso de análisis forense dentro del ciclo de gestión de las evidencias (Norma UNE 71506/2013 anteriormente descrita).
<br>

![Alt text](img/UNE-71506.png)

---

## **Fases de la norma UNE 71506/2013**

**1. Preservación:** En esta fase se pretende mantener en todo momento la validez y confiabilidad de las evidencias.

**2. Adquisición:** En esta fase se realiza un clonado a bajo nivel de los datos originales, siguiendo un procedimiento documentado para asegurar que el proceso de adquisición es reproducible y repetible, calculando el código hash de cada evidencia.

**3. Documentación:** En esta fase se documentará el procedimiento completo de una forma detallada y concisa que siga una linea temporal correcta (Fecha, hora, ubicación, etc..).

**4. Análisis:** En esta fase se llevarán a cabo una serie de procesos y tareas que intentarán dar respuesta a preguntas relacionadas con el evento que se está investigando.

**5. Presentación:** En esta fase se escribirá un informe pericial con toda la información obtenida a lo largo del proceso de análisis. 

---

## **Norma ISO 27027 (Recopilación de evidencias)**

 Esta norma se basa en la fases de identificación, adquisición y preservación de evidencias digitales. Esta norma está dirigida a los dispositivos actuales estando más acorde con la técnica actual.

 ![ISO-27037](img/esquemaiso.png)

---

## **Fases de la norma ISO 27037**

**1. Identificación:** Es la primera de las fases de esta norma y trata de buscar, reconocer y documentar posibles evidencias digitales.

**2. Recolectar o adquirir:** Es la segunda de las fases e indica que la evidencia identificada debe ser recogida o adquirida para su procesamiento. Indica que deben hacerse copias de una imagen del disco, copia de los contenidos de la memoria y los contenidos de un correo eléctronico. Las copias deben hacerse mediante un proceso conocido, defendible y bien documentado.

**3. Preservar:** Esta tercera fase define preservar como el proceso de mantener y salvaguardar la integridad y/o el estado original de la potencial evidencia digital, esto requiere estrictos controles de acceso para proteger los artículos de la modificación accidental o deliberada como de tener los controles de entorno apropiados.

---

## **Metodología NIST**

  
- Se desarrolló principalmente para ser usada por agencias federales.

- Adopta un enfoque holístico 

- Aporta un plan para adquirir los datos adecuadamente basándose en volatilidad, valor probable y cantidad de esfuerzo requerido

- Pretende transformar los dispositivos en evidencia


---

## **Fases de la norma NIST**


![NIST](img/Metodologia_NIST.drawio.png)

---

## **Metodología RFC 3227**

La metodología RFC 3227 es una guía para administradores y profesionales de seguridad que establece pautas para la recopilación y preservación de evidencia relacionada con eventos de seguridad informática, tales como intrusiones. Ofrece mejores prácticas para determinar la volatilidad de los datos, priorizar evidencia y cómo almacenar y documentar los datos.

---

## **Fases de la metodología RFC 3227**

**1. Introducción:** La introducción destaca la importancia de recopilar evidencia en incidentes de seguridad, de una forma estructurada, metódica y organizada.

**2. Pautas de Recopilación de Evidencia:** Esta fase establecen pautas para la recolección, incluyendo priorizar la captura precisa de datos, minimizar cambios, eliminar vías de alteración y proceder desde lo más volátil.

**3. Procedimiento de Recolección:** Etapa que destaca la importancia de la transparencia en los métodos utilizados. Los principios clave incluyen identificar la evidencia, priorizar la relevancia, seguir un orden de volatilidad, minimizar cambios externos, documentar y considerar la generación de checksums y firmas criptográficas sin alterar las pruebas.

---

**4. Procedimiento de Archivado:** Para almacenar la evidencia de manera adecuada, se requiere un registro detallado de la cadena de custodia que incluye quién, cuándo y dónde descubrió, manejó o examinó la evidencia, así como quién tuvo custodia, la duración y el almacenamiento. La evidencia se almacena en medios comunes y se restringe el acceso, documentándolo para evitar accesos no autorizados.

**5. Herramientas:** Este apartado recomienda una lista de herramientas preparadas para la recolección de evidencia y análisis forense.

---

![RFC3227](img/Metodología_RFC_3227.drawio.png)

---

# **¡Muchas gracias por su atención!**

## IES Rafael Alberti - Ciberseguridad en las TI

## 2023-2024
