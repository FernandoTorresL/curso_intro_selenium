# Curso de Introduction a Selenium, Platzi, v2020

> Selenium es un framework de automatización de navegadores multilenguaje

<a href="https://github.com/FernandoTorresL/curso_intro_selenium/commits/master" target="_blank">![GitHub last commit](https://img.shields.io/github/last-commit/FernandoTorresL/curso_intro_selenium)</a> <a href="https://github.com/FernandoTorresL/curso_intro_selenium" target="_blank">![GitHub repo size](https://img.shields.io/github/repo-size/FernandoTorresL/curso_intro_selenium)</a>

---

## Descripción


Con Selenium podrás simular las acciones de tus usuarios dentro de aplicaciones web con fines de testing, generar los reportes correspondientes, automatizar tareas repetitivas e incluso extraer datos de la web. Cualquier acción humana puede ser replicada y serás capaz de programarla.

Link al [curso en Platzi](https://platzi.com/cursos/intro-selenium/)
Profesor: Héctor Vega Quiñones, [@TerragnigmArk](https://twitter.com/TerranigmArk)

En este curso aprenderemos:
- Sincronizar pruebas
- Interactuar con elementos
- Utilizar comandos básicos
- Preparar entorno de trabajo

## Instalación y setup

#### Verificar tu versión de Python
> Debes tener una versión >= 3.6
```sh
$ python3 --version
Python 3.8.9
```

#### Crear un ambiente virtual

OS X & Linux:

```sh
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

Windows:

```sh
$ python -m venv venv
$ .\venv\Scripts\activate
(venv) $
```

Con python3 instalado también puedes usar:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $
```
> El prompt puede variar si utilizas otro shell o configuración, como pk10 y zsh

Al finalizar, para cerrar el ambiente virtual:

OS X & Linux & Windows:

```sh
(venv) $ deactivate
$
```

#### Instalar lo necesario

Con el ambiente activo, utiliza:

OS X & Linux & Windows:

```sh
(venv) $ python -m pip install -r requirements.txt
```

### Ejecuta el primer ejemplo, hello.py

```sh
(venv) $ python hello.py
```
Si todo es correcto, se abrirá un navegador, verás que automáticamente visita un par de sitios, se cierra el browser y verás en terminal una salida similar a la siguiente:
```sh
(venv) $
Running tests...
----------------------------------------------------------------------

 test_hello_world (__main__.HelloWorld) ... OK (15.069140)s
 test_visit_wikipedia (__main__.HelloWorld) ... OK (1.880560)s

----------------------------------------------------------------------
Ran 2 tests in 21.682s

OK

Generating HTML reports...
Template is not specified, load default template instead.
Reports generated: /Users/.. ../hello-world-report.html
```

Ahora ya puedes probar todos los ejemplos contenidos en este repositorio. Si tienes algún problema, puedes contactarme e intentaremos resolverlo juntos.

## Contribuir

1. Haz Fork al projecto (<https://github.com/FernandoTorresL/curso_intro_selenium/fork>)
2. Crea tu rama feature (`git checkout -b feature/fooBar`)
3. Haz Commit a tus cambios (`git commit -am 'Add some fooBar'`)
4. Push a tu rama (`git push origin feature/fooBar`)
5. Crea un nuevo Pull Request
## Meta

<div align="center">
    <a href="https://fertorresmx.dev/">
      <img height="150em" src="https://raw.githubusercontent.com/FernandoTorresL/FernandoTorresL/main/media/FerTorres-dev1.png">
  </a>
</div>

#### :globe_with_meridians: [Twitter](https://twitter.com/FerTorresMx), [Instagram](https://www.instagram.com/fertorresmx/): @fertorresmx
