1. Identificar la vulnerabilidad en la aplicación web que fue explotada por el atacante.

La vulnerabilidad que se ha encontrado es una inyección de comandos a través de ping.php. Esta vulnerabilidad se ha usado a través de un ping.php que se encuentra en la ruta '/var/www/ping.php'.
![ping.php-ruta](./img/ruta_ping.php-contenido.png)
2. Determinar la IP, el cliente y el sistema operativo utilizado por el atacante durante el ataque.

La IP del atacante es la 192.168.1.6 y su sistema operativo es un Linux 86x64 rev 78.0.
![ip-so](./img/ip-so-atacante.png)

3. Descubrir qué datos fueron exfiltrados del servidor comprometido.

El fichero que se ha exfiltrado es el /etc/passwd. Se ha descubierto a través de strings a la imagen de la memoria recibida que se redirigió el contenido del fichero a través de cat utilizando una inyección de comandos con ping.php.
![cat-ping](./img/string_ping_passwd.png)
Además encontramos el fichero passwd.txt en la ruta /var/www/passwd.txt
![ruta-passwd.txt](./img/passwd-var-ruta-contenido.png)

4. Analizar por qué el archivo original no muestra actividad durante el incidente.

El archivo original no muestra actividad ya que como se ha mencionado anteriormente, se ha utilizado el comando cat para redirigir el contenido de /etc/passwd a un passwd.txt

5. Proponer soluciones para reparar la vulnerabilidad explotada.

La mejor solución para la inyección de comandos a través del ping.php es validar a través de una función en php, que la cadena insertada en el formulario es una dirección IP y en caso de que no sea una dirección IP de algún tipo de error.
