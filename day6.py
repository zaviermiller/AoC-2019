nodes = {}

class Node:
    def __init__(self,value):
        self.value = value
        self.children = []
        self.direct_orbits = 0
        self.parent = None
    
    def __repr__(self):
        return str(self.value)
    
    def add_child(self, value):
        if value in nodes:
            node = nodes[value]
        else:
            node = Node(value)
        node.parent = self
        self.children.append(node)
        return node
    
    def get_child(self, value):
        if next((x for x in self.children if x.value == value),None) != None:
            print(self, value)
            return next((x for x in self.children if x.value == value))
        else:
            for n in self.children:
                return n.get_child(n)
        return 'test'

orbits = [x.split(')') for x in open('day6_input.txt').read().split('\n')]
# orbit_dict = dict()

# def create_dict(orbit,orbit_dict):
#     if orbit[0] in orbit_dict:
#         orbit_dict[orbit[0]] = {orbit[1]: {}}
#     else:
#         for key in orbit_dict:
#             create_dict(orbit,orbit_dict[key])
        
#         orbit_dict[orbit[0]] = {orbit[1]: {}}

# for orbit in orbits:
#     create_dict(orbit,orbit_dict)
# print((orbit_dict)['B'])

root = None

for i,orbit in enumerate(orbits):
    if orbit[0] not in nodes:
        root = Node(orbit[0])
        nodes[root.value] = root
        new_node = root.add_child(orbit[1])
        nodes[new_node.value] = new_node
    else:
        node = nodes[orbit[0]]
        new_node = node.add_child(orbit[1])
        nodes[new_node.value] = new_node

counter = 0

for key in nodes:
    node = nodes[key]
    while node.parent != None:
        counter += 1
        node = node.parent

points = {"YOU": [], "SAN": []}

for key in nodes:
    if key in points:
        node = nodes[key]
        while node.parent != None:
            points[key].append(node.value)
            node = node.parent

intersect = [value for value in points["YOU"] if value in points["SAN"]][0]

print(points["YOU"].index(intersect) + points["SAN"].index(intersect) - 2)
# print(len(orbits))

# indirect_count = 0

# def count_indirects(orbit):


            
