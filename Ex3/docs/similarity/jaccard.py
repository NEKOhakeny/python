class jaccard:      
    
    def calc(list1,list2):
        set_intersection = set.intersection(set(list1), set(list2))
        num_and = len(set_intersection)
        set_or = set.union(set(list1), set(list2))
        num_or = len(set_or)
    
        return float(num_and) / num_or