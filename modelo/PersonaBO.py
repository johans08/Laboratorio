import mysql.connector # para instalarlo -> pip3 install mysql-connector 



class PersonaBO:

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
    def guardar(self, t_personas):
        try:
            if(self.validar(t_personas)):#se valida que tenga la información

                if(not self.exist(t_personas)): #si no existe lo agrega
                    t_personas.lastUser = "ChGari"
                    
                    insertSQL = "INSERT INTO Personas (id_Usuario`, `nombreUsuario`, `contraseña`, `correo`, `nombrePersona`, `apellidoPersona`, `fechaNacimiento`, `estado`, `descripcionPersona`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    insertValores =  (t_personas.idUsuario.get(),t_personas.nombreUsuario.get(),t_personas.contraseña.get(), t_personas.correo.get(), t_personas.nombrePersona.get(), t_personas.apellidoPersona.get(), t_personas.fechaNacimiento.get(), t_personas.estado(), t_personas.descripcionPersona())
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
    def exist(self , t_personas):
        try:
            existe = False
            selectSQL = "Select * from t_personas where idUsuario = " + t_personas.idUsuario.get()
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
    def validar (self, t_personas):
        valido = True
        t_personas.printInfo()
        if t_personas.idUsuario.get() == "" :
            valido = False
        
        if t_personas.nombreUsuario.get() == "" :
            valido = False

        if t_personas.contraseña.get() == "" :
            valido = False

        if t_personas.correo.get() == "" :
            valido = False

        if t_personas.nombrePersona.get() == "" :
            valido = False

        if t_personas.apellidoPersona.get() == "" :
            valido = False

        if t_personas.fechaNacimiento.get() == "" :
            valido = False
        
        if t_personas.estado.get() == "" :
            valido = False
        
        if t_personas.descripcionPersona.get() == "" :
            valido = False

        return valido

    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select idUsuario as idUsuario, \
                            nombreUsuario, contraseña, correo, \
                            nombrePersona, apellidoPersona, fechaNacimiento, estado, descripcionPersona \
                            from t_personas" 
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
    def consultarPersona(self, t_personas):
        try:
            selectSQL = "Select * from t_personas where idUsuario = " + t_personas.idUsuario.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            personaDB = cursor.fetchone()
            if (personaDB) : #Metodo obtiene un solo registro o none si no existe información
                t_personas.idUsuario.set(personaDB[0]),
                t_personas.nombreUsuario.set(personaDB[1])
                t_personas.contraseña.set(personaDB[2])
                t_personas.correo.set(personaDB[3])
                t_personas.nombrePersona.set(personaDB[4])
                t_personas.apellidoPersona.set(personaDB[5])
                t_personas.fechaNacimiento.set(personaDB[6])
                t_personas.estado.set(personaDB[7])
                t_personas.descripcionPersona.set(personaDB[8])
            else:
                raise Exception("La cédula consultada no existe en la base de datos") 
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 

    #*************************************************************************
    #Metodo para eliminar a una persona de la base de datos
    #*************************************************************************
    def eliminar(self, t_personas):
        try:
            deleteSQL = "delete  from t_personas where idUsuario = " + t_personas.idUsuario.get()
            cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
            cursor.execute(deleteSQL) #ejecuta el SQL con las valores
            self.db.commit() #crea un commit en la base de datos
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 



    #*************************************************************************
    #Metodo que guarda una persona en la base de datos
    #*************************************************************************
    def modificar(self, t_personas):
        try:
            if(self.validar(t_personas)):#se valida que tenga la información

                if(self.exist(t_personas)): #si  existe lo modifica
                    t_personas.lastUser = "ChGari"
                    updateSQL = "UPDATE Personas  set `nombreUsuario` = %s, `contraseña` = %s, `correo` = %s, `nombrePersona` = %s, `apellidoPersona` = %s, `fechaNacimiento` = %s, `estado` = %s, `descripcionPersona` = %s WHERE `idUsuario` =  %s"
                    updateValores =  (t_personas.nombreUsuario.get(),t_personas.contraseña.get(), t_personas.correo.get(), t_personas.nombrePersona.get(), t_personas.apellidoPersona.get(), t_personas.fechaNacimiento.get(), t_personas.estado(), t_personas.descripcionPersona(), t_personas.idUsuario.get())
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