from flask import Flask, render_template, request
from models import db, Albums

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/home")
def home():
     username="Heidi"
     age=14
     return render_template("home.html", username=username, age=age)

@app.route("/music")
def music() :
    return("Hola aqui encontraras musica")

@app.route("/albumes")
def albumes() :
    return("Albumes de musica")

@app.route("/nueva_cancion")
def nueva_cancion():
     return render_template("nueva_cancion.html")

@app.route("/guardar_informacion", methods  = ["POST"])
def guardar_informacion():
    name =request.form["name"]
    new_songalbum = Albums(
        name = name
    )
    db.session.add(new_songalbum)
    db.sesson.commit()
    return render_template("home.html")
app.run(port=4000)