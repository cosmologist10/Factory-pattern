import json
import cPickle
import uuid

class Node(object):
    """ Return values of root, left, right andd level of tree. """

    def __init__(self, info):  # constructor of class
        self.info = info
        self.left = None
        self. right = None
        self.level = None

    def __str__(self):
        return str(self.info)  # return as string


class BinaryTree(object):
    """ Return add data,Search methods and Height of tree. """

    def __init__(self):  # constructor of class
        self.root = None

    def display(cosmo):
        """ Display the tree nicely """

        distance = cosmo.getHeight()*8
        cosmo._display(cosmo.root, distance=distance, count=1)

    def _display(self, node, distance=0, count=0):
        """ Display this node """

        print " "*distance,
        print  node.info
        if node.left != None:
            # Decrease distance
            node_distance = distance - count*5
            self._display(node.left, node_distance, count + 1)
        if node.right != None:
            node_distance = distance + count*5
            self._display(node.right, node_distance, count + 1)

    def build(self, val):
        """ Build binary tree search nodes step by step """

        if self.root is None:
            self.root = Node(val)

        else:
            current = self.root

            while True:

                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break

                elif val > current.info:

                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break

                else:
                    break

    def save(self):
        """ Serialising the tree and saves to a file """

        filename = uuid.uuid4().hex + '.pkl'
        cPickle.dump(self, file(filename, 'w'))
        print 'Tree is saved in',filename
        return filename

    @classmethod
    def load(cls, filename):
        """ Deserialises a previously saved tree and returns the object """

        return cPickle.load(open(filename))

    def update(self, filename):
        """ Loading and updating the state from a file """

        state = cPickle.load(open(filename))
        # Update self.__dict__ from it
        self.__dict__ = state.__dict__

    def preOrder(self, node):
        """ Return preorder traversal. """

        if node is not None:
            print (node.info)
            self.preorder(node.left)
            self.preorder(node.right)

    def inOrder(self, node):
        """ Return inorder traversal. """

        if node is not None:
            self.inorder(node.left)
            print (node.info)
            self.inorder(node.right)

    def postOrder(self, node):
        """ Return postorder traversal. """

        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print (node.info)

    def levelOrder(root):
        """ Return level order traversal """

        queue = []
        queue.append(root)
        while(len(queue) > 0):
            node = queue.pop(0)
            return node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def lookup(self, root, target):
        """looks for a value into the tree. """

        if root is None:
            return 0
        else:
            # if it has found it...
            if target == root.data:
                return 1
            else:
                if target < root.data:
                    # left side
                    return self.lookup(root.left, target)
                else:
                    # right side
                    return self.lookup(root.right, target)

    def minValue(self, root):
            """ Goes down into the left arm and returns the last value. """

            while(root.left is not None):
                root = root.left
            return root.data

    def _getHeight(self, node):
        """ Method for returning height. """

        if not node:
            return -1
        return 1 + max(self._getHeight(node.left), self._getHeight(node.right))

    def getHeight(self):
        """ Return height of tree. """

        return self._getHeight(self.root)


    def printTree(self, root):
        """prints the tree path. """

        if root is None:
            pass
        else:
            self.printTree(root.left)
            print root.data,
            self.printTree(root.right)

    def printRevTree(self, root):
        """ prints the tree path in reverse order. """

        if root is None:
            pass
        else:
            self.printRevTree(root.right)
            print root.data,
            self.printRevTree(root.left)
