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

En vista al auge de la computación en la nube, la infraestructura como servicio (_IaaS_) y las nubes de almacenamiento las organizaciones están adoptando cada vez más servicios basados en la nube para almacenar y procesar datos. Si bien la nube ofrece numerosas ventajas, también plantea diferentes enfoques y aspectos a tener en cuenta para el análisis forense. 

Este documento explora las características de la nube que impactan el análisis forense, describe las estrategias para recopilar evidencia de la nube y analiza los requisitos legales y reglamentarios aplicables a los entornos de nube. Al final del mismo además encontraremos una serie de recomendaciones que nos ayuden a enfrentar mejor una situación que requiera de análisis forense en la nube, así como mejorar la efectividad de las investigaciones.

# Características de la nube y su impacto en el análisis forense

# Estrategias


    Network packets for traffic analysis.
    Workload memory.
    Workload disk volumes.
    Logs and event data from workloads and cloud environments.


## Algunos tipos de metodología

# Requirimientos legales y regulaciones aplicables a entornos de nube

Al pensar en las cuestiones legales referidas al análisis forense en la nube podemos plantearnos una serie de preguntas:

¿Quien debe ceder el acceso a la información, la empresa que propietaia de los discos que contienen la información o del usuario en sí? ¿Es necesario siempre extraer la información de la nube? ¿Si subo una foto a un servidor externo que tiene una infraestructura de tipo cloud, es información pública?

Bien, para comenzar debemos tener en cuenta que la normativa general que se aplica al análisis forense en las infraestructuras cloud es la misma que a nivel internacional, es decir:

- **El convenio de Budapest**: Un marco de normas y estándares que sirve como guía internacional para desarrollar legislación en materia de cibercrimen. Cualquier país puede adherirse a él
- **Reglamento general de protección de datos**: Es la  normativa general europea cuyo objetivo es proteger la privacidad y datos personales de los ciudadanos. Establece una serie de requisitos para tratar nuestra información digital y define sanciones por su incumplimiento.
- **Directiva NIS**: ES otra normativa de la unión europea con el objetivo de mejorar la ciberseguridad general europea. Esta normativa incluye obligaciones para que los operadores tomen medidas adecuadas para gestionar riesgos de seguridad y notificar los incidentes que sufran y sean significativos para la integridad, confidencialidad y disponibilidad de los datos.

Estas normativas son aplicadas de forma general y a nivel internacional (convenio de Budapest) y europeo (RHPD Y NIS). 

Teniéndolas en cuenta, a un nivel muy superficial se debe realizar una diferencia fundamental en la información de la nube: 
**El hecho de necesitar contraseña para su acceso.** 

Cuando un usuario sube una foto a los servidores de _Instagram_, y la publica, valga la redundancia, en el apartado público de su perfil, automáticamente podríamos referirnos a esa foto como información de fuentes abiertas y podría analizarse sin ningún tipo de orden judicial por un agente de la ley. 

Sin embargo, para que esa persona pueda acceder a sus chats de _Instagram_, es necesario que acceda a su cuenta con sus credenciales de usuario. Si se quisiera consultar esos chats, aún estando en la nube, sería necesaria una orden de registro oficial por parte de las autoridades, lo que a su vez requiere de establecer una *causa probable* judicial. Por supuesto, todo ello debe tener en cuenta que los datos almacenados en aquellos dispositivos que sean catalogados como propiedad privada de una empresa requieren también de esta orden, entre ellos, los servidores que conformarían una posible nube o lo necesario para que exista **IaaS** (*Infrastructure as a service*).

# Recomendaciones para facilitar el análisis forense

Para conseguir ser más eficientes y tener mejores prácticas en el proceso de análisis forense podríamos tener una serie de detalles a tener en cuenta.

Por ejemplo, **No siempre debemos acceder a la nube como tal para investigar... la nube**, es decir; Muchas aplicaciones, por ejemplo las de mensajería, a pesar de que almacenan en la nube muchos de sus datos, generan **logs** de que lo están haciendo: metadatos, registros, _thumbnails_... etc. Todo ello son artefactos a los que deben prestarse especial atención y pueden resultar muy útil en un caso de análisis forense en la nube.

También, debido a lo comentado en la sección de [Requerimientos legales y regulaciones aplicables](#requirimientos-legales-y-regulaciones-aplicables-a-entornos-de-nube), deben tenerse muy en cuenta la captura, recolección y preservación de la evidencia en vivo, debido a que esta puede mantener conexiones, sesiones abiertas y caché que podría ser de gran utilidad a la hora del examen forense y deben.

Otra medida, esta vez como usuarios o propietarios, que podríamos tomar, es la automatización de _snapshots_ del sistema o captura del estado regular de nuestros servicios de nube, hosting o similar. Muchas de estas plataformas disponen de esta opción, y activarla nos garantizaría algo similar a una imagen de disco que puede resultar de utilidad en el proceso de análisis.

Además, es importante fomentar la colaboración entre equipos de seguridad, administradores de sistemas y personal forense tanto de una posible empresa como de su proveedor de servicios o IaaS es fundamental para mejorar la efectividad del análisis forense en la nube. Al establecer protocolos claros de comunicación y procedimientos de colaboración puede agilizar la respuesta a incidentes, compartir información relevante y garantizar una gestión coordinada de la seguridad.


# Referencias

- Techtarget. (s.f.). Cloudcomputing forensics techniques for evidence acquisition. Recuperado de [https://www.techtarget.com/searchsecurity/tip/Cloudcomputing-forensics-techniques-for-evidence-acquisition](https://www.techtarget.com/searchsecurity/tip/Cloudcomputing-forensics-techniques-for-evidence-acquisition)

- Mahalik Barnhart, H. (s.f.). How to Lawfully Collect and Examine Data in the Cloud. *Forensic Magazine*. Recuperado de [https://www.forensicmag.com/3425-Featured-Article-List/575758-How-to-Lawfully-Collect-and-Examine-Data-in-the-Cloud/](https://www.forensicmag.com/3425-Featured-Article-List/575758-How-to-Lawfully-Collect-and-Examine-Data-in-the-Cloud/)

- Tidmarsh, D. (s.f.). What do you need to know about cloud forensics? *CybersecurityExchange*. Recuperado de [https://www.eccouncil.org/cybersecurity-exchange/computer-forensics/what-is-cloud-forensics/](https://www.eccouncil.org/cybersecurity-exchange/computer-forensics/what-is-cloud-forensics/)

- Council of Europe. (junio de 2021). Cyber-buda benefits [PDF]. Recuperado de [https://rm.coe.int/cyber-buda-benefits-junio2021a-es/1680a2e4de](https://rm.coe.int/cyber-buda-benefits-junio2021a-es/1680a2e4de)

- European Union Agency for Cybersecurity. (s.f.). NIS Directive - New. Recuperado de [https://www.enisa.europa.eu/topics/cybersecurity-policy/nis-directive-new](https://www.enisa.europa.eu/topics/cybersecurity-policy/nis-directive-new)

- Departamento de Seguridad Nacional (España). (s.f.). Publicación Directiva NIS. Recuperado de [https://www.dsn.gob.es/es/actualidad/sala-prensa/publicacion-directiva-nis](https://www.dsn.gob.es/es/actualidad/sala-prensa/publicacion-directiva-nis)
