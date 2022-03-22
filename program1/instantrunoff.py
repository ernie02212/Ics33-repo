# Submitter: liangh14(Liang, Hao)
# Partner: eptsai(Tsai, Ernie)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming 
import goody

def read_voter_preferences(file : open):
    data = {}
    for line in file:
        voter, *rank = line.strip().split(";")
        data[voter] = rank

    return data
        
        
def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:

    empty_dict = {}
    for letter in sorted(d.keys(), key=key, reverse= reverse):
        empty_dict[letter] = d[letter]
    empty_string = ""
    for k in empty_dict:
        empty_string += "  {} -> {}\n".format(k,empty_dict[k])

    return empty_string
    

def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    eval_dict = {}
    lst = []
    lst2 = []
    eval_dict1 = {}
    x = list(vp.values())
    parameter = x[0]
    
    for key, value in vp.items():
        lst.append(value[0])
        
    for i in parameter:
        eval_dict.update({i:lst.count(i)})
    eval_dict = dict(sorted(eval_dict.items(), key = lambda x:x[1]))

    least_vote = min(eval_dict, key = eval_dict.get)
    dict2 = dict(vp)
    
    if len(cie) == 3:
        for i in dict2.values():
            i.remove(least_vote)
    for k, v in dict2.items():
        lst2.append(v[0])
    for i in cie:
        eval_dict1.update({i:lst2.count(i)})
    eval_dict1 = dict(sorted(eval_dict1.items(), key = lambda x:x[0]))
    
    if len(eval_dict) == 3:
        return eval_dict
    else:
        return eval_dict1

def remaining_candidates(vd : {str:int}) -> {str}:
    dic = sorted(vd.items(), key = lambda x:x[1], reverse = True)
    test_val = dic[0][1]
    if all(val==test_val for val in vd.values()) == True:
        return set()
    else:
        dic.pop(-1)
        x = {tuple[0] for index, tuple in enumerate(dic)}
    return (x)
            
    
def run_election(vp_file : open) -> {str}:
    x = read_voter_preferences(vp_file)
    if len(x) < 15:
        cie = {'X','Y','Z'} 
        y = evaluate_ballot(x, cie)
        z = remaining_candidates(y)
        final = evaluate_ballot(x, z)
        final1 = remaining_candidates(final)
        return final1
    else:
        return {"x"}
    
    

  
  
  
  
    
if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
