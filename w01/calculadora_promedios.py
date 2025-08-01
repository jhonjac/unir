def ingresar_calificaciones():
    """
    Función que permite al usuario ingresar materias y sus calificaciones.
    Retorna dos listas: una con los nombres de las materias y otra con las calificaciones.
    """
    materias = []
    calificaciones = []
    
    print("=== SISTEMA DE CALIFICACIONES ===")
    print("Ingrese las materias y sus calificaciones (0-10)")
    print()
    
    while True:
        # Solicitar nombre de la materia
        materia = input("Ingrese el nombre de la materia: ").strip()
        if not materia:
            print("El nombre de la materia no puede estar vacío. Intente nuevamente.")
            continue
        
        # Solicitar y validar la calificación
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para {materia} (0-10): "))
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("La calificación debe estar entre 0 y 10. Intente nuevamente.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        # Almacenar los datos
        materias.append(materia)
        calificaciones.append(calificacion)
        
        # Preguntar si desea continuar
        while True:
            continuar = input("\n¿Desea ingresar otra materia? (s/n): ").lower().strip()
            if continuar in ['s', 'si', 'sí', 'y', 'yes']:
                print()
                break
            elif continuar in ['n', 'no']:
                return materias, calificaciones
            else:
                print("Por favor, responda 's' para sí o 'n' para no.")


def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    
    Args:
        calificaciones (list): Lista de calificaciones numéricas
    
    Returns:
        float: Promedio de las calificaciones
    """
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Determina qué materias están aprobadas y cuáles reprobadas según un umbral.
    
    Args:
        calificaciones (list): Lista de calificaciones
        umbral (float): Calificación mínima para aprobar (por defecto 5.0)
    
    Returns:
        tuple: (lista de índices aprobados, lista de índices reprobados)
    """
    aprobadas = []
    reprobadas = []
    
    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    
    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Encuentra los índices de la calificación más alta y más baja.
    
    Args:
        calificaciones (list): Lista de calificaciones
    
    Returns:
        tuple: (índice de calificación máxima, índice de calificación mínima)
    """
    if not calificaciones:
        return None, None
    
    indice_max = 0
    indice_min = 0
    
    for i in range(1, len(calificaciones)):
        if calificaciones[i] > calificaciones[indice_max]:
            indice_max = i
        if calificaciones[i] < calificaciones[indice_min]:
            indice_min = i
    
    return indice_max, indice_min


def main():
    """
    Función principal que coordina todo el programa.
    """
    print("¡Bienvenido al Sistema de Gestión de Calificaciones!")
    print("=" * 50)
    
    # Obtener datos del usuario
    materias, calificaciones = ingresar_calificaciones()
    
    # Verificar si se ingresaron materias
    if not materias:
        print("\nNo se ingresaron materias. El programa terminará.")
        print("¡Hasta luego!")
        return
    
    print("\n" + "=" * 50)
    print("RESUMEN DE CALIFICACIONES")
    print("=" * 50)
    
    # Mostrar todas las materias con sus calificaciones
    print("\n📚 MATERIAS Y CALIFICACIONES:")
    print("-" * 30)
    for i, (materia, calificacion) in enumerate(zip(materias, calificaciones), 1):
        print(f"{i:2d}. {materia:<20} : {calificacion:5.1f}")
    
    # Calcular y mostrar promedio general
    promedio = calcular_promedio(calificaciones)
    print(f"\n📊 PROMEDIO GENERAL: {promedio:.2f}")
    
    # Determinar materias aprobadas y reprobadas
    aprobadas, reprobadas = determinar_estado(calificaciones)
    
    print(f"\n✅ MATERIAS APROBADAS ({len(aprobadas)}):")
    if aprobadas:
        for i in aprobadas:
            print(f"   • {materias[i]} ({calificaciones[i]:.1f})")
    else:
        print("   Ninguna materia aprobada")
    
    print(f"\n❌ MATERIAS REPROBADAS ({len(reprobadas)}):")
    if reprobadas:
        for i in reprobadas:
            print(f"   • {materias[i]} ({calificaciones[i]:.1f})")
    else:
        print("   Ninguna materia reprobada")
    
    # Encontrar calificaciones extremas
    indice_max, indice_min = encontrar_extremos(calificaciones)
    
    if indice_max is not None and indice_min is not None:
        print(f"\n🏆 MEJOR CALIFICACIÓN:")
        print(f"   {materias[indice_max]} con {calificaciones[indice_max]:.1f}")
        
        print(f"\n📉 PEOR CALIFICACIÓN:")
        print(f"   {materias[indice_min]} con {calificaciones[indice_min]:.1f}")
    
    # Mensaje de despedida
    print("\n" + "=" * 50)
    print("¡Gracias por usar el Sistema de Gestión de Calificaciones!")
    print("¡Que tengas un excelente día! 🎓")
    print("=" * 50)


if __name__ == "__main__":
    main()