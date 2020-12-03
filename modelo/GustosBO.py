import mysql.connector # para instalarlo -> pip3 install mysql-connector 



class GustosBO:

    #*************************************************************************
    #El constructor de la clase Gustos BO crea un objeto de conexion a la base de datos
    #*************************************************************************
    def __init__(self):
        #se crea la conexión con la base de datos
        self.db = mysql.connector.connect(host ="127.0.0.1", 
                                     user = "root", 
                                     password = "root", 
                                     db ="red_social") 

    #*************************************************************************
    #Cuando el objeto es destruido por el interprete realiza la desconexion con la base de datos
    #*************************************************************************
    def __del__(self):
        self.db.close() #al destriurse el objeto cierra la conexion 
  
    #*************************************************************************
    #Metodo que guarda los gustos de una persona en la base de datos
    #*************************************************************************
    def guardar(self, t_gustos):
        try:
            if(self.validar(t_gustos)):#se valida que tenga la información

                if(not self.exist(t_gustos)): #si no existe lo agrega
                    t_gustos.lastUser = "ChGari"
                    
                    insertSQL = "INSERT INTO t_gustos (`idNombreGustos`, `descripcionGustos`, `idUsuario_TGustos`, `nombreGustos`) VALUES (%s, %s, %s, %s)"
                    insertValores =  (t_gustos.idNombreGustos.get(),t_gustos.descripcionGustos.get(),t_gustos.idUsuario_TGustos.get(),t_gustos.nombreGustos.get())
                    #print(insertValores)
                    cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
                    cursor.execute(insertSQL, insertValores) #ejecuta el SQL con las valores
                    self.db.commit() #crea un commit en la base de datos
                else:
                    raise Exception('La cédula indicada en el formulario existe en la base de datos')  # si existe el registro con la misma cedual genera el error
            else:
                raise Exception('Los datos no fueron digitados por favor validar la información')  # si no tiene todos los valores de genera un error
        except mysql.connector.Error as e:
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 
    
    #*************************************************************************
    #Metodo que verifica en la base de datos si la persona existe por cédula
    #*************************************************************************
    def exist(self , t_gustos):
        try:
            existe = False
            selectSQL = "Select * from t_personas where idUsuario = " + t_gustos.idNombreGustos.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            if (cursor.fetchone()) : #Metodo obtiene un solo registro o none si no existe información
                existe  = True

            return existe
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 


    #*************************************************************************
    #Metodo para validar al información que proviene de la vista
    #*************************************************************************
    def validar (self, t_gustos):
        valido = True
        t_gustos.printInfo()
        if t_gustos.idNombreGustos.get() == "" :
            valido = False
        
        if t_gustos.descripcionGustos.get() == "" :
            valido = False

        if t_gustos.idUsuario_TGustos.get() == "" :
            valido = False

        if t_gustos.nombreGustos.get() == "" :
            valido = False

        return valido

    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select idNombreGustos as idNombreGustos, \
                            descripcionGustos, idUsuario_TGustos, nombreGustos, \
                            from t_gustos" 
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            myresult = cursor.fetchall()
            final_result = [list(i) for i in myresult]
            return final_result
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 


    #*************************************************************************
    #Metodo para consultar la información de una persona
    #*************************************************************************
    def consultarGustos(self, t_gustos):
        try:
            selectSQL = "Select * from t_personas where idNombreGusto = " + t_gustos.idNombreGustos.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            gustosDB = cursor.fetchone()
            if (gustosDB) : #Metodo obtiene un solo registro o none si no existe información
                t_gustos.idNombreGustos.set(gustosDB[0]),
                t_gustos.descripcionGustos.set(gustosDB[1])
                t_gustos.idUsuario_TGustos.set(gustosDB[2])
                t_gustos.nombreGusto.set(gustosDB[3])
            else:
                raise Exception("La id Nommbre del Gusto consultada no existe en la base de datos") 
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 

    #*************************************************************************
    #Metodo para eliminar un gusto de la base de datos
    #*************************************************************************
    def eliminar(self, t_gustos):
        try:
            deleteSQL = "delete  from t_gustos where idNombreGustos = " + t_gustos.idNombreGustos.get()
            cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
            cursor.execute(deleteSQL) #ejecuta el SQL con las valores
            self.db.commit() #crea un commit en la base de datos
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 



    #*************************************************************************
    #Metodo que guarda el gusto de una persona en la base de datos
    #*************************************************************************
    def modificar(self, t_gustos):
        try:
            if(self.validar(t_gustos)):#se valida que tenga la información

                if(self.exist(t_gustos)): #si  existe lo modifica
                    t_gustos.lastUser = "ChGari"
                    updateSQL = "UPDATE t_gustos  set `descripcionGustos` = %s, `idUsuario_TGustos` = %s, `nombreGustos` = %s, WHERE `idNombreGustos` =  %s"
                    updateValores =  (t_gustos.descripcionGustos.get(),t_gustos.idUsuario_TGustos.get(), t_gustos.nombreGustos.get(), t_gustos.idNombreGustos.get())
                    #print(insertValores)
                    cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
                    cursor.execute(updateSQL, updateValores) #ejecuta el SQL con las valores
                    self.db.commit() #crea un commit en la base de datos
                else:
                    raise Exception('La cédula indicada en el formulario no existe en la base de datos')  # si existe el registro con la misma cedual genera el error
            else:
                raise Exception('Los datos no fueron digitados por favor validar la información')  # si no tiene todos los valores de genera un error
        except mysql.connector.Error as e:
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 
    