class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        # super().voar()
        print("Pardal pode voar...")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao pode voar...")


def plano_de_voo(obj):
    obj.voar()


# pardal = Pardal().voar()
# avestruz = Avestruz().voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)