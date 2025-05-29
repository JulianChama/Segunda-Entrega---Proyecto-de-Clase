# Segunda-Entrega---Proyecto-de-Clase
Entrega segundo informe  Esteban Figueroa - 2190057 / Jhoan Sebastian Barreto Villamizar - 2203045 / Julian David Vargas Gomez 2221885 / David Andres Parra Leiva 2230047
Esta vez, al estar basado en un sistema de árboles y gracias al cambio de sistema de organizacion de datos ahora se presenta menos limitación para añadir paradas. Antes solo se podian añadir paradas al inicio de la ruta, pero ahora gracias al sistema de árboles se pueden crear varias ramas de rutas de transporte. Se aprovecharon las librerías de BigTree y sus herramientas para esta implementacion.
# Entrega Final ---Proyecto-de-Clase
Entrega ultimo informe  Esteban Figueroa - 2190057 / Jhoan Sebastian Barreto Villamizar - 2203045 / Julian David Vargas Gomez 2221885 / David Andres Parra Leiva 2230047
Este proyecto desarrolla un sistema de gestión de rutas de transporte público, evolucionando desde listas enlazadas (rutas lineales) hasta grafos (redes complejas con distancias). El objetivo es comparar cómo cada estructura de datos (listas, árboles, grafos) representa y optimiza las conexiones entre paradas. La primera entrega modela rutas secuenciales, la segunda introduce ramificaciones con árboles, y la tercera permite conexiones cruzadas y rutas ponderadas con grafos. El análisis final determina qué estructura es más eficiente para diferentes escenarios de transporte.

class GrafoRutas:
def _init_(self):
self.grafo = {} # Diccionario de adyacencia
self.distancias = {} # Diccionario para guardar distancias entre pares de nodos

def agregar_parada(self, nombre):
if nombre not in self.grafo:
self.grafo[nombre] = []

def conectar_paradas(self, origen, destino, distancia):
self.agregar_parada(origen)
self.agregar_parada(destino)

self.grafo[origen].append(destino)
self.grafo[destino].append(origen)

self.distancias[(origen, destino)] = distancia
self.distancias[(destino, origen)] = distancia

def buscar_ruta(self, inicio, fin):
from collections import deque

visitados = set()
cola = deque([[inicio]])

while cola:
ruta = cola.popleft()
nodo = ruta[-1]
if nodo == fin:
return ruta

if nodo not in visitados:
visitados.add(nodo)
for vecino in self.grafo.get(nodo, []):
nueva_ruta = list(ruta)
nueva_ruta.append(vecino)
cola.append(nueva_ruta)
return None

def mostrar_grafo(self):
for nodo, vecinos in self.grafo.items():
conexiones = ", ".join(f"{v} ({self.distancias.get((nodo, v), '?')} km)" for v in vecinos)
print(f"{nodo} -> {conexiones}")

if _name_ == "_main_":
sistema = GrafoRutas()

sistema.conectar_paradas("Central", "Parada A", 5)
sistema.conectar_paradas("Parada A", "Parada B", 3)
sistema.conectar_paradas("Central", "Parada C", 7)

sistema.mostrar_grafo()

ruta = sistema.buscar_ruta("Parada B", "Parada C")
print(f"\nRuta encontrada: {ruta}")
