# Submitter: hying5(Ying, Hao)
# Partner  : eptsai(Tsai, Ernie)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming


import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable = False,  defaults =  {}):
    def show_listing(s):
        for ln_number, text_of_ln in enumerate(s.split('\n'),1):       
            print(f' {ln_number: >3} {text_of_ln.rstrip()}')

    # put your code here
    r_ex = r'^[A-Za-z](((\_)|[A-Za-z0-9])?)*$'
    if type(type_name) != str:
        raise SyntaxError
    elif re.match(r_ex, type_name):
        if keyword.iskeyword(type_name):
            raise SyntaxError('000')
    else:
        raise SyntaxError('111')
    
    #unique generator
    def unique(iterable):
        unique_set = set()
        for i in iterable:
            if i not in unique_set:
                unique_set.add(i)
                yield i

    if type(field_names) == list or type(field_names) == str:
        if type(field_names) == str:
            field_names = [i.rstrip(',') for i in field_names.split()]
        #clear duliplicate
        field_names = [i for i in unique(field_names)]
        for i in field_names:
            if not re.match(r_ex, i) or keyword.iskeyword(i) :
                raise SyntaxError('2222')           
    else:
        raise SyntaxError('3333')
    
    
    for k in defaults:
        if k not in field_names:
            raise SyntaxError('4444')
    
    # bind class_definition (used below) to the string constructed for the class
    class_definition = '''\
import re, keyword
class {type_name}:
    _fields = {field_names}
    _mutable = {mutable}\n\n'''.format(type_name = type_name, field_names = field_names, mutable = mutable)
        
    def gen_init(lst):
        final_str = '''\
    def __init__(self,{args1}):
        {args2}\n\n'''
        args_1 = ','.join([x if x not in defaults else f'{x}={defaults[x]}' for x in field_names])
        args_2 = '\n        '.join([f'self.{x} = {x}' for x in field_names])
        final_str = final_str.format(args1 = args_1, args2 = args_2)
        return final_str
    
    class_definition += gen_init(field_names)
    
    def gen_setattr():
        final_str = '''\
    def __setattr__(self, name, value):
        if name in self.__dict__ and self._mutable == False:
            raise AttributeError
        else:
            self.__dict__[name] = value\n\n'''
        return final_str
    
    class_definition += gen_setattr()
                                 
    def gen_repr(type_name, field_names):
        final_str = '''\
    def __repr__(self):
        return \'{ty_name}({args1})\'.format({args2})\n\n'''
        args1 = ','.join([f'{i}=' + '{' + f'{i}' + '}' for i in field_names])
        args2 = ','.join([f'{x}=self.{x}' for x in field_names])
        return final_str.format(ty_name=type_name, args1=args1, args2=args2)
    
    class_definition += gen_repr(type_name, field_names)
    
    def gen_get_field(field_names):
        final_str = ''
        for x in field_names:
            final_str += '''\
    def get_{x}(self):
        return self.{x}\n\n'''.format(x=x)
        return final_str
    
    class_definition += gen_get_field(field_names)
    
    def gen_getitem(field_names):
        max_index = len(field_names) - 1
        final_str = '''\
    def __getitem__(self, index):
        if (type(index) == int and index > {max_index}) or (type(index) != int and index not in self.__dict__):
            raise IndexError
        {args1}\n\n'''
        args1 = '\n        '.join([f'''\
if index == {index} or index == \'{field_names[index]}\':
            return self.get_{field_names[index]}()''' for index in range(len(field_names))])
        return final_str.format(max_index = max_index, args1 = args1)
    
    class_definition += gen_getitem(field_names)
    
    def gen_equal(field_names):
        final_str = '''\
    def __eq__(self, right):
        {args0}
            {args1}
            return True
        {args2}\n\n'''
        args0 = 'if type(self).__name__ == type(right).__name__:'
        args1 = '\n            '.join([f'if self[\'{x}\'] != right[\'{x}\']: return False' for x in field_names])
        args2 = f'return False'
        return final_str.format(args0 = args0, args1 = args1, args2 = args2) 
    
    class_definition += gen_equal(field_names)
    
    def gen_asdict(field_names):
        final_str = '''\
    def _asdict(self):
        return {args1}\n\n'''
        args1 = ','.join([f'\'{x}\': self[\'{x}\']' for x in field_names])
        args1 = '{' + args1 + '}'
        return final_str.format(args1 = args1)
    
    class_definition += gen_asdict(field_names)  
    
    def gen_make(field_names, type_name):
        final_str = '''\
    @staticmethod
    def _make(iter_1):
        return {args1}\n\n'''
        x = ','.join([f'{field_names[i]}=iter_1[{i}]' for i in range(len(field_names))])
        args1 = f'{type_name}' + '(' + x + ')'
        return final_str.format(args1=args1)
    
    class_definition += gen_make(field_names, type_name)
    
    def gen_replace(type_name, field_names):
        final_str = '''\
    def _replace(self,**kargs):
        for k in kargs:
            if not re.match(r'^[A-Za-z](((\_)|[A-Za-z0-9])?)*$', k) or keyword.iskeyword(k) or k not in {field_names}:
                raise TypeError
        if self._mutable:
            for x in kargs:
                self.__dict__[x] = kargs[x]
        else:
            new_dict = dict(self.__dict__)
            for x in kargs:
                new_dict[x] = kargs[x]
            return {type_name}(**new_dict)\n'''
        return final_str.format(type_name = type_name, field_names = field_names)
    
    class_definition += gen_replace(type_name, field_names)

    # Debugging aid: uncomment show_listing below so it always displays source code
    show_listing(class_definition)
    
    # Execute class_definition's str from name_space; followed by binding the
    #   attribute source_code to the class_definition; after the try/except bloc
    #   return this created class object; if any syntax errors occur, show the
    #   listing of the class and trace the error, in the except clause
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )                
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):                    
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')

    #driver tests
    import driver  
    driver.default_file_name = 'bscp3F21.txt'
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
