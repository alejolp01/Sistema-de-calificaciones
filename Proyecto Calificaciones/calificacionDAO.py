from calificacion import Calificacion
from conexion import Conexion

# DAO = Data Access Object
class CalificacionDAO:
    SELECCIONAR='SELECT * FROM calificaciones'
    INSERT= 'INSERT INTO calificaciones(Estudiante, Asignatura, Nota) VALUES(%s,%s,%s)'
    ACTUALIZAR='UPDATE calificaciones SET Nota=%s WHERE Estudiante=%s AND Asignatura=%s '
    ELIMINAR='DELETE FROM calificaciones WHERE Estudiante=%s AND Asignatura=%s '
    
    @classmethod
    def seleccionar(cls):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros=cursor.fetchall()
            # Mapeo de clase-tabla calificaciones
            calificaciones=[]
            for registro in registros:
                calificacion=Calificacion(registro[0],registro[1],registro[2])
                calificaciones.append(calificacion)
            return calificaciones
        except Exception as e:
            print(f'Ocurrió un error: {e}')
        finally:
            if cursor is not None: 
                cursor.close() # Liberamos cualquier objeto de conexión para que esté disponible para otro usuario 
            if conexion is not None:
                Conexion.liberar_conexion(conexion)
                
    @classmethod 
    def insertar(cls, calificacion):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(calificacion.Estudiante,calificacion.Asignatura,calificacion.Nota)
            cursor.execute(cls.INSERT, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar la calificación: {e}')
        finally:
            if cursor is not None: 
                cursor.close() # Liberamos cualquier objeto de conexión para que esté disponible para otro usuario 
            if conexion is not None:
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def actualizar(cls,calificacion):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(calificacion.Nota, calificacion.Estudiante, calificacion.Asignatura)
            cursor.execute(cls.ACTUALIZAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e: 
            print(f'Ocurrió un error al actualizar la calificación: {e}')
        finally:
            if cursor is not None: 
                cursor.close() # Liberamos cualquier objeto de conexión para que esté disponible para otro usuario 
            if conexion is not None:
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def eliminar(cls,calificacion):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(calificacion.Estudiante, calificacion.Asignatura)
            cursor.execute(cls.ELIMINAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e: 
            print(f'Ocurrió un error al eliminar la calificación: {e}')
        finally:
            if cursor is not None: 
                cursor.close() # Liberamos cualquier objeto de conexión para que esté disponible para otro usuario 
            if conexion is not None:
                Conexion.liberar_conexion(conexion)
                
#if __name__=='__main__':
    # Seleccionar clientes
    #calificaciones=CalificacionDAO().seleccionar()
    #for calificacion in calificaciones:
        #print(calificacion)
    # Insertar 
    #calificacion1=Calificacion(Estudiante='Alejandra', Asignatura='Física', Nota=3.9)
    #calificaciones_insertadas=CalificacionDAO.insertar(calificacion1)
    #print(f'Calificaciones insertadas: {calificaciones_insertadas}')
    
    # Actualizar
    #calificacion_actualizar=Calificacion('Mariana Osorio','Matemáticas',4.2) # Tienen que ser los parámetros en el orden de la clase "Calificación"
    #calificaciones_actualizadas=CalificacionDAO.actualizar(calificacion_actualizar)
    #print(f'Calificaciones actualizadas: {calificaciones_actualizadas}')
    
    # Eliminar
    #calificacion_eliminada=Calificacion('Victor Lopera','Historia')
    #calificaciones_eliminadas=CalificacionDAO.eliminar(calificacion_eliminada)
    #print(f'Calificaciones eliminadas: {calificaciones_eliminadas}')
    