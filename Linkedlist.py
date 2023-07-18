from Node import Node

# init, head node, insert data, printing data, remove node
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
        
    def get_head_node(self):
        return self.head_node
    
    def insert_data(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    # make a string to put data into, set up a variable starting from head node, work though the nodes till next node is null, add the value of current 
    # node to the string, and set node to next node
    def springify_list(self):
        springify = ""
        current_node = self.head_node
        while current_node:
            springify += str(current_node.value) + "\n"
            current_node = current_node.get_next_node()
        return springify        
        
    
    
    # remove node, set up a variable starting from head, if that variable is value to remove set head node to next node else
    # while theres nodes to explore set up a next node check that value if its the target value set current node to next next node else move current node along
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.next_node = next_node.get_next_node()
                    current_node = None
                else:
                    current_node = next_node
        