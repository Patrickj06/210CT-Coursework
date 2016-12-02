#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)

def TreeSort(Nodes):
    t=tree_insert(None,Nodes[0])
    for i in range(1,len(Nodes)):
        tree_insert(t,Nodes[i])
    in_order(t)

'''
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right!=None):
        in_order(tree.right)
'''

def in_order(tree):
    '''Iterative function that traverses the graph in order
    '''
    Stack = []
    done = False
    while done != True:
        
        if tree != None:         #Finds the left most node 
            Stack.append(tree)   #Push node to stack 
            tree = tree.left     #Sets current node to the next left node  
            
        elif len(Stack)> 0:    #if the Stack is empty then break while loop
            tree = Stack[-1]   #Pops top of the stack 
            del Stack[-1]
            print(tree.value)#Prints the left most node 
            
            tree = tree.right#Checks for right node

        else:
            done = True

        
        

    
    
if __name__ == '__main__':
    TreeSort([6,10,5,2,3,4])
  
 
