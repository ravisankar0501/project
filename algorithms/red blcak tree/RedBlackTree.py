import matplotlib.pyplot as plt
from pylab import rcParams

class TreeNode(object):
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left = left_child
        self.right = right_child
        self.color = 1  # 1 for red, 0 for black

    def traverse_infix(self, result=None):
        if result == None:
            result = []

        if self.left:
            self.left.traverse_infix(result)
        result.append(self.data)

        if self.right:
            self.right.traverse_infix(result)
        return result

# create a graphical representation of a binary tree (plot_tree, below, uses plot_node)
def plot_node(node, rb=True, level=1, posx=0, posy=0):
    width = 2000.0 * (0.5 ** (level))  # This will be used to space nodes horizontally
    if node.color == 0 or rb == False:
        plt.text(posx, posy, str(node.data), horizontalalignment='center', color='k', fontsize=10)
    else:
        plt.text(posx, posy, str(node.data), horizontalalignment='center', color='r', fontsize=10)
    if node.left:
        px = [posx, posx - width]
        py = [posy - 1, posy - 15]
        if node.left.color == 0 or rb == False:
            plt.plot(px, py, 'k-') #,hold=True)
        else:
            plt.plot(px, py, 'r-')#, hold=True)
        plot_node(node.left, rb, level + 1, posx - width, posy - 20)
    if node.right:
        plot_node(node.right, rb, level + 1, posx + width, posy - 20)
        px = [posx, posx + width]
        py = [posy - 1, posy - 15]
        if node.right.color == 0 or rb == False:
            plt.plot(px, py, 'k-')#, hold=True)
        else:
            plt.plot(px, py, 'r-')#, hold=True)

def plot_tree(node, figsize=(10, 6)):
    if node.color == 1:
        rb = False
    else:
        rb = True
    rcParams['figure.figsize'] = figsize
    fig, ax = plt.subplots()
    ax.axis('off')
    plot_node(node, rb)
    plt.show()

### Here is the LLRBT implementation.
class RBT(object):
    def __init__(self):
        """Initialize a red/black tree."""
        self.TNULL = TreeNode(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.tree = None

    def _find_node(self, node, obj):
        """Private function for traversing tree to lookup obj."""
        if node == None:
            return None
        if node.data == obj:
            return node
        if obj < node.data:
            return self._find_node(node.left, obj)
        else:  # so obj > node.data
            return self._find_node(node.right, obj)

    def is_element(self, obj):
        """Public function to lookup obj. Returns True iff obj is in tree."""
        node = self._find_node(self.tree, obj)
        if node:
            return True
        else:
            return False

    def _insert(self, node, obj, ):
        """Private function for traversing tree to insert obj. Perform color changes on the way down, and rotations on the way up, to preserve RBT properties."""
        # somewhat working version
        if node == None:
            return TreeNode(obj)  # If we've arrived at a terminus, then make new node.
        if obj < node.data:
            if node.left:
                self._insert(node.left, obj)
            else:
                node.left = TreeNode(obj)
            if self._isRed(node.left) and self._isRed(node.right):
                self._colorFlip(node)  # If both children are red, then colorflip

        elif obj > node.data:
            if node.right:
                self._insert(node.right, obj)
            else:
                node.right = TreeNode(obj)
            if self._isRed(node.left) and self._isRed(node.right):
                self._colorFlip(node)  # If both children are red, then colorflip

        return node


        #original code
        #if self._isRed(node.left) and self._isRed(node.right):
        #     self._colorFlip(node)  # If both children are red, then colorflip
        # if obj < node.data:
        #     node.left = self._insert(node.left, obj)
        # elif obj > node.data:
        #     node.right = self._insert(node.right, obj)
        # if self._isRed(node.right) and not self._isRed(node.left):
        #     node = self._rotateLeft(node)
        # if self._isRed(node.left) and self._isRed(node.left.left):
        #     node = self._rotateRight(node)
        # return node



    def insert(self, obj):
        """Public function to insert obj in tree."""
        #working and original
        if self.tree == None:
            self.tree = TreeNode(obj)
        else:
            self.tree = self._insert(self.tree, obj)
            self.tree.color = 0  # The root must always be black


    def _colorFlip(self, node):  # flip the colors of node and its children
        """Flip the color of node and its children. Used internally to preserve RBT properties."""
        node.color = 1 - node.color
        if node.left: node.left.color = 1 - node.left.color
        if node.right: node.right.color = 1 - node.right.color

    def _rotateRight(self, node):  # rotate right
        """Rotate node right, preserving RBT properties."""
        originalLeft = node.left
        node.left = originalLeft.right
        originalLeft.right = node
        originalLeft.color = node.color
        node.color = 1
        return originalLeft

    def _rotateLeft(self, node):  # rotate left
        """Rotate node left, preserving RBT properties."""
        originalRight = node.right
        node.right = originalRight.left
        originalRight.left = node
        originalRight.color = node.color
        node.color = 1
        return originalRight

    def _isRed(self, node):
        """Returns True iff node is red."""
        if node == None: return 0  # Nil nodes are black
        return (node.color == 1)

    def _delete_node(self, node, obj):
        """Private function for traversing tree to delete obj. Perform movements and rotations during traversal to preserve RBT properties."""
        if node == None: return node
        if obj < node.data:
            if node.left == None or (not self._isRed(node.left) and not self._isRed(node.left.left)):
                node = self._moveRedLeft(node)
            node.left = self._delete_node(node.left, obj)
        else:
            if self._isRed(node.left): node = self._rotateRight(node)
            if obj == node.data and node.right == None:
                return None
            if node.right == None or (not self._isRed(node.right) and not self._isRed(node.right.left)):
                node = self._moveRedRight(node)
            if obj == node.data:
                node.data = self._min(node.right)
                node.right = self._deleteMin(node.right)
            else:
                node.right = self._delete_node(node.right, obj)
        return self.fixUp(node)

    def _deleteMin(self, node):
        """Delete the minimum descendant of node. Performs movements during traversal to preserve RBT properties."""
        if node.left == None: return None
        if node.left == None or (not self._isRed(node.left) and not self._isRed(node.left.left)):
            node = self._moveRedLeft(node)
        node.left = self._deleteMin(node.left)
        return self.fixUp(node)

    def _min(self, node):
        """Return the data of the minimum descendant of node."""
        while node.left != None: node = node.left
        if node == None:
            return None
        else:
            return node.data

    def _moveRedLeft(self, node):
        """Moves red node left. Used internally to preserve RBT properties."""
        self._colorFlip(node)
        if node.right and self._isRed(node.right.left):
            node.right = self._rotateRight(node.right)
            node = self._rotateLeft(node)
            self._colorFlip(node)
        return node

    def _moveRedRight(self, node):
        """Moves red node right. Used internally to preserve RBT properties."""
        self._colorFlip(node)
        if node.left and self._isRed(node.left.left):
            node = self._rotateRight(node)
            self._colorFlip(node)
        return node

    def delete(self, obj):
        """Public function for deleting node containing obj."""
        if self.tree == None:
            return
        else:
            self.tree = self._delete_node(self.tree, obj)

    def fixUp(self, node):
        """Rotates and colorflips where necessary. Used internally to preserve RBT properties."""
        if self._isRed(node.right):
            node = self._rotateLeft(node)
        if self._isRed(node.left) and self._isRed(node.left.left):
            node = self._rotateRight(node)
        if self._isRed(node.left) and self._isRed(node.right):
            self._colorFlip(node)
        return node

# Testing out insert on the family tree from homework 9
people1 = [9,1,12,0,4,11,18,2,7,14,19,5,13,15]

rbt = RBT()
for p in people1:
    rbt.insert(p)
plot_tree(rbt.tree, figsize=(14,4))


rbt.insert(16)
plot_tree(rbt.tree, figsize=(14,4))

rbt.delete(1)
plot_tree(rbt.tree, figsize=(14,4))