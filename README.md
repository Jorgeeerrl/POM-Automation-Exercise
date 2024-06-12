<img align="center" src="https://www.automationexercise.com/static/images/home/logo.png" width="450" />

# POM Automation Exercise

## Descripción del Proyecto

Este proyecto es una suite de pruebas automatizadas basada en el patrón de diseño Page Object Model (POM). Está diseñado para probar las funcionalidades de una aplicación web, enfocándose en diferentes aspectos como las interacciones de usuario, la navegación de productos, los procesos de pago, entre otros. Las pruebas están escritas en Python y utilizan el framework `pytest` para su ejecución.

## Características Destacables

- **Diseño basado en Page Object Model (POM)**: Cada página web está representada por una clase que encapsula sus elementos e interacciones. De esta manera logramos un código más limpio, así como una buena reutilización y un mejor mantenimiento del mismo.
- **Cobertura de Pruebas Integral**: Incluye pruebas para acciones de usuario, gestión de productos, proceso de pago, y diversas funcionalidades del sitio.
- **Generación de Datos**: Utiliza un generador de datos de prueba que usa la librería Fake bajo un Patrón Singleton asegurando que sólo haya una instancia de la clase Datos durante la ejecución.
- **Configuración y Utilidades**: Archivos de configuración y utilidades adicionales para facilitar las pruebas.
- **Resultados de Test**: Utiliza Allure para mostrar y guardar los resultados de las pruebas, con pasos y marcadores según los principales Funcionalidades e Historias de Usuario relacionadas.

## Estructura del Proyecto

```plaintext
POM_Automation_Exercise/
├── conftest.py                   # Configuración de pytest
├── pages/                        # Clases de páginas que siguen el patrón POM
│   ├── page_base.py
│   ├── page_carrito.py
│   ├── page_checkout.py
│   ├── page_contacto.py
│   ├── page_cuenta_borrada.py
│   ├── page_cuenta_creada.py
│   ├── page_detalles_producto.py
│   ├── page_envio.py
│   ├── page_header_footer.py
│   ├── page_home.py
│   ├── page_login_registro.py
│   ├── page_pago.py
│   ├── page_productos.py
│   ├── page_registro.py
│   └── page_test_cases.py
├── tests/                        # Suites de pruebas
│   ├── test_base.py
│   ├── test_suite_checkout.py
│   ├── test_suite_navegacion_scroll.py
│   ├── test_suite_productos.py
│   ├── test_suite_support.py
│   ├── test_suite_suscripcion.py
│   └── test_suite_usuario.py
├── utils/                        # Utilidades adicionales
│   ├── generador_datos.py
│   └── urls.py
└── Tabla Organización Test Cases.xlsx  # Documento de organización de casos de prueba
```

## Detalle de los Casos de Prueba

- **`test_suite_checkout.py`**: Pruebas relacionadas con el proceso de pago, incluyendo verificación de precios, envío, y confirmación de pedido.
- **`test_suite_navegacion_scroll.py`**: Pruebas de navegación y desplazamiento en la página, asegurando que los elementos son accesibles y visibles.
- **`test_suite_productos.py`**: Pruebas de la gestión de productos, como la visualización de detalles, adición al carrito, y categorías de productos.
- **`test_suite_support.py`**: Pruebas de las funcionalidades de soporte y contacto, verificando el envío y la recepción de mensajes.
- **`test_suite_suscripcion.py`**: Pruebas de las funcionalidades de suscripción a newsletters y notificaciones.
- **`test_suite_usuario.py`**: Pruebas relacionadas con la gestión de cuentas de usuario, como registro, inicio de sesión, y eliminación de cuentas.

## Cómo Ejecutar las Pruebas

1. **Instalar Dependencias**: Asegúrate de tener Python y `pytest` instalados.
    ```sh
    pip install pytest
    ```

2. **Ejecutar las Pruebas**: Navega al directorio del proyecto y ejecuta las pruebas.
    ```sh
    pytest
    ```

## Casos de Prueba Cubiertos en los Tests

<details>
  <summary><strong>✅Test Case 1: Register User</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3.Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8.Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14.Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16.Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18.Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 2: Login User with correct email and password</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter correct email address and password
7. Click 'login' button
8. Verify that 'Logged in as username' is visible
9. Click 'Delete Account' button
10. Verify that 'ACCOUNT DELETED!' is visible

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 3: Login User with incorrect email and password</strong></summary>
&nbsp;
    
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter incorrect email address and password
7. Click 'login' button
8. Verify error 'Your email or password is incorrect!' is visible

&nbsp;
</details>

#### ✅Test Case 4: Logout User
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter correct email address and password
7. Click 'login' button
8. Verify that 'Logged in as username' is visible
9. Click 'Logout' button
10. Verify that user is navigated to login page

#### ✅Test Case 5: Register User with existing email
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and already registered email address
7. Click 'Signup' button
8. Verify error 'Email Address already exist!' is visible

#### ✅Test Case 6: Contact Us Form
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Contact Us' button
5. Verify 'GET IN TOUCH' is visible
6. Enter name, email, subject and message
7. Upload file
8. Click 'Submit' button
9. Click OK button
10. Verify success message 'Success! Your details have been submitted successfully.' is visible
11. Click 'Home' button and verify that landed to home page successfully

#### ✅Test Case 8: Verify All Products and product detail page
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. The products list is visible
7. Click on 'View Product' of first product
8. User is landed to product detail page
9. Verify that detail detail is visible: product name, category, price, availability, condition, brand

#### ✅Test Case 9: Search Product
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. Enter product name in search input and click search button
7. Verify 'SEARCHED PRODUCTS' is visible
8. Verify all the products related to search are visible

#### ✅Test Case 10: Verify Subscription in home page
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Scroll down to footer
5. Verify text 'SUBSCRIPTION'
6. Enter email address in input and click arrow button
7. Verify success message 'You have been successfully subscribed!' is visible
