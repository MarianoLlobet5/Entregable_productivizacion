from flask import Flask, render_template, request, redirect, url_for
from Productivizacion_prueba import analizar_texto


app = Flask(__name__)

# Agrega aquí tus funciones de análisis de texto

@app.route('/', methods=['GET', 'POST'])
def mostrar_formulario():
    if request.method == 'POST':
        texto_analizar = request.form['texto']  # Obtén el texto del formulario
        resultado = analizar_texto(texto_analizar)  # Usa tu función para obtener la predicción

        # Redirige al usuario a la página de resultado con la predicción como parámetro
        return redirect(url_for('mostrar_resultado', resultado=resultado))

    return render_template('formulario.html')
@app.route('/resultado/<resultado>')
def mostrar_resultado(resultado):
    return render_template('resultado.html', resultado=resultado)
if __name__ == '__main__':
    app.run(debug=True, port=3500)

