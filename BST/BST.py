# python implementation of a binary search tree

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value = }"

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.insert_rec(self.root, value)

    def insert_rec(self, node, value):
        # if a spot is found insert the new node
        if node == None:
            return Node(value=value)

        # otherwise check whether the value is less or greater
        # than the current value, and insert recursively
        else:
            if value < node.value:
                # go left
                node.left = self.insert_rec(node.left, value)
            else:
                # go right
                node.right = self.insert_rec(node.right, value)
        return node
        
    # gets the min value in the BST
    # this is the left-most value
    def find_min(self, node) -> Node:
        while node.left != None:
            node = node.left
        return node

    def delete(self, value):
        # set the root to be the result of recursively deleting a value
        self.root = self.delete_rec(self.root, value)

    def delete_rec(self, node, value):
        # base case: node not found
        if node == None:
            return None

        # recursively search for the node
        if node.value != value:
            node.left = self.delete_rec(node.left, value)
            node.right = self.delete_rec(node.right, value)
            return node

        # case 1: 2 children
        # go on spot to the right first
        # then dfs to the left
        if node.right != None and node.left != None:
            new_node = node.right
            if new_node.left == None:
                # if you cant go left just promote the right node
                # by adding the left branch under new_node
                new_node.left = node.left
            
            else:
                # otherwise continues dfs'ing to the left
                # and add to branch under leftmost
                left_most = self.find_min(new_node)
                left_most = node.left
            return new_node
        
        # case 2: 0 or 1 children
        # returns None if not found
        # otherwise returns the child if there is 1
        else:
            if node.left != None:
                return node.left
            else:
                return node.right
        
    def balance(self):
        # store the elements of the bst in a sorted list
        # rebuild the tree by recursively inserting the middle element
        sorted_list = []
        self.store_in_order(self.root, sorted_list)
        self.root = self.build_balanced_tree(sorted_list, 0, len(sorted_list)-1)

    def store_in_order(self, node, unsorted_list):
        # use in order traversal to add node values to the list
        if node != None:
            self.store_in_order(node.left, unsorted_list)
            unsorted_list.append(node.value)
            self.store_in_order(node.right, unsorted_list)

    def build_balanced_tree(self, sorted_list, start, end):
        if start > end:
            return None
        
        # find the middle element and make it root
        mid = (start + end)//2
        node = Node(sorted_list[mid])

        # recusively build the left and right subtrees
        node.left = self.build_balanced_tree(sorted_list, start, mid-1)
        node.right = self.build_balanced_tree(sorted_list, mid + 1, end)
        return node


    def dfs(self, target_value) -> bool:
        return self.dfs_rec(self.root, target_value)

    def dfs_rec(self, node, target_value) -> bool:
        if node == None:
            return False
        
        # if the current node contains the target value, its found
        # otherwise continue rec search in left/right subtrees
        if node.value == target_value:
            return True
        elif target_value < node.value:
            return self.dfs_rec(node.left, target_value)
        else:
            return self.dfs_rec(node.right, target_value)

    def print_in_order_traversal(self):
        self.print_in_order_traversal_rec(self.root)

    def print_in_order_traversal_rec(self, node):
        # if not at a leaf node yet, search in order:
        # (left, node, right) traversal
        if node.left != None:
            self.print_in_order_traversal_rec(node.left)
        print(f"{node.value}")
        if node.right != None:
            self.print_in_order_traversal_rec(node.right)

    def print_tree(self):
        self.print_tree_rec(self.root, "", True)

    def print_tree_rec(self, node, indent, is_left):
        if node == None:
            return None
        
        # print the current node with indentation
        if is_left:
            print(f"{indent}L--- {node.value}")
        else:
            print(f"{indent}R--- {node.value}")

        # then recursively print left and right subtrees
        if is_left:
            indent_full = f"{indent}|   "
        else:
            indent_full = f"{indent}    "

        self.print_tree_rec(node.left, indent_full, True)
        self.print_tree_rec(node.right, indent_full, False)


# TESTING: 
# create BST and test methods:
bst = BST()
bst.insert(7)
bst.insert(4)
bst.insert(11)
bst.insert(2)
bst.insert(5)
bst.insert(1)
bst.insert(3)
bst.insert(10)
bst.insert(14)
bst.insert(9)
bst.print_tree()

# dfs search
print("DFS Search for 3: " + str(bst.dfs(3))) #true
print("DFS Search for 100: " + str(bst.dfs(100))) #false

# in order traversal
print("In-order Traversal: ")
bst.print_in_order_traversal()
print()

# deletion
bst.delete(3)
print("after deletion of 3: ")
bst.print_tree()

# in order traversal
print("In-order Traversal: ")
bst.print_in_order_traversal()
print()

# reset the tree to be unbalanced
# Balancing
bst = BST()
bst.insert(20)
bst.insert(10)
bst.insert(5)
bst.insert(11)
bst.insert(2)
bst.insert(8)
bst.insert(15)
bst.insert(14)
bst.insert(16)
bst.insert(13)
bst.insert(17)

print("unbalanced tree: ")
bst.print_tree()

# Balancing
bst.balance()
print("after balancing: ")
bst.print_tree()

# in order traversal
print("In-order Traversal: ")
bst.print_in_order_traversal()
print()
