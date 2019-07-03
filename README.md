# Minesweeper

Minesweeper
Ziel des Projekts war das Programmieren des Spieles Minesweeper.
Das Projekt besteht aus folgenden Teilen: 

1. Programmierern der Algorithmen
Generale Mechanik:
Das Minenfeld wird durch eine Matrix  (nparray) dargestellt jedes Feld gibt an wie viele Bomben es angrenzt (0-8). Wenn auf einem Feld eine Bombe liegt hat die Matrix dort den Wert 9. Wenn ein Feld geflaggt ist wird der Wert um 10 erhöht. Wenn ein Feld aufgedeckt ist wird der Wert um 20 erhöht. Zum Beispiel wird eine Aufgedeckte 1 wird als 21 abgespeichert.
Minenplatzierung und nummerieren der Nachbarfelder:
Die Bomben werden erst nach dem ersten Klick vom Benutzer zufällig platziert, sodass beim ersten Klick noch keine Bombe aufgemacht wird. Das erreichen wir dadurch das wir die Felder neben den Klick nicht vom Zufalls-algorithmus gewählt werden können. (random.sample stellt sicher, dass wir eine fixe Anzahl von Bomben haben)
Die Felder ohne Bombe sollen anzeigen, an wie viele Bomben sie angrenzen. Dafür  iterieren wir über alle Bombenfelder und erhöhen den Wert der Nachbarfelder (die nicht Bomben sind) um  1.
Floodfill Algorithmus:
Wenn ein Feld mit einer 0 aufgedeckt wird soll das Programm sofort alle Nachbarfelder aufdecken. Dafür wird ein Floodfill Algorithmus verwendet. Der Algorithmus nimmt eine Liste von Feldern die den Wert Null haben öffnet die Nachbarfelder und schaut ob er  0er aufgedeckt hat. Falls ja wird der Algorithmus mit den gefunden 0er-Feldern wiederholt.

2.Graphische Implementierung tkinter
Die GUI haben wir mit tkinter programmiert. Sie besteht aus zwei Teilen, dem Menüscreen und dem Gamescreen. 
Beim Menü-screen kann man die Schwierigkeitsstufen durch Radiobuttons einstellen und durch einen Button das Spiel starten.
Im Gamescreen befindet sich das Spielfeld, jedes Feld wird durch einen Button mit Bild dargestellt. Das Bild zeigt den Wert des Feldes an (falls es aufgedeckt ist ansonsten sonst ist das Bild Grau).



Projekt von:
Cedrine Nilles: nilles.cedrine@gmail.com
Johannes Becker: johanness.beckerr@gmail.com
Alexander Posch: alex.j.posch@gmail.com

Tutor: Joaquín Padilla Montani
