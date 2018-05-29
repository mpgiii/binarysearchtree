from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime
import time
import sys

from queue import *

screenMin = 0
screenMax = 300


class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class. 
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
        def getVal(self):
            return self.val
        
        def setVal(self, newval):
            self.val = newval
            
        def getLeft(self):
            return self.left
        
        def getRight(self):
            return self.right
        
        def setLeft(self, newleft):
            self.left = newleft
            
        def setRight(self, newright):
            self.right = newright
            
        # This method deserves a little explanation. It does an inorder traversal
        # of the nodes of the tree yielding all the values. In this way, we get
        # the values in ascending order.
        def __iter__(self):
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right is not None:
                for elem in self.right:
                    yield elem

        def inorder(self):
            res = []
            if self.left is not None:
                res = res + self.left.inorder()
            res.append(self.getVal())
            if self.right is not None:
                res = res + self.right.inorder()
            return res

        def preorder(self):
            res = []
            res.append(self.getVal())
            if self.left is not None:
                res = res + self.left.preorder()
            if self.right is not None:
                res = res + self.right.preorder()
            return res

        def postorder(self):
            res = []
            if self.left is not None:
                res = res + self.left.postorder()
            if self.right is not None:
                res = res + self.right.postorder()
            res.append(self.getVal())
            return res

        def __repr__(self):
            return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            
            
    # Below are the methods of the BinarySearchTree class. 
    def __init__(self, root=None, contents=None):
        self.root = root
        if contents is not None:
            for x in contents:
                self.insert(x)
        
    def insert(self, val):
        self.root = BinarySearchTree.__insert(self.root, val)
        
    def __insert(root, val):
        if root is None:
            return BinarySearchTree.Node(val)
        
        if val < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(), val))
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(), val))
            
        return root

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    def delete(self, val):
        self.root = BinarySearchTree.__delete(self.root, val)

    def __delete(root, val):
        if root is None:
            return None

        if val < root.getVal():
            root.setLeft(BinarySearchTree.__delete(root.getLeft(), val))

        elif val > root.getVal():
            root.setRight(BinarySearchTree.__delete(root.getRight(), val))

        else:
            if root.getLeft() is None:
                temp = root.getRight()
                root = None
                return temp
            elif root.getRight() is None:
                temp = root.getLeft()
                root = None
                return temp

            temp = minValueNode(root.getRight())
            root.setVal(temp.getVal())
            root.setRight(BinarySearchTree.__delete(root.getRight(), val))

        return root

    def __iter__(self):
        if self.root is not None:
            return iter(self.root)
        else:
            return iter([])

    def inorder(self):
        if self.root is not None:
            return list(self.root.inorder())
        else:
            return list(self.root.inorder())

    def preorder(self):
        if self.root is not None:
            return list(self.root.preorder())
        else:
            return list(self.root.preorder())

    def postorder(self):
        if self.root is not None:
            return list(self.root.postorder())
        else:
            return list(self.root.postorder())

    def levelorder(self):
        thelist = []
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            x = queue.dequeue()
            thelist.append(x.getVal())
            if x.getLeft() is not None:
                queue.enqueue(x.getLeft())
            if x.getRight() is not None:
                queue.enqueue(x.getRight())
        return thelist


    def __str__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"


class Visualization(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.paused = False
        self.stop = False
        self.running = False
        self.locked = False

    def buildWindow(self):

        cv = ScrolledCanvas(self, 600, 600, 600, 600)
        cv.pack(side=tkinter.LEFT)
        t = RawTurtle(cv)
        screen = t.getscreen()
        screen.tracer(100000)

        screen.setworldcoordinates(screenMin, screenMin, screenMax, screenMax)
        screen.bgcolor("white")
        t.ht()

        frame = tkinter.Frame(self)
        frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        tree = BinarySearchTree()

        def insertHandler():
            node = nodeInput.get()
            tree.insert(node)

        def deleteHandler():
            node = nodeInput.get()
            tree.delete(node)

        def containsHandler():
            node = nodeInput.get()
            if node in tree:
                tkinter.messagebox.showwarning("Search Results", "Item is in tree!")
            else:
                tkinter.messagebox.showwarning("Search Results", "Item is NOT in tree!")

        def quitHandler():
            self.master.quit()

        quitButton = tkinter.Button(frame, text="Quit", command=quitHandler)
        quitButton.pack()

        text = tkinter.Label(frame, text="Node Value:")
        text.pack()

        nodeInput = tkinter.Entry(frame, width=20)
        nodeInput.pack()

        insertButton = tkinter.Button(frame, text="Insert", command=insertHandler)
        insertButton.pack()

        deleteButton = tkinter.Button(frame, text="Remove", command=deleteHandler)
        deleteButton.pack()

        containsButton = tkinter.Button(frame, text="Contains?", command=containsHandler)
        containsButton.pack()


def main():
    root = tkinter.Tk()
    root.title("Binary Tree Visualization")
    application = Visualization(root)
    application.mainloop()


if __name__ == "__main__":
    main()
