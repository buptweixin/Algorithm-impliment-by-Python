#encoding=utf-8
__author__ = 'weixin'

########################################################
'''
查找二叉树： 左子树所有节点均不大于根节点，右子树所有节点均不小于根节点的不完全二叉树
与最小堆得区别：最小堆没有要求左堆小于右堆，且堆必须是完全二叉树
Search Minimum Maximum Successor Predecessor 的复杂度为O(h)
中序遍历的复杂度为O(n)
'''
########################################################

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.p = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def TreeInsert(self, node):
        '''
        y指针始终指向x的父节点
        '''
        y = None
        x = self.root
        while x != None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.p = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def TreeDelete(self, node):
        '''
        1st step: 将y指向将要被删除的结点(若node结点有一个子女或没有子女则y指向其本身， 若node有两个子女则指向node的后继结点)
        2nd step: 将x指向y的子女或None
        3rd step: 通过修改y.p和x将y删除
        4th step: 如果删除的是node的后继节点，则将y的值复制到node中
        :param node: 将要删除的结点
        :return:被删除的结点
        '''
        if node.left == None or node.right == None:
            y = node
        else:
            y = self.TreeSuccessor(node)
        if y.left != None:
            x = y.left
        else:
            x = y.right
        if x != None:
            x.p = y.p
        if y.p == None: #若是根节点
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        if y != node:
            node.key = y.key
            node.value = y.value
        return y
    #####
    #   前趋与后继： O(h)
    #####
    #后继：大于node节点的最小节点
    def TreeSuccessor(self, node):
        if node.right != None:
            node = self.TreeMinimum(node.right)
        return node
    #前趋： 小于node节点的最大节点
    def TreePredecessor(self, node):
        if node.left != None:
            node = self.TreeMaximum(node.left)
        return node

    # 最大和最小
    ## 非递归法
    def TreeMinimum(self, node):
        while node.left != None:
            node = node.left
        return node

    def TreeMaximum(self, node):
        while node.right != None:
            node = node.right
        return node
    ## 递归法
    def RecursionTreeMinimum(self, node):
        if node.left != None:
            return self.RecursionTreeMinimum(node.left)
        return node

    def RecursionTreeMaximum(self, node):
        if node.right != None:
            return self.RecursionTreeMaximum(node.right)
        return node

    #########
    #   查找
    #########

    # 查找递归版本
    def TreeSearch(self, node, k):
        if node == None or k == node.key:
            return node
        elif k < node.key:
            return self.TreeSearch(node.left, k)
        else:
            return self.TreeSearch(node.right, k)
    # #非递归版本
    # def IterativeTreeSearch(self, node, k):
    #     while k != node.key and node != None:
    #         if k < node.key: node = node.left
    #         else: node = node.right
    #     return node


    #########
    #   遍历
    #########

    # 中序遍历
    def InOrderTreeWalk(self, node):
        if node != None:
            self.InOrderTreeWalk(node.left)
            print node.key
            self.InOrderTreeWalk(node.right)


if __name__ == '__main__':
    key = raw_input("Please input key:")
    value = raw_input("Please input value:")
    bst = BST()

    while value != 'Q':
        node = Node(key, value)
        bst.TreeInsert(node)
        key = raw_input("Please input key:")
        value = raw_input("Please input value:")
    bst.InOrderTreeWalk(bst.root)














