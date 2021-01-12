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

    def __repr__(self):
        return "self.head:{}".format(self.head.data)

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

    # Desafios

    def display(self):
        contents = self.head
        # If the list is null
        if contents is None:
            print("List has no element")
        while contents:
            print(contents.data)
            contents = contents.next
        print("----------")

    def set_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def set_on_index(self, data, index):
        new_node = Node(data)

        if self.head is None:
            print("There is no nodes yet")
            return

        if index < 0 or index >= len(self.list()):
            print("ERROR: 'Set' Index out of range!")
            return None

        if index == 0:
            self.set_start(data)

        current_node = self.head
        i = 1
        while i != index and current_node is not None :
            current_node = current_node.next
            i += 1

        new_node.next = current_node.next
        current_node.next = new_node
        return

    def set_end(self, data):
        new_node = Node(data)
        current_node = self.head

        if current_node is None:
            current_node = new_node
            return

        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return

    def remove_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = None


one = LinkedList()
one.append(17)
one.append(2)
one.append(2)
one.append(1)
one.set_end(24)
one.set_on_index(6, 1)
print(one.display())
one.set_on_index(3, 2)
print(one.display())








