from binarytreevis import *
import unittest


class Asg3Tests(unittest.TestCase):
    def test_binsearchtree_constructor1(self):
        bt1 = BinarySearchTree(contents=[0, 1, 2, 5, 90, -1])
        bt2 = BinarySearchTree(contents=[0, 1, 2, 5, 90, -1])

        self.assertListEqual(bt1.inorder(), bt2.inorder())
        self.assertListEqual(bt1.preorder(), bt2.preorder())
        self.assertListEqual(bt1.postorder(), bt2.postorder())
        self.assertListEqual(bt1.levelorder(), bt2.levelorder())

    def test_binsearchtree_inorder1(self):
        bt = BinarySearchTree(contents=[0, -1, 1])
        self.assertListEqual(bt.inorder(), [-1, 0, 1])

    def test_binsearchtree_preorder1(self):
        bt = BinarySearchTree(contents=[2, 0, 1])
        self.assertListEqual([2, 0, 1], bt.preorder())

    def test_binsearchtree_postorder1(self):
        bt = BinarySearchTree(contents=[2, 0, 1])
        self.assertListEqual([1, 0, 2], bt.postorder())

    def test_binsearchtree_levelorder1(self):
        bt = BinarySearchTree(contents=[2, 0, 1, 6, 10])
        self.assertListEqual([2, 0, 6, 1, 10], bt.levelorder())

    def test_binsearchtree_insert1(self):
        bt = BinarySearchTree()
        bt.insert(0)
        bt.insert(-1)
        bt.insert(1)
        self.assertListEqual(bt.inorder(), [-1, 0, 1])

    def test_binsearchtree_delete1(self):
        bt = BinarySearchTree(contents=[0, 1, 2])
        bt.delete(0)
        self.assertListEqual(bt.inorder(), [1, 2])

    def test_binsearchtree_contains1(self):
        bt = BinarySearchTree(contents=[0, 1, 2])
        self.assertTrue(0 in bt)
        bt.delete(0)
        self.assertFalse(0 in bt)


if __name__ == '__main__':
    unittest.main()
