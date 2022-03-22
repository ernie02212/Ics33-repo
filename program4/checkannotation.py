from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation:
    # First bind the class attribute to True allowing checking to occur (but
    #   only if the object's attribute self._checking_on is also bound to True)
    checking_on  = True
  
    # First bind self._checking_on = True, for checking the decorated function f
    def __init__(self, f):
        self._f = f
        self._checking_on = True

    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # First compare check's function annotation with its arguments
        def anytype():
            assert isinstance(value, annot), repr(param)+' failed annotation check(wrong type): value = '+repr(value)+\
                     '\n was type '+str(type(value).__name__)+ f'...should be type {annot.__name__}\n' + check_history
            return isinstance(value,annot)
        def check_list():
            assert isinstance(value,list), repr(param)+' failed annotation check(wrong type): value = '+repr(value)+\
                     '\n was type '+str(type(value).__name__)+ f'...should be type {type(annot).__name__}\n' + check_history
            if len(annot) == 1:
                for i in range(len(value)):
                    self.check(param, annot[0], value[i], check_history + f"list[{i}] check: " + str(annot[0]) + '\n')
            elif len(annot) > 1:
                assert len(annot) == len(value), repr(param)+' failed annotation check(wrong number of elements): value = '+repr(value)+\
                     '\n annotation had '+str(len(annot))+ " elements" + str(annot) + "\n"+ check_history
                for a,v in zip(annot, value):
                    self.check(param, a, v)

        
        def check_tuple():
            assert type(value) == tuple, repr(param)+' failed annotation check(wrong type): value = '+repr(value)+\
                     '\n was type '+str(type(value).__name__)+ f'...should be type {type(annot).__name__}\n' + check_history
            if len(annot) == 1: 
                check_s = ''
                for i in range(len(value)):
                    if i == len(value) - 1:
                        self.check(param, annot[0],value[i], check_s)
                    else:
                        self.check(param, annot[0],value[i])
                        
            elif len(annot) > 1:
                assert len(annot) == len(value), repr(param)+' failed annotation check(wrong number of elements): value = '+repr(value)+\
                     '\n annotation had '+str(len(annot))+ " elements" + str(annot) + "\n"+ check_history
                for a,v in zip(annot, value):
                    self.check(param, a, v)

        
        def check_dict():
            assert isinstance(value,dict), print(repr(param)+' failed annotation check(wrong type): value = '+repr(value)+\
                     '\n was type '+str(type(value).__name__)+ f'...should be type {type(annot).__name__}\n' + check_history)
            if len(annot) == 1:
                K,V = list(annot.items())[0]  
                for k,v in value.items():
                    self.check(param, K, k)
                    self.check(param, V, v)
            else:
                assert isinstance(value,dict), print(repr(param)+' annotation inconsistency: dict should have 1 item but had '+str(len(annot))+
                     '\n annotation =  '+str(annot)+ '\n' + check_history)


        
        def check_set():
            if not isinstance(value, set):
                raise AssertionError
            elif len(annot) == 1:
                a = list(annot)[0]
                for v in value:
                    self.check(param, a, v)
            elif len(annot) > 1:
                raise AssertionError

    
        def check_frozenset():
            if not isinstance(value, frozenset):
                raise AssertionError
            elif len(annot) == 1:
                a = list(annot)[0]
                for v in value:
                    self.check(param, a, v)
            elif len(annot) > 1:
                raise AssertionError

          
        def check_lambda():
            if len(inspect.signature(annot).parameters) != 1:
                raise AssertionError
            try:
                if not annot(value):
                    raise AssertionError
            except:
                raise AssertionError
        
        def check_str():
            try:
                y = eval(annot, self._f)
                assert y, print(y) 
            except:
                raise AssertionError
            
           

        if annot == None:
            pass
        elif type(annot) is type:
            anytype()
        elif isinstance(annot, list):
            check_list()
        elif isinstance(annot, tuple):
            check_tuple()
        elif isinstance(annot, dict):
            check_dict()
        elif isinstance(annot, set):
            check_set()
        elif isinstance(annot, frozenset):
            check_frozenset()
        elif inspect.isfunction(annot):
            check_lambda()
        elif isinstance(annot, str):
            check_str()
        else:
            try:
                annot.__check_annotation__(self.check, param, value, check_history)
            except AssertionError:
                raise
            except:
                raise AssertionError
              
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        # Return the argument/parameter bindings as an OrderedDict (it's derived
        #   from a dict): bind the function header's parameters using its order
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments
        
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        
        if self.checking_on == False or self._checking_on == False:
            return self._f(*args, **kargs)
        try:
            # For each detected annotation, check it using its parameter's value
            self.dict0 = param_arg_bindings()
            # Compute/remember the value of the decorated function
            # If 'return' is in the annotation, check it
            if 'return' in self._f.__annotations__:
                self.dict0['_return'] = self._f(*args, **kargs)
            # Return the decorated answer
            for k in self.dict0:
                if k == '_return':
                    self.check(k, self._f.__annotations__['return'], self.dict0[k])
                    
                else:
                    self.check(k, self._f.__annotations__[k], self.dict0[k])
            #remove after adding real code in try/except
           
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            '''print(80*'-')
            for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
                print(l.rstrip())
            print(80*'-')'''
            raise




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    '''def f(x:int): pass
    f = Check_Annotation(f)
    f(3)
    f('a')
    
    @Check_Annotation
    def f(x:[[int]]): pass
    
    f([[1,2],[3,4],[5,'a']])'''
    
    #driver tests
    import driver
    driver.default_file_name = 'bscp4SF1.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
