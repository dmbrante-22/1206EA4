#Funciones: sin parametros / sin retorno
#           sin parametros / con retorno
#           con parametros / sin retorno
#           con parametros / con retorno
#Validación:agregar personas a una lista, cuyos datós serán:
#           rut /nombre/edad
#           Debe generar una función separada para validar:
#           rut - sin espacios y largo entre 7 - 9 caracteres
#           nombre - sin espacio y largo minimo 3
#           edad -  numero entre 10 y 99
lista_personas=[] #Aquí es donde se van a ir guardando todas las personas

def menu(): #No tiene parametros ni tiene retorno
    print("===MENÚ PRINCIPAL===")
    print("1. Agregar persona")
    print("2. Listar persona")
    print("3. Salir")

def seleccion(): #Esta funcion me debe devolver el numero que yo he seleccionado desde el teclado
    try: #opción sin parametros (porque no pide nada) y con retorno
        op=int(input("Seleccione: "))
        if op>=1 and op<=3:
            return op
        print("Sólo números entre 1 y 3")
        return 0 #Es un valor que indica que no es correcto
    except ValueError:
        print("Ingrese solo numeros")
        return 0

def rutas(op): #funcion que recibe un parametro
    match op:
        case 1:
            print("===AGREGAR UNA PERSONA===")
            resp=ingresarPersona(lista_personas)
            if resp == True:
                print("Grabó...")
            else:
                print("No grabó")
        case 2:
            print("===LISTAR LAS PEROSNAS===")
            listar()
        case 3:
            print("===ELIMINAR===")
            resp=eliminar(lista=lista_personas)



def validarRut(rut):
    if len(rut.strip()) in (7,8):
        return True
    return False

def validarNombre(nom):
    if len(nom.strip())>=3:
        return True
    return False

def validarEdad(ed):
    try:
        ed=int(ed)
        if ed>=10 and ed<=99:
            return True
        return False
    except ValueError:
        print("Debe ingresar un número")
        return False
def listar(lista):
    for p in lista:
        print(f"rut: {p["rut"]} - Nombre: {p["nombre"]} - Edad: {p["edad"]}")
        
def ubicarRegistro(rut,lista):
    for indice,p in enumerate (lista):
        if p ["rut"]==rut:
            return indice
    return -1

def eliminar(lista):
    rut=input("Ingrese rut a eliminar")
    resp=validarRut(rut)
    if resp==False:
        print("Rut incorrecto")
        return False
    ubicacion=ubicarRegistro(rut,lista)
    if ubicacion != 1:
        lista.pop(ubicacion)
        print("Eliminó")
    else:
        print("no existe")
    
def ingresarPersona(lista):
    perso={} #Crear una colección
    rut =input("Ingrese el rut: ")
    resp=validarRut(rut)
    if resp==False:
        print("Rut incorrecto")
        return False
    
    nombre=input("Ingrese nombre: ")
    resp=validarNombre(nombre)
    if resp==False:
        print("Nombre minimo 3 caracteres")
        return False
    
    edad=input("Ingrese edad: ")
    resp=validarEdad(edad)
    if resp==False:
        print("Edad incorrecta, debe ser entre 10 y 99")
        return False
    perso={
        "rut":rut,"nombre":nombre,"edad":int(edad)
    }#Se construye la colección con todos los datos validados
    lista.append(perso)
    return True

ciclo=True
while ciclo:
    menu() #sin parametro / sin retorno
    opcion=seleccion() #sin parametros / con retorno
    rutas(opcion)#con parametros / sin retorno