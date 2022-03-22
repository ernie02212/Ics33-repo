from goody import type_as_str
from math import sqrt

class Interval:
    def __init__(self, minm, maxm):
        self.minm = minm 
        self.maxm = maxm
        
    @staticmethod
    def min_max(minm, maxm = None):
        print(minm, maxm)
        if type(minm) != int and type(minm) != float:
            raise AssertionError
        elif (type(maxm) != int and type(maxm) != float and maxm != None):
            raise AssertionError
        elif maxm == None:
            maxm = minm
        elif minm > maxm:
            raise AssertionError
        return Interval(minm,maxm)
    
    @staticmethod
    def mid_err(midVal, error = 0):
        print(midVal)
        print(error)
        if type(midVal) != int and type(midVal) != float:
            raise AssertionError
        elif type(error) != int and type(error) != float:
            raise AssertionError
        if error < 0 :
            raise AssertionError
        return Interval(midVal - error, midVal + error)
    
    def best(self):
        print(self.minm, self.maxm)
        average = (self.minm + self.maxm)/2
        return average
    
    def error(self):
        return abs(self.maxm - Interval.best(self))
    
    def relative_error(self):
        return abs(Interval.error(self)/Interval.best(self))*100
    
    def __repr__(self):
        empty_string = "Interval({},{})".format(self.minm, self.maxm)
        return empty_string
    
    def __str__(self):
        empty_strings = "{}(+/-{})".format(Interval.best(self),Interval.error(self))
        return empty_strings
    
    def __bool__(self):
        if self.error() != 0:
            return True
        else:
            return False
        
    def __pos__(self):
        return self
    
    def __neg__(self):
        return Interval(-self.minm,-self.maxm)
    
    def __add__(self,right):
        if type(right) == int or type(right) ==float:
            right = Interval(right, right)
        if type(right) != Interval:
            raise TypeError
        xmin = self.minm + right.minm
        xmax = self.maxm + right.maxm
        return Interval(xmin,xmax)
    
    def __radd__(self,left):
        if type(left) == int or type(left) ==float:
            left = Interval(left, left)    
        if type(left) != Interval:
            raise TypeError
        xmin = self.minm + left.minm
        xmax = self.maxm + left.maxm
        return Interval(xmin,xmax)
    
    def __sub__(self,right):
        if type(right) == int or type(right) ==float:
            right = Interval(right, right)
        if type(right) != Interval:
            raise TypeError
        xmin = self.minm - right.maxm
        xmax = self.maxm - right.minm
        return Interval(xmin,xmax)
    
    def __rsub__(self,left):
        if type(left) == int or type(left) ==float:
            left = Interval(left, left)
        if type(left) != Interval:
            raise TypeError
        xmin = left.minm - self.maxm
        xmax = left.maxm - self.minm
        return Interval(xmin,xmax)
    
    def __mul__(self,right):
        if type(right) == int or type(right) ==float:
            right = Interval(right, right)
        if type(right) != Interval:
            raise TypeError
        x1 = self.minm * right.minm
        x2 = self.maxm * right.maxm
        x3 = self.minm * right.maxm
        x4 = self.maxm * right.minm
        lst = [x1,x2,x3,x4]
        sorted_lst = sorted(lst)
        xmin = min(sorted_lst)
        xmax = max(sorted_lst)
        return Interval(xmin,xmax)
    
    def __rmul__(self,left):
        if type(left) == int or type(left) ==float:
            left = Interval(left, left)
        if type(left) != Interval:
            raise TypeError
        x1 = self.minm * left.minm
        x2 = self.maxm * left.maxm
        x3 = self.minm * left.maxm
        x4 = self.maxm * left.minm
        lst = [x1,x2,x3,x4]
        sorted_lst = sorted(lst)
        xmin = min(sorted_lst)
        xmax = max(sorted_lst)
        return Interval(xmin,xmax)
    
    def __truediv__(self,right):
        if type(right) == int or type(right) ==float:
            right = Interval(right, right)
        if type(right) != Interval:
            raise TypeError
        if (self.minm == 0 or self.maxm == 0) or (right.minm == 0 or right.maxm == 0) :
            raise ZeroDivisionError
        x1 = self.minm / right.minm
        x2 = self.maxm / right.maxm
        x3 = self.minm / right.maxm
        x4 = self.maxm / right.minm
        lst = [x1,x2,x3,x4]
        sorted_lst = sorted(lst)
        xmin = min(sorted_lst)
        xmax = max(sorted_lst)
        return Interval(xmin,xmax)
        
   
        
    
        
    
if __name__ == '__main__':
    """
    g = Interval.mid_err(9.8,.05)
    print(repr(g))
    g = Interval.min_max(9.75,9.85)
    print(repr(g))
    d = Interval.mid_err(100,1)
    t = (d/(2*g)).sqrt()
    print(t,repr(t),t.relative_error())"""

    import driver    
    driver.default_file_name = 'bscp22F21.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
