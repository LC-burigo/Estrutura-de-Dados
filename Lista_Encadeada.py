class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # se não há nenhum nó, adicionar esta primeira data ao primeiro nó, que estará armazenado dentro do self.head
        if self.head is None:
            self.head = Node(data)

        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node = Node(data)

    def lenght(self):
        current_node = self.head

        node_size = 0
        if self.head is None:
            return node_size == 0




