# password-hash-checker

> Script educativo en Python que calcula y muestra los hash de una contraseña con varios algoritmos comunes (MD5, SHA-1, SHA-256).

---

## Índice

* [Qué hace](#qué-hace)
* [Requisitos](#requisitos)
* [Cómo ejecutarlo](#cómo-ejecutarlo)
* [Contenido (script)](#contenido-script)
* [Ejemplo de uso / salida](#ejemplo-de-uso--salida)
* [Limitaciones importantes](#limitaciones-importantes)
* [Aviso de seguridad y ética](#aviso-de-seguridad-y-ética)
* [Licencia](#licencia)

---

## Qué hace

Este pequeño script solicita al usuario una contraseña en texto plano y calcula su representación hash usando tres algoritmos comunes: **MD5**, **SHA-1** y **SHA-256**. Imprime en consola el nombre del algoritmo y el hash resultante. Es una herramienta **educativa** útil para ver cómo cambian los hashes según el algoritmo.

---

## Requisitos

* Python 3.x (cualquier versión moderna de Python 3 funcionará).
* No necesita librerías externas (usa la librería estándar `hashlib`).

---

## Cómo ejecutarlo

1. Guarda el script en un archivo, por ejemplo `password-hash-checker.py`.
2. Ejecuta desde la terminal:

```bash
python3 password-hash-checker.py
```

3. Cuando se te solicite, escribe la contraseña y presiona Enter.

---

## Contenido (script)

```python
import hashlib

password = input("Introduce una contraseña: ")

for algo in ['md5', 'sha1', 'sha256']:
    hash_value = getattr(hashlib, algo)(password.encode()).hexdigest()
    print(f"{algo.upper()}: {hash_value}")
```

---

## Ejemplo de uso / salida

Si introduces `contraseña123` como entrada, la salida será algo así (valores ilustrativos):

```
Introduce una contraseña: contraseña123

MD5: e99a18c428cb38d5f260853678922e03
SHA1: 7c222fb2927d828af22f592134e8932480637c0d
SHA256: ef92b778bafe771e89245b89ecbcf2a1f1f1f3a0d5f3b4d1a2e6a7b8c9d0e1f
```

---

## Limitaciones importantes

* **Uso educativo:** no está pensado para gestionar contraseñas reales en producción.
* **MD5 y SHA-1 no son seguros** para almacenamiento de contraseñas (son vulnerables a colisiones y ataques por fuerza/brute-force y tablas rainbow).
* El script **muestra** hashes en texto plano; no implementa salting, iteraciones (PBKDF2), hashing adaptativo (bcrypt/argon2) ni protección contra fugas.
* No hay validación de entrada ni manejo de excepciones especializadas.


---

## Aviso de seguridad y ética ⚠️

Usa este script solo con contraseñas tuyas o con permiso explícito. No utilices hashes para intentar vulnerar cuentas ajenas ni para compartir datos sensibles. Para almacenamiento real de contraseñas, emplea algoritmos diseñados para eso (bcrypt/argon2) y buenas prácticas de seguridad.

---

## Licencia

Usalo libremente para aprendizaje y pruebas. Si querés, agrego una cabecera con una licencia explícita (por ejemplo MIT). Indícame cuál preferís y la incluyo.
