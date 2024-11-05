from calificacion import Calificacion
from calificacionDAO import CalificacionDAO

print('****Calificaciones****')
opcion=None
while opcion!=5:
    print('Menú:')
    print('1. Mostrar calificaciones')
    print('2. Agregar una calificación')
    print('3. Actualizar una calificación')
    print('4. Eliminar una aplicación')
    print('5. Salir del menú')
    opcion=int(input('Escribe tu opción (1-5): '))
    if opcion==1:
        calificaciones=CalificacionDAO.seleccionar()
        print('\n*** Calificaciones***')
        for calificacion in calificaciones:
            print(calificacion)
        print()
    elif opcion==2:
        estudiante=input('Escribe el nombre del estudiante: ')
        asignatura=input('Escribe el nombre de la asignatura: ')
        nota=float(input('Escribe el valor de la nota (0-5) : '))
        calificacion=Calificacion(estudiante,asignatura,nota)
        calificaciones_insertadas=CalificacionDAO.insertar(calificacion)
        print(f'Calificaciones insertadas: {calificaciones_insertadas}')
    elif opcion==3:
        estudiante=input('Escribe el nombre del estudiante: ')
        asignatura=input('Escribe el nombre de la asignatura: ')
        nota=float(input('Escribe el valor de la nueva nota del estudiante (0-5) : '))
        calificacion_actualizar=Calificacion(estudiante,asignatura,nota) 
        calificaciones_actualizadas=CalificacionDAO.actualizar(calificacion_actualizar)
        print(f'Calificaciones actualizadas: {calificaciones_actualizadas}')
    elif opcion==4:
        estudiante=input('Escribe el nombre del estudiante: ')
        asignatura=input('Escribe el nombre de la asignatura: ')
        calificacion_eliminada=Calificacion(estudiante,asignatura)
        calificaciones_eliminadas=CalificacionDAO.eliminar(calificacion_eliminada)
        print(f'Calificaciones eliminadas: {calificaciones_eliminadas}')
else:
    print('Saliendo del menú...')