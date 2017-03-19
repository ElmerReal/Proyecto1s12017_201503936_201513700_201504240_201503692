from NodoMatriz import NodoMatriz
from grafos import grafo

class MatrizDispersa():
	def __init__(self):
		self.cabeza=None#Esta cabeza la utilizare para las cabeceras de empresas
		self.cabeza1 = None#Esta cabeza la utilizare para las cabeceras de departamentos



	def insertar(self, valor):#Paso 1 Tiene todo que ver con las empresas (aqui se valida si existe, si va antes o despues); independientemente de lo 
	#									que se haga siempre se devuelve el nodo con el nombre del dominio recibido
		nodo = NodoMatriz()
		nodo.valor=valor
		aux = None#Esta variable me servira para retornar el nodo
		if self.cabeza is None:#No existe ninguna empresa, inserto la empresa en la cabeza, le asigno ese nodo a aux y lo retorno
			self.cabeza = nodo
			aux = self.cabeza
		else:
			temp = self.cabeza
			bandera = 0#Esta variable me indicara si el dominio se agrega al final de las demas empresas
			while (temp is not None):#While utilizado para recorrer de forma horizontal las empresas
				nombresEmpresas=[temp.valor, valor]
				nombresEmpresas.sort()
				if temp.valor == valor:#si la empresa recibida ya existe me limito solo a igualarlo a aux para ser posteriormente retornado
					aux = temp
					bandera = 1
					print("Esta empresa ya existe perro")
					break
				if (nombresEmpresas.index(temp.valor)==1):#Si el nodo en el que estoy es mayor al que recibi significa que deberia
													# insertar el nodo antes de este, por lo tanto lo hago y lo igualo a aux para ser retornado
					if temp == self.cabeza: #Si el nodo mayor es la cabeza se hace una operacion especial
						self.cabeza.anterior = nodo
						self.cabeza.anterior.siguiente = self.cabeza
						self.cabeza = nodo
						aux = self.cabeza
						print("Se cambio la cabeza")
					else: #Si el nodo mayor es cualquier otro diferente a la cabeza se hace lo siguiente
						temp.anterior.siguiente = nodo
						temp.anterior.siguiente.anterior = temp.anterior
						nodo.siguiente = temp
						temp.anterior = nodo
						aux = temp.anterior
						print("Se cambio nodo diferente a cabeza")
					bandera = 1
					break
				temp = temp.siguiente
			if bandera == 1 :#Bandera es igual a 1, significa que ya se creo el nodo, por lo tanto no se hace mas
				print("")
			else:# de lo contrario se agrega el dominio al final y se iguala a aux
				temp = self.cabeza
				while temp.siguiente is not None:
					temp = temp.siguiente
				temp.siguiente = nodo
				temp.siguiente.anterior = temp
				temp = temp.siguiente
				aux = temp
				print("Se ingreso al final")
		return aux

	def vis(self):
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				print(temp.valor)
				temp = temp.siguiente
	def vis1(self):
		temp = self.cabeza1
		if(temp!=None):
			while(temp!=None):
				print(temp.valor)
				temp = temp.abajo

	def insertar1(self, valor):#Paso2 Tiene todo que ver con los departamentos (aqui se valida si existe, si va arriba o abajo); independientemente de lo 
	#									que se haga siempre se devuelve el nodo con el nombre del departamento recibido
		nodo = NodoMatriz()
		nodo.valor=valor
		aux = None#Esta variable me servira para retornar el nodo
		if self.cabeza1 is None:#Si no existe ningun departamento lo agrego a la cabeza
			self.cabeza1 = nodo
			aux = self.cabeza1
		else:
			temp = self.cabeza1
			bandera = 0#Me servira para saber si debo de ingresar el nodo al final
			while temp is not None:#utilizo este while para recorrer todos los nodos y validar algunos casos
				nombresDepartamentos=[temp.valor, valor]
				nombresDepartamentos.sort()
				if temp.valor == valor:#Si ya existe un nodo con el departamento recibido solo igualo el nodo a aux
					aux = temp
					bandera=1
					print("Este departamento ya existe perro")
					break
				if (nombresDepartamentos.index(temp.valor)==1):#Si existe algun nodo con inicial mayor al departamento recibido significa que el departamento recibido
													#deberia ir arriba
					if temp == self.cabeza1:#Si el departamento mayor es la cabeza se hace una operacion especial
						self.cabeza1.arriba = nodo
						self.cabeza1.arriba.abajo = self.cabeza1
						self.cabeza1 = nodo
						aux = self.cabeza1
						print("Se inserto en la cabeza")
					else:#de lo contrario se juega con los apuntadores para insertar el nodo enmedio
						temp.arriba.abajo=nodo
						temp.arriba.abajo.arriba= temp.arriba
						nodo.abajo = temp
						temp.arriba = nodo
						aux = temp.arriba
						print("Se inserto en cualquier otro lado")
					bandera =1
					break
				temp  = temp.abajo
			if bandera ==1:#Si entro en algunos casos ya no se hace nada
				print("")
			else:# de lo contrario se agrega al final y se asigna a aux para ser retornado
				temp = self.cabeza1
				while temp.abajo is not None:
					temp = temp.abajo
				temp.abajo = nodo
				temp.abajo.arriba= temp
				temp = temp.abajo
				aux = temp
				print("Se inserto al final")
		return aux

	def obtenerNodoPrevioDominio(self, x,valor,letra):#Este metodo recibe el nodo dominio, el nombre del correo, y la inicial del nombre
		#Utilizo este metodo para bajar desde el dominio y verificar donde ingresar el nodo con el nombre del correo
		temp = NodoMatriz()#Este nodo me servira para bajar partiendo desde el nodo dominio recibido
		temp = x.abajo
		nodo = NodoMatriz()#Este nodo contendra todos los valores del correo
		nodo.valor=valor
		nodo.dominio = x.valor
		nodo.letra = letra
		aux = None#este nodo me servira para devolver el nodo de valores cuando se haya ingresado (o sea que ya tenga sus apuntadores verticales)
		bandera = 0
		if temp is None:#Si el nodo abajo del dominio es none se agrega y se iguala a aux
			x.abajo = nodo
			x.abajo.arriba = x
			aux = x.abajo
		else:
			while temp is not None:#uso este while para recorrer los correos que existen con el dominio recibido
				if temp.letra == letra:#Si existe un nodo con la letra de mi nodo valor quiere decir que debo de enviarlo a atras
					if temp.atras is None:
						nodo.adelante = temp
						nodo.adelante.atras = nodo
						temp = temp.atras
					else:
						while temp.atras is not None:
							temp = temp.atras
						temp.atras = nodo
						temp.atras.adelante = temp
					bandera = 1
					break#--------------------------
				if ord(temp.letra[0])>ord(letra[0]):#Averiguo si deberia meter mi nodo valores antes de cualquier otro
					if temp == x:
						x.abajo = nodo
						x.abajo.arriba = x
						aux = x.abajo
					else:
						temp.arriba.abajo = nodo
						temp.arriba.abajo.arriba =temp.arriba
						nodo.abajo = temp
						temp.arriba = nodo
						aux = temp.arriba
					bandera = 1
					break
				temp = temp.abajo
			if bandera == 1:
				print("")
			else: #Si no entre a ningun caso entonces lo agrego al final de todos los correos del dominio recibido
				temp = x
				while temp.abajo is not None:
					temp = temp.abajo
				temp.abajo = nodo
				temp.abajo.arriba = temp
				temp = temp.abajo
				aux = temp
		return aux

	def unir(self,NodoLetra, NodoValores):#Este metodo lo utilizo para setear los apuntadores horizontales de mi nodo valores
	#									  por eso recibo como valores mi nodo letra y mi nodo valores(el cual ya tiene sus apuntadores verticales)
		if NodoValores != None:#Esta validacion la hago porque cuando agrego nodos atras de cualquier otro ya no retorno ese nodo porque ya tiene apuntadores
			bandera = 0
			print(NodoLetra)
			if NodoLetra.siguiente is None:#Si no existe ningun nodo siguiente al encabezado de la letra lo agrego ahi
				NodoValores.anterior = NodoLetra
				NodoValores.anterior.siguiente = NodoValores
			else:#Si ya existe algun nodo, entonces debo de recorre hacia la derecha para ver si el dominio de mi nodo valores va antes que otro 
			# nodo de valores porque su dominio es menor o si mi nodo valores va hasta de ultimo 
				temp = NodoLetra.siguiente
				#//--print("----------", temp.dominio, NodoValores.dominio,ord((temp.dominio)[0]), ord((NodoValores.dominio)[0]))
				while  temp is not None:#Para recorrer los nodos valores apuntados por el nodo letras
					if ord((temp.dominio)[0])> ord((NodoValores.dominio)[0]):#si algun dominio es mayor al de mi nodo valores lo agrego antes
						temp.anterior.siguiente= NodoValores
						temp.anterior.siguiente.anterior= temp.anterior
						NodoValores.siguiente = temp
						temp.anterior = NodoValores
						bandera =1
						break
					temp = temp.abajo
				if bandera != 1:#Si ningun dominio era mayor entonces lo agrego al final de todos los nodos valores apuntados por ese nodo letra
					temp = NodoLetra.siguiente
					while temp.siguiente is not None:
						temp = temp.siguiente
					temp.siguiente = NodoValores
					temp.siguiente.anterior = temp

	def visualizar1(self, aux):#Este metodo recibe un nodo dominio e imprime todos los hijos de es dominio
		print("---------------Visualizando horizontalmente-----")
		text = ""
		temp = aux.abajo
		while temp is not None:
			text += temp.anterior.valor+" | "+temp.valor+"\n"
			print(temp.anterior.valor," | ",temp.valor)
			if temp.atras != None:
				a=temp.atras
				while a != None:
					text += "---->"+a.valor+"\n"
					print("---->"+a.valor+"\n")
					a = a.atras
			temp = temp.abajo
		return text	

	#def eliminar(self, letra, dominio,valor):
		temp = self.cabeza#Este es el nodo encabezado dominio
		temp1 = self.cabeza1#Este es el nodo encabezado letra
		casoEncabezadoDominio = 0
		casoEncabezadoLetra = 0
		if temp!= None and temp1 != None:
			while temp.valor != dominio:
				temp = temp.siguiente
			if temp==self.cabeza:
				casoEncabezadoDominio =1#La letra esta en la cabeza
			elif temp.siguiente ==None:
				casoEncabezadoDominio = 2#La letra es la ultima
			else:
				casoEncabezadoDominio=3#La letra esta en medio
		#---------------------------------------------------------		
			while temp1.valor != letra:
				temp1 = temp1.abajo
			if temp1==self.cabeza1:
				casoEncabezadoLetra =1#La letra esta en la cabeza
			elif temp1.abajo ==None:
				casoEncabezadoLetra = 2#La letra es la ultima
			else:
				casoEncabezadoLetra=3#La letra esta en medio
		#---------------------------------------------------------
			aux = temp.abajo#aux es el nodo 'cabeza' con ese dominio y esa letra
			while aux.letra!=letra:
				aux = aux.abajo
			casoNodoValor = 0
			aux1 = aux
			if aux1.atras == None:
				casoNodoValor=1#Es el unico valor con esa letra y ese dominio 
			else:
				while aux1.valor!=valor:
					aux1 = aux1.atras
				if aux1.atras == None:
					casoNodoValor = 3#Es el ultimo
					aux1.adelante.atras = None
				else:
					casoNodoValor = 2#Hay uno antes y uno despues
					aux1.atras.siguiente = aux1.siguiente
					aux1.siguiente.atras = aux1.atras
		#----------------------------------------------------------------
			if casoNodoValor == 1:#Hay que eliminar el nodo
				if aux.abajo != None:
					aux.arriba.abajo = aux.abajo
					aux.abajo.arriba = aux.arriba.abajo	
				else:
					aux.arriba.abajo = None
				#***********************************************
				if temp.abajo==None:
					if casoEncabezadoDominio ==1:
						if temp.siguiente != None:
							self.cabeza = self.cabeza.siguiente
						else:
							self.cabeza = None
					elif casoEncabezadoDominio ==2:
						temp.anterior.siguiente = None
					else:
						temp.anterior.siguiente=temp.siguiente
						temp.siguiente.anterior = temp.anterior
				#***********************************************
				if aux.siguiente != None:
					aux.anterior.siguiente = aux.siguiente
					aux.siguiente.anterior = aux.anterior
				else:
					aux.anterior.siguiente = None
				#***********************************************
				if temp1.siguiente==None:
					if casoEncabezadoLetra ==1:
						if temp1.abajo != None:
							self.cabeza1 = self.cabeza1.abajo
						else:
							self.cabeza1 = None
					elif casoEncabezadoDominio ==2:
						temp1.arriba.abajo = None
					else:
						temp1.arriba.abajo=temp1.abajo
						temp1.arriba.abajo.arriba = temp1.arriba

	def graficarMatriz(self):
		gra = grafo('Matriz')
		gra.declararNodos("A", " ")
		tempDepto = self.cabeza1
		contador = 0
		while tempDepto != None:
			tempDepto.indice = contador
			gra.declararNodos(tempDepto.indice, tempDepto.valor)
			contador += 1
			tempDepto = tempDepto.abajo
		tempDepto =self.cabeza1
		gra.declararTrancisiones("A",tempDepto.indice)
		while tempDepto != None:
			if(tempDepto.abajo!=None):
				gra.declararTrancisiones(tempDepto.indice,tempDepto.abajo.indice)
			tempDepto = tempDepto.abajo
		tempEmpresas = self.cabeza
		while tempEmpresas != None:
			tempEmpresas.indice = contador
			gra.declararNodos(tempEmpresas.indice, tempEmpresas.valor)
			contador += 1
			tempEmpresas = tempEmpresas.siguiente
		tempEmpresas = self.cabeza
		gra.declararTrancisiones("A",tempEmpresas.indice)
		while tempEmpresas != None:
			if(tempEmpresas.siguiente!=None):
				gra.declararTrancisiones(tempEmpresas.indice,tempEmpresas.siguiente.indice)
			tempEmpresas = tempEmpresas.siguiente
		gra.terminarGrafo('Matriz')
	def eliminar1(self,letra,dominio,valor):
		texto =""
		tempDominio = self.cabeza
		tempLetra = self.cabeza1
		bandera = 0
		while tempDominio.valor != dominio:
			tempDominio = tempDominio.siguiente

		while tempLetra.valor != letra:
			tempLetra = tempLetra.abajo
		t = tempDominio.abajo
		tValor = None
		while t !=None:
			if t.valor == valor:
				if t.atras == None:
					tValor = t
					break
				else:
					t.atras.arriba = t.arriba
					t.atras.arriba.abajo = t.atras
					if t.abajo != None:
						t.atras.abajo = t.abajo
						t.abajo.arriba = t.atras
					else:
						t.atras.abajo =None
						t.atras.arriba = t.arriba
					
				bandera = 2
				break
			if t.atras != None:
				t1 = t.atras
				while t1 != None:
					if t1.valor == valor:
						tValor = t1
						bandera=1
						break
					t1 = t1.atras
			t = t.abajo
		if tValor ==None:
			texto ="No existe el correo ingresado"
		else:
			if bandera == 0:
				if tValor.siguiente != None:
					tValor.anterior.siguiente = tValor.siguiente
					tValor.siguiente.anterior = tValor.anterior
				else:
					tValor.anterior.siguiente = None

				if tValor.abajo != None:
					tValor.arriba.abajo = tValor.abajo
					tValor.abajo.arriba = tValor.arriba
				else:
					tValor.arriba.abajo = None
			elif bandera == 2:
				print("Ya estuvo")
			else:
				if tValor.atras !=None:
					tValor.adelante.atras = tValor.atras
					tValor.atras.adelante =tValor.adelante
				else:
					tValor.adelante.atras = None
			texto="Eliminacion exitosa"
		return texto


	def buscarPorLetra(self,letra):
		texto = ""
		aux = self.cabeza1
		while(aux.valor != letra):
			aux = aux.abajo
		contador = 0
		gra = grafo('Lista Correos por Letra')
		aux.indice = 0
		gra.declararNodos(aux.indice,aux.valor)
		t = aux
		aux = aux.siguiente
		
		
		if aux == None:
			gra.declararNodos('0', 'Lista Vacia')
			texto = "No hay correos con esa letra"
		else:
			
			contador+=1
			while aux != None:
				texto+=aux.valor+"\n"
				aux.indice = contador
				gra.declararNodos(aux.indice,aux.valor)
				if aux.atras != None:
					t1 = aux.atras
					while t1 != None:
						contador+=1
						texto+="->"+t1.valor+"\n"
						t1.indice = contador
						gra.declararNodos(t1.indice,t1.valor)
						t1 = t1.atras
				contador+=1
				aux = aux.siguiente
			while t !=None:
				if t.siguiente!= None:
					gra.declararTrancisiones(t.indice,t.siguiente.indice)
				if t.atras != None:
					t1 = t
					while t1.atras != None:
						gra.declararTrancisiones(t1.indice,t1.atras.indice)
						t1 = t1.atras
						if t1.atras == None:
							gra.declararTrancisiones(t1.indice,t.indice)
				t = t.siguiente
		gra.terminarGrafo('Lista correos por Letra')
		return texto

	def buscarPorDominio(self,dominio):
		texto = ""
		aux = self.cabeza
		while(aux.valor != dominio):
			aux = aux.siguiente
		contador = 0
		gra = grafo('Lista Correos por Letra')
		aux.indice = 0
		gra.declararNodos(aux.indice,aux.valor)
		t = aux
		aux = aux.abajo
		
		
		if aux == None:
			gra.declararNodos('0', 'Lista Vacia')
			texto = "No hay correos con este dominio"
		else:
			contador+=1
			while aux != None:
				texto+=aux.valor+"\n"
				aux.indice = contador
				gra.declararNodos(aux.indice,aux.valor)
				if aux.atras != None:
					t1 = aux.atras
					while t1 != None:
						contador+=1
						texto+="->"+t1.valor+"\n"
						t1.indice = contador
						gra.declararNodos(t1.indice,t1.valor)
						t1 = t1.atras
				contador+=1
				aux = aux.abajo	
			while t !=None:
				if t.abajo!= None:
					gra.declararTrancisiones(t.indice,t.abajo.indice)
				if t.atras != None:
					t1 = t
					while t1.atras != None:
						gra.declararTrancisiones(t1.indice,t1.atras.indice)
						t1 = t1.atras
						if t1.atras == None:
							gra.declararTrancisiones(t1.indice,t.indice)
				t = t.abajo
		gra.terminarGrafo('Lista correos por Dominio')
		return texto

	def verLista(self):
		temp = self.cabeza
		while temp!=None:
			print("-------------------Comenzamos------------------")
			self.visualizar1(temp)
			temp = temp.siguiente