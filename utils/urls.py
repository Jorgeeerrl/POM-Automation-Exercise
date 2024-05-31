# La clase Urls tiene un conjunto de variables de clase (atributos estáticos) para almacenar las URLs del sitio.
# La f antes de la cadena indica que es una "f-string". Permite la inserción de variables dentro de la cadena.

class Urls:

    HOST = "https://automationexercise.com/"
    PAGE_HOME = f"{HOST}"
    PAGE_LOGIN_REGISTRO = f"{HOST}login"
    PAGE_REGISTRO = f"{HOST}signup"
    PAGE_CUENTA_CREADA = f"{HOST}account_created"
    PAGE_CUENTA_BORRADA = f"{HOST}delete_account"
    PAGE_CONTACTO = f"{HOST}contact_us"
