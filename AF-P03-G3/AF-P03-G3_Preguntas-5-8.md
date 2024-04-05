# Parte 1: Investigación

## Preguntas

5. Dado el interés conocido de Richard por el fútbol y la música rock y heavy, investigar su actividad en línea relacionada con estos intereses. Además, verificar si ha visualizado contenido en línea que pueda justificar un despido procedente, como la visualización de una película online. Documentar cualquier hallazgo relevante.

Haciendo uso del software *FTK Imager v4.7.1.2* montamos la imagen forense del disco duro de Richard. Luego navegamos por los directorios hasta llegar a C:\\Users\\Richard\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\mt13hmmn.default-release, siendo este su perfil del navegador Mozilla Firefox. Si entramos en esa carpeta y bajamos, veremos una base de datos llamada **places.sqlite**, que es la que almacena el historial del navegador, así que la descargamos también.

![Mozilla-1](img/4-Mozilla-Firefox.png)

![Mozilla-2](img/4-Mozilla-Firefox-1.png)

Luego abriremos dicha base de datos con el programa *DB Browser for SQLite Versión 3.12.2*, y mostraremos los datos de la tabla **moz_places**. En esta vemos las urls que el usuario ha visitado, junto con otros datos como el título de la página o la búsqueda realizada en Google, el número de visitas realizadas a cada página o la última hora de visita de cada una, en formato Epoch Time.

![SQLite-1](img/5-SQLite-Browser-1.png)

Una vez que entramos en dicha tabla, vemos que el usuario Richard ha buscado en Google "trabajo basura español download", que resulta ser una película del año 1999. Revisa las páginas rebeldemule.org, cine24h.net y new.c.mi.

![SQLite-2](img/5-SQLite-Browser-2.png)

La hora Epoch de la búsqueda 14 es **1677076184188000**, que corresponde a la búsqueda de la película en cuestión en la página new.c.mi o CUEVANA.HD.

![SQLite-2](img/5-SQLite-Browser-4.png)

Si convertimos este dato en horario GMT, este resulta ser las 14:29:44 del 22 de febrero de 2023.

![SQLite-Epoch](img/5-SQLite-Browser-5.png)

Más tarde busca en Google discos duros Western Digital y Crucial de 4TB, un disco duro Western Digital de 10TB y un disco duro Seagate de 10TB.

![SQLite-3](img/5-SQLite-Browser-3-1.png)

Y finalmente, realiza unas búsquedas de páginas de trading como eToro, busca ropa de mujer y finalmente descarga el software PulseAudio 1.1.

![SQLite-6](img/5-SQLite-Browser-6.png)

8. Buscar evidencia de que Richard haya asistido a competidores o terceros mediante la exfiltración de datos por correo electrónico.

Con el software *FTK Imager v4.7.1.2* montamos la imagen forense del disco duro de Richard. Luego navegamos por los directorios hasta llegar a C:\\Users\\Richard\\AppData\\Roaming\\Thunderbird, donde vemos que tenía instalado el cliente de correo electrónico Mozilla Thunderbird. 

![FTK-1](img/1-Evidence-Tree.png)

Sabiendo esto, ahondamos más y encontramos un perfil de correo electrónico en la carpeta \\Thunderbird\\Profiles\\tvtlv94f.default-release, así que extraemos el perfil entero, a fin de poder procesarlo con el software *SysTools MBOX Viewer v4.0*.

![MBOX-Viewer](img/2-SysTools-MBOX-Viewer.png)

Gracias a este programa, accedemos a los correos electrónicos de Richard, por lo que comenzamos a leer. Después de unos momentos, nos percatamos que el usuario Richard se encontraba entablando una conversación con otro usuario, cuyo correo es **proba2.seguridade@gmail.com**. En esta conversación, Richard acuerda una subida de sueldo, de 38000€ a 45000€.

![Mail-1](img/3-Mail-1.png)

Notamos que el 20/02/2023 a las 21:05, el usuario **proba2** le responde a esta petición de subida salarial.

![Mail-2](img/3-Mail-2.png)

En un correo más tarde, a las 0:58:55, Richard vuelve a contactar a proba2, acordando firmar el contrato laboral, el pago del dinero acordado y la salida de su empresa a cambio de algo que Richard califica de "unas pruebas".

![Mail-3](img/3-Mail-3.png)

Luego, unos 8 minutos más tarde, a las 1:06:44, vemos que Richard envía 4 archivos **pom.xml** a proba2, como respuesta a la contestación afirmativa de este usuario, recibida a las 1:01. Estos archivos consisten en archivos de configuración de Maven.

![Mail-4](img/3-Mail-4.png)

![Mail-4-Attachments](img/3-Mail-4-Attachments.png)

36 minutos más tarde, a las 1:40:17 Richard envía un correo a otro usuario con email **phy.reg@gmail.com**, en el que le avisa que planea abandonar la empresa.

![Mail-5](img/3-Mail-5.png)

Horas más tarde, a las 15:06:09, el usuario Richard envía un enlace de Google Drive a proba2, y le advierte que está protegido con contraseña, la cual sólo proporcionará cuando proba2 le pague.

![Mail-6](img/3-Mail-6.png)

Finalmente, 4 minutos más tarde, a las 15:10:23, el usuario proba2 afirma haber realizado el pago Richard, solicitándole la contraseña. También vemos un último correo de Richard a las 15:25:27, de nuevo a phy.reg@gmail.com, en el que le termina de avisar de su inminente salida de la empresa.

![Mail-7](img/3-Mail-7.png)

![Mail-8](img/3-Mail-8.png)