from smartphone import Smartphone

catalog = [
    Smartphone("Honor", "A35", "+79007894512")
    Smartphone("Xiaomi", "CG456", "+79004587512")
    Smartphone("Samsung", "Galaxy", "+79965414512")
    Smartphone("POCO", "AS78", "+79056214812")
    Smartphone("PQ", "LKJ", "+7984579522")
]

#печать каталога смартфонов
for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.nomer}")