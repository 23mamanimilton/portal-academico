from flask import Flask, render_template, request, redirect, url_for, session, flash

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
            session['usuario'] = usuario
            flash(f"¡Bienvenido, {usuario}!", "success")
            return redirect(url_for('cursos'))
        else:
            flash("Usuario o contraseña incorrectos.", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/perfil')
def perfil():
    if 'usuario' not in session:
        flash("Acceso restringido. Por favor inicia sesión.", "error")
        return redirect(url_for('login'))
    return render_template('perfil.html', usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash("La sesión fue cerrada correctamente.", "info")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
