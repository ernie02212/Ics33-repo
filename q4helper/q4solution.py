# Generators must be able to iterate through any kind of iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

def sequence(*iterables):
    for i in iterables:
        for element in i:
            yield element
    return
    yield None
            
           
def group_when(iterable,p):
    in_lst = []
    for i in iterable:
        if p(i):
            in_lst += i
            yield in_lst
            in_lst = []
        else:
            in_lst += i
    if len(in_lst) > 0:
        yield in_lst
    return
    yield None
             
def drop_last(iterable,n):
    hidden = iter(iterable)
    hidden_lst = []
    while True:
        try:
            y = next(hidden)
            hidden_lst.append(y)
        except StopIteration:
            break
    for i in range(len(hidden_lst)-n):
        yield hidden_lst[i]

    return
    yield None
    

def yield_and_skip(iterable,skip):
    hidden = iter(iterable)
    while True:
        try:
            x = next(hidden)
            yield x
            for i in range(skip(x)):
                next(hidden)
        except StopIteration:
            break

  
def alternate_all(*args):
    hidden_lst = []
    for arg in args:
        hidden_lst.append(iter(arg))
    while hidden_lst != []:
        tmp = []
        for i in hidden_lst:
            #print(tmp)
            try: 
                yield next(i) 
                tmp.append(i) 
            except StopIteration: 
                pass
        hidden_lst = tmp
        #print(hidden_lst)

    return
    yield None




def min_key_order(adict):
    for key, value in sorted(adict.items()):
        yield(key,value)
    

        
if __name__ == '__main__':
    from goody import irange
    
    # Test sequence; you can add any of your own test cases
    print('Testing sequence')
    for i in sequence('abc', 'd', 'ef', 'ghi'):
        print(i,end='')
    print('\n')

    print('Testing sequence on hidden')
    for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
        print(i,end='')
    print('\n')


    # Test group_when; you can add any of your own test cases
    print('Testing group_when')
    for i in group_when('combustibles', lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')

    print('Testing group_when on hidden')
    for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')


    # Test drop_last; you can add any of your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')

    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')


    # Test sequence; you can add any of your own test cases
    print('Testing yield_and_skip')
    for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')

    print('Testing yield_and_skip on hidden')
    for i in yield_and_skip(hide('abbabxcabbcaccabb'),lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')


    # Test alternate_all; you can add any of your own test cases
    print('Testing alternate_all')
    for i in alternate_all('abcde','fg','hijk'):
        print(i,end='')
    print('\n')
    
    print('Testing alternate_all on hidden')
    for i in alternate_all(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print('\n\n')
       
         
    # Test min_key_order; add your own test cases
    print('\nTesting Ordered')
    d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
    i = min_key_order(d)
    print(next(i))
    print(next(i))
    del d[8]
    print(next(i))
    d[32] = 'z'
    print(next(i))
    print(next(i))
    


         
         
    import driver
    driver.default_file_name = "bscq4F21.txt"
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
    
