class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_data_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_data_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, value_list):
        for el in value_list:
            self.insert_data_end(el)
        return

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception('Index out of bound')
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            print('COUNT', count, '--DATA', itr.data)
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception('Index out of bound')
        
        if index == 0:
            self.head = Node(data, self.head)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            count += 1
            itr = itr.next
        
    def insert_value_after(self, bef_value, af_value):

        itr = self.head
        while itr:
            if itr.data == bef_value:
                itr.next = Node(af_value, itr.next)
                break
            
            itr = itr.next
    
    def remove_by_value(self, value):
        itr = self.head
        while itr:
            print(itr.data, itr.next.data)
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print(self):

        if self.head is None:
            print('blank')
            return
        dat = ''
        itr = self.head
        while itr:
            dat += str(itr.data) + ' >> '
            itr = itr.next
        print(dat)   

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_data_beginning('r')
    ll.insert_data_end('o')
    ll.insert_data_end('s')
    ll.insert_data_end('z')
    ll.insert_data_end('a')
    ll.insert_data_end('n')
    ll.print()
    ll.insert_value_after('r', 'xx')
    ll.print()
    # ll.remove_by_value('xx')
    # ll.remove_by_value('z')
    # ll.print()
    ll.print()
    ll.insert_value_after('s', 'h')
    ll.print()
    ll.remove_by_value('xx')
    ll.remove_by_value('z')
    ll.print()
    