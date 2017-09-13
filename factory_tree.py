import random
import sys
import unittest
from tree import BinaryTree


class TreeFactory(object):
    """
    Factory class for creating tree objects from different types of inputs
    """

    @classmethod
    def build_from_list(cls, inlist=[]):
        """ Construct tree from given list. """

        tree = BinaryTree()
        for x in inlist:
            tree.build(val=x)

        return tree

    @classmethod
    def build_tree_random(cls, num_nodes, start=0, end=100):
        """Create random tree from given depth """

        tree = BinaryTree()
        for x in range(num_nodes):
            tree.build(val=random.randrange(start, end))

        return tree


if __name__ == "__main__":
    mytree = TreeFactory.build_from_list([10,4,5,3,6,9])
    print mytree
    mytree.display()
    filename1 = mytree.save()
    print 'Loading and displaying', filename1
    BinaryTree.load(filename1).display()

    mytree1 = TreeFactory.build_tree_random(5)
    print mytree1
    mytree1.display()
    filename2 = mytree1.save()
    print 'Loading and displaying', filename2
    BinaryTree.load(filename2).display()

    mytree2 = TreeFactory.build_tree_random(5)
    print mytree2
    mytree2.display()

    # Save it
    filename = mytree2.save()
    # Put state of mytree => mytree2
    mytree.update(filename)
    print mytree
    mytree.display()

    # import pdb; pdb.set_trace()
