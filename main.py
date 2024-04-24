from collections import namedtuple

Car = namedtuple('Car', ['brand', 'model', 'year'])

class CarDatabase:
    def __init__(self):
        self.cars = []

    def create_car(self, brand, model, year):
        car = Car(brand=brand, model=model, year=year)
        self.cars.append(car)
        print("Avto yaratildi: ", car)

    def read_cars(self):
        if self.cars:
            for idx, car in enumerate(self.cars, start=1):
                print(f"{idx}. Avto: {car}")
        else:
            print("Bazada avtolar mavjud emas.")

    def update_car(self, index, brand, model, year):
        if 0 < index <= len(self.cars):
            self.cars[index - 1] = Car(brand=brand, model=model, year=year)
            print(f"{index} avto o'zgartirildi.")
        else:
            print("Noto'g'ri indeks.")

    def delete_car(self, index):
        if 0 < index <= len(self.cars):
            deleted_car = self.cars.pop(index - 1)
            print("Avto ochirildi: ", deleted_car)
        else:
            print("Noto'g'ri indeks.")

car_db = CarDatabase()

while True:
    print("1. Avto yaratish")
    print("2. Avtolar ro'yxatini ko'rsatish")
    print("3. Avto o'zgartirish")
    print("4. Avto ochirish")
    print("5. Chiqish")

    choice = input("Bajariladigan operatsiyani tanlang (1/2/3/4/5): ")

    if choice == '1':
        brand = input("Brand: ")
        model = input("Model: ")
        year = input("Yil: ")
        car_db.create_car(brand, model, year)
    elif choice == '2':
        print("Avtolar ro'yxati: ")
        car_db.read_cars()
    elif choice == '3':
        index = int(input("O'zgartiriladigan avtoning indeksi: "))
        brand = input("Brend: ")
        model = input("Madel: ")
        year = input("Yil: ")
        car_db.update_car(index, brand, model, year)
    elif choice == '4':
        index = int(input("O'chiriladigan avtoning indeksi: "))
        car_db.delete_car(index)
    elif choice == '5':
        print("Chiqish...")
        break
    else:
        print("Noto'g'ri tanlov. Iltimos, qaytadan urunib ko'ring.")
