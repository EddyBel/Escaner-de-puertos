<h1 align="center">Escáner de Puertos</h1>

<p align="center">
 <img alt="banner_01" src="https://img.shields.io/github/last-commit/EddyBel/Escaner-de-puertos?color=%23AED6F1&style=for-the-badge" />
 <img alt="banner_02" src="https://img.shields.io/github/license/EddyBel/Escaner-de-puertos?color=%23EAECEE&style=for-the-badge" />
 <img alt="banner_03" src="https://img.shields.io/github/languages/top/EddyBel/Escaner-de-puertos?color=%23F9E79F&style=for-the-badge" />
 <img alt="banner_04" src="https://img.shields.io/github/languages/count/EddyBel/Escaner-de-puertos?color=%23ABEBC6&style=for-the-badge" />
 <img alt="banner_05" src="https://img.shields.io/github/languages/code-size/EddyBel/Escaner-de-puertos?color=%23F1948A&style=for-the-badge" />
</p>

<p align="center">Simple escaner de puertos</p>

## 📝 Descripción del repositorio

Este proyecto es una herramienta sencilla diseñada para escanear todos los puertos TCP en un equipo y determinar qué conexiones están activas. La herramienta utiliza un enfoque de escaneo de puertos completo, lo que significa que escanea todos los puertos posibles en el equipo y proporciona una lista detallada de los puertos abiertos y cerrados.

Esta herramienta es útil para identificar posibles vulnerabilidades en un equipo, ya que los puertos abiertos pueden ser aprovechados por los hackers para acceder al equipo. También es útil para identificar qué servicios están en ejecución en el equipo.

## 😸 Porque cree este repositorio?

Este proyecto fue diseñado con el objetivo de proporcionar a los usuarios una herramienta sencilla y fácil de usar para escanear los puertos de su equipo. El escaneo de puertos es una técnica comúnmente utilizada para identificar qué puertos están abiertos en un sistema y si hay conexiones activas a través de esos puertos. Esto puede ser muy útil para los administradores de sistemas que necesitan supervisar el tráfico de red en sus sistemas, o para los usuarios que desean asegurarse de que su sistema no tenga puertos abiertos no deseados que podrían ser utilizados por atacantes para acceder a su sistema.

El proyecto está diseñado de manera que sea fácil de usar para cualquier persona, incluso si no tiene experiencia en el escaneo de puertos. Todo lo que se necesita es ejecutar el script, ingresar la dirección IP que se desea escanear y esperar a que el escaneo se complete. El resultado del escaneo se mostrará en la pantalla, lo que permite a los usuarios ver rápidamente los puertos que están abiertos y cualquier conexión activa a través de esos puertos.

## 🎢 Características

- [x] Escaneo de todos los puertos disponibles.
- [x] Registro de todos los puertos abiertos y sus procesos asociados.
- [x] Indicador de progreso en tiempo real.
- [x] Opción para guardar los resultados en un archivo de registro.
- [x] Cálculo del tiempo total de escaneo.

## 🧪 Cómo ejecutar el proyecto?

Para usar este script, sigue los siguientes pasos:

Primero, debe crear un entorno virtual para el proyecto usando virtualenv. Esto es útil para aislar las dependencias del proyecto del sistema principal de Python. Para crear el entorno virtual, ejecute el siguiente comando en la terminal:

```bash
python -m venv env
```

Esto creará una carpeta llamada "env" en su directorio actual, que contendrá todas las dependencias del proyecto.

A continuación, debe activar el entorno virtual que acaba de crear. Dependiendo del sistema operativo que esté utilizando, deberá ejecutar uno de los siguientes comandos:

### Linux

```bash
source env/bin/activate
```

### Windows

```bash
env/Scripts/activate
```

Esto activará el entorno virtual y cambiará su prompt de la terminal para indicar que está en el entorno virtual. Ahora puede instalar los requerimientos del proyecto sin afectar su sistema principal de Python.

A continuación, debe instalar los requerimientos del proyecto en el entorno virtual. Para hacer esto, simplemente ejecute el siguiente comando en la terminal:

```bash
pip install -r requirements.txt
```

Esto instalará todas las dependencias necesarias para ejecutar el proyecto.

Finalmente, puede ejecutar el script principal del proyecto usando el siguiente comando:

```bash
python main.py
```

Esto iniciará el escaneo de puertos en su equipo y mostrará información sobre los procesos asociados a cada puerto abierto. Una vez que el escaneo haya finalizado, se mostrará un mensaje indicando que el proceso ha finalizado.

## 📑 Licence

<h3 align="center">MIT</h3>

---

<p align="center">
  <a href="https://github.com/EddyBel" target="_blank">
    <img alt="Github" src="https://img.shields.io/badge/GitHub-%2312100E.svg?&style=for-the-badge&logo=Github&logoColor=white" />
  </a> 
  <a href="https://www.linkedin.com/in/eduardo-rangel-eddybel/" target="_blank">
    <img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
  </a> 
</p>
