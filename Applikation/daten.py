import json
ausgaben_dict = "Static/daten/datenbank.json"




#Speicherung von Daten
def ausgaben_add_db(datei, key, value):
    try:
        with open(datei) as open_file:
            dict_content = json.load(open_file)   #Hiermit werden die Daten geladen
    except FileNotFoundError:                      #falls es die datei nicht findet
        dict_content = {}

    dict_content[str(key)] = value

    with open(datei, "w") as open_file:
        json.dump(dict_content, open_file, indent=4)

        open_file.close()




#Die Daten mit einer ID versehen
def ausgaben_save_data(new_ausgaben):
    ausgaben_id = str((len(formular_ausgaben_db().keys())) + 1)
    ausgaben_number = str("ausgaben " + ausgaben_id) #erstellt eine ID für jede neu hinzugefügte ID. Prüft nicht ob wert bereits vorhanden ist.

    ausgaben_add_db(ausgaben_dict, ausgaben_number, new_ausgaben)

    return ausgaben_number, new_ausgaben




def formular_ausgaben_db():
    try:
        with open(ausgaben_dict) as open_file:
            dict_content = json.load(open_file)

    except FileNotFoundError:
        dict_content = {}

    return dict_content