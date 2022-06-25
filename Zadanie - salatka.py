# Zadanie formatowanie zapisów

wagiZakupow = [350, 325, 350]  # dla kolejno pomidora, mozarelli, salaty
pomidor = [19, 1, 0, 4, 5.7]
serMozarella = [248, 18, 19, 2, 38.32]
salata = [13, 1, 0, 2, 3.15]

print("Salatka:")

print(
    f"pomidor: kalorie: { (pomidor[0] * 3.5):^10} b: {(pomidor[1] * 3.5):^5}  t:{(pomidor[2] * 3.5):^5}  w: {(pomidor[3] * 3.5):^5} waga: {(wagiZakupow[0]):^5}g  koszt:{(pomidor[4] * 0.35):^5} PLN")
print(
    f"pomidor: kalorie: {(serMozarella[0] * 3.25):^10} b: {(serMozarella[1] * 3.25):^5}  t:{(serMozarella[2] * 3.25):^5}  w: {serMozarella[3] * 3.25}   waga: {(wagiZakupow[1]):^5}g  koszt:{(serMozarella[4] * 0.325):^5}  PLN")
print(
    f"pomidor: kalorie: {(salata[0] * 3.5):^10} b: {(salata[1] * 3.5):^5}  t:{(salata[2] * 3.5):^5}  w: {(salata[3] * 3.5):^5} waga: {(wagiZakupow[2]):^5}g  koszt:{(salata[4] * 0.35):^5}  PLN")
print(
    "======================================================================================================================================================")
print(f" SUMA:   kalorie: {((pomidor[0] * 3.5) + (serMozarella[0] * 3.25) + (salata[0] * 3.5)):^10} b:{(pomidor[1] * 3.5) + (serMozarella[1] * 3.25) + (salata[1] * 3.5)}    t: {((pomidor[2] * 3.5) + (serMozarella[2] * 3.25) + (salata[2] * 3.5)):^5} w: {((pomidor[3] * 3.5) + (serMozarella[3] * 3.25) + (salata[3] * 3.5)):^5} waga: {(wagiZakupow[0] + wagiZakupow[1] + wagiZakupow[2]):^5}   koszt:{(pomidor[4] * 0.35)+(serMozarella[4] * 0.325)+(salata[4]*0.35)}")
