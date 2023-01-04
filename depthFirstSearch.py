# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space where v are the number of vertices and e is the number of edges
    def depthFirstSearch(self, array):
        '''This algorithm will do deep by looking at the vertex children starting from the left then
        moving to the right of the graph when a vertex does not have any edges'''
        # append the first (root) vertex to empty array
        array.append(self.name)
        # traverse through list of children and call depthFirstSearch recursively on that vertex
        # which will append said vertex to array and repeat process
        for child in self.children:
            child.depthFirstSearch(array)
        return array
