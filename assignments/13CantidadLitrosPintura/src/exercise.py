import math
def main():
    #escribe tu código abajo de esta línea
    ap=float(input("Area a pintar en metros: "))
    r=float(input("Rendimiento (m2/l): "))
    s=(ap/r)
    print("Litros a comprar:",math.ceil(s))
if __name__ == '__main__':
    main()
