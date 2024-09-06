

inventions = ["inteligencia artificial (IA)", "Robotica + IA", "Biotecnologia y Edición Genómica", "El teléfono", "Nanotecnología", "Energia renovable", "Almacenamiento de energía", "La bomba de vapor", "computacion cuántica", "Máquina de coser", "Interfaces neuronales", "coche sin conductor", "Realidad Virtual y Aumentada", "La máquina de vapor", "Exploración espacial y colonización"]
option = 1
I = 0
def print_list(option):
    if (option == 1):
        print(inventions)
    elif ( option == 2):
            for invent in inventions:
                print(invent)
    else :
        print ("error opcion no valida")
def delete_items():
    for invent in inventions:
        inventions.remove("El teléfono")
        inventions.remove("Energia renovable")
        inventions.remove( "Máquina de coser")
        inventions.remove( "Nanotecnología")
        inventions.remove( "La bomba de vapor")
        inventions.remove( "Biotecnologia y Edición Genómica")
        inventions.remove( "Almacenamiento de energía")
        inventions.remove( "inteligencia artificial (IA)")
        inventions.remove( "computacion cuántica")
        inventions.remove( "Realidad Virtual y Aumentada")
        inventions.remove( "La máquina de vapor")
        inventions.remove( "Exploración espacial y colonización" )
        if ( invent == "Los LED azules"):
            inventions.remove("Los LED azules")
        return inventions
        
def insert_invents(invent):
    inventions.append(invent)
    return inventions
            
            
while I != 404 :
    print(" MENU \n 1.  imprimir lista en una sola fila \n 2. imprimir lista elemento por elemento \n 3. Eliminar inventos fuera de este siglo\n 4. adicione elementos\n 5. comprobar o agregar el elemento impresion 3D\n 6. comprobar o agregar el elemento Internet de las cosas (IoT)\n 7. Actualizar elemento 'coche sin conductor' a 'coche autonomo' \n 8. mostrar la lista ordenada ascendentemente\n 9. mostrar la lista ordenada descendentemente \n  10. mostrar la cantidad de elementos que tiene la lista\n 404. para salir")
    option = int(input(" Ingrese una opcion "))
    
    if ( option == 1 ):
        print_list(option)
    elif ( option == 2 ):
        print_list(option)
    elif (option == 3 ):
        delete_items()
    elif (option == 4 ):
        insert_invents("El iPad")
        insert_invents("Los LED azules")
        print("se adicionaron los elementos: 'El iPad' y 'Los LED azules' ")
    elif (option == 5 ):
        if "Impresión 3D" not in inventions:
            inset_invents("Impresión 3D")
    elif (option == 6 ):
        if "Internet de las cosas(IoT)" not in inventions:
            inset_invents("Internet de las cosas(IoT)")
    elif ( option == 7 ):
        if "coche sin conductor" in inventions:
            x = inventions.index("coche sin conductor")
            inventions.remove("coche sin conductor")
            inventions.insert(x, "coche autónomo")
    elif ( option == 8 ):
        print (inventions.sort())
    elif ( option == 9 ):
        inventions_order = inventions.copy()
        inventions_order.sort()
        print( inventions_order.reversed())
    elif ( option == 10 ):
        print (inventions.len())
    elif (option == 404 ):
        I == option
        break
    else: 
        print("que es esa opcion???")
        
