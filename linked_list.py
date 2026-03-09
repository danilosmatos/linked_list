class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaLigada:
    def __init__(self):
        self.head = None

    def insert_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        # Se não tiver nada na lista
        if not self.head:
            self.head = new_node
            return
        # Se tiver
        old_node = self.head
        while old_node.next:
            old_node = old_node.next
        old_node.next = new_node

    def remove(self, value):
        # A lista está vazia
        if not self.head:
            print("Lista vazia.")
            return

        # O elemento a ser removido é a head
        if self.head.data == value:
            self.head = self.head.next
            return

        # Ta em outro lugar da lista
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        
        print(f"Valor {value} não encontrado na lista.")