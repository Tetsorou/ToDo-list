ToDo-list: Proyecto en Java + Python + SQLite
=============================================

Este proyecto combina una aplicación backend en Java y un frontend en Python (usando Streamlit), con una base de datos SQLite compartida. El objetivo es gestionar tareas de manera colaborativa entre diferentes tecnologías.

Requisitos
----------
- Java 17 o superior
- Maven
- Python 3.10 o superior
- pip

Estructura del proyecto
-----------------------
- /src/ : Contiene el código Java. El archivo principal es:
  src/main/java/org/example/Main.java

- /frontend/ : Contiene la interfaz visual usando Streamlit.
  - app.py          → App principal
  - utils.py        → Funciones auxiliares
  - requirements.txt→ Dependencias de Python

- structure.sql : Script para crear las tablas en SQLite
- tasks.db       : Archivo de base de datos SQLite ya generado
- pom.xml        : Archivo Maven para compilar el backend
- README.txt     : Este archivo

Cómo correr el proyecto
-----------------------

[1] Backend Java
----------------
1. Asegúrate de tener Java y Maven instalados.
2. Desde la raíz del proyecto, ejecuta:

   mvn compile
   mvn exec:java -Dexec.mainClass="org.example.Main"

[2] Frontend con Streamlit (Python)
-----------------------------------
1. Navega a la carpeta frontend:
   cd frontend

2. Crea un entorno virtual (opcional pero recomendado):
   python -m venv venv
   venv\Scripts\activate  (Windows)
   source venv/bin/activate (Linux/macOS)

3. Instala dependencias:
   pip install -r requirements.txt

4. Corre la app:
   streamlit run app.py

[3] Base de datos
-----------------
- El archivo tasks.db ya está incluido.
- Si deseas recrearlo, ejecuta el script structure.sql usando:
  - DB Browser for SQLite (gráfico)
  - o por terminal: sqlite3 tasks.db < structure.sql

Notas adicionales
-----------------
- El backend y frontend se comunican usando el archivo SQLite.
- Se puede expandir usando sockets o APIs REST en el futuro.

