from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE='calificaciones_db'
    USERNAME='root'
    PASSWORD='admin'
    DB_PORT='3306'
    HOST='localhost'
    POOL_SIZE=8  # Depende del númeor de usuarios, pero en este caso se pone un valor al azar (No se recomienda que sea un valor alto)
    POOL_NAME='calificaciones_pool'
    pool=None
    
    
    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool=pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                
                return cls.pool
            except Error as e:
                print(f'Ocurrió un error al obtener pool: {e}')
        else:
            return cls.pool
        
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    
    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()
        
        
# Prueba
#if __name__=='__main__':
    # Creación del objeto pool
    #pool=Conexion.obtener_pool()
    #print(pool)
    # Obtener un objeto conexion
    #cnx1= Conexion.obtener_conexion()
    #print(cnx1)
    #Conexion.liberar_conexion(cnx1)
    