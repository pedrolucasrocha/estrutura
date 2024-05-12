class Node:
    def __init__(self, qtd, preco, descricao):
        self.qtd = qtd
        self.preco = preco
        self.descricao = descricao
        self.next = None

class OrdenedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def insert(self, qtd, preco, descricao):
        new_node = Node(qtd, preco, descricao)

        if self.is_empty() or descricao <= self.head.descricao:
            new_node.next = self.head 
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.descricao < descricao:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def search(self, descricao):
        current = self.head
        while current is not None and current.descricao <= descricao:
            if current.descricao == descricao:
                return current
            current = current.next
        return None
    
    def remove(self, descricao):
        if self.is_empty():
            return None
    
        if self.head.descricao == descricao:
            removed_node = self.head
            self.head = self.head.next
            return removed_node
        
        current = self.head
        while current.next is not None and current.next.descricao < descricao:
            current = current.next
        
        if current.next is None or current.next.descricao > descricao:
            return None
        
        removed_node = current.next
        current.next = current.next.next
        return removed_node

    def display(self):
        if self.is_empty():
            print("A lista ordenada está vazia!")
        else:
            current = self.head
            while current:
                print(f"Qtd: {current.qtd}, Preço: {current.preco}, Descrição: {current.descricao}")
                current = current.next
