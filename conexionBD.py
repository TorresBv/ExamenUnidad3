import mysql.connector

class Registro_Juego():
    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='juego', 
                                            user = 'root',
                                            password ='Mobkun7u7')
    def inserta_juego(self,codigo, nombre, plataforma, precio, estrellas):
        cur = self.conexion.cursor()
        sql='''INSERT INTO game (CODIGO, NOMBRE, PLATAFORMA, PRECIO, ESTRELLAS) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(codigo, nombre, plataforma, precio, estrellas)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
    def buscar_juegos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM game " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_juego(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM game WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombrex = cur.fetchall()
        cur.close()     
        return nombrex

    def elimina_juegos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM game WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        nom = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return nom   
    def actualiza_juegos(self, codigo, nombre, plataforma, precio, estrellas):
        cur = self.conexion.cursor()
        sql ='''UPDATE game SET  CODIGO =' {}' , PLATAFORMA = '{}', PRECIO = '{}', ESTRELLAS = '{}'
        WHERE NOMBRE = '{}' '''.format(codigo,  plataforma, precio, estrellas, nombre)
        cur.execute(sql)
        act = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return act  