# Program koji ucitava txt file redak po redak, sprema u listu, ispisuje najdulji redak

if __name__ == '__main__':
    # Ime txt datoteke, koja se mora nalaziti u istom folderu.
    filename = "test.txt"

    # Otvara se text.txt te ga file.readLines() cita liniju po liniju i ubacuje u listu lines.
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]  # Ovaj red je opcionalan, samo izbacuje prazne redove dok cita.

    print(max(lines, key=len))  # Funkcija max uzima listu, te vadi samo najdulju liniju iz liste
