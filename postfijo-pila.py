# -*- coding: utf-8 -*-
class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            print "la pila esta vacia"
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

def postfijo(lista):
    #   postfijo([4,3,"+",5,8,"*","-"]);
    p=Pila()
    tam=len(lista)
    for x in range(tam):
        if type(lista[x])==int:
            p.apilar(lista[x])
        else:
            p.apilar(operar(lista[x],p.desapilar(),p.desapilar()))
    return p.desapilar()
    
def operar(o, y, x):
    if o=="+":
        z=x+y
    if o=="-":
        z=x-y
    if o=="*":
        z=x*y
    if o=="/":
        z=x/y
    return z

def start ():
    print ("Escribe la lista de elementos en postfijo a ingresar: dentro de [] y separado por comas [a, b, +]")
    lista=raw_input("Escribe la lista de elementos en postfijo a ingresar: dentro de [] y separado por comas [a, b, +]")
    postfijo(lista)

    
start()
