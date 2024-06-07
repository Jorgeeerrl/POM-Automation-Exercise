
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

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (feature/nueva-funcionalidad).
3. Realiza tus cambios.
4. Envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, revisa el archivo LICENSE.
