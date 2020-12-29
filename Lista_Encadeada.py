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
            return
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(data)
            return

        # if self.head:
        #     # inserção quando a lista já possui elementos
        #     current_node = self.head
        #     while current_node.next:
        #         current_node = current_node.next
        #     current_node.next = Node(data)
        # else:
        #     # primeira inserção
        #     self.head = Node(data)

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

        while current_node:
            nodes_list.append(current_node.data)
            current_node = current_node.next
        return nodes_list

    def get_by_index(self, index):
        current_node = self.head
        current_index = 0

        if index < 0 or index > len(self.list()):
            print("ERROR: 'Get' Index out of range!")
            return None

        if current_node is None:
            print("ERROR: 'Get' Index out of range!")

        while current_node:
            if current_index == index:
                return current_node.data
            current_node = current_node.next
            current_index += 1

    def get_by_value(self, value):
        current_node = self.head

        if current_node is None:
            print("List has no elements")

        while current_node:
            if current_node.data == value:
                print("Item found")
                return True
            current_node = current_node.next
        print("Item not found")
        return False


one = LinkedList()
print(one.list())
one.append(17)
one.append(2)
one.append(1)
one.append(24)
print(one.list())






