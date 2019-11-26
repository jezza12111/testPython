class Stav:

    hotove = {}

    def __init__(self, stav):
        self.predchudce = stav
        self.smerZPredchoziho = None
        self.poziceNuly = -1;
        self.naslednici = []
        self.stavovePole = []

    def nastavPocatecniStav(self):
        self.poziceNuly = 4
        self.stavovePole = [7, 2, 4, 5, 0, 6, 8, 3, 1]

    def kontrolaDuplicity(self, stav):
        return stav.dejHash() in self.hotove

    def dejHash(self):
        return self.stavovePole[0] + self.stavovePole[1] * 10 + self.stavovePole[2] * 100 + self.stavovePole[3] * 1000 \
               + self.stavovePole[4] * 10000 \
               + self.stavovePole[5] * 100000\
               + self.stavovePole[6] * 1000000 + self.stavovePole[7] * 10000000 + self.stavovePole[8] * 100000000;

    def muzuVlevo(self):
        return self.poziceNuly != 0 and self.poziceNuly != 3 and self.poziceNuly != 6

    def muzuVPravo(self):
        return self.poziceNuly != 2 and self.poziceNuly != 5 and self.poziceNuly != 8

    def muzuDolu(self):
        return self.poziceNuly != 6 and self.poziceNuly != 7 and self.poziceNuly != 8

    def muzuNahoru(self):
        return self.poziceNuly != 0 and self.poziceNuly != 1 and self.poziceNuly != 2

    def nastavStavZPredchudce(self):
        if self.predchudce is not None:
            if self.predchudce.stavovePole is not None:
                self.stavovePole = self.predchudce.stavovePole.copy()
            else:
                self.stavovePole = []

    def generujNasledniky(self):
        if self.muzuVlevo():
            stav = Stav(self)
            stav.nastavStavZPredchudce()
            stav.smerZPredchoziho()
            docasna = stav.stavovePole[self.poziceNuly - 1]
            stav.stavovePole[self.poziceNuly - 1] = 0
            stav.stavovePole[self.poziceNuly] = docasna
            stav.poziceNuly = self.poziceNuly - 1
            if self.kontrolaDuplicity(stav):
                self.naslednici.append(stav)

        if self.muzuVPravo():
            stav = Stav(self)
            stav.nastavStavZPredchudce()
            stav.smerZPredchoziho()
            docasna = stav.stavovePole[self.poziceNuly + 1]
            stav.stavovePole[self.poziceNuly + 1] = 0
            stav.stavovePole[self.poziceNuly] = docasna
            stav.poziceNuly = self.poziceNuly + 1
            if self.kontrolaDuplicity(stav):
                self.naslednici.append(stav)

        if self.muzuDolu():
            stav = Stav(self)
            stav.nastavStavZPredchudce()
            stav.smerZPredchoziho()
            docasna = stav.stavovePole[self.poziceNuly + 3]
            stav.stavovePole[self.poziceNuly + 3] = 0
            stav.stavovePole[self.poziceNuly] = docasna
            stav.poziceNuly = self.poziceNuly + 3
            if self.kontrolaDuplicity(stav):
                self.naslednici.append(stav)

        if self.muzuNahoru():
            stav = Stav(self)
            stav.nastavStavZPredchudce()
            stav.smerZPredchoziho()
            docasna = stav.stavovePole[self.poziceNuly - 3]
            stav.stavovePole[self.poziceNuly - 3] = 0
            stav.stavovePole[self.poziceNuly] = docasna
            stav.poziceNuly = self.poziceNuly - 3
            if self.kontrolaDuplicity(stav):
                self.naslednici.append(stav)
