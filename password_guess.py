import random
target= input("Enter the Target password:")
gp= "abcdefghijklmnopqrstuvwxyz"
l= len(target)
current= "a"*l
current= list(current)
attempt=0

def get_random_char():
    return random.choice(gp)

flag= False
for i in range(l):
    while current[i]!= target[i]:
        current[i]= get_random_char()
        attempt += 1

print("".join(current))
print("number of attempts:",attempt)

        

    
    


