import mysql.connector # para instalarlo -> pip3 install mysql-connector 



class AmigosBO:

    #*************************************************************************
    #El constructor de la clase persona BO crea un objeto de conexion a la base de datos
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
    #Metodo que guarda una persona en la base de datos
    #*************************************************************************
    def guardar(self, t_amigos):
        try:
            if(self.validar(t_amigos)):#se valida que tenga la información

                if(not self.exist(t_amigos)): #si no existe lo agrega
                    t_amigos.lastUser = "ChGari"
                    
                    insertSQL = "INSERT INTO Amigos (nivelAmistad`, `idUsuario`, `idAmigo`) VALUES (%s, %s, %s)"
                    insertValores =  (t_amigos.nivelAmistad.get(),t_amigos.idUsuario.get(),t_amigos.idAmigo.get())
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
    def exist(self , t_amigos):
        try:
            existe = False
            selectSQL = "Select * from Personas where PK_cedula = " + t_amigos.idUsuario.get()
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
    def validar (self, t_amigos):
        valido = True
        t_amigos.printInfo()
        if t_amigos.nivelAmistad.get() == "" :
            valido = False
        
        if t_amigos.idUsuario.get() == "" :
            valido = False

        if t_amigos.idAmigo.get() == "" :
            valido = False

        return valido

    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select nivelAmigos as nivelAmigos, \
                            idUsuario, idAmigo, \
                            from amigos" 
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
    #Metodo para consultar la información de una amistad
    #*************************************************************************
    def consultarAmigos(self, t_amigos):
        try:
            selectSQL = "Select * from Personas where PK_cedula = " + t_amigos.idUsuario.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            amigosDB = cursor.fetchone()
            if (amigosDB) : #Metodo obtiene un solo registro o none si no existe información
                t_amigos.nivelAmistad.set(amigosDB[0]),
                t_amigos.idUsuario.set(amigosDB[1])
                t_amigos.idAmigo.set(amigosDB[2])
            else:
                raise Exception("La cédula consultada no existe en la base de datos") 
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 

    #*************************************************************************
    #Metodo para eliminar una amistad de la base de datos
    #*************************************************************************
    def eliminar(self, t_amigos):
        try:
            deleteSQL = "delete  from Personas where idUsuario = " + t_amigos.idUsuario.get()
            cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
            cursor.execute(deleteSQL) #ejecuta el SQL con las valores
            self.db.commit() #crea un commit en la base de datos
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 



    #*************************************************************************
    #Metodo que guarda una amistad en la base de datos
    #*************************************************************************
    def modificar(self, t_amigos):
        try:
            if(self.validar(t_amigos)):#se valida que tenga la información

                if(self.exist(t_amigos)): #si  existe lo modifica
                    t_amigos.lastUser = "ChGari"
                    updateSQL = "UPDATE Personas  set `idUsuario` = %s, `idAmistad` = %s WHERE `nivelAmistad` =  %s"
                    updateValores =  (t_amigos.idUsuario.get(), t_amigos.idAmigo.get(), t_amigos.nivelAmistad.get())
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
    