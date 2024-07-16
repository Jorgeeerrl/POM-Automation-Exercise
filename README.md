<img align="center" src="https://www.automationexercise.com/static/images/home/logo.png" width="450" />

# POM Automation Exercise

## Descripción del Proyecto

Este proyecto es un conjunto de suites de pruebas automatizadas basado en el patrón de diseño Page Object Model (POM). Está diseñado para probar las funcionalidades de una tienda virtual, enfocándose en diferentes aspectos como las interacciones de usuario, la navegación de productos y los procesos de pago, entre otros. Para su desarrollo he utilizado 'Pycharm' y utilizan `pytest` para su ejecución y `allure` para la visualización de sus resultados.

## Características Destacables

- **Diseño basado en Page Object Model (POM)**: Cada página web está representada por una clase que encapsula sus elementos e interacciones. De esta manera logramos un código más limpio, así como una buena reutilización y un mejor mantenimiento del mismo.
- **Cobertura de Pruebas Integral**: Incluye pruebas para acciones de usuario, gestión de productos, proceso de pago, y diversas funcionalidades del sitio.
- **Generación de Datos**: Utiliza un generador de datos de prueba que usa la librería 'Fake' bajo un 'Patrón Singleton', asegurando que sólo haya una instancia de la clase Datos durante la ejecución.
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

1. **Instalar Dependencias**: Las dependencias están en el archivo 'requirements.txt'. Asegúrate de tenerlas instaladas.
    ```sh
    pip install -r requirements.txt
    ```

2. **Ejecutar las Pruebas**: Navega al directorio del proyecto y ejecuta las pruebas.
    ```sh
    pytest --alluredir=./allure/resultados/<nombre_archivo_resultados>
    ```
    
3. **Visualizar los resultados de las pruebas**
    ```sh
    allure serve ./allure/resultados/<nombre_archivo_resultados>  
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

<details>
  <summary><strong>✅Test Case 4: Logout User</strong></summary>
&nbsp;

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

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 5: Register User with existing email</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and already registered email address
7. Click 'Signup' button
8. Verify error 'Email Address already exist!' is visible

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 6: Contact Us Form</strong></summary>
&nbsp;
    
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

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 8: Verify All Products and product detail page</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. The products list is visible
7. Click on 'View Product' of first product
8. User is landed to product detail page
9. Verify that detail detail is visible: product name, category, price, availability, condition, brand

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 9: Search Product</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. Enter product name in search input and click search button
7. Verify 'SEARCHED PRODUCTS' is visible
8. Verify all the products related to search are visible

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 10: Verify Subscription in home page</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Scroll down to footer
5. Verify text 'SUBSCRIPTION'
6. Enter email address in input and click arrow button
7. Verify success message 'You have been successfully subscribed!' is visible

&nbsp;
</details>


<details>
  <summary><strong>✅Test Case 10: Verify Subscription in home page</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Scroll down to footer
5. Verify text 'SUBSCRIPTION'
6. Enter email address in input and click arrow button
7. Verify success message 'You have been successfully subscribed!' is visible

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 11: Verify Subscription in Cart page</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Cart' button and scroll down to footer
5. Verify text 'SUBSCRIPTION'
6. Enter email address in input and click arrow button
7. Verify success message 'You have been successfully subscribed!' is visible

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 12: Add Products in Cart</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Products' button
5. Hover over first product and click 'Add to cart'
6. Click 'Continue Shopping' button
7. Hover over second product and click 'Add to cart'
8. Click 'View Cart' button
9. Verify both products are added to Cart
10. Verify their prices, quantity and total price

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 13: Verify Product quantity in Cart</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'View Product' for any product on home page
5. Verify product detail is opened
6. Increase quantity to 4
7. Click 'Add to cart' button
8. Click 'View Cart' button
9. Verify that product is displayed in cart page with exact quantity

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 14: Place Order: Register while Checkout</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Add products to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click Proceed To Checkout
8. Click 'Register / Login' button
9. Fill all details in Signup and create account
10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
11. Verify 'Logged in as username' at top
12. Click 'Cart' button
13. Click 'Proceed To Checkout' button
14. Verify Address Details and Review Your Order
15. Enter description in comment text area and click 'Place Order'
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click 'Pay and Confirm Order' button
18. Verify success message 'Congratulations! Your order has been confirmed!'
19. Click 'Delete Account' button
20. Verify 'ACCOUNT DELETED!' and click 'Continue' button

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 15: Place Order: Register before Checkout</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill all details in Signup and create account
6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
7. Verify 'Logged in as username' at top
8. Add products to cart
9. Click 'Cart' button
10. Verify that cart page is displayed
11. Click Proceed To Checkout
12. Verify Address Details and Review Your Order
13. Enter description in comment text area and click 'Place Order'
14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
15. Click 'Pay and Confirm Order' button
16. Verify success message 'Congratulations! Your order has been confirmed!'
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' and click 'Continue' button

&nbsp;
</details>


<details>
  <summary><strong>✅Test Case 16: Place Order: Login before Checkout</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill email, password and click 'Login' button
6. Verify 'Logged in as username' at top
7. Add products to cart
8. Click 'Cart' button
9. Verify that cart page is displayed
10. Click Proceed To Checkout
11. Verify Address Details and Review Your Order
12. Enter description in comment text area and click 'Place Order'
13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
14. Click 'Pay and Confirm Order' button
15. Verify success message 'Congratulations! Your order has been confirmed!'

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 17: Remove Products From Cart</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Add products to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click 'X' button corresponding to particular product
8. Verify that product is removed from the cart

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 18: View Category Products</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that categories are visible on left side bar
4. Click on 'Women' category
5. Click on any category link under 'Women' category, for example: Dress
6. Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'
7. On left side bar, click on any sub-category link of 'Men' category
8. Verify that user is navigated to that category page

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 19: View & Cart Brand Products</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify that Brands are visible on left side bar
5. Click on any brand name
6. Verify that user is navigated to brand page and brand products are displayed
7. On left side bar, click on any other brand link
8. Verify that user is navigated to that brand page and can see products

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 20: Search Products and Verify Cart After Login</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify user is navigated to ALL PRODUCTS page successfully
5. Enter product name in search input and click search button
6. Verify 'SEARCHED PRODUCTS' is visible
7. Verify all the products related to search are visible
8. Add those products to cart
9. Click 'Cart' button and verify that products are visible in cart
10. Click 'Signup / Login' button and submit login details
11. Again, go to Cart page
12. Verify that those products are visible in cart after login as well
13. Remove all products that have been added
14. Verify 'Cart is empty! Click here to buy products.' is visible

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 21: Add review on product</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify user is navigated to ALL PRODUCTS page successfully
5. Click on 'View Product' button
6. Verify 'Write Your Review' is visible
7. Enter name, email and review
8. Click 'Submit' button
9. Verify success message 'Thank you for your review.'

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 22: Add to cart from Recommended items</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Scroll to bottom of page
4. Verify 'RECOMMENDED ITEMS' are visible
5. Click on 'Add To Cart' on Recommended product
6. Click on 'View Cart' button
7. Verify that product is displayed in cart page

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 23: Verify address details in checkout page</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill all details in Signup and create account
6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
7. Verify 'Logged in as username' at top
8. Add products to cart
9. Click 'Cart' button
10. Verify that cart page is displayed
11. Click Proceed To Checkout
12. Verify that the delivery address and the billing address are the same address filled at the time of account registration
13. Click 'Delete Account' button
14. Verify 'ACCOUNT DELETED!' and click 'Continue' button

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 24: Download Invoice after purchase order</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Add products to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click Proceed To Checkout
8. Click 'Register / Login' button
9. Fill all details in Signup and create account
10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
11. Verify 'Logged in as username' at top
12. Click 'Cart' button
13. Click 'Proceed To Checkout' button
14. Verify Address Details and Review Your Order
15. Enter description in comment text area and click 'Place Order'
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click 'Pay and Confirm Order' button
18. Verify success message 'Congratulations! Your order has been confirmed!'
19. Click 'Download Invoice' button and verify invoice is downloaded successfully
20. Click 'Continue' button
21. Click 'Delete Account' button
22. Verify 'ACCOUNT DELETED!' and click 'Continue' button

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Scroll down page to bottom
5. Verify 'SUBSCRIPTION' is visible
6. Click on arrow at bottom right side to move upward
7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen

&nbsp;
</details>

<details>
  <summary><strong>✅Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality</strong></summary>
&nbsp;

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Scroll down page to bottom
5. Verify 'SUBSCRIPTION' is visible
6. Scroll up page to top
7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen

&nbsp;
</details>

