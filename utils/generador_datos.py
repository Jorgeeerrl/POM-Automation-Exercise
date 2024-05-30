from dotenv import load_dotenv  # Para cargar variables de entorno desde un archivo .env
import random
from faker import Faker

load_dotenv()

# Funcionalidad del Archivo: Implementa un patrón Singleton asegurando que sólo haya una instancia de la clase Datos
#    durante la ejecución.


class Datos:

    _instancia_singleton = None  # Variable de clase que almacenará la única instancia de Data.

    def __new__(cls, *args, **kwargs):  # Método especial que controla la creación de nuevas instancias.
        if not cls._instancia_singleton:
            cls._instancia_singleton = super(Datos, cls).__new__(cls)
            cls._instancia_singleton._iniciada = False
        return cls._instancia_singleton

    # Si _instancia_singleton es None, se crea una nueva instancia; de lo contrario, se devuelve la instancia existente.

    def __init__(self):
        if not self._iniciada:  # Se ejecuta solo si _iniciada es False.
            self.fake = Faker()  # Instancia de Faker para generar datos.
            self.email = self.generar_email_random()
            self.nombre_login = self.fake.name()
            self.password = 'fakepass147'
            self.nombre_registro = self.fake.first_name()
            self.apellido_registro = self.fake.last_name()
            self.empresa = self.fake.company()
            self.direccion = self.fake.street_address()
            self.direccion_secundaria = self.fake.secondary_address()
            self.country = 'India'
            self.provincia = self.fake.state()
            self.poblacion = self.fake.city()
            self.codigo_postal = self.fake.zipcode()
            self.telefono = self.fake.phone_number()
            self.dia_nacimiento = str(self.fake.random_int(min=1, max=31))
            self.mes_nacimiento = self.fake.month_name()
            self.any_nacimiento = str(self.fake.random_int(min=1900, max=2021))
            self.any_caducidad = str(self.fake.random_int(min=1900, max=2021))
            self.mes_caducidad = str(self.fake.random_int(min=1, max=12)).zfill(2)
            self.cvc_tarjeta = str(self.fake.random_int(min=1, max=999)).zfill(3)
            self.numero_tarjeta = self.fake.credit_card_number(card_type=None)
            self.nombre_tarjeta = f'{self.nombre_registro} {self.apellido_registro}'
            self._iniciada = True  # Marca la instancia como inicializada para evitar que se vuelva a ejecutar __init__

    def generar_email_random(self):
        generar_email_random = random.randint(0, 9999)
        return f"testmail{generar_email_random}@mail.com"