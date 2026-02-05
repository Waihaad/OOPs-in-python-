#Create a program for an Online Shopping System using Multilevel Inheritance.

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)


class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        self.display_product()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)


class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        self.display_electronic_product()
        print("RAM:", self.ram)
        print("Storage:", self.storage)


mobile1 = MobilePhone(
    "Smartphone",
    25000,
    "Samsung",
    "1 Year",
    "8 GB",
    "128 GB"
)

mobile1.display_mobile_details()

#Task 2 ----------------------------------------------------------------------

class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera Quality:", self.camera_quality)


class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print("Sound Quality:", self.sound_quality)


class SmartPhone(Camera, MusicPlayer):
    def __init__(self, brand, camera_quality, sound_quality):
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)
        self.brand = brand

    def display_smartphone_details(self):
        print("Brand:", self.brand)
        self.display_camera_details()
        self.display_music_details()


phone1 = SmartPhone(
    "Samsung",
    "108 MP",
    "Dolby Atmos"
)

phone1.display_smartphone_details()

