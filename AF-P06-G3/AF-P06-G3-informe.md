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

# Introducción

# Características de la nube y su impacto en el análisis forense

Hoy en día es muy normal en internet encontrarnos con el término "nube" pero no mucha gente sabe realmente qué es, que características tiene y en el caso del análisis forense, su impacto teniendo en cuenta una serie de inconvenientes que dificultan más el análisis de los datos.

Antes de entrar en materia, es bueno saber que es la nube y cuales son las características que la componen.

La "nube" permite almacenar y acceder a datos a través de internet en lugar de tener el dispositivo de almacenamiento en nuestro ordenador. No solo permite el almacenamiento de archivos, también permite acceder a aplicaciones que solemos tener en nuestros dispositivos informáticos sin necesidad de tenernos instalados en nuestro equipo. Los usuarios que hayan contratado los servicios, pueden tener acceso a la nube siempre que tengan una conexión a internet.

Como tal la componen un conjunto de servidores remotos que estan conectados y funcionan de manera coordinada como un único ecosistema.

Hoy en día existen cuatro tipos de nubes, nube pública, nube comunitaria, nube privada y nube híbrida. Como bien indica su nombre, la nube pública ofrece sus servicios a cualquier usuario de itnernet.

Una nube comunitaria ofrece servicios de manera exclusiva por una comunidad de consumidores de una organización.

La nube privada ofrece los servicios a usuarios limitados por ejemplo a través de redes empresariales y la híbrida ofrece estos servicios de manera pública o privada en función de las necesidades.

Obviamente tener nuestros datos en la nube tiene una serie de inconvenientes para los expertos en la ciencia forense ya que dependiendo del tipo de servicio y sus características dificultan el análisis forense siempre teniendo en cuenta el responsable de la gestión de los datos almacenados y el softare.

En el caso del software como servicio o SaaS, el software y los datos se encuentran disponibles constantemente en la nube, siendo el usuario el que accede directamente a la misma. El proveedor del servicio será el responsable de gestionar los datos y el software.

En el caso de la plataforma como servicio o Paas, el propietario de la plataforma es el responsable de los datos y aplicaciones que contienen, sin serlo referente al almacenamiento, la red, los servidores o el sistema operativo.

Y por último en el caso de infraestructura como servicio o Iaas, se aloja en un proveedor de nube externo. El proveedor es el propietario de la red y del almacenamiento, pero el desarrollador del servicio final es el responsable de la integridad de los datos, las aplicaciones y el sistema operativo.

Como bien sabemos el uso de la nube existen muchos procesos y usuarios que estan utilizando el software, hardware y recursos que estamos analizando haciendo que la plataforma no sea estable. Tenemos que tener en cuenta también que la jurisdicción física debe ser donde se encuentra el servidor y dependiendo de donde se encuentre, dependerá de la legislación local.

Como vemos no tenemos el control sobre el entorno y el hardware necesitando siempre la colaboración del tercero para realizar el análisis forense.

Las pruebas forenses podrían ser contaminadas teniendo en cuenta que la compartición de los recursos y los datos pueden ser utilizados por otras compañías o usuarios de manera pública y constante.

La dificultad para recuperar por ejemplo datos borrados se complica dada la volatilidad y la movilidad de los datos y la gran cantidad de información que se involucra.

Otra dificultad nos la encontramos al momento de utilizar herramientas tradicionales siendo necesaria la creación de herramientas específicas para las plataformas como Google Drive, AWS etc..

Además, los proveedores tienen distintas formas de proceder y entender la nube teniendo que aprender como funciona cada plataforma gestionada por cada proveedor y como la manejan.

# Estrategias


    Network packets for traffic analysis.
    Workload memory.
    Workload disk volumes.
    Logs and event data from workloads and cloud environments.


## Algunos tipos de metodología

# Requirimientos legales y regulaciones aplicables a entornos de nube

But these days, that crucial text message or photo is likely to live in the cloud, and not on the devices that investigators collect. Data contained in online resources like social media and news websites generally originates in the cloud. In addition, privacy regulations dictate how and when investigators can gain access to a person’s data in the cloud.

At a high level, there are really only two options.

Publicly available data can be obtained without any paperwork. This is similar to what you might find from sites that scrape public records and social media for information on a person. This might be the person’s name, DOB, address, previous residences, jobs, and things they post publicly on social media (all privacy settings are set to “public”).

Anything else that is hosted by a company and is considered private information requires a search warrant issued to the cloud provider (e.g., Dropbox, Facebook, etc.). This would include items postmarked as “private” via a user’s social media privacy settings, messages, etc. Search warrants require investigators to establish “probable cause.”

Al pensar en las cuestiones legales referidas al análisis forense en la nube se nos plantean una serie de preguntas:

¿Quien debe ceder el acceso a la información, la empresa que propietaia de los discos que contienen la información o del usuario en sí? ¿Es necesario siempre extraer la información de la nube? ¿Si subo una foto a un servidor externo que tiene una infraestructura de tipo cloud, es información pública?

Bien, para comenzar debemos tener en cuenta que la normativa general que se aplica al análisis forense en las infraestructuras cloud es la misma que a nivel internacional, es decir:

- *El convenio de Budapest*: Un marco de normas y estándares que sirve como guía internacional para desarrollar legislación en materia de cibercrimen. Cualquier país puede adherirse a él
- *Reglamento general de protección de datos*: Es la  normativa general europea cuyo objetivo es proteger la privacidad y datos personales de los ciudadanos. Establece una serie de requisitos para tratar nuestra información digital y define sanciones por su incumplimiento.
- 

# Recomendaciones para facilitar el análisis forense

Automatizar la recogida de snapshots etc
Buscar artefactos
Tener muy en cuenta los dispositivos ya encendidos



# Referencias

- Techtarget. (s.f.). Cloudcomputing forensics techniques for evidence acquisition. Recuperado de [https://www.techtarget.com/searchsecurity/tip/Cloudcomputing-forensics-techniques-for-evidence-acquisition](https://www.techtarget.com/searchsecurity/tip/Cloudcomputing-forensics-techniques-for-evidence-acquisition)

- Mahalik Barnhart, H. (s.f.). How to Lawfully Collect and Examine Data in the Cloud. *Forensic Magazine*. Recuperado de [https://www.forensicmag.com/3425-Featured-Article-List/575758-How-to-Lawfully-Collect-and-Examine-Data-in-the-Cloud/](https://www.forensicmag.com/3425-Featured-Article-List/575758-How-to-Lawfully-Collect-and-Examine-Data-in-the-Cloud/)

- Tidmarsh, D. (s.f.). What do you need to know about cloud forensics? *CybersecurityExchange*. Recuperado de [https://www.eccouncil.org/cybersecurity-exchange/computer-forensics/what-is-cloud-forensics/](https://www.eccouncil.org/cybersecurity-exchange/computer-forensics/what-is-cloud-forensics/)

- https://rm.coe.int/cyber-buda-benefits-junio2021a-es/1680a2e4de

- ¿Qué es la nube y como funciona internet? (s.f). Recuperado de [https://www.implika.es/blog/que-es-nube-internet](https://www.implika.es/blog/que-es-nube-internet)

- Fuentes, F. (7 de Noviembre de 2022). Análisis forense en la nube ¿Qué es y en qué consiste?. Recuperado de [https://www.arsys.es/blog/analisis-forense-cloud](https://www.arsys.es/blog/analisis-forense-cloud)

- De Pedro Pérez, Ó., & Mora López, I. (28 de Octubre de 2020). Introducción al análisis forense en entornos 'cloud'. Recuperado de [https://www.redseguridad.com/especialidades-tic/cloud-y-virtualizacion/introduccion-al-analisis-forense-en-entornos-cloud_20201028.html](https://www.redseguridad.com/especialidades-tic/cloud-y-virtualizacion/introduccion-al-analisis-forense-en-entornos-cloud_20201028.html)

- Técnicas para Análisis Forense Digital en la Nube: Guía completa. (s.f) Recuperado de [https://newformacion.com/seguridad-2/tecnicas-analisis-forense-digital-nube/](https://newformacion.com/seguridad-2/tecnicas-analisis-forense-digital-nube/)

