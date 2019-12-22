def compt_carac(texte):
    carac = {}
    for i in texte:
        if i in carac :
            carac[i]+=1
        else:
            carac[i] = 1
    return sorted([(i,carac[i])for i in carac],key=lambda colonnes : colonnes[1], reverse=True)

def index_pos(list,weight):
    i = 0
    while  i < len(list)-1 and list[i].weight<weight:
        i+=1
    return i+1

class Node :
    def __init__(self, NodeL, NodeR):
        self.NodeL = NodeL
        self.NodeR = NodeR
        self.string = NodeL.string + NodeR.string
        self.weight = NodeL.weight + NodeR.weight


class Leaf:
    def __init__(self,string,weight):
        self.string = string
        self.weight = weight
        self.NodeL = self
        self.NodeR = self


class TreeBuilder : 
    def __init__(self,text):
        self.text = text
        self.caracs = compt_carac(text)

    def tree(self):
        tree = []
        for carac,weight in self.caracs :
            tree.append(Leaf(carac,weight))
        tree = sorted(tree,key=lambda value: value.weight)
        working_nodes = sorted(tree,key=lambda value: value.weight)
        while len(working_nodes)>1:
            print(list(map(lambda x : x.string,working_nodes)))
            nodeL = working_nodes.pop(0)
            nodeR = working_nodes.pop(0)
            node = Node(nodeL,nodeR)
            tree.append(node)
            working_nodes.insert(index_pos(working_nodes,node.weight), node)
        return tree

tree = TreeBuilder('abcdefefe').tree()
for i in tree:
    print (i.string, i.weight, i.NodeL.string, i.NodeR.string)


class Codec :
    def __init__(self):
        

