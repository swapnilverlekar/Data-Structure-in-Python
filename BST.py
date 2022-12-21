class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #Function to add a child in the BST
    def insert_child(self, data):
        #check for duplicate entry
        if self.data == data:
            return
        if data < self.data:
            #add data to left subtree
            if self.left:
                self.left.insert_child(data)
            else:
                self.left = BST(data)
        else:
            #add data to right subtree
            if data > self.data:
                # add data to left subtree
                if self.right:
                    self.right.insert_child(data)
                else:
                    self.right = BST(data)

    #Inorder traversal in the created BST
    def inorder_traversal(self):
        elements = []
        #visit the left subtree
        if self.left:
            elements += self.left.inorder_traversal()
        #visit the base node
        elements.append(self.data)
        #visit the right subtree
        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    #finding the max element in the given BST
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    #finding the min element in the given BST
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    #delete a value in BST and replace with the max val in the Right subtree
    def delete_value(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_value(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_value(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_value(max_val)
        return self

#Function to Build the BST taking each element of the provided input list
def build_tree(elements):
    root = BST(elements[0])
    for i in range(1,len(elements)):
        root.insert_child(elements[i])
    return root




if __name__ == '__main__':
    print("******Binary Search Tree operations******")
    numbers = list(map(int,input("Enter tree elements seperated by comma:\t").split(',')))
    number_bst = build_tree(numbers)
    print("\nSelect operation\n1. Insert value to the BST\n2. Find the MAX element in BST\n3. Find the MIN element in BST\n4. Delete value from BST\n5. Print the BST\n6. Enter 0 to exit")
    n=10
    while (n!=0):
        n = int(input("Enter choice:\t"))
        if n==1:
            number_bst.insert_child(int(input("Enter the data:\t")))
            print("The Binary search tree elements in order are:\t",number_bst.inorder_traversal())
        elif n==2:
            print("Max node is:\t",number_bst.find_max())
        elif n==3:
            print("Min node is:\t", number_bst.find_min())
        elif n==4:
            number_bst.delete_value(int(input("Enter value to be removed from BST")))
            print("The New Binary search tree elements in order are:\t", number_bst.inorder_traversal())
        elif n==5:
            print("The Binary search tree elements in order are:\t",number_bst.inorder_traversal())



