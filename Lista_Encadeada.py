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
        node_size = 0
        current_node = self.head

        if current_node is None:
            return 0

        while current_node:
            node_size += 1
            current_node = current_node.next
        return node_size

    def list(self):
        nodes_list = []
        current_node = self.head

        if current_node is None:
            return []

        while current_node:
            nodes_list.append(current_node.data)
            current_node = current_node.next
        return nodes_list







