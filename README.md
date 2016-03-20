# InventarioLibros

•Desarrollada en Python 3 con la ayuda de QPython 3

◦QPython es una App que se distribuye para dispositivos con Android

◦QPython permite ejecutar código Python desde tu dispositivo móvil

•Utiliza SL4A

◦SL4A es la abreviatura de "Scripting Layer for Android", esto es, una capa de software para utilizar scripts en Android. Es una librería que permite la creación y ejecución de scripts, escritos en distintos lenguajes, en dispositivos Android

◦Estos scripts tienen acceso a muchas de las APIs (Interfaz de programación de aplicaciones ) disponibles en los programas Android desarrollados normalmente en Java, pero con un interfaz simplificado. Los scripts pueden ejecutarse en un terminal, o como servicio utilizando la arquitectura de servicios en Android

•Emplea SQLite

◦Es un sistema de gestión de base de datos relacional pequeño

◦Viene incluido en los dispositivos Android

◦Python incluye soporte para Sqlite con el módulo sqlite3

•Los datos para generar el QR-Code estan en formato JSON

◦El formato JSON (Javascript Object Notation) es un formato popular para la representación de estructuras de datos fáciles de leer y escribir tanto por un ser humano como por un programa

◦La estructura es un conjunto de pares (clave,valor) encerrado entre los caracteres “{” y “}”, separando la clave del valor por el símbolo “:”, y separando cada par del siguiente con el carácter “,”

•Consta de las clases

◦data.py se encarga de la conexión a la base de datos y la ejecución de sentencias SQL

◦libro.py y libroDao.py mantienen los datos de los libros, agrega nuevos libros, modifica el estado de los ya existentes, lista el catálogo de los libros, busca títulos y autores 

◦view.py define toda la interfaz de la aplicación, el menú de inicio, la entrada de los QR-Code, la presentación de la información de un libro, la captura del patrón de búsqueda, la lista de títulos del catálogo

•Adicionalmente tiene los archivos

◦utils.py, con funciones de apoyo para convertir cadenas de caracteres a diccionarios y diccionarios a listas

◦main.py, el módulo principal con las reglas descritas en las opciones de la aplicación

◦queries.py, las cadenas de texto que usa la App, sentencias SQL

