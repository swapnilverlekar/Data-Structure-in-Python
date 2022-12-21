class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
        return

    def insert_value(self,dataList):
        self.head = None
        itr = self.head
        for i in dataList:
            self.insert_at_end(i)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index<0 or index>=ll.get_length():
            raise Exception("Index is not valid")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at_index(self, index, data):
        if index<0 or index>ll.get_length():
            raise Exception("invalid index")
            return
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def print(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        itr = self.head
        itrString = ''
        while itr:
            itrString+=str(itr.data)+"-->"
            itr = itr.next
        print("Current linked list:\t",itrString)


if __name__ == '__main__':
    print("******Linked List operations******")
    print("\nSelect operation\n1. Create a new Linked List using a list\n2. Insert at the begining\n3. Insert at the end\n4. Insert at a particular index\n5. Remove from a index\n6. Check length of the linked list\n7. Print the Linked List\n8. Enter 0 to exit")
    n=10
    ll = LinkedList()
    while (n!=0):
        n = int(input("Enter choice:\t"))
        if n==1:
            datalist = list(input("Enter the List:\t").split(','))
            ll.insert_value(datalist)
            ll.print()
        elif n==2:
            ll.insert_at_begining(input("Enter the data:\t"))
            ll.print()
        elif n==3:
            ll.insert_at_end(input("Enter the data:\t"))
            ll.print()
        elif n==4:
            ll.insert_at_index(int(input("Enter the index:\t")),input("Enter the data:\t"))
            ll.print()
        elif n==5:
            ll.remove_at(int(input("Enter the index from where the data needs to be removed:\t")))
            ll.print()
        elif n==6:
            print("Current Length of the Linked List is : ",ll.get_length())
        elif n==7:
            ll.print()
