from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_secreta_academica_2026"

usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "pedro": "2026"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

        if usuario in usuarios and usuarios[usuario] == password:
            return redirect(url_for('index'))
        else:
            flash("Usuario o contraseña incorrectos.", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
