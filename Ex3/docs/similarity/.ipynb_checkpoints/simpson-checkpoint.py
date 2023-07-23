class simpson:
    def __init__(self):
        pass
    
    
    def calc(list1,list2):
        x = frozenset(list1)
        y = frozenset(list2)
        return len(x & y) / float(min(map(len, (x, y))))