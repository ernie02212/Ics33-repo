import re
from goody import irange
from collections import defaultdict
#^([1-9][0-9]*?)([-:])?(?:([1-9][0-9]*?)[\/]?([1-9][0-9]*?)?)?$
# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. The patterns must be all on the first line

def pages (page_spec : str, unique :  bool) -> [int]: #result in ascending order
    lst = []
    for i in page_spec.split(","):
        pattern = re.match(r'^([1-9][0-9]*?)([-:])?(?:([1-9][0-9]*)?(?:[\/]?)([1-9][0-9]*)?)?$', i)
        if pattern.group(2) == None and pattern.group(3) == None and pattern.group(4) == None:
            lst.append(int(pattern.group(1)))
        if pattern.group(2) == "-" and pattern.group(4) == None:
            if int(pattern.group(1)) > int(pattern.group(3)):
                raise AssertionError
        if pattern.group(2) == "-" and pattern.group(4) != None:
            for i in range(int(pattern.group(1)), int(pattern.group(3))+1, int(pattern.group(4))):
                lst.append(i)
        elif pattern.group(2) == "-":
            for i in range(int(pattern.group(1)),int(pattern.group(3))+1):
                lst.append(i)
        if pattern.group(2) == ":" and pattern.group(4) == None:
            for i in range(int(pattern.group(1)), int(pattern.group(1))+int(pattern.group(3))):
                lst.append(i)
        elif pattern.group(2) == ":":
            for i in range(int(pattern.group(1)), int(pattern.group(1))+int(pattern.group(3)), int(pattern.group(4))):
                lst.append(i)
    if unique == True:
        u_lst = list(set(lst))
        final_lst = sorted(u_lst)
        return final_lst
    elif unique == False:
        nu_lst = sorted(lst)
        return nu_lst




def expand_re(pat_dict:{str:str}): 
    index = 1
    key = [i for i in pat_dict.keys()]
    for k,v in pat_dict.items():
        if index != len(key):
            pat_dict[key[index]] = pat_dict[key[index]].replace("#{}#".format(k), "(?:{})".format(v))
            index +=1
    return pat_dict
        
    
   
    
    





if __name__ == '__main__':
    
    p1a = open('repattern1a.txt').read().rstrip() # Read pattern on first line
    print('Testing the pattern p1a: ',p1a)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1a,text)
        print(' ','Matched' if m != None else "Not matched")
        
    p1b = open('repattern1b.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p1b: ',p1b)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1b,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
        
    p2 = open('repattern2a.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2: ',p2)
    for text in open('bm2a.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
    print('\nTesting pages function')
    for text in open('bm2b.txt'):
        text = text.rstrip().split(';')
        text,unique = text[0], text[1]=='True'
        try:
            p = pages(text,unique)
            print('  ','pages('+text+','+str(unique)+') = ',p)
        except:
            print('  ','pages('+text+','+str(unique)+') = raised exception')
        
    
    print('\nTesting expand_re')
    pd = dict(digit = r'[0-9]', integer = r'[+-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary
    # {'digit': '[0-9]', 'integer': '[+-]?(?:[0-9])(?:[0-9])*'}
    
    pd = dict(integer       = r'[+-]?[0-9]+',
              integer_range = r'#integer#(..#integer#)?',
              integer_list  = r'#integer_range#(,#integer_range#)*',
              integer_set   = r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer': '[+-]?[0-9]+',
    #  'integer_range': '(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?',
    #  'integer_list': '(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*',
    #  'integer_set': '{(?:(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(?,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'a': 'correct',
    #  'b': '(?:correct)',
    #  'c': '(?:(?:correct))',
    #  'd': '(?:(?:(?:correct)))',
    #  'e': '(?:(?:(?:(?:correct))))',
    #  'f': '(?:(?:(?:(?:(?:correct)))))',
    #  'g': '(?:(?:(?:(?:(?:(?:correct))))))'
    # }
    
    print()
    print()
    import driver
    driver.default_file_name = "bscq2F21.txt"
    #driver.default_show_traceback = True
    #driver.default_show_exception = True
    #driver.default_show_exception_message = True
    driver.driver()
