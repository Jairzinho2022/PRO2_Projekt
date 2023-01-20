from flask import Flask
from flask import render_template
from flask import request
import daten
import json

app = Flask('Ausgaben-Tracker')


#sind die headings für die tabelle
headings = ("Datum", "Typ", "Konto", "Betrag")

#die python Funktion wird benötigt um die Summen nach Kategorien zu berechnen
def berechnung_ausgaben(file_name, expense_type):
    with open(file_name, "r") as f:
        expenses = json.load(f)
    total_sum = 0
    for key, value in expenses.items():
        if value["ausgaben_typ"] == expense_type:
            total_sum += int(value["ausgaben_betrag"])
    return total_sum



@app.route('/home')
def home():
    return render_template('index.html')

@app.route("/Kostensicht")
def ausgaben():
    # hier wurden die Kategorien definiert damit sie einzeln aufgerufen werden können
    ausgaben_krankenversicherung = berechnung_ausgaben("Static/daten/datenbank.json", "Krankenversicherung")
    ausgaben_lebensmittel = berechnung_ausgaben("Static/daten/datenbank.json", "Lebensmittel")
    ausgaben_ausgang = berechnung_ausgaben("Static/daten/datenbank.json", "Ausgang")
    ausgaben_kleider = berechnung_ausgaben("Static/daten/datenbank.json", "Kleider")
    ausgaben_schule = berechnung_ausgaben("Static/daten/datenbank.json", "Schule")
    ausgaben_it = berechnung_ausgaben("Static/daten/datenbank.json", "IT")
    ausgaben_diverses = berechnung_ausgaben("Static/daten/datenbank.json", "Diverses")

    return render_template("kostensicht.html", ausgaben_krankenversicherung=ausgaben_krankenversicherung, ausgaben_lebensmittel=ausgaben_lebensmittel, ausgaben_ausgang=ausgaben_ausgang, ausgaben_kleider=ausgaben_kleider,ausgaben_schule=ausgaben_schule, ausgaben_it=ausgaben_it, ausgaben_diverses=ausgaben_diverses)


@app.route("/formular")
def ausgaben_display_db():

#Tabelle anzuzeigen, quelle: https://www.youtube.com/watch?v=mCy52I4exTU
    ausgaben = daten.formular_ausgaben_db()
    return render_template("formular.html", headings=headings, data=ausgaben)

#Wird benötigt um Daten zu speichern
@app.route("/add", methods=['GET', 'POST'])
def ausgaben_save():
    if request.method == 'POST':
        ausgaben_datum = request.form["ausgaben_datum"]
        ausgaben_typ = request.form["ausgaben_typ"]
        ausgaben_konto = request.form["ausgaben_konto"]
        ausgaben_betrag = request.form["ausgaben_betrag"]

#Wenn eine neue Eingabe statt findet, wird sie folgendermassen eingespeichert
        new_ausgaben = {
            "ausgaben_datum": ausgaben_datum,
            "ausgaben_typ": ausgaben_typ,
            "ausgaben_konto": ausgaben_konto,
            "ausgaben_betrag": ausgaben_betrag,
        }
        daten.ausgaben_save_data(new_ausgaben)

#und das wird benötigt um die erstellten Daten anzuzeigen
        return render_template("add_result.html",
                               headings=headings,
                               ausgaben_datum=ausgaben_datum,
                               ausgaben_typ=ausgaben_typ,
                               ausgaben_konto=ausgaben_konto,
                               ausgaben_betrag=ausgaben_betrag,
                               )
    return render_template("/add.html")

@app.route("/add_result")
def add_result():
    return render_template("add_result.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)

