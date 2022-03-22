from goody import irange
from goody import type_as_str

import math


class Fraction:
    # Call as Fraction._gcd(...); no self parameter
    # Helper method computes the Greatest Common Divisor of x and y
    @staticmethod
    def _gcd(x : int, y : int) -> int:
        assert x >= 0 and y >= 0, 'Fraction._gcd: x('+str(x)+') and y('+str(y)+') must be >= 0'
        while y != 0:
            x, y = y, x % y
        return x

    # Returns a string that is the decimal representation of a Fraction, with
    #   decimal_places digits appearing after the decimal points.
    # For example: if x = Fraction(23,8), then x(5) returns '2.87500'
    def __call__(self, decimal_places):
        answer = ''
        num = self.num
        denom = self.denom
    
        # handle negative values
        if num < 0:
            num, answer = -num, '-'
    
        # handle integer part
        if num >= denom:
            answer += str(num//denom)
            num     = num - num//denom*denom
            
        # handle decimal part: 
        answer += '.'+f'{num*10**decimal_places//denom:0>{decimal_places}}'
        return answer
    
    @staticmethod
    # Call as Fraction._validate_arithmetic(..); with no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), lt (left type) and rt (right type)
    # An example call (from my __add__ method), which checks whether the type of
    #   right is a Fraction or int is...
    # Fraction._validate_arithmetic(right, {Fraction,int},'+','Fraction',type_as_str(right))
    def _validate_arithmetic(v, t : set, op : str, lt : str, rt : str):
        if type(v) not in t:
            raise TypeError('unsupported operand type(s) for '+op+
                            ': \''+lt+'\' and \''+rt+'\'')        

    @staticmethod
    # Call as Fraction._validate_relational(..); with no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), and rt (right type)
    def _validate_relational(v, t : set, op : str, rt : str):
        if type(v) not in t:
            raise TypeError('unorderable types: '+
                            'Fraction() '+op+' '+rt+'()')        


    def __init__(self,num=0,denom=1):
        self.num = num
        self.denom = denom
        if type(self.num) != int or type(self.denom) != int or self.denom == 0:
            raise AssertionError
        
        if self.num == 0:
            self.num = num
            self.denom = 1
            
        if self.denom < 0 and self.num < 0:
            self.denom = abs(self.denom)
            self.num = abs(self.num)
            self.num = int(self.num//Fraction._gcd(self.num,self.denom))
            self.denom = int(self.denom/Fraction._gcd(self.num,self.denom))
        
        elif self.denom < 0 or self.num < 0:
            self.denom = abs(self.denom)
            self.num = abs(self.num)
            y = Fraction._gcd(self.num,self.denom)
            self.num = -int(self.num//y)
            self.denom = int(self.denom//y)
        
        else:
            x = Fraction._gcd(self.num,self.denom)
            self.num = int(self.num//x)
            self.denom = int(self.denom//x)
            

    def __repr__(self):
        return "Fraction({},{})".format(self.num,self.denom)
    
    def __str__(self):
        return "{}/{}".format(self.num,self.denom)
    
    def __bool__(self):
        if self.num == 0 and self.denom == 1:
            return False
        elif self.num > 0:
            return True
    
    def __getitem__(self,i):
        if i == 0:
            return self.num
        if i == 1:
            return self.denom
        x = "numerator"
        y = "denominator"
        i = str(i)
        if x.startswith(i) == True:
            return self.num
        if y.startswith(i) == True:
            return self.denom
        else:
            raise TypeError

    def __pos__(self):
        return self
    
    def __neg__(self):  
        return "{}/{}".format(-self.num,self.denom)
    
    def __abs__(self):
        return "{}/{}".format(abs(self.num),abs(self.denom))


    def __add__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'+','Fraction',type_as_str(right))
        if type(right) == int:
            right = Fraction(right,1)
        final_denom = self.denom*right.denom
        final_num = self.num*right.denom + self.denom*right.num
        return Fraction(final_num,final_denom)
        

    def __radd__(self,left):
        Fraction._validate_arithmetic(left, {Fraction,int},'+','Fraction',type_as_str(left))
        if type(left) == int:
            right = Fraction(left,1)
        final_denom = self.denom*right.denom
        final_num = self.num*right.denom + self.denom*right.num
        return Fraction(final_num,final_denom)
  


    def __sub__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'-','Fraction',type_as_str(right))
        if type(right) == int:
            right = Fraction(right,1)
        final_denom = self.denom*right.denom
        final_num = self.num*right.denom - self.denom*right.num
        return Fraction(final_num,final_denom)

     
    def __rsub__(self,left):
        Fraction._validate_arithmetic(left, {Fraction,int},'-','Fraction',type_as_str(left))
        if type(left) == int:
            right = Fraction(left,1)
        final_denom = self.denom*right.denom
        final_num = self.denom*right.num - self.num*right.denom 
        return Fraction(final_num,final_denom)

     
    def __mul__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'*','Fraction',type_as_str(right))
        if type(right) == int:
            right = Fraction(right,1)
        final_denom = self.denom*right.denom
        final_num = self.num*right.num
        return Fraction(final_num,final_denom)


    def __rmul__(self,left):
        Fraction._validate_arithmetic(left, {Fraction,int},'*','Fraction',type_as_str(left))
        if type(left) == int:
            right = Fraction(left,1)
        final_denom = self.denom*right.denom
        final_num = self.num*right.num
        return Fraction(final_num,final_denom)
    

    def __truediv__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'/','Fraction',type_as_str(right))
        if type(right) == int:
            right = Fraction(right,1)
        final_denom = self.denom*right.num
        #print(final_denom)
        final_num = self.num*right.denom
        #print(final_num)
        return Fraction(final_num,final_denom)
    
    def __rtruediv__(self,left):
        Fraction._validate_arithmetic(left, {Fraction,int},'/','Fraction',type_as_str(left))
        if type(left) == int:
            right = Fraction(left,1)
        final_denom = self.denom*right.num
        final_num = self.num*right.denom
        #print(final_num)
        return Fraction(final_denom,final_num)


    def __pow__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'**','Fraction',type_as_str(right))
        #print(right)
        x = abs(right)
        final_denom = pow(self.denom,x)
        final_num = self.num
        
        return Fraction(final_num,final_denom)
    
    def __eq__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'==','Fraction',type_as_str(right))
        if type(right) == int:
            right = Fraction(right,1)
        if self.num == right.num and self.denom == right.denom:
            return True
        else:
            return False

    def __lt__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'<','Fraction',type_as_str(right))
        if type(right) == int:
            right = Fraction(right,1)
        if self.num*right.denom < self.denom*right.num:
            return True
        else:
            return False
        

    def __gt__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'>','Fraction',type_as_str(right))
        if type(right) == int:
            right = Fraction(right,1)
        if self.num*right.denom > self.denom*right.num:
            return True
        else:
            return False
   

    # Uncomment this method when you are ready to write/test it
    # If this is pass, then no attributes will be set!
    def __setattr__(self,name,value):
        self.__dict__[name] = value
        
        
    
    

##############################


# Newton: pi = 6*arcsin(1/2); see the arcsin series at http://mathforum.org/library/drmath/view/54137.html
# Check your results at http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
#   also see http://www.numberworld.org/misc_runs/pi-5t/details.html
def compute_pi(n):
    def prod(r):
        answer = 1
        for i in r:
            answer *= i
        return answer
    
    answer = Fraction(1,2)
    x      = Fraction(1,2)
    for i in irange(1,n):
        big    = 2*i+1
        answer += Fraction(prod(range(1,big,2)),prod(range(2,big,2)))*x**big/big       
    return 6*answer


if __name__ == '__main__':
    # Put in simple tests for Fraction before allowing driver to run
 
    print()
    import driver
    
    driver.default_file_name = 'bscq31F21.txt'
    #driver.default_show_traceback= True
    #driver.default_show_exception= True
    #driver.default_show_exception_message= True
    driver.driver()
