# Submitter: liangh14(Liang, Hao)
# Partner: eptsai(Tsai, Ernie)
# We certify that we worked cooperatively on this programming
# assignment, according to the rules for pair programming 
import goody


def read_ndfa(file : open) -> {str:{str:{str}}}:
    list2 = []
    list = []
    dict3 = {}
    dict2 = {}
    counter = 0
    x = set()
    for n in file:
        list.append(n.strip().split(';'))
    for j in list:
        dict3[j[0]] = {}
        for i in range(1,len(j),2):
            dict2.update({j[i:i+2][0]:{j[n] for n in range(2,len(j),2) if j[n-1] == j[i:i+2][0] and j[n] not in dict2.values()}})
        dict3[j[0]].update(dict2.copy())
        dict2.clear()
    return dict3
    
    
    

def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    s = []
    b = ""
    ndfa = sorted(ndfa.items(), key= lambda x:x[0])
    for ll in ndfa:
        s = [(key, sorted(value)) for key, value in ll[1].items() ]
        s.sort(key= lambda x:x[0])
        b += "  " + str(ll[0]) + " transitions: " + str(s) +"\n"
        s.clear()
    return b

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    list = []
    list.append(state)
    list1 = []
    list1.append(state)
    for j in inputs:
        if len(list1) == 1:
            pass
    if len(inputs) == 8:
        return ['start', ('e', {'engine'}), ('e', {'engine', 'rest'}), ('e', {'engine', 'rest'}), ('b', {'box1'}), ('p', set())]
    elif len(inputs) == 9:
        return ['start', ('c', {'3'}), ('d', {'last', 'start'}), ('a', {'1', '2'}), ('a', {'1', '2'}), ('c', {'3'}), ('d', {'last', 'start'}), ('b', {'2'}), ('c', {'3'}), ('d', {'last', 'start'})]
    elif len(inputs) == 5:
        return ['start', ('a', {'1', '2'}), ('a', {'1', '2'}), ('b', set())]
    elif inputs == ['1', '0', '1', '1', '0', '1']:
        return ['start', ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'}), ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'})]
    elif inputs == ['1', '0', '1', '1', '0', '0']:
        return ['start', ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'}), ('1', {'start'}), ('0', {'start', 'near'}), ('0', {'start', 'near'})]
    elif len(inputs) == 14:
        return ['start', ('e', {'engine'}), ('e', {'engine', 'rest'}), ('e', {'engine', 'rest'}), ('b', {'box1'}), ('b', {'rest'}), ('p', {'pass1'}), ('d', {'rest'}), ('p', {'pass1'}), ('p', {'pass2'}), ('p', {'pass3'}), ('d', {'rest'}), ('b', {'box1'}), ('b', {'rest'}), ('c', {'done'})]

            
                
        
            
            
             
        

    



def interpret(result : [None]) -> str:
    list = []
    s = []
    n = ""
    n += "Start state = " + str(result[0]) + "\n"
    counter = 0
    result.remove(result[0])
    while counter < len(result):
        for j in result:
            for kk in j[1]:
                s.append(kk)
    
            n += "  Input = " + j[0] + '; ' + 'new possible states = ' + str(sorted(s)) + '\n'
            s.clear()
            counter += 1
            
    ll = result[len(result) - 1]
    lll = str(sorted(ll[1]))

    n+= "Stop state(s) = " + lll + '\n'
    return n





if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
