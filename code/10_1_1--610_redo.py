"""
二叉查找树的实现
比父节点小的都在左子树，比父节点大的key都在右子树
类BST表示二叉树  TreeNode表示一个节点  BST的root引用根结点TreeNode
"""


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return self.parent and not self.hasAnyChildren()

    def hasAnyChildren(self):
        return self.hasLeftChild() or self.hasRightChild()

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for node in self.leftChild:
                    yield node
            yield self.key
            if self.hasRightChild():
                for node in self.rightChild:
                    yield node

    def findSuccessor(self):  # 找到比当前节点的key大的下一个节点，即右子树中最左边的节点
        return self.rightChild.findMinChild()

    def findMinChild(self):   # 找到最左边的子节点
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasLeftChild():
            if self.isLeftChild():
                self.parent.leftChild = self.leftChild
            else:
                self.parent.rightChild = self.leftChild
        else:
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.length()

    def put(self, key, val):  # 插入一个键值对
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node: TreeNode):  # put的辅助方法
        if key < current_node.key:
            if current_node.hasLeftChild():
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, val, parent=current_node)
        else:
            if current_node.hasRightChild():
                self._put(key, val, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, val, parent=current_node)

    def __setitem__(
        self, key, value
    ):  # 这样就不需要调用Put方法，而直接使用mytree[1] = 'red'来赋值
        self.put(key, value)

    def get(self, key):  # 取某个key的值
        res = self._get(key, self.root)
        if res:
            return res.payload
        else:
            return None

    def _get(self, key, current_node: TreeNode) -> TreeNode:
        if not current_node:
            return None
        elif key == current_node.key:
            return current_node
        elif key < current_node.key:
            if current_node.hasLeftChild():
                return self._get(key, current_node.leftChild)
        else:
            if current_node.hasRightChild():
                return self._get(key, current_node.rightChild)

    def __getitem__(self, key):  # 这样就不用get方法，直接使用mytree[3]来得到值
        return self.get(key)

    def __contains__(self, key):  # 这样可以直接使用key in mytree来得到该key是否在树里
        return bool(self._get(key, self.root))

    def __iter__(self):  # 迭代输出节点
        return self.root.__iter__()

    def delete(self, key):  # 删除一个节点
        if self.size > 1:
            nodeToDelete = self._get(key, self.root)
            if nodeToDelete:
                self._delete(nodeToDelete)
                self.size -= 1
            else:
                raise KeyError(f"Delete {key} failed, {key} not in tree")
        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(f"Delete {key} failed, {key} not in tree")

    def _delete(self, current_node: TreeNode):
        if current_node.isLeaf():
            if current_node.isLeftChild():
                current_node.parent.leftChild = None
            else:
                current_node.parent.rightChild = None
        elif current_node.hasBothChildren():
            succ = current_node.findSuccessor()
            succ.spliceOut()
            current_node.key, current_node.payload = succ.key, succ.payload
        else:
            if current_node == self.root:
                if current_node.hasLeftChild():
                    self.root = current_node.leftChild
                    self.root.parent = None
                if current_node.hasRightChild()():
                    self.root = current_node.rightChild
                    self.root.parent = None
            else:
                if current_node.isLeftChild() and current_node.hasLeftChild():
                    current_node.parent.leftChild = current_node.leftChild
                    current_node.leftChild.parent = current_node.parent
                elif current_node.isLeftChild() and current_node.hasRightChild():
                    current_node.parent.leftChild = current_node.rightChild
                    current_node.rightChild.parent = current_node.parent
                elif current_node.isRightChild() and current_node.hasLeftChild():
                    current_node.parent.rightChild = current_node.leftChild
                    current_node.leftChild.parent = current_node.parent
                elif current_node.isRightChild() and current_node.hasRightChild():
                    current_node.parent.rightChild = current_node.rightChild
                    current_node.rightChild.parent = current_node.parent

    def __delitem__(self, key):  # 这样就不用调用delete 直接用del mytree[3]来删除
        self.delete(key)


import unittest

class TestTreeNode(unittest.TestCase):
    def test_init(self):
        node = TreeNode(1, 'one', TreeNode(2, 'two'), TreeNode(3, 'three'), TreeNode(0, 'zero'))
        self.assertEqual(node.key, 1)
        self.assertEqual(node.payload, 'one')
        self.assertEqual(node.leftChild.key, 2)
        self.assertEqual(node.rightChild.key, 3)
        self.assertEqual(node.parent.key, 0)

    def test_has_children(self):
        node = TreeNode(1, 'one', TreeNode(2, 'two'), TreeNode(3, 'three'), TreeNode(0, 'zero'))
        self.assertTrue(node.hasLeftChild())
        self.assertTrue(node.hasRightChild())
        self.assertFalse(node.isLeaf())
        self.assertTrue(node.hasAnyChildren())
        self.assertTrue(node.hasBothChildren())

    def test_replace_node_data(self):
        node = TreeNode(1, 'one', TreeNode(2, 'two'), TreeNode(3, 'three'), TreeNode(0, 'zero'))
        node.replaceNodeData(4, 'four', TreeNode(5, 'five'), TreeNode(6, 'six'))
        self.assertEqual(node.key, 4)
        self.assertEqual(node.payload, 'four')
        self.assertEqual(node.leftChild.key, 5)
        self.assertEqual(node.rightChild.key, 6)
        self.assertEqual(node.parent.key, 0)

    def test_find_successor(self):
        node = TreeNode(1, 'one', TreeNode(2, 'two'), TreeNode(3, 'three'), TreeNode(0, 'zero'))
        successor = node.findSuccessor()
        self.assertEqual(successor.key, 3)

    def test_find_min(self):
        node = TreeNode(1, 'one', TreeNode(2, 'two'), TreeNode(3, 'three'), TreeNode(0, 'zero'))
        min_node = node.findMinChild()
        self.assertEqual(min_node.key, 2)


class TestBinarySearchTree(unittest.TestCase):
    def test_put_and_get(self):
        bst = BinarySearchTree()
        bst.put(1, 'one')
        bst.put(2, 'two')
        bst.put(3, 'three')
        self.assertEqual(bst.get(1), 'one')
        self.assertEqual(bst.get(2), 'two')
        self.assertEqual(bst.get(3), 'three')
        self.assertIsNone(bst.get(4))

    def test_set_and_get_item(self):
        bst = BinarySearchTree()
        bst[1] = 'one'
        bst[2] = 'two'
        bst[3] = 'three'
        self.assertEqual(bst[1], 'one')
        self.assertEqual(bst[2], 'two')
        self.assertEqual(bst[3], 'three')
        self.assertIsNone(bst.get(4))

    def test_contains(self):
        bst = BinarySearchTree()
        bst.put(1, 'one')
        bst.put(2, 'two')
        bst.put(3, 'three')
        self.assertIn(1, bst)
        self.assertIn(2, bst)
        self.assertIn(3, bst)

    def test_delete(self):
        bst = BinarySearchTree()
        bst.put(1, 'one')
        bst.put(2, 'two')
        bst.put(3, 'three')
        bst.delete(2)
        self.assertIsNone(bst.get(2))
        self.assertEqual(bst.get(1), 'one')
        self.assertEqual(bst.get(3), 'three')

    def test_delete_root(self):
        bst = BinarySearchTree()
        bst.put(1, 'one')
        bst.delete(1)
        self.assertIsNone(bst.root)

    def test_delete_not_found(self):
        bst = BinarySearchTree()
        bst.put(1, 'one')
        bst.put(2, 'two')
        with self.assertRaises(KeyError):
            bst.delete(3)

    def test_delete_item(self):
        bst = BinarySearchTree()
        bst.put(1, 'one')
        bst.put(2, 'two')
        bst.put(3, 'three')
        del bst[2]
        self.assertIsNone(bst.get(2))
        self.assertEqual(bst.get(1), 'one')
        self.assertEqual(bst.get(3), 'three')

    def test_iterator(self):
        bst = BinarySearchTree()
        bst.put(1, 'one')
        bst.put(2, 'two')
        bst.put(3, 'three')
        self.assertEqual(list(bst), [1, 2, 3])


if __name__ =='__main__':
    unittest.main()
