from collections import defaultdict
from goody import type_as_str

# Iterators are covered in Week #4
# Implement all methods but iterators after Week #3

class Bag:
    def __init__(self,empty_bag = []):
        self.dictBag = {}
        for i in empty_bag:
            self.dictBag.update({i:empty_bag.count(i)})
    def __repr__(self):
        empty_string = ""
        for key, value in self.dictBag.items():
            empty_string += key*value
        x = ",".join(empty_string[i:i+1] for i in range(0, len(empty_string)))
        final_string = "Bag(["
        final_string += x + "])"
        print(final_string)
        return final_string
    
    def __str__(self):
        empty_str = "Bag("
        empty_str += ",".join(f"{x}[{y}]" for x, y in self.dictBag.items())
        empty_str += ")"
        return empty_str
    
    def __len__(self):
        lst = []
        for x,y in self.dictBag.items():
            lst.append(y)
        total = sum(lst)
        return total
        
    def unique(self):
        s = set()
        for i in self.dictBag:
            s.add(i)
        x = len(s)
        return x
    def __contains__(self,items):
        for i in self.dictBag:
            if i == items:
                return True
        return False
    def count(self, num):
        count = 0
        for i in self.dictBag:
            if i == num:
                count+=1
        return count
    def add(self, item):
        if item in self.dictBag:
            self.dictBag[item] += 1
        else:
            self.dictBag[item] = 1
        
        
                

     




if __name__ == '__main__':
    #Put your own test code here to test Bag before doing bsc tests

    print('Start simple testing')

    import driver
    driver.default_file_name = 'bscp21F21.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()
