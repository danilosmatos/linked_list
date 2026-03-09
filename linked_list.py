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
        if not self.head:
            self.head = new_node
            return
        old_node = self.head
        while old_node.next:
            old_node = old_node.next
        old_node.next = new_node

    def remove_data(self, valor):
        atual = self.head
        last = None

        while atual:
            if atual.dado == valor:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.head = atual.proximo
                return True  # Removido com sucesso
            anterior = atual
            atual = atual.proximo
        return False  # Valor não encontrado
