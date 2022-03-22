from collections import defaultdict  # Use or ignore

def function_cycler(*fs : callable) -> callable:
    if not fs :
        raise TypeError
    
    fs = list(fs)
    def f_1(x : object) -> object:
        result = fs[0](x)
        fs.append(fs.pop(0))
        f_1.times_called = f_1.times_called + 1
        return result
    
    f_1.times_called = 0
    return f_1

    

def jobs(db1 : {str:{str:int}}, min_skill_level : int) -> {str}:
    return {job for names in db1 for job in db1[names] if db1[names][job] >= min_skill_level} # for full credit, use a single return statement  



def rank(db1 : {str:{str:int}}) -> [str]:
    dic = {}
    lst = []
    for name in db1:
        dic[name] = sum(db1[name].values())/len(db1[name])
    dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    for i in dic:
        lst.append(i[0])
    return lst
    # for full credit, use a single return statement  



def popular(db1 : {str:{str:int}}) -> [str]:
    return [job[0] for job in sorted(sorted({num:[y[0] for name in db1 for y in db1[name].items()].count(num) for num in [z[0] for i in db1 for z in db1[i].items()]}.items(),key=lambda x: x[0]), key = lambda x:x[1], reverse = True)]
    # for full credit, use a single return statement  



def who(db1 : {str:{(str,int)}}, job : str, min_skill_level : int) -> [(str,int)]:
    return sorted(sorted([(names,db1[names][j]) for names in db1 for j in db1[names] if db1[names][j] >= min_skill_level if job == j], key=lambda x: x[0]), key=lambda x:x[1], reverse= True) # for full credit, use a single return statement  
    # for full credit, use a single return statement  



def by_job(db1 : {str:{str:int}}) -> {str:{str:int}}:
    dic = {}
    for key, val in db1.items():
        for name, job in val.items():
            if name not in dic:
                dic[name] = {}
            if key not in dic[name]: 
                dic[name][key] = job 
    dic = dict(sorted(dic.items(), key = lambda x:x[0]))
    return dic 


 
def by_skill(db1 : {str:{str:int}}) -> [int,[str,[str]]]:
    result = defaultdict(lambda : defaultdict(list))
    for name, jobs in db1.items():
        for job, rank in jobs.items():
            result[rank][job].append(name)
    for rank, info in result.items():
        lst = []
        result[rank] = lst
        for job, ppl in sorted(info.items()):
            lst.append((job, sorted(ppl)))
    return sorted(result.items(), reverse = True)





if __name__ == '__main__':
    from goody import irange
    
    print('\nTesting function_cycler')
    try:
        cycler0 = function_cycler()
        print("Incorrect: Did not raise required exception for no-argument function call")
    except TypeError:
        print("Correct: rasised required exception for no-argument function call")
    cycler1 = function_cycler( (lambda x : x), (lambda x : x**2))
    print('Cycler 1:',[cycler1(x) for x in irange(1,10)],'... times called: ',cycler1.times_called)
    cycler2 = function_cycler( (lambda x : x+1), (lambda x : 2*x), (lambda x : x**2))
    print('Cycler 2:',[cycler2(x) for x in irange(1,10)],'... times called: ',cycler2.times_called)
 
    print('Cycler 1 again:',[cycler1(x) for x in irange(10,15)],'... times called: ',cycler1.times_called)
    print('Cycler 2 again:',[cycler2(x) for x in irange(10,20)],'... times called: ',cycler2.times_called)
    
    
    # Note: the keys in this dicts are not specified in alphabetical order
    db1 = {
          'Diane':   {'Laundry': 2,   'Cleaning': 4, 'Gardening': 3},
          'Betty':   {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3},
          'Charles': {'Plumbing': 2,  'Cleaning': 5},
          'Adam':    {'Cleaning': 4,  'Tutoring': 2, 'Baking': 1}
          }

    db2 = {
           'Adam': {'Laundry': 2, 'Driving': 2, 'Tutoring': 2, 'Reading': 1, 'Gardening': 1},
           'Emil': {'Errands': 4, 'Driving': 1, 'Baking': 3},
           'Chad': {'Repairing': 2, 'Reading': 2, 'Errands': 4, 'Baking': 2},
           'Ivan': {'Gardening': 5, 'Errands': 5, 'Reading': 4, 'Cleaning': 3},
           'Gene': {'Driving': 1, 'Laundry': 1, 'Baking': 2, 'Gardening': 2, 'Repairing': 2, 'Errands': 5},
           'Dana': {'Driving': 2}, 
           'Hope': {'Driving': 5, 'Reading': 3, 'Errands': 2, 'Shopping': 2, 'Gardening': 1, 'Laundry': 2},
           'Bree': {'Baking': 2, 'Errands': 5},
           'Faye': {'Tutoring': 2, 'Reading': 5, 'Repairing': 5, 'Baking': 4}
           }

    print('\nTesting jobs')
    print('jobs(db1,0):',jobs(db1,0))
    print('jobs(db1,3):',jobs(db1,3))
    print('jobs(db2,0):',jobs(db2,0))
    print('jobs(db2,5):',jobs(db2,5))


    print('\nTesting rank')
    print ('rank(db1):',rank(db1))
    print ('rank(db2):',rank(db2))


    print('\nTesting popular')
    print ('popular(db1):',popular(db1))
    print ('popular(db2):',popular(db2))


    print('\nTesting who')
    print("who(db1,'Cleaning',4):", who(db1,'Cleaning',4))
    print("who(db1,'Gardening',0):", who(db1,'Gardening',0))
    print("who(db1,'Tutoring',3):", who(db1,'Tutoring',3))
    print("who(db1,'Gambling',0):", who(db1,'Gambling',0))
    print("who(db2,'Baking',0):", who(db2,'Baking',0))
    print("who(db2,'Cleaning',1):", who(db2,'Cleaning',1))
    print("who(db2,'Driving',2):", who(db2,'Driving',2))
    print("who(db2,'Errands',3):", who(db2,'Errands',3))
    print("who(db2,'Gardening',4):", who(db2,'Gardening',4))
    print("who(db2,'Laundry',5):", who(db2,'Laundry',5))

    print('\nTesting by_job')
    print ('by_job(db1):',by_job(db1))
    print ('by_job(db2):',by_job(db2))


    print('\nTesting by_skill')
    print ('by_skill(db1):',by_skill(db1))
    print ('by_skill(db2):',by_skill(db2))



    print('\ndriver testing with batch_self_check:')
    import driver
    driver.default_file_name = 'bscq1F21.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
