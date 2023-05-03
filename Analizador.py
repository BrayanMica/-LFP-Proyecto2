
import os


# ruta_absoluta = os.getcwd()
# archivo = open(str(ruta_absoluta)+'/entrada.txt', 'r')
# lineas = ''
# print(archivo)
# for i in archivo.readlines():
#     lineas += i

#print(lineas)


class Analizador:
    def __init__(self, entrada:str):
        self.lineas = entrada #ENTRADA DEL ARCHIVO CARGADO EN MEMORIA
        self.index = 0 #POSICION DE CARACTERES EN LA ENTRADA
        self.fila = 1 #FILA ACTUAL
        self.columna = 1 #COLUMNA ACTUAL
        self.ListaTokens = [] # Lista para Guardar Tokens
        self.ListaErrores = [] # LISTA PARA GUARDAR ERRORES
        
        self.E7oE8 = "" # Seleccion de los estados 7 y 8
        

    def get_ListaTokens(self):
        return self.ListaTokens
    
    def set_ListaTokens(self,token):
        self.ListaTokens.append(token)
        
    def Limpiar_ListaTokens(self):
        self.ListaTokens.clear()
        
    def _token(self, token:str, estado_actual:str, estado_sig:str):
        if self.lineas[self.index] != " ":
            text = self._juntar(self.index, len(token))
            if self._analizar(token, text):
                self.index += len(token) - 1
                self.columna += len(token) - 1
                return estado_sig
            else:
                #GUARDARIA ERROR LEXICO
                return 'ERROR'
        else:
            return estado_actual
        
    def _juntar(self,_index:int, _count:int):
        try:
            tmp = ''
            for i in range(_index, _index + _count):
                tmp += self.lineas[i]
            self.E7oE8 = tmp
            return tmp
        except:
            return None
        
    def _analizar(self, token, texto):
        try:
            count = 0
            tokem_tmp = ""
            for i in texto:
                #CUANDO LA LETRA HAGA MATCH CON EL TOKEN ENTRA
                if str(i) == str(token[count]):
                    tokem_tmp += i  
                    count += 1 
                else:
                    #print('ERROR1')
                    return False
            
            if tokem_tmp == '/*' or tokem_tmp == '---':
                pass
            else:
                self.set_ListaTokens(tokem_tmp)
                print(f'++++++ ENCONTRE - {tokem_tmp} ++++++++')
            return True
        except:
            #print('ERROR2')
            return False
        
    def _analizarCadena(self):
        estado_aux = ""
        tmp = self.index
        cadena = ""
        while self.lineas[tmp] != "":
            
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[tmp] == '\n':
                return 'ERROR'
            elif self.lineas[tmp] == ' ' and estado_aux == '': 
                #print("INICIO")
                estado_aux = "INICIO"
            elif self.lineas[tmp] == ' ' and estado_aux == 'INICIO':
                #print("fin")
                return [cadena, tmp]
            elif estado_aux == 'INICIO':
                cadena += self.lineas[tmp]
                #print(self.lineas[1])
                #print(f'CADENA - {self.lineas[tmp] } ')

            
    
            #INCREMENTAR POSICION
            if tmp < len(self.lineas) - 1:
                tmp +=1
            else:
                break
               
    def _analizarIdentificador(self):
        estado_aux = ""
        tmp = self.index
        cadena = ""
        while self.lineas[tmp] != "":
            
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[tmp] == '\n':
                return 'ERROR'
            elif self.lineas[tmp] == '"' and estado_aux == '': 
                #print("INICIO")
                estado_aux = "INICIO"
            elif self.lineas[tmp] == '"' and estado_aux == 'INICIO':
                #print("fin")
                return [cadena, tmp]
            elif estado_aux == 'INICIO':
                cadena += self.lineas[tmp]
                #print(self.lineas[1])
                #print(f'CADENA - {self.lineas[tmp] } ')

            #INCREMENTAR POSICION
            if tmp < len(self.lineas) - 1:
                tmp +=1
            else:  
                break 
    
    def _compile(self):
        estado_actual = 'S0'
        while self.lineas[self.index] != "":
            #print(f'CARACTER - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 1

            # ************************
            #         ESTADOS
            # ************************

            # S0 -> Funcion S1
            elif estado_actual == 'S0':
                _com = self._token('---', 'S0', 'COMENTARIO')
                _comC = self._token("/*",'S0', 'COMENTARIO')
                if _com == 'COMENTARIO':
                    self._comentarioSimple()
                    estado_actual == 'S0'
                    print("######### ComentarioSimple #########")
                elif _comC == 'COMENTARIO':
                    self._comentariosDeBloque()
                    estado_actual == 'S0'
                    print("######### ComentarioDeBloque #########")
                else:
                    funciones = ['CrearBD','EliminarBD','CrearColeccion','EliminarColeccion','InsertarUnico','ActualizarUnico','EliminarUnico','BuscarTodo','BuscarUnico']
                    for i in funciones:
                        estado_actual = self._token(i, 'S0', 'S1')
                        if estado_actual != 'ERROR':
                            break

            # S1 -> ID S2
            elif estado_actual == 'S1':
                result = self._analizarCadena()
                #print(result)
                valor_cadena = result[0]
                self.set_ListaTokens(valor_cadena)
                print(valor_cadena)
                self.index = result[1]
                estado_actual = 'S2'
                
            # S2 -> = S3
            elif estado_actual == 'S2':
                
                funciones = ['=']
                for i in funciones:
                    estado_actual = self._token(i, 'S2', 'S3')
                    if estado_actual != 'ERROR':
                        break
            
            # S3 -> nueva S4
            elif estado_actual == 'S3':
                funciones = ['nueva']
                for i in funciones:
                    estado_actual = self._token(i, 'S3', 'S4')
                    if estado_actual != 'ERROR':
                        break
                    
            # S4 -> nueva S5
            elif estado_actual == 'S4':
                funciones = ['CrearBD','EliminarBD','CrearColeccion','EliminarColeccion','InsertarUnico','ActualizarUnico','EliminarUnico','BuscarTodo','BuscarUnico']
                for i in funciones:
                    estado_actual = self._token(i, 'S4', 'S5')
                    if estado_actual != 'ERROR':
                        break
            
            # S5 -> nueva S6
            elif estado_actual == 'S5':
                funciones = ['(']
                for i in funciones:
                    estado_actual = self._token(i, 'S5', 'S6')
                    if estado_actual != 'ERROR':
                        break
            
            # S6 -> atributo S7 | ) S8
            elif estado_actual == 'S6':
                aux_siguiente = 'S7oS8'
                funciones = ['"',')']
                for i in funciones:
                    estado_actual = self._token(i, 'S6', aux_siguiente)
                    
                    if self.lineas[self.index] == i:
                        result = self._analizarIdentificador()
                        #print(result)
                        valor_cadena = result[0]
                        self.set_ListaTokens(valor_cadena)
                        print(valor_cadena)
                        self.index = result[1]
                        estado_actual = self._token('"', 'S6', 'S7')
                    else:
                        estado_actual = self._token(')', 'S6', 'S8')
                        
                    if estado_actual != 'ERROR':
                        break
                        
            # S7 -> nueva S8
            elif estado_actual == 'S7':
                funciones = [')']
                for i in funciones:
                    estado_actual = self._token(i, 'S7', 'S8')
                    if estado_actual != 'ERROR':
                        break
            
            # S8 -> nueva S0
            elif estado_actual == 'S8':
                funciones = [';']
                for i in funciones:
                    estado_actual = self._token(i, 'S8', 'S0')
                    estado_actual = 'S0'
                    if estado_actual != 'ERROR':
                        break

            # ************************
            # ************************

            
            # ERRORES 
            if estado_actual == 'ERROR':
                #print('\t AQUI OCURRIO UN ERROR')
                estado_actual = 'S0'
            
            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break

    def _comentarioSimple(self):
        estado_actual = 'S0'
        while self.lineas[self.index] != "":
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                return
            
            # ERRORES 
            if estado_actual == 'ERROR':
                return
            elif self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break
    
    def _comentariosDeBloque(self):
        estado_actual = 'S0'
        while self.lineas[self.index] != "":
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '*' and self.lineas[self.index+1] == '/':
                return
            
            # ERRORES 
            if estado_actual == 'ERROR':
                return
            
            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break

    def guardarErrores(self, token, fila, columna):
        self.ListaErrores.append({"token":token, "fila": fila, "columna":columna})

        

    