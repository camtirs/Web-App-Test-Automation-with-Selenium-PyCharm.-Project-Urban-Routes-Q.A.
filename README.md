# Pruebas de automatización web de Urban Routes

**  Sprint 9:Proyecto**

## Descripción

Este proyecto implementa pruebas automatizadas de interfaz de usuario para Urban Routes mediante Python, Selenium WebDriver y pytest.

El objetivo es verificar las principales funcionalidades del proceso de reservación de taxis, desde la configuración de la ruta hasta la visualización de la información del conductor.

Las pruebas están organizadas en escenarios independientes y utilizan el patrón Page Object Model (POM) para separar las interacciones con la interfaz de los casos de prueba.

## Objetivos

- Automatizar escenarios funcionales de la reservación de taxis.
- Verificar los datos introducidos por el usuario.
- Validar la selección de tarifa, el teléfono, el método de pago y las opciones del viaje.
- Comprobar el modal de búsqueda del automóvil y la información del conductor.
- Mejorar la mantenibilidad y la confiabilidad de las pruebas automatizadas.

## Tecnologías

- **Python:** lenguaje de programación.
- **Selenium WebDriver:** automatización de las interacciones con el navegador.
- **pytest:** ejecución y organización de las pruebas.
- **Chrome:** navegador utilizado para ejecutar los escenarios.

## Estructura de archivos

- `main.py`: contiene los nueve escenarios de prueba y la configuración del navegador.
- `pages.py`: contiene la clase `UrbanRoutesPage`, los localizadores y los métodos de interacción.
- `data.py`: centraliza la URL y los datos de prueba.
- `helpers.py`: contiene la función proporcionada por TripleTen para recuperar el código de confirmación telefónica.
- `README.md`: documentación del proyecto.
- `.gitignore`: excluye archivos temporales y configuraciones locales.

## Escenarios de prueba

1. Configuración de las direcciones de origen y destino.
2. Selección y validación de la tarifa Comfort.
3. Registro y confirmación del número telefónico.
4. Agregado del método de pago.
5. Introducción y validación del mensaje para el conductor.
6. Selección de manta y pañuelos.
7. Selección de dos helados.
8. Visualización del modal de búsqueda del automóvil.
9. Verificación de la información del conductor.

## Estrategias de automatización

- Localizadores mediante ID, XPath, CSS Selector y Class Name.
- Esperas explícitas para elementos dinámicos.
- Validaciones mediante aserciones.
- Preparación independiente de los escenarios.
- Cierre del navegador después de cada prueba.

## Instalación

Se recomienda utilizar un entorno virtual de Python.

```bash
python -m venv venv
```

Activar el entorno en Windows:

```bash
venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Antes de ejecutar las pruebas, actualiza `urban_routes_url` en `data.py` con la URL activa proporcionada por TripleTen.

Verifica también que Chrome, Selenium y el controlador del navegador sean compatibles con el entorno de ejecución.

## Ejecución de las pruebas

Ejecutar todos los escenarios:

```bash
pytest main.py -v
```

Ejecutar un escenario específico:

```bash
pytest main.py::TestUrbanRoutes::test_set_route -v
```

## Resultado esperado

pytest muestra el resultado individual de cada escenario, permitiendo identificar las pruebas aprobadas y las que necesitan revisión.

El resultado real debe confirmarse ejecutando la suite contra el servidor activo de Urban Routes.

## Autor

Camilo Tiuzo

QA Engineer 88| TripleTen
