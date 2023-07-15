
def menu_ingreso():
    opcion = int(input('Menu\n----------\t'+
                       '\n\t1. Añadir nuevo libro'
                       '\n\t2. Ver lista de libros'
                       '\n\t3. Buscar libro por título'
                       '\n\t4. Inscribir usuario'
                       '\n\t5. Inscribir empleado'
                       '\n\t6. Salir del sistema\n'))
    if opcion ==1:
        print('Añadiendo el nuevo libro')
    elif opcion ==2:
        print('Mostrando la lista de libros')
    elif opcion ==3:
        print('Buscando el libro por título')
    elif opcion ==4:
        print('Usuario inscrito')
    elif opcion ==5:
        print('Empleado instrito')
    else:
        print('¡Opción no valida!')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu_ingreso()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
