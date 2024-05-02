# Herramientas para la adquisición de dispositivos Android e IoT

## Metodos de extracción de evidencias

- **Adquisición física:** Es el método más utilizado. Consiste en realizar una réplica idéntica del original por lo que se preservan la totalidad de las evidencias potenciales. Este procedimiento presenta la ventaja de que es posible buscar elementos eliminados. Su desventaja principal es su complejidad respecto a los otros métodos y el tiempo que lleva su realización.

- **Adquisición lógica:** Consiste en realizar una copia de los objetos almacenados en el dispositivo. Para ello, se utilizan los mecanismos implementados de manera nativa por el fabricante, es decir, aquellos que son utilizados de manera habitual para sincronizar el terminal con un ordenador. de modo que se solicita la información deseada al sistema operativo del dispositivo móvil.

- **Adquisición del sistema de ficheros:** Permite obtener todos los ficheros visibles mediante el sistema de ficheros, lo que no incluye ficheros eliminados o particiones ocultas. Dependiendo del tipo de investigación puede resultar suficiente utilizar este método. Para llevarlo a cabo se aprovecha de los mecanismos integrados en el sistema operativo para realizar el copiado de los ficheros, Android Device Bridge (ADB) en el caso de Android. Mediante este método es posible recuperar cierta información eliminada ya que algunos sistemas operativos como es el caso de Android e iOS se valen de una estructura que utiliza bases de datos SQLite para almacenar gran parte de la información. Cuando se eliminan registros de los ficheros, únicamente se marcan como disponibles para sobrescritura, por lo que temporalmente siguen estando disponibles y por tanto es posible recuperarlos.

## Herramientas para IoT

(Sin terminar)

## Herramientas para móviles

En este punto se especifican una serie de herramientas Open Source y gratuitas para la adquisición de datos en dispositivos móviles.

### Android Debug Bridge (ADB)

Es una herramienta mediante la cual por comandos crea un puente entre nuestro ordenador y el teléfono móvil. Podemos traer archivos del móvil hacia nuestro ordenador gracias a ello. 

Para poder usar ADB con el dispositivo móvil, necesitamos activar la depuración USB e instalar los drivers ADB universales. Tiene una serie de comandos sencillos que permiten desde crear una shell para el dispositivo móvil como extraer o subir archivos al dispositivo móvil.

Muchas de las herramientas que se mencionarán en los siguientes puntos, utilizan o necesitan de esta herramienta instalada en nuestro ordenador.

### AFLogical OSE - Open source Android Forensics app and framework

Esta herramienta es una apk que podemos instalar en nuestro dispositivo móvil para adquirir datos. Se debe ejecutar en el dispositivo o usando adb shell.

En el dispositivo android del que queramos hacer la adquisición, debemos abrir la aplicación y elegir los datos que deseamos etraer, simplemente tendremos que seguir las instrucciones dadas por la propia apliación. Se debe tener una tarjeta SD en el dispositivo para extraer los datos en ella.

Luego copiamos estos datos a nuestro ordenador para analizar estos datos o usamos adb pull. Los datos pueden ser registros de llamadas, contactos, aplicaciones, mensajes de texto o audiovisuales… Esta información será recuperada o bien conectada a una tarjeta en un dispositivo externo o a través del ADB.

### Andriller CE

Andriller CE es una herramienta para la adquisición de dispositivos móviles. Realiza adquisiciones no destructivas, solidas y de solo lectura desde dispositivos Android. Contiene decodificadores personalizados para datos de bases de datos de android para decodificar comunicaciones. Las extraciones y los decodificadors producen informes en formatos HTML y Excel.

**Características:**

- Extracción y decodificación de datos automatizada
- Extracción de datos de dispositivos no rooteados mediante Android Backup (versiones de Android 4.x, soporte variado/limitado)
- Extracción de datos con permisos de root: demonio ADB raíz, modo de recuperación CWM o binario SU (Superusuario)
- Análisis y decodificación de datos para estructura de carpetas, archivos Tarball (de copias de seguridad de nanddroid) y copia de seguridad de Android ( archivos backup.ab )
- Selección de decodificadores de bases de datos individuales para aplicaciones de Android Descifrado de bases de datos archivadas cifradas de WhatsApp (.crypt a .crypt12, debe tener el archivo de clave correcto )
- Cracking de pantalla de bloqueo para patrón, PIN y contraseña.
- Descomprimiendo los archivos de copia de seguridad de Android
- Captura de pantalla de la pantalla de un dispositivo

### LIME- Linux Memory Extractor

Esta herramienta Open Source permite la adquisición de memoria volátil desde dispositivos basados en linux y android. Es la primera herramienta que permite captura de memoria completa en dispositivos Android. Minimiza su interacción entre el usuario y los procesos del espacio del kernel durante la adquisición lo que permite crear capturas de memorias más sólidas desde el punto de vista forense.

**Características**

- Adquisición completa de memoria de Android
- Adquisición a través de interfaz de red
- Huella mínima del proceso
- Hash de memoria volcada

### WhatsApp Xtract

Es una herramienta que permite extraer del dispositivo móvil todas las conversaciones en el ordenador. Esta aplicación de Windows trabaja con archivos .bat utilizandolo con la ruta "/sdcard/WhatsApp/Databases/msgstore.db.crypt" desde la cual tendremos que ejecutar la herramienta.

Requiere tener instalado Active Python.

## Referencias

- [https://www.incibe.es/incibe-cert/blog/herramientas-para-realizar-analisis-forenses-dispositivos-moviles](https://www.incibe.es/incibe-cert/blog/herramientas-para-realizar-analisis-forenses-dispositivos-moviles)
- [https://github.com/nowsecure/android-forensics](https://github.com/nowsecure/android-forensics)
- [https://github.com/den4uk/andriller](https://github.com/den4uk/andriller)
- [https://peritos-informaticos.com/blog/herramientas-analisis-forense-moviles/](https://peritos-informaticos.com/blog/herramientas-analisis-forense-moviles/)
- [https://www.xatakandroid.com/tutoriales/adb-android-que-puedes-utilizarlo](https://www.xatakandroid.com/tutoriales/adb-android-que-puedes-utilizarlo)
- [https://github.com/504ensicsLabs/LiME](https://github.com/504ensicsLabs/LiME)
- [https://www.ideal.es/sociedad/201504/11/como-guardar-conversaciones-whatsapp-20150410170133.html](https://www.ideal.es/sociedad/201504/11/como-guardar-conversaciones-whatsapp-20150410170133.html)