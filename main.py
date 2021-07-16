from ALV_Cachipun.Batalla import Batalla
from ALV_Cachipun.Cachipun import Cachipun

Piedra = Cachipun("Piedra", "Tijera", "Papel")
Papel  = Cachipun("Papel","Piedra","Tijera")
Tijera = Cachipun("Tijera","Papel","Piedra")

print("Batalla del infinito")
game = Batalla(Tijera, Papel)
game.IniciarCombate()