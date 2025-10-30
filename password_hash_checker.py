#!/usr/bin/env python3
"""
password_hash_checker.py - Educational password hashing tool by Hersec Labs

Este script permite generar los hash de una contraseña utilizando distintos algoritmos.
Sirve para entender cómo funcionan las funciones hash (MD5, SHA1, SHA256, SHA512)
y cómo verificar coincidencias de hash de forma segura.

Uso educativo: No utilices este script para obtener o comparar hashes ajenos.
"""

import hashlib

def generar_hashes(password: str):
    algoritmos = ['md5', 'sha1', 'sha256', 'sha512']
    resultados = {}

    for algo in algoritmos:
        h = getattr(hashlib, algo)(password.encode()).hexdigest()
        resultados[algo.upper()] = h
    return resultados

def comparar_hash(password: str, hash_existente: str):
    """
    Compara si el hash de una contraseña coincide con un hash dado,
    detectando automáticamente el tipo de algoritmo si es posible.
    """
    for algo in ['md5', 'sha1', 'sha256', 'sha512']:
        generado = getattr(hashlib, algo)(password.encode()).hexdigest()
        if generado == hash_existente.lower():
            return f"Coincidencia con {algo.upper()}"
    return "❌ No coincide con ninguno de los algoritmos estándar."

if __name__ == "__main__":
    print("🔐 Hersec Password Hash Checker 🔐\n")
    password = input("Ingrese una contraseña: ")

    hashes = generar_hashes(password)
    for algo, valor in hashes.items():
        print(f"{algo}: {valor}")

    opcion = input("\n¿Desea comparar con un hash existente? (s/n): ").strip().lower()
    if opcion == 's':
        hash_existente = input("Ingrese el hash a comparar: ").strip()
        resultado = comparar_hash(password, hash_existente)
        print(f"\nResultado: {resultado}")
