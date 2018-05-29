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

    def delete(self, val):
        self.root = BinarySearchTree.__delete(self.root, val)

    def __delete(root, val):

        def minValueNode(node):
            current = node

            # loop down to find the leftmost leaf
            while current.left is not None:
                current = current.left

            return current

        if root is None:
            return None

        if val < root.getVal():
            root.setLeft(BinarySearchTree.__delete(root.getLeft(), val))

        elif val > root.getVal():
            root.setRight(BinarySearchTree.__delete(root.getRight(), val))

        else:
            if root.getLeft() is None:
                temp = root.getRight()
                return temp
            elif root.getRight() is None:
                temp = root.getLeft()
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

    def levelorderwithlevels(self):
        thelist = []
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            x = queue.dequeue()
            if x is not None:
                thelist.append(x.getVal())
                queue.enqueue(x.getLeft())
                queue.enqueue(x.getRight())
            else:
                thelist.append(None)
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

        xinit = 150
        yinit = 280
        xratio = 0
        yratio = 0
        cv = ScrolledCanvas(self, 600, 600, 600, 600)
        cv.pack(side=tkinter.LEFT)
        t = RawTurtle(cv)
        screen = t.getscreen()
        screen.tracer(100000)

        screen.setworldcoordinates(screenMin, screenMin, screenMax, screenMax)
        screen.bgcolor("white")
        # t.hideturtle()

        frame = tkinter.Frame(self)
        frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        tree = BinarySearchTree()

        def insertHandler():
            node = int(nodeInput.get())
            tree.insert(node)
            t.clear()
            redraw()

        def deleteHandler():
            node = int(nodeInput.get())
            tree.delete(node)
            t.clear()
            redraw()

        def containsHandler():
            node = nodeInput.get()
            if node in tree:
                tkinter.messagebox.showwarning("Search Results", "Item is in tree!")
            else:
                tkinter.messagebox.showwarning("Search Results", "Item is NOT in tree!")

        def quitHandler():
            self.master.quit()

        def drawline(x0, y0, x1, y1):
            t.goto(x0, y0)
            t.down()
            t.goto(x1, y1)
            t.up()

        def redraw():
            lst = tree.levelorderwithlevels()
            lev0 = []
            lev1 = []
            lev2 = []
            lev3 = []
            lev4 = []
            lev5 = []
            lev6 = []
            middle = 150
            print(lst)
            for i in range(len(lst)):
                if len(lev0) < 1:
                    lev0.append(lst[i])
                elif len(lev1) < 2:
                    lev1.append(lst[i])
                elif len(lev2) < 4:
                    lev2.append(lst[i])
                elif len(lev3) < 8:
                    lev3.append(lst[i])
                elif len(lev4) < 16:
                    lev4.append(lst[i])
                elif len(lev5) < 32:
                    lev5.append(lst[i])
                elif len(lev6) < 64:
                    lev6.append(list[i])
            for x in lev0:
                t.goto(150, 260)
                t.write(x, False)
            for i in range(len(lev1)):
                if lev1[i] is not None:
                    drawline(150, 260, (i+1)*100, 220)
                    t.goto((i + 1) * 100, 220)
                    t.write(lev1[i], False)
            for i in range(len(lev2)):
                if lev2[i] is not None:
                    t.goto((i+1)*60, 180)
                    t.write(lev2[i], False)
            for i in range(len(lev3)):
                if lev3[i] is not None:
                    t.goto((i+1)*33, 140)
                    t.write(lev3[i], False)
            for i in range(len(lev4)):
                if lev4[i] is not None:
                    t.goto((i+1)*17, 100)
                    t.write(lev4[i], False)
            for i in range(len(lev5)):
                if lev5[i] is not None:
                    t.goto((i+1)*9, 60)
                    t.write(lev5[i], False)
            for i in range(len(lev6)):
                if lev6[i] is not None:
                    t.goto((i+1)*4, 20)
                    t.write(lev6[i], False)



            # yratio = xratio = 0
            # t.goto(xinit, yinit)
            # lst = tree.levelorder()
            # root = lst[0]
            # t.write(root, False)
            # for i in range(1, len(lst)):
            #     if lst[i] < lst[i-1]:
            #         xratio -= 1
            #         t.goto(120, 300 - ((yratio+1) * 20))
            #         t.write(lst[i], False)
            #
            #     elif lst[i] > lst[i-1]:
            #         yratio += 1
            #         xratio += 1
            #         t.goto(180, 300 - ((yratio+1) * 20))
            #         t.write(lst[i], False)




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
