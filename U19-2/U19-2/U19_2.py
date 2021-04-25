d = {}

class Maträtt:
    def __init__(self, namn, pris, co2, smak, svår, poäng): 
        self.namn = namn
        self.pris = pris
        self.co2 = co2
        self.smak = smak
        self.svår = svår
        self.poäng = poäng

    def stats(self):
        print("Statistik för ", self.namn,": ")
        print("Pris: ", (10-self.pris), "/ 10")
        print("CO2: ", (10-self.co2), "/ 10") 
        print("Smak: ", self.smak, "/ 10")
        print("Svårighetsgrad: ", (10-self.svår), "/ 10")
        print("Total mängd poäng: ", self.poäng, "/ 40")
        print("\n")

    def IngaIdeer(self): #det här får räknas som en klassfunktion. 
        print("Jag vet inte vad mer man kan vilja göra med en maträtt...")

def rätter(): #Frågar frågor om vilka egenskaper maträtten har och gör en klass med de egenskaperna
    namn=str(input("Vad heter din maträtt? ")).capitalize()
    pris=int(input("Hur dyr är den på en skala från 0/10 där 0 är gratis och 10 är jävligt dyr? ")) #Det finns ingenting som hindrar användaren att skriva in högre nummer än 10. Men det får vara deras problem
    co2 = int(input("Hur stor koldioxidpåverkan har rätten på jorden på en skala från 0/10 där 0 är ingen alls och 10 är jävligt hög? "))
    smak = int(input("Hur god är maten på en skala från 0/10 där 0 är äcklig och 10 är jävligt god? "))
    svår = int(input("Hur svår är rätten att laga på en skala från 0/10 där 0 är superlätt och 10 är jävligt svår? "))
    poäng = (10-pris) + smak + (10-svår) + (10-co2)
    print("\n") 
    rätt = Maträtt(namn, pris, co2, smak, svår, poäng)
    placeholderDict = {namn:rätt} #Kopierade detta från förra uppgiften eftersom att det funkade
    d.update(placeholderDict) #Updatear ett existerande dictionary med placeholderDict

def ValAvRätt():
    namn=str(input("Vilken rätt vill du se statistik och poäng för? ")).capitalize()
    if namn in d:
        print("\n")
        d[namn].stats()
    else:
        print("Nu gick någonting fel...")
        print("Här är listan med rätter du kan välja på: ")
        print(d)
        print("\n")

while True: #Den här låter användaren skriva in rätter tills hen är nöjd
    rätter()
    if input("Vill du skriva in fler rätter? Svara med J eller N: ").capitalize()=="N": #Den här täcker inte felinmatningar som typ "sjied". Men jag orkar inte bry mig om det. 
        break

while True:
    ValAvRätt()
    if input("Vill du se statistik för fler rätter? Svara med J eller N: ").capitalize()=="N": #Den här täcker inte felinmatningar som typ "sjied". Men jag orkar inte bry mig om det.
        break

input()
