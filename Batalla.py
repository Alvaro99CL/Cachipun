from ALV_Cachipun.Cachipun import Cachipun

class Batalla:
    def __init__(self, a: Cachipun, b: Cachipun):
        self.py1 = a
        self.com = b

    def IniciarCombate(self):
        print(self.py1.nombre + " VS " + self.com.nombre)
        if self.py1.debilidad == self.com.nombre:
            print("Haz perdido amigo terricola ")

        if self.py1.fuerza == self.com.nombre:
            print("Ganaste !!!!")

        if self.py1.nombre == self.com.nombre:
            print("epaa , nadie se rompe, otra ronda")