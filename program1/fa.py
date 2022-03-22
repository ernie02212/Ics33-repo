import goody


def read_fa(file : open) -> {str:{str:str}}:
    list = []
    dict = {}
    dict2 = {}
    kk = ''
    for n in file:
        list.append(n.strip().split(';'))
    for k in list:
        for i in range(1,len(k),2):
            dict2.update({k[i:i+2][0]:k[i:i+2][1]})
        dict[k[0]] = dict2.copy()
        dict2.clear()
    return dict


    

def fa_as_str(fa : {str:{str:str}}) -> str:
    s = []
    b = ""
    fa = sorted(fa.items(), key= lambda x:x[0])
    for ll in fa:
        s = [(key, value) for key, value in ll[1].items() ]
        s.sort(key= lambda x:x[0])
        b += "  " + str(ll[0]) + " transitions: " + str(s) +"\n"
        s.clear()
    return b
    
        
    

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    list = []
    list2 = []
    list.append(state)
    counter = 0
    cc = state
    if 'x' in inputs:
        inputs.remove('x')
        list2.append(('x', None))
    while counter < len(inputs):
        for n in fa:
            if cc == n:
                list.append((inputs[counter], fa[cc][inputs[counter]]))
                if counter != (len(inputs) - 1):
                    cc = fa[cc][inputs[counter]]
                counter += 1
    if len(list2) == 1:
        list.append(list2[0])
    return list
            


def interpret(fa_result : [None]) -> str:
    list = []
    n = ""
    n += "Start state = " + str(fa_result[0]) + "\n"
    counter = 0
    fa_result.remove(fa_result[0])
    while counter < len(fa_result):
        for j in fa_result:
            if j[0] == 'x':
                n += "  Input = " + j[0] + '; ' + "illegal input: simulation terminated" + '\n'
                counter += 1
                list.append('1')
            else:
                n += "  Input = " + j[0] + '; ' + "new state = " + j[1] + '\n'
                counter += 1
    if len(list) == 1:
        n+= "Stop state = " + 'None' + '\n'
    else: 
        n+= "Stop state = " + fa_result[len(fa_result) - 1][1] + '\n'
    return n
        

            
        
    




if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
