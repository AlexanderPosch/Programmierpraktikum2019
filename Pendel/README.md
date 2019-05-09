# Programmierpraktikum 2019
Das Multipendel:

Ziel des Projekts ist die Simulation eines Multipendels. Ein Multipendel sind mehrere Pendel, die aneinander gehängt sind. Solche Multipendel sind interessant da sie chaotisches Verhalten aufweisen.

Das Projekt besteht aus folgenden Teilen:
1)  Berechnung der Differenzialgleichungen die die Bewegung der Pendel bestimmen (sympy)
2)  Numerisches Lösen der Differenzialgleichungen (scipy)
3)  Animation des Pendels (matplotlib)
4)  Graphical User Interface mit Einlesen von Parametern (vielleicht dash)

Teil 0) haben wir bereits erledigt. Es können bis hin zu 5 Pendeln vereinfachte Gleichungssysteme gefunden werden und für mehr können nicht vereinfachte Gleichungssysteme gefunden werden. 

Für das Numerisches Lösen der Differenzialgleichungen bietet sich die scipy an. Jedoch ist uns noch unklar ob unser Code schnell genug sein wird um die Gleichungssysteme live zu lösen oder ob wir sie vorab berechnen und dann ein Video ablaufen lassen.

Für die Animation kann zum Beispiel mit matplotlib implementiert werden.

Die Graphical User Interface soll die Parameter einlesen: Anzahl der Pendel, Gewichte, Länge der Verbindungen, Startwinkel, Gravitationskonstante. Außerdem wäre es cool wenn die Animation darin eingebettet ist. Dies könnte man zum Beispiel mit der Library dash implementieren.
