"""
3.feladat: Snooker világranglista

Az UTF-8 karakterkodolású "snooker.txt" a következő adatokat találja:

Helyezes;Nev;Orszag;Nyeremeny
52;Akani Sunny;Thaiföld;118500
7;Allen Mark;Észak-Írország;681000
72;Anda Zhang;Kína;44750
76;Astley John;Anglia;40000
73;Baird Sam;Anglia;44750

Az állomány sorai a versenyzők neve szerinti abécésorednben tárolja a versenyző helyezését a ranglistán, nevét, országát és az elmúlt időszakban elnyert pénzdíjak összegét angol fontban. Az állomány első sora az adatok fejlécét tartalmazza. Az adatokat pontosvesszővel választottuk el.

3.1: Készitsen konzolalkalmazást a következő feladatok megoldásához, amelynek forráskódját Snooker néven mentse el!

3.2  Hozzon létre egy osztályt (class), ami reprezentálja egy versenyző példányait (object isntance). Az osztály konstruktora (constructor) paraméterként kapjon meg egy beolvasott sort, és ebből határozza meg meg az adott attribútumokat (property). Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! 
Továbbá olvassa be az UTF-8 kódolású snooker.txt állományban sorait és tárolja el adatokat egy homogén listába, amely használatával a további feladatok megoldhatók! A terminálra való kiírás legyen a mintának megfelelő!

3.3: Határozza meg és írja ki a képernyőre a minta szerint, hogy hány versenyző szerepel a világranglistán!

3.4: Határozza meg, hogy a ranglistán szereplő versenyzők átlagosan mekkora bevételre tettek szert az elmúlt időszakban! Az eredményt két tizedesjegyre kerekítve jeleítse meg a minta szerint!

3.5: Határozza meg és írja ki a képernyőre a minta szerint a legjobban kereső kinai játékos adatait! Feltételezheti, hogy legalább egy kínai versenyző  volt, és nem alakult ki holtverseny közöttük. A nyeremény összegét forintba jelenítse meg! Az átszámoláshoz 380 FT-os angol font árfolyammal dolgozzon!

3.6: Határozza meg, hogy a világranglistán található-e norvég játékos!

Minta output:________________________________________________

3.feladat: A világranglistán 100 versenyző szerepel
4.feladat: A versenyzok átlagosan 183373.50 fontot kerestek
5.feladat:lejobban kereső kinai játékos:
            helyezés: 17
            Név: Yan Bingtao
            Ország: Kína
            nyeremény: 285000
            Nyeremény összege: 108300000 Ft
6. feladat: A versenyzők között van norvég versenyző.

_____________________________________________________________
"""

'''Helyezes;Nev;Orszag;Nyeremeny'''


class Snooker:
    def __init__(self,sor):
        sor = sor.strip().replace(".",",").split(";")
        self.Helyezes = int(sor[0])
        self.nev = str(sor[1])
        self.orszag = str(sor[2])
        self.nyer = int(sor[3])

#1-2.feladat:_________________________________________________________________________________

with open("snooker.txt","r",encoding="latin2") as f:
    elsosor= f.readline()
    lista = [Snooker(sor) for sor in f]
    
#3.feladat:_________________________________________________________________________________

print(f"3.feladat: A világranglistán {len(lista)} versenyző szerepel")

#4.feladat:_________________________________________________________________________________

ossz = [ sor.nyer for sor in lista ]
atlag = sum(ossz)
atlag2 = atlag / len(ossz)

print(f"4.feladat: A versenyzok átlagosan {atlag2:.2f} fontot kerestek")

#5.feladat:_________________________________________________________________________________

kinaiak = [(sor.nyer,sor )for sor in lista if sor.orszag == "Kína"]
kinaiak2, adatok = max(kinaiak)
forint = kinaiak2 * 380

print("5.feladat:lejobban kereső kinai játékos:")
print(f'''            helyezés: {adatok.Helyezes}
            Név: {adatok.nev}
            Ország: {adatok.orszag}
            nyeremény: {adatok.nyer}
            Nyeremény összege: {forint} Ft''')

#6.feladat:_________________________________________________________________________________
norveg = [sor for sor in lista if sor.orszag == "Norvégia"]

if len(norveg) > 0:
    print(f'6. feladat: A versenyzők között van norvég versenyző.')
else:
    print(f'6. feladat: A versenyzők között nincs norvég versenyző.')






