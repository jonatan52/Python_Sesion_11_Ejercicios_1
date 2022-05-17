#Ejercicio 1

# Enunciado del ejercicio:

# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.


import sqlite3

def conexion():
    conexion = sqlite3.connect("Colegio.db")
    conexion.commit()
    conexion.close()


def crear_tabla():
    conexion = sqlite3.connect("Colegio.db")
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL
    )
    """)
    conexion.commit()
    conexion.close()

def insertar_datos():
    conexion = sqlite3.connect("Colegio.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Alumnos VALUES (NULL, 'Juan', 'Perez')")
    cursor.execute("INSERT INTO Alumnos VALUES (NULL, 'Maria', 'Garcia')")
    cursor.execute("INSERT INTO Alumnos VALUES (NULL, 'Pablo', 'Zabaleta')")
    cursor.execute("INSERT INTO Alumnos VALUES (NULL, 'Juan', 'Gomez')")
    cursor.execute("INSERT INTO Alumnos VALUES (NULL, 'Maria', 'Gonzalez')")
    cursor.execute("INSERT INTO Alumnos VALUES (NULL, 'Pedro', 'Garcia')")
    cursor.execute("INSERT INTO Alumnos VALUES (NULL, 'Juan', 'Lopez')")
    cursor.execute("INSERT INTO Alumnos VALUES (NULL, 'Maria', 'Quiroz')")
    conexion.commit()
    conexion.close()    

def buscar_alumno():
    conexion = sqlite3.connect("Colegio.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Alumnos WHERE nombre='Juan'")
    print(cursor.fetchall())
    conexion.commit()
    conexion.close()

    
   

if __name__ == "__main__":
    #conexion()
    #crear_tabla()
    #insertar_datos()
    buscar_alumno()