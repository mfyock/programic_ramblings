"""
Architecture for creating linked lists
"""

class Node():
    """
    Primary component for a linked list

    Parameters:
        data (Required): Holds any datatype.  Default=None
        previous: Pointer to the previous Node in the linked list
        next: Pointer to the next node in linked list
    """

    def __init__(self, data=None):
        self.data = data
        self.previous = None
        self.next = None

class LinkedList():
    """
    Creates a linked list and provides means to manipulate and transform it

    Parameters:
        head (Required): Pointer to a Node instance
    """

    tail = None

    def __init__(self, head):
        self.head = head

    def append_node(self, node):
        """
        Appends a new node to end of the linked list

        Parameters:
            node (Required): Pointer to Node instance
        """

        if not isinstance(node, Node):
            raise 'Argument Error: must be instance of Node class'

        if not self.tail:
            # If the tail attribute doesn't exist, create it

            self.__setattr__('tail', node)
            self.head.next = node
            self.tail = node
            self.tail.previous = self.head

        else:
            # Set the current tail's 'next' attribute to the new Node instance
            self.tail.next = node

            # Declare a temporary variable to hold the current tail Node instance
            tmp_tail = self.tail

            # Set the current tail to the new tail Node instance
            self.tail = node

            # Set the new tail's 'previous' attribute to the tmp_tail variable
            self.tail.previous = tmp_tail

    def count_nodes(self):
        """
        Counts the nodes in the linked list
        """

        def traverse_list(node, count=1):
            """
            Traverses a linked list from head to tail
            """

            if node.next != None:
                return traverse_list(node.next, count+1)
            return count

        return traverse_list(self.head)

    def find_node(self, data):
        """
        Finds the location of a Node using the data stored within the Node instance

        Parameters:
            data (Required): data stored in a Node instance
        """

        def search_list(node, data):
            """
            Searches the linked list for stored data starting at the head
            """

            if node.data != data:
                return search_list(node.next, data)
            return node

        try:
            return search_list(self.head, data)
        except AttributeError:
            raise 'Unable to locate Node instance with stored data: {}'.format(data)

    def set_node_data(self, data_orig, data_new):
        """
        Finds the Node within a linked list and replaces the stored data with a new value

        Parameters:
            data_orig (Required): Original data stored in Node
            data_new (Required): New data that will replace original in Node
        """

        node = self.find_node(data_orig)

        node.data = data_new

    def declare_new_head(self, node):
        """
        Declares a new head to the linked list.

        Parameters:
            node (Required): New Node instance
        """

        if not isinstance(node, Node):
            raise 'Argument Error: must be instance of Node class'

        # Declare a temporary variable and store the current head of the linked list in it
        tmp_node = self.head

        # Set the 'previous' attribute of the current head to the new Node instance
        self.head.previous = node

        # Reset the head of the linked list to the new Node instance
        self.head = node

        # Set the 'next' attribute of the new Node instance to the temporary node variable
        self.head.next = tmp_node

        # If the linked list does not include a tail, declare it as the temporary node
        if not self.tail:
            self.tail = tmp_node

    def remove_node(self, data):
        """
        Removes a Node from the linked list using the data stored in the instance

        Parameters:
            data (Required): data stored in Node instance
        """
        
        rNode = self.find_node(data)

        previousNode = rNode.previous
        nextNode = rNode.next

        nextNode.previous = previousNode
        previousNode.next = nextNode

        del rNode
    
    def insert_node(self, node, **kwargs):
        # TODO Create function to insert node into linked list using 'location' kwarg
        # kwargs['location'] == 'before' or kwargs['location'] == 'after'
        pass
    
    def reverse_linked_list(self):
        previousN = None
        currentN = self.head
        while currentN is not None:
            nextNode = currentN.next
            currentN.next = previousN
            previousN = currentN
            currentN = nextNode
        self.head = previousN
    
    def print_nodes(self):
        n = self.head
        while n.next:
            print(n)
            n = n.next