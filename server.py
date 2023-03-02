from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
visitas = 0

@app.route('/')
def contador_visitas():
    global visitas
    visitas += 1
    session['visitas'] = visitas
    return render_template("index.html", visitas=visitas)

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    global visitas
    visitas = 0
    session.clear()
    session['visitas']= 1
    return redirect(url_for('contador_visitas'))

@app.route('/add_visits', methods=['POST'])
def add_visits():
    global visitas
    visitas += 1
    session['visitas'] = visitas
    return redirect(url_for('contador_visitas'))

@app.route('/increment_visits', methods=['POST'])
def increment_visits():
    global visitas
    increment = int(request.form['increment'])
    visitas = (visitas - 1) + increment
    session['visitas'] = visitas
    return redirect(url_for('contador_visitas'))

if __name__ == "__main__":
    app.secret_key = 'Platano_33'
    app.config['SESSION_TYPE'] = 'redis'
    app.run(debug=True)
