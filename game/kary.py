class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
class Queue():
    
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        insert_Node = Node(value)

        if self.is_empty():
            self.front = insert_Node
            self.rear = insert_Node
        else:
            self.rear.next = insert_Node
            self.rear = insert_Node

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        ret_val = self.front.value

        self.front = self.front.next

        return ret_val

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value


    def is_empty(self):
        if self.front is None:
            return True
        return False

class KaryNode(object):
    def __init__(self,value):
        self.value = value
        self.children = []

class KaryTree():
    def __init__(self,root = None):
        self.root = root

    

    def breadth_first(self):
        ret_val = []
        temp_q = Queue()
        temp_q.enqueue(self.root)
        current = temp_q.dequeue()
        while current:
            if current.children:
                for item in current.children:
                    temp_q.enqueue(item)
            ret_val.append(current.value)
            if temp_q.is_empty():
                current = None
            else:
                current = temp_q.dequeue()
        return ret_val
    
    
def fbt(kary):
    newTree = KaryTree()
    temp_q = Queue()
    temp_q.enqueue(kary.root)
    current = temp_q.dequeue()
    count = 0
    while current:
        if current.children:
            for item in current.children:
                temp_q.enqueue(item)
        if  not (current.value % 15):
             newNode = KaryNode('FizzBuzz') 
        elif not (current.value % 5):
             newNode = KaryNode('Buzz') 
        elif not (current.value % 3):
             newNode = KaryNode('Fizz') 
        else:
             newNode = KaryNode(f'{current.value}')
        if count < 1:
            newTree.root = newNode
        
        if temp_q.is_empty():
            current = None
        else:current = temp_q.dequeue()
        count += 1
    return kary.breadth_first()


if __name__=="__main__":
    # create nodes
    one = KaryNode(1)
    two = KaryNode(2)
    three = KaryNode(3)
    four = KaryNode(4)
    five = KaryNode(5)
    six = KaryNode(6)
    seven = KaryNode(7)
    eight = KaryNode(8)
    nine = KaryNode(9)
    ten = KaryNode(10)
    eleven = KaryNode(11)
    twelve = KaryNode(12)
    thirteen = KaryNode(13)
    fourteen = KaryNode(14)
    fifteen = KaryNode(15)

    #ones children
    one.children.append(two)
    one.children.append(three)
    one.children.append(five)

    #twos children
    two.children.append(four)
    two.children.append(seven)
    two.children.append(eight)
    two.children.append(eleven)
    two.children.append(thirteen)
    two.children.append(fourteen)
    two.children.append(fifteen)

    #threes children
    three.children.append(six)
    three.children.append(nine)
    three.children.append(twelve)

    #fives children
    five.children.append(ten)

    tree = KaryTree(one)

    print(fbt(tree))