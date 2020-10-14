from particulas import Particula

class Administradora():
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

p01 = Particula(1, 5, 6, 7, 8, 10, 255, 23, 0)
p02 = Particula(2, 200, 300, 400, 150, 79, 55, 232, 101)
p03 = Particula()
admin_particula = Administradora()

admin_particula.agregar_final(p01)
admin_particula.agregar_inicio(p02)
admin_particula.agregar_inicio(p03)

admin_particula.mostrar()