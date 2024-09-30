Repositorio de Arquitectura Cliente-Servidor
Este repositorio contiene un ejemplo de aplicación cliente-servidor desarrollado en HTML y JavaScript, utilizando WebSockets para permitir la comunicación en tiempo real entre múltiples clientes y un servidor.

1. Estructura del Repositorio
Servidor: Contiene el código fuente para el servidor que maneja las conexiones de los clientes.
Cliente: Incluye el código fuente para el cliente que se conecta al servidor y envía/recibe mensajes.
README.md: Este archivo, que proporciona información sobre el proyecto.
2. Descripciones Detalladas de las Carpetas
a. Servidor
Implementación del servidor que maneja múltiples conexiones de clientes simultáneamente utilizando WebSockets.
Utiliza hilos (threads) para permitir la comunicación concurrente entre el servidor y varios clientes.
Identifica a los clientes y reenvía mensajes entre ellos.
Responde a mensajes específicos enviados por los clientes.
b. Cliente
Implementación del cliente que se conecta al servidor.
Solicita al usuario la IP y el puerto del servidor al que desea conectarse.
Permite al usuario enviar mensajes y recibir mensajes de otros clientes a través del servidor.
Permite a los clientes identificarse con un nombre o ID único.
3. Ejecución de los Proyectos
Clona este repositorio a tu máquina local.
Instala Python: Asegúrate de que tienes Python instalado en tu sistema.

Inicia el servidor:

Navega a la carpeta del servidor en la terminal.

Ejecuta el servidor con el siguiente comando
Inicia los clientes:

Abre un navegador web y carga el archivo cliente.html.
Cada cliente deberá ingresar la IP y el puerto del servidor para conectarse.

4. Requisitos Previos
Asegúrate de tener instalado Python 3.x.
5. Notas Adicionales
El cliente permite múltiples conexiones, así que puedes abrir varias ventanas del navegador para probar la comunicación entre diferentes clientes.
El puerto por defecto es 2020, asegúrate de que este puerto esté disponible.
