# insert into dictionary
def insert_dict(query, dict):
    if query[0]=='i':
        dict[query[1]]=query[2]
    else:
        print(-1)
    
    

# deleting from dictionary
def del_dict(query, dict):
     if query[0] == 'd':
        del dict[query[1]]
    
    # Your code here
    
    
    
    

# print marks of required name
def print_dict(key, dict):
    if key in dict.keys():
        print(f'Marks of {key} is {dict[key]}')
    else:
        print(-1)
    # Your code here
    
    
    