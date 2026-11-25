
# INFORME TÉCNICO - AIREX

## 1. Introducción

AIREX es una aplicación de escritorio desarrollada en Python para registrar equipos de aire acondicionado y llevar un control de los mantenimientos realizados.

El programa cuenta con una interfaz gráfica sencilla que permite realizar estas operaciones de manera fácil.

## 2. Objetivo del proyecto

Desarrollar un sistema que permita registrar equipos de aire acondicionado, consultar sus características y almacenar temporalmente la información de sus mantenimientos.

## 3. Herramientas utilizadas

- Lenguaje de programación: Python.
- Entorno de desarrollo: Visual Studio Code.
- Interfaz gráfica: Tkinter.
- Paradigma: Programación Orientada a Objetos.

## 4. Organización del programa

El proyecto está dividido en los siguientes archivos:

- main.py: inicia la aplicación.
- equipo.py: contiene la clase Equipo y sus clases derivadas.
- mantenimiento.py: contiene la clase Mantenimiento.
- interfaz.py: controla las ventanas, botones y operaciones del programa.

## 5. Aplicación de la Programación Orientada a Objetos

En AIREX se aplican los siguientes conceptos:

### Abstracción
Se utiliza la clase Equipo como clase abstracta para representar las características generales de un aire acondicionado.

### Herencia
Las clases AireConvencional y AireInverter heredan los atributos y métodos de la clase Equipo.

### Encapsulamiento
Los atributos principales de las clases se protegen utilizando doble guion bajo y se consultan mediante propiedades.

### Polimorfismo
El método obtener_tipo() se implementa de manera diferente en las clases AireConvencional y AireInverter.

### Relaciones entre objetos
Cada equipo tiene una lista de mantenimientos asociados, lo que permite relacionar los equipos con los trabajos realizados.

## 6. Funcionalidades

El sistema permite:

1. Registrar equipos de aire acondicionado.
2. Consultar los equipos registrados.
3. Registrar mantenimientos para cada equipo.
4. Consultar el historial de mantenimientos.

## 7. Pruebas realizadas

Se realizaron pruebas de funcionamiento para comprobar el registro de equipos convencionales e inverter, la consulta de equipos y el registro y consulta de mantenimientos.

Las pruebas permitieron verificar el funcionamiento de las principales opciones de la aplicación.

## 8. Limitaciones

La información se almacena temporalmente en memoria. Por esta razón, los registros se pierden cuando se cierra el programa.

## 9. Conclusión

El desarrollo de AIREX permitió aplicar los conceptos principales de la Programación Orientada a Objetos mediante un proyecto práctico relacionado con el mantenimiento de aires acondicionados.
