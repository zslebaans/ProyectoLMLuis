from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta para mostrar el cuestionario
@app.route('/')
def questionnaire():
    return render_template('questionnaire.html')

# Ruta para procesar el cuestionario
@app.route('/submit-questionnaire', methods=['POST'])
def submit_questionnaire():
    # Recopilar datos enviados por el formulario
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    preferences = request.form.get('preferences')
    comments = request.form.get('comments')

    # Aquí puedes guardar los datos en una base de datos o procesarlos como necesites.
    print("Nombre:", name)
    print("Correo:", email)
    print("Edad:", age)
    print("Preferencias:", preferences)
    print("Comentarios:", comments)

    # Redirigir al usuario a una página de agradecimiento (puedes personalizarla)
    return redirect(url_for('thank_you'))

# Ruta de agradecimiento
@app.route('/thank-you')
def thank_you():
    return "<h1>Gracias por enviar el formulario. ¡Nos pondremos en contacto contigo pronto!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
