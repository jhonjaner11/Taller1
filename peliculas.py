from pila import Pila

print("Escoger una película hoy")

generos = Pila()
pelicula = Pila()

print("1. Mostrar las de acción")
print("2. Mostrar las de drama")
print("3. Mostrar las de terror")
print("4. Mostrar los documentales")
print("5. Mostrar las de culto")
print("6. Mostrar las de animación")
                                    
generos.apilar("Acción")
generos.apilar("Drama")
generos.apilar("Terror")
generos.apilar("Documental")
generos.apilar("Culto")
generos.apilar("Animación")

accion = Pila()
drama = Pila()
terror = Pila()
documental = Pila()
culto = Pila()
animacion = Pila()

accion.apilar("Terminator")
accion.apilar("Duro de matar")
accion.apilar("Búsqueda implacable")
accion.apilar("Identidad desconocida")
accion.apilar("La liga de la justicia")

drama.apilar("Titanic")
drama.apilar("El pianista")
drama.apilar("Forrest Gump")
drama.apilar("La lista de Schindler")
drama.apilar("La vida es bella")

terror.apilar("Eso")
terror.apilar("El conjuro")
terror.apilar("La noche del demonio")
terror.apilar("El resplandor")
terror.apilar("Juegos macabros 1")

documental.apilar("La segunda guerra mundial")
documental.apilar("otro documental")
documental.apilar("otro documental")
documental.apilar("otro documental")
documental.apilar("otro documental")

culto.apilar("Tiempos violentos")
culto.apilar("La naranja mecánica")
culto.apilar("Donnie Darko")
culto.apilar("Trainspotting")
culto.apilar("El club de la pelea")

animacion.apilar("Los increibles")
animacion.apilar("Buscando a Nemo")
animacion.apilar("El rey león")
animacion.apilar("Up")
animacion.apilar("Grandes héroes")

def desapilarAccion():
    while accion.es_vacia() == False:
        print(accion.desapilar())
    print("No hay más de acción")
    
def desapilarDrama():
    while drama.es_vacia() == False:
        print(drama.desapilar())
    print("No hay más de drama")

def desapilarTerror():
    while terror.es_vacia() == False:
        print(terror.desapilar())
    print("No hay más de terror")

def desapilarDocumental():
    while documental.es_vacia() == False:
        print(documental.desapilar())
    print("No hay más documentales")

def desapilarCulto():
    while culto.es_vacia() == False:
        print(culto.desapilar())
    print("No hay más de culto")

def desapilarAnimacion():
    while animacion.es_vacia() == False:
        print(animacion.desapilar())
    print("No hay más de animación")


def preguntar(numero):
    
    if numero == 1:
        print(accion.es_vacia())
        desapilarAccion()      
    else:
        if numero == 2:
            print(drama.es_vacia())
            desapilarDrama()
        else:
            if numero == 3:
                print(terror.es_vacia())
                desapilarTerror()
            else:
                if numero == 4:
                    print(documental.es_vacia())
                    desapilarDocumental()
                    
                else:
                    if numero == 5:
                        print(culto.es_vacia())
                        desapilarCulto()
                    else:
                        if numero == 6:
                            print(animacion.es_vacia())
                            desapilarAnimacion()
                        else:
                            print("Hagalo nuevamente por favor")
                            

numero = int(input("digite el número:"))
preguntar(numero)

def preguntarNuevamente(res):
    print("Desea ver otro género")
    while respuesta == 's' or 'S':
        numero = int(input("digite el número:"))
        preguntar(numero)      
print("Desea ver otro género")

respuesta = (input("S/N:"))
preguntarNuevamente(respuesta)















    
        
            
        
