Problembeschreibung/Motivation
 - Warum dieses Projekt
Die eigenen Ausgaben festzuhalten und diese zu überprüfen, ist der erste Schritt um sich die Kontrolle über die Ausgaben zu verschafen. Dadurch kann nachvollzogen werden, in welche Kategorien wie viel Ausgegeben wird. 
 - Welches Problem löst das Projekt
Eine eigene Applikation um seine Finanzen festzuhalten in vorgegebenen Kategorien.
 - Was macht das Projekt
Es nimmmt Daten vom Anwender engegen und speichert diese in einer JSON Datei ab. Die AUsgaben werden nach Ausgaben Kategorie summiert und ihm auf der Kostenübersicht Seite angezeigt. 
Betrieb
 - Welche zusätzliche Pakete müssen bei Bedarf installiert werden. (Muss im Normalfall nicht beachtet werden. Python muss nicht erwähnt werden, da das bei einem Python Projekt impliziert ist.)
keine weitere Pakete werden benötigt ausser die Pakete welche in der main.py erwähnt werden.
 - Was muss man bei der Ausführung beachten. Was muss eventuell davor noch gemacht werden.
Wenn die main.py gestartet wird, kann man auf das Projekt zugreifen und alle unterseiten funktionieren. Um die Flaskapplikation aufzurufen folgende URL aufrufen: http://127.0.0.1:5000/home
 - Welch Datei muss ausgeführt werden

Benutzung
- Wie wird das Projekt benutzt
Die Navigation erfolgt über die NAV Bar. Es können Kosten erfasst werden über das Formular.
- Welche Optionen oder auch Spezialitäten existieren

Architektur
- Hier bei Bedarf eine kurze Beschreibung des Ablaufs des Programms auf Code Ebene z.B. als Ablaufdiagramm.

Ungelöste/unbearbeitete Probleme
 - Was wurde nicht gelöst
Auf der summierten Kostensicht wäre es praktisch, wenn man ein individuellen Zeitraum oder Tag eintragen könnte und die Summierten Ausgaben sich nur auf diese Eingabe beziehen. Da die Ausgaben bereits über ein Datum enthalten in den Datenwerten, wäre dies eine mögliche Erweiterung und vermutlich mit wenig Aufwand verbunden. 
 - Welche Verbesserungen könnten noch gemacht werden.
Es könnte beim Formular für die Kostenerfassung die Möglichkeit geboten werden, neue Ausgaben Kategorien zu erstellen.