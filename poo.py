# codigo en poo reaciendo el taller previo

class Invention():
    name = ""
    century = 18
    def _init_ (self, name, century):
        self.name = name
        self.century = century
        
    def inset_invents ( self, name ):
        inventions.append(self.name)
        return inventions
    def print_list():
        print("lista en una fila: {} \n ".format(inventions))
        print("lista elemento por elemento: \n")
        for invent in inventions:
            print(invent)

inteligencia_artificial = Invention("Inteligencia artificial (IA)", 20 ) 
robotica_ia = Invention("Robótica + IA", 20) 
biotecnologia_ed = Invention("Biotecnología y Edición Genómica ", 20 )
telefono = Invention("El teléfono ", 19 )
nanotecnologia = Invention("Nanotecnología ", 20)
energia_renovable = Invention("Energía renovable ", 20)
almacenamiento_energia = Invention("Almacenamiento de energía", 20)  
bomba_vapor = Invention("La bomba de vapor ", 18)
computascion_cuantica = Invention("Computación cuántica ", 21) 
maquina_coser = Invention("Máquina de coser ", 19)
interfas_neuronal = Invention("Interfaces neuronales ", 21)
coche_sin_conductor = Invention("coche sin conductor ", 21)
realidad_virtual_aumentada = Invention("Realidad Virtual y Aumentada ", 21)
maquina_vapor = Invention("La máquina de vapor ", 18)
exploracion_espacial = Invention("Exploración espacial y colonización", 20)

inventions = {inteligencia_artificial.name, 
    robotica_ia.name, biotecnologia_ed.name,
    telefono.name, nanotecnologia.name,
    energia_renovable.name, almacenamiento_energia.name, 
    bomba_vapor.name, computascion_cuantica.name,
    maquina_coser.name, interfas_neuronal.name,
    coche_sin_conductor.name, realidad_virtual_aumentada.name,
    maquina_vapor.name, exploracion_espacial.name }

Invention.print_list()

Invention.inset_invents("El iPad")
Invention.inset_invents("Los LED azules")

if "Impresion 3D" not in inventions:
    Invention.inset_invents("Impresion 3D")
elif "Internet de las cosas (IoT)" not in inventions:
    Invention.inset_invents("Internet de las cosas (IoT)")
elif "coche sin conductor " in inventions:
    x = inventions.index("coche sin conductor")
    inventions.remove("coche sin conductor")
    inventions.insert(x, "coche autonomo")
    
print("lista ordenada ascendente es: {}\n".format(inventions.sort()))
ordered_inventions = inventions.copy()
ordered_inventions.sort()
print("la lista ordenada descendiente es: {}\n".format(ordered_inventions.reversed()))
print("la lista tiene una longitud de: {}\n".format(inventions.len))
