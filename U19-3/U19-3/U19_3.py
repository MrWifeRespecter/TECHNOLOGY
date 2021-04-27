#Det här är vad uppgiften säger att du ska göra:
#Jag fattar inte den här uppgiften, men nu är den klar antar jag?

class Djur:
    def __init__(self, ålder, vikt, längd):
        self.ålder = ålder
        self.vikt = vikt
        self.längd = längd

class Däggdjur(Djur):
    def __init__(self, ålder, vikt, längd):
        super().__init__(ålder, vikt, längd)

    def spring():
        print("Springer")

    def levandeBarn():
        print("Föder levande barn")


class Fåglar(Djur):
    def __init__(self, ålder, vikt, längd):
        super().__init__(ålder, vikt, längd)

    def flyg():
        print("Kan flyga")

    def ägg():
        print("Lägger ägg")

class Fiskar(Djur):
    def __init__(self, ålder, vikt, längd):
        super().__init__(ålder, vikt, längd)

    def simma():
        print("Kan simma")

    def ägg():
        print("Lägger ägg")

input()