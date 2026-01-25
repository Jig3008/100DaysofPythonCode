initial_list = [1,2,3]
initial_list.append(4)
print(initial_list)
initial_list.extend([5,6])
print(initial_list)
initial_list.insert(0,10)
print(initial_list)

#Code for who pays the bill
import random
friends_list = ['Ted','Barney','Marshall','Lily','Robin']
print(random.choice(friends_list)) #Choice function helps in finding a random value from a list
