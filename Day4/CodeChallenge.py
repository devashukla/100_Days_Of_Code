# Who will pay the bill?
import random

# random.choice() => Used to print random string in python

friends = ["Deva", "Saksham", "Suksham", "Ansh", "Harsh", "Tejas"]
#Method-1:- Using value
print(random.choice(friends))

#Method-2:- Using Index
random_index = random.randint(0,5)
print((friends[random_index]))
