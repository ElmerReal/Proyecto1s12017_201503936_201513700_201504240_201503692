from MatrizDispersa import MatrizDispersa
from flask import Flask, request, Response,render_template
app = Flask(__name__)

class principal():
    global lista
    global matriz
    matriz = MatrizDispersa()

    @app.route('/') 
    def metodo1():
        return "WEB SERVICE PROYECTO 1 FUNCIONANDO,Hola Memo"

    @app.route('/tarea2',methods=['GET'])
    def formulario():
        return render_template('index.html')

    @app.route('/tarea2',methods=['POST'])
    def metodo9():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])
        encabezadoEmpresa = matriz.insertar(parametro1)#Envio mi empresa y recibo un nodo empresa
        matriz.vis()
        print("*******************************************************")
        encabezadoDepartamento = matriz.insertar1(parametro2)#Envio mi depto y recibo el nodo depto
        matriz.vis1()
        matriz.graficarMatriz()
        texto = "<h1>Empresa: "+parametro1+"<h1>"
        texto += "<h1>Departamento: "+parametro2+"<h1>"
        texto += "\t Operacion realizada\n Carne: 201503936"
        return texto

    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')