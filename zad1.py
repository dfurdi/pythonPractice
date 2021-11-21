# Unijeti string i znak, te vratiti niz znakova od unesenog stringa koji se nalaze iza pojave unesenog znaka u stringu.
# string:Volim python, znak:y > thon

if __name__ == '__main__':
    # input
    print("Upisi recenicu.\n")
    recenica = str(input())

    print("Upisi znak.\n")
    char = str(input())

    # output
    print("ORIGINAL: " + recenica)

    # funkcija "split" se nadodaje na kraj stringa, koji se zove recenica.
    # split prima jedan karakter(u ovom slucaju moze i vise od jednoga posto je isto string), te ga razdvaja u listu
    # 1) ogranicava maksimalni parametar liste na listu sa 2 elementa. (0 i 1)
    # [1] oznacuje da se printa druga varijabla iz liste, kao u primjeru navednom gore, prva varijabla[0] bi bila "Volim p", a druga je "thon"

    print("SPLITAN: " + recenica.split(char, 1)[1])
