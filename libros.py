import os
import time

#lista donde se guardarán todos los libros
lista_libros=[]

def ingresar():
    os.system("cls")
    print("===INGRESAR LIBROS===")
    libro={}
    try:
        libro["codigo"]=int(input("Ingrese código numérico del libro: "))
        libro["titulo"]=input("Ingrese título del libro: ")
        libro["autor"]=input("Ingrese autor: ")
        libro["stock"]=int(input("Ingrese stock disponible: "))
        lista_libros.append(libro)
    except ValueError:
        print("Error, código y stock deben ser valores numéricos")
    time.sleep(3)

def listar():
    os.system("cls")
    print("=== LISTADO DE LIBROS ===")
    if len(lista_libros)==0:
        print("No hay libros registrados")
    else:
        for libro in lista_libros:
            print(f"codigo: {libro["codigo"]} - Título: {libro["titulo"]} - Autor: {libro["autor"]} - Stock: {libro["stock"]}")
    time.sleep(3)

def buscar():
    os.system("cls")
    print("=== BUSCAR LIBROS ===")
    try:
        codigo=int(input("Ingrese código del libro a buscar: "))
        encontrado=False
        for libro in lista_libros:
            if libro["codigo"]== codigo:
                print("Libro encontrado")
                print(f"Título: {libro["titulo"]} - Autor: {libro["autor"]} - Stock: {libro["stock"]}")
                encontrado=True
                break #el break es para que no siga recorriendo la lista si ya encontró el libro
        if encontrado==False:
            print("No existe un libro con ese código")
    except ValueError:
        print("Debe ingresar sólo números")
    time.sleep(3)

def eliminar():
    os.system("cls")
    print("===ELIMINAR LIBRO===")
    try:
        codigo=int(input("Ingrese código del libro a eliminar: "))
        encontrado=False
        for libro in lista_libros:
            if libro["codigo"]==codigo:
                lista_libros.remove(libro)
                encontrado=True
                print("Libro eliminado correctamente...")
                break
            
        if encontrado==False:
            print("No existe un libro con ese código")
    except ValueError:
        print("Debe ingresar sólo números")
    time.sleep(3)

def modificar():
    os.system("cls")
    print("=== MODIFICAR LIBRO ===")
    try:
        codigo=int(input("Ingrese el código del libro a modificar: "))
        encontrado=False
        for libro in lista_libros:
            if libro["codigo"]==codigo:
                print("Libro encontrado, ingrese nuevos datos:")
                libro["titulo"]=input("Nuevo título: ")
                libro["autor"]=input("Nuevo autor: ")
                libro["stock"]=int(input("Nuevo stock: "))
                encontrado=True
                print("Libro modificado correctamente...")
                break

        if encontrado==False:
            print("No existe un libro con ese código")
    except ValueError:
        print("Debe ingresar sólo números")
    time.sleep(3)

def menu():
    ciclo=True
    while ciclo:
        os.system("cls")
        print('''
    ===MENÚ BIBLIOTECA===
    1. Ingresar Libro
    2. Listar libro
    3. Buscar libro
    4. Eliminar libro
    5. Modificar libro
    6. Salir
        ''')
        try:
            op=int(input("Seleccione una opción (1-6): "))
            match op:
                case 1:
                    ingresar()
                case 2:
                    listar()
                case 3:
                    buscar()
                case 4:
                    eliminar()
                case 5:
                    modificar()
                case 6:
                    ciclo=False
                case _:
                    print("Opción inválida")
                    time.sleep(3)
        except ValueError:
            print("Debe ingresar sólo números")
            time.sleep(3)
    print("Adios...")

menu()