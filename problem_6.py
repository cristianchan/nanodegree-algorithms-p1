class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    llist1_count = generate_map(llist_1)
    union_list = LinkedList();
   
    llist_1_node = llist_1.head;
    while llist_1_node:
        union_list.append(llist_1_node.value)
        llist_1_node = llist_1_node.next 
    
    llist_2_node = llist_2.head;
    while(llist_2_node):
        if llist_2_node.value not in llist1_count:
            union_list.append(llist_2_node.value)
        elif llist_2_node.value in llist1_count and llist1_count.get(llist_2_node.value) == 0:
            union_list.append(llist_2_node.value)
        elif llist_2_node.value in llist1_count and llist1_count.get(llist_2_node.value) > 0:
            llist1_count[llist_2_node.value] = llist1_count.get(llist_2_node.value) - 1
        llist_2_node = llist_2_node.next   

    return union_list

def intersection(llist_1, llist_2):
    llist1_count = generate_map(llist_1)
    intersection_list = LinkedList();
    llist_2_node = llist_2.head;

    while(llist_2_node):
        if llist_2_node.value in llist1_count and llist1_count.get(llist_2_node.value) > 0:
            intersection_list.append(llist_2_node.value)
            llist1_count[llist_2_node.value] = llist1_count.get(llist_2_node.value) - 1
        llist_2_node = llist_2_node.next

    return intersection_list
   
def generate_map(llist):
    nums_count = dict({})
    llist_node = llist.head
    while(llist_node):
        nums_count[llist_node.value] = nums_count.get(llist_node.value,0) + 1
        llist_node = llist_node.next
    return nums_count



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4]
element_2 = [1,7,8]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

#3->2->4->1->7->8->
print (union(linked_list_3,linked_list_4))
#empty
print (intersection(linked_list_3,linked_list_4))


# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4]
element_2 = [1,7,8,2,2]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

#3->2->4->1->7->8->2->
print (union(linked_list_3,linked_list_4))
#2->
print (intersection(linked_list_3,linked_list_4))


# Test case 4

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4]
element_2 = [1,7,8,2,2,4,3]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

#3->2->4->1->7->8->2->
print (union(linked_list_3,linked_list_4))
#2->4-3->
print (intersection(linked_list_3,linked_list_4))