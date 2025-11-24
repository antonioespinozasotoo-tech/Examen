from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        else:
            descuento = total_sin_descuento * 0.25

        total = total_sin_descuento - descuento

        return render_template(
            'Ejercicio1.html',
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total=total
        )

    return render_template('Ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""

    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario == "juan" and password == "admin":
            mensaje = "Bienvenido Administrador juan"
        elif usuario == "pepe" and password == "user":
            mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('Ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
