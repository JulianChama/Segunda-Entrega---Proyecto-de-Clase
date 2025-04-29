from bigtree import Node, find_name, find_path

class SistemaRutas:
    def __init__(self):
        self.root = Node("Central")  # raiz del arbol
    
    def agregar_parada(self, nombre, padre=None, distancia=0):
        if not padre:
            padre = self.root
        new_node = Node(nombre, parent=padre)
        new_node.distancia = distancia  # añadido aparte, no en el constructor
        return new_node

    def buscar_parada(self, nombre):
        result = find_name(self.root, nombre)
        if not result:
            print("Parada no encontrada")
        return result

    def encontrar_ruta(self, inicio, fin):
        nodo_inicio = self.buscar_parada(inicio)
        nodo_fin = self.buscar_parada(fin)
        if not nodo_inicio or not nodo_fin:
            return None
        
        path = find_path(nodo_inicio, nodo_fin)
        if path:
            return [nodo.name for nodo in path]
        return None

    def mostrar_arbol(self):
        for node in self.root.descendants:
            print(f"{node.name} (Distancia: {getattr(node, 'distancia', 'N/A')})")

# ejemplo:
if __name__ == "__main__":
    sistema = SistemaRutas()
    
    # agregar paradas
    parada_a = sistema.agregar_parada("Parada A", distancia=5)
    parada_b = sistema.agregar_parada("Parada B", padre=parada_a, distancia=3)
    sistema.agregar_parada("Parada C", distancia=7)  

    # mostrar arbol 
    sistema.mostrar_arbol()

    # buscar ruta
    ruta = sistema.encontrar_ruta("Parada B", "Parada C")
    print(f"\nRuta encontrada: {ruta}")