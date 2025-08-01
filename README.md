# Trabajo 1: Sintaxis Python
Desarrollo de una calculadora de promedios escolares en Python utilizando variables, operadores, estructuras de control y funciones básicas.

## Instrucciones
Crea un nuevo archivo Python llamado calculadora_promedios.py que contendrá todo el código de tu programa.

Implementa una función llamada ingresar_calificaciones() que permita al usuario introducir el nombre de una materia y su calificación correspondiente. Esta función debe:

Solicitar al usuario que ingrese el nombre de la materia
Solicitar la calificación (validando que sea un número entre 0 y 10)
Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones)
Preguntar si desea continuar ingresando más materias
Retornar ambas listas cuando el usuario decida terminar
Crea una función calcular_promedio(calificaciones) que reciba una lista de calificaciones y devuelva el promedio de todas ellas.

Desarrolla una función determinar_estado(calificaciones, umbral) que reciba la lista de calificaciones y un valor umbral (por defecto 5.0), y devuelva dos listas: una con los índices de las materias aprobadas y otra con los índices de las reprobadas.

Implementa una función encontrar_extremos(calificaciones) que identifique el índice de la calificación más alta y el índice de la más baja en la lista de calificaciones.

En la función principal (main), llama a la función ingresar_calificaciones() para obtener los datos del usuario.

Utiliza las funciones creadas para calcular el promedio general, determinar materias aprobadas/reprobadas y encontrar las materias con calificaciones extremas.

Muestra un resumen final que incluya:

Todas las materias con sus calificaciones
El promedio general
Las materias aprobadas y reprobadas
La materia con mejor calificación y su valor
La materia con peor calificación y su valor
Asegúrate de manejar casos especiales, como cuando no se ingresa ninguna materia, utilizando estructuras condicionales apropiadas.

Finaliza el programa con un mensaje de despedida e implementa la estructura if __name__ == "__main__": para ejecutar la función principal.
