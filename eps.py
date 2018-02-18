class Cola:
    def __init__(self):
        self.items=[]

    def encolar(self, a):
        self.items.append(a)

    def desencolar(self):
	if self.es_vacia():
            return None 
        else:
            return self.items.pop(0)

    def es_vacia(self):
        return self.items == []

def start():
    odt=Cola()
    fisio=Cola()
    medGen=Cola()
    while True:
        print ("\n1- Agregar Nuevo Paciente")
        print ("2- Llamar al proximo Paciente")
        print ("3- Cantidad de pacientes")
        print ("4- Salir \n")
        res=raw_input("")
        res=int(res)
        if res==1:
            paciente=raw_input("Nombre del paciente\n")
            while True:
                print ("\nQue tipo de Cita?")    
                print ("1- Odontologia")
                print ("2- Fisioterapia")
                print ("3- Medicina General")
                x=raw_input("")
                x= int(x)
                if x==1:
                    odt.encolar(paciente)
		    break
                elif x==2:
                    fisio.encolar(paciente)
                    break
	        elif x==3:
                    medGen.encolar(paciente)
                    break
	        else:
                    break
        if res==2:
            while True:
                print ("Que tipo de Cita desea atender?\n")    

                print ("1- Odontologia")
                print ("2- Fisioterapia")
                print ("3- Medicina General")
                y=raw_input("")
                y= int(y)
                if y==1:
		    print ("El paciente "+odt.desencolar() +" fue atendido")
                    break
                elif y==2:
	            print ("El paciente "+fisio.desencolar()+" fue atendido")
                    break

                elif y==3:
	            print ("El paciente "+medGen.desencolar()+" fue atendido")
                    break
                else:
                    break
        	  
        if res==3:
                print ("\nCantidad de pacientes por: ")    




                print ("Odontologia: ") 
                print(odt.items)
                print ("Fisioterapia: ")
                print(fisio.items)
                print ("Medicina General ")
                print (medGen.items)
                
        if res==4:
            break

start()





