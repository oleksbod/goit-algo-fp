class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Метод для вставки в початок списку
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Метод для вставки в кінець списку
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Метод для вставки після вказаного вузла
    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Метод для видалення вузла зі списку за заданим ключем
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    # Метод для пошуку елемента в списку
    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    # Метод для виводу списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Функція для реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Функція сортування списку методом злиття (merge sort)
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head
        mid = self._get_middle(self.head)
        left_half = LinkedList()
        right_half = LinkedList()
        left_half.head = self.head
        right_half.head = mid.next
        mid.next = None
        left_half.merge_sort()
        right_half.merge_sort()
        self.head = self._merge(left_half.head, right_half.head)

    def _get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.data < right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)
        return result

    # Функція для об'єднання двох відсортованих списків
    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        current_self = self.head
        current_other = other_list.head
        while current_self and current_other:
            if current_self.data < current_other.data:
                merged_list.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                merged_list.insert_at_end(current_other.data)
                current_other = current_other.next
        while current_self:
            merged_list.insert_at_end(current_self.data)
            current_self = current_self.next
        while current_other:
            merged_list.insert_at_end(current_other.data)
            current_other = current_other.next
        return merged_list
    

# Приклад використання:
llist1 = LinkedList()
llist1.insert_at_end(3)
llist1.insert_at_end(1)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(4)
llist2.insert_at_end(2)
llist2.insert_at_end(6)

print('Список 1:')
llist1.merge_sort()
llist1.print_list()  # Виведе відсортований список [1, 3, 5]

print('Список 2:')
llist2.merge_sort()
llist2.print_list()  # Виведе відсортований список [2, 4, 6]

print('Обєднаний список:')
merged_list = llist1.merge_sorted_lists(llist2)
merged_list.print_list()  # Виведе відсортований список [1, 2, 3, 4, 5, 6]