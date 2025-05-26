from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, db

# Inicializa la app de Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://communication-ff364-default-rtdb.firebaseio.com/'
})

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]
        

        # Guarda en Firebase
        ref = db.reference("usuarios")
        ref.push({
            "nombre": nombre,
            "email": email,
            "mensaje": mensaje
        })

        return redirect("/")

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
