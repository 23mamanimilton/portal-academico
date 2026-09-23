from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response

app = Flask(__name__)
app.secret_key = "clave_secreta_academica_2026"

usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "pedro": "2026"
}

cursos_lista = [
    {"nombre": "Programación Web", "docente": "Luis Pérez", "cupos": 15},
    {"nombre": "Bases de Datos", "docente": "Ana López", "cupos": 8},
    {"nombre": "Inteligencia Artificial", "docente": "Carlos Rojas", "cupos": 0}
]

@app.route('/')
def index():
    usuario_cookie = request.cookies.get('usuario_preferido')
    return render_template('index.html', usuario_cookie=usuario_cookie)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

        if usuario in usuarios and usuarios[usuario] == password:
            session['usuario'] = usuario
            flash(f"¡Bienvenido, {usuario}!", "success")
            
            # Guardar cookie usuario_preferido y redirigir a /cursos
            response = make_response(redirect(url_for('cursos')))
            response.set_cookie('usuario_preferido', usuario, max_age=60*60*24*7)
            return response
        else:
            flash("Usuario o contraseña incorrectos.", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html', cursos=cursos_lista)

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

@app.route('/eliminar_cookie')
def eliminar_cookie():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('usuario_preferido')
    flash("Cookie eliminada correctamente.", "info")
    return response

if __name__ == '__main__':
    app.run(debug=True)
