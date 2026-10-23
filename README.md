# 9 SPRINT PROJECT —  Pruebas de Automatización Web de Urban Routes.
 — 
*Descripción*
=

Este proyecto contiene pruebas automatizadas de interfaz de usuario de extremo a extremo
para la aplicación web Urban Routes. El
objetivo es validar el proceso completo de reservación de taxis,
asegurando que los usuarios puedan solicitar con éxito
un viaje a través de diferentes escenarios de reservación y
configuraciones de acuerdo con los requisitos especificados.

Las pruebas automatizadas verifican los flujos críticos de los usuarios,
las validaciones de entrada, la selección de tarifas, las opciones de viaje y
el comportamiento general de la aplicación, desde los pasos iniciales de la reserva
hasta la confirmación final del viaje.

## Archivos principales
- `data.py`: contiene todos los datos de prueba, valores de entrada,
resultados esperados y configuraciones necesarias para
ejecutar los escenarios de prueba automatizados.


- `main.py`: contiene los casos de prueba automatizados con Selenium
que validan el flujo de trabajo completo de reserva de taxis,
incluidas diferentes variaciones de solicitud de viaje
basadas en los requisitos de negocio.


## Tecnologías y técnicas de prueba utilizadas
### Lenguaje de programación

- Python:
Lenguaje principal utilizado para desarrollar pruebas automatizadas de la interfaz de usuario.

### Marcos y herramientas de automatización

- Selenium WebDriver:
Se utiliza para automatizar las interacciones con el navegador
y simular el comportamiento real de los usuarios.


- WebDriverWait:
Se utiliza para implementar esperas explícitas
y manejar elementos web dinámicos de manera eficiente.

### Enfoques de prueba

- Pruebas de automatización de la interfaz de usuario:
Validación automatizada de los componentes
e interacciones de la interfaz de usuario.


- Pruebas de extremo a extremo (E2E):
Verificación del proceso completo de reserva
de taxis de principio a fin.


- Pruebas funcionales:
Validación de los requisitos de negocio
y la funcionalidad de la aplicación.


- Pruebas de regresión:
Aseguran que las funciones existentes sigan
funcionando correctamente después de cambios o actualizaciones.

### Estrategias de localización

- El proyecto utiliza múltiples técnicas de localización
para garantizar una identificación confiable de los elementos:
  - ID
  + Nombre de clase
  * XPath
  + Selectores CSS
  + Nombre
  + Nombre de etiqueta
___________

### Técnicas de interacción

- Interacciones con formularios:
  - Completar campos de texto
  - Ingresar información del usuario
  - Validar campos de entrada


- Interacciones con botones:
  - Acciones al hacer clic
  - Navegación a través de los flujos de trabajo de la aplicación


- Manejo de modales:
  - Interacción con ventanas emergentes y cuadros de diálogo modales


- Administración de elementos dinámicos:
  - Esperas explícitas para elementos cargados de forma asincrónica

### Cobertura de pruebas

Las pruebas automatizadas validan:
  - El flujo de trabajo completo de reservación de taxi
  - La validación de la información ingresada por el usuario
  - La selección y configuración del viaje
  - El comportamiento de la interfaz de usuario y la navegación
  - El manejo de elementos dinámicos
  - Escenarios de reservación de principio a fin
  - El manejo de errores y los mensajes de validación

### Mejores prácticas implementadas
- Estrategia de espera explícita:
Uso adecuado de WebDriverWait para
mejorar la estabilidad y la confiabilidad de las pruebas.


- Convenciones de nomenclatura descriptivas:
Nombres claros y significativos para variables,
funciones y casos de prueba.


- Estructura de pruebas mantenible:
Estructura de código bien organizada para facilitar
el mantenimiento y la escalabilidad.


- Datos de prueba reutilizables:
Gestión centralizada de los datos de prueba
para simplificar las actualizaciones y reducir la duplicación.


- Código legible y escalable:
Arquitectura del proyecto diseñada para soportar la futura
expansión de las pruebas y el mantenimiento a largo plazo.

````

Objetivo del proyecto

El objetivo de este proyecto es demostrar experiencia práctica
en la automatización de pruebas de interfaz de usuario (UI) utilizando Selenium WebDriver y Python, mediante la validación de flujos de negocio críticos dentro de una aplicación de reservación de taxis.

Este proyecto pone de manifiesto habilidades en:
- Automatización de pruebas
- Selenium WebDriver
- Python
- Pruebas de interfaz de usuario (UI)
- Pruebas de extremo a extremo
- Pruebas funcionales
- Pruebas de regresión
- Diseño de pruebas
- Control de calidad de software
````

Elaborado por Camilo Tiuzo 
Q.A Enginner 88
