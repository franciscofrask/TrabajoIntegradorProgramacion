# Simulación de una Biblioteca - Búsqueda y Ordenamiento con Bubble Sort, Búsqueda Binaria y Lineal

def mostrar_libros(libros):
    print("\n📚 Lista de libros disponibles:")
    for i, libro in enumerate(libros):
        print(f"{i + 1}. {libro}")

def bubble_sort(libros, ascendente=True):
    n = len(libros)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascendente and libros[j].lower() > libros[j+1].lower()) or (not ascendente and libros[j].lower() < libros[j+1].lower()):
                libros[j], libros[j+1] = libros[j+1], libros[j]
    return libros

def busqueda_binaria(libros, titulo):
    low = 0
    high = len(libros) - 1
    while low <= high:
        mid = (low + high) // 2
        if libros[mid].lower() == titulo.lower():
            return True
        elif libros[mid].lower() < titulo.lower():
            low = mid + 1
        else:
            high = mid - 1
    return False

def busqueda_lineal(libros, titulo):
    for libro in libros:
        if libro.lower() == titulo.lower():
            return True
    return False

def menu():
    libros = [
        "El Principito",
        "Cien Años de Soledad",
        "Rayuela",
        "Don Quijote",
        "Ficciones",
        "La Odisea",
        "1984",
        "Crimen y Castigo"
    ]

    while True:
        print("\n🔹 Menú Biblioteca 🔹")
        print("1. Mostrar lista de libros")
        print("2. Ordenar libros (Bubble Sort)")
        print("3. Buscar un libro")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_libros(libros)

        elif opcion == "2":
            orden = input("¿Orden ascendente (A) o descendente (D)? ").lower()
            if orden == "a":
                libros = bubble_sort(libros, ascendente=True)
                print("✔ Libros ordenados ascendentemente (Bubble Sort).")
            elif orden == "d":
                libros = bubble_sort(libros, ascendente=False)
                print("✔ Libros ordenados descendentemente (Bubble Sort).")
            else:
                print("❌ Opción inválida.")

        elif opcion == "3":
            metodo = input("¿Usar búsqueda binaria (B) o lineal (L)? ").lower()
            titulo = input("🔍 Ingresa el título del libro a buscar: ")

            if metodo == "b":
                if libros != sorted(libros, key=lambda x: x.lower()):
                    print("⚠️ Los libros deben estar ordenados ascendentemente para usar búsqueda binaria. Ordenándolos automáticamente...")
                    libros = bubble_sort(libros, ascendente=True)
                encontrado = busqueda_binaria(libros, titulo)
            elif metodo == "l":
                encontrado = busqueda_lineal(libros, titulo)
            else:
                print("❌ Método de búsqueda inválido.")
                continue

            if encontrado:
                print(f"📖 El libro '{titulo}' está en la biblioteca.")
            else:
                print(f"❌ El libro '{titulo}' no se encuentra.")

        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
