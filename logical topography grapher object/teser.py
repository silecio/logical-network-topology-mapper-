import yaml
list1 = ['1', '2', '3']
str1 = ''.join(list1)
print(str1)
parents = ["ace"]
children = ["a","b"]

class parent:
    def __init__(self):
        self.name = parents[0]
        self.connections = children

s = parent()
ss = {"name":s.name,"connections": s.connections}
print(ss)