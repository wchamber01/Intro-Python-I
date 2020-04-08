# Exercise 1
'''
1. How many seconds are there in 21 minutes and 15 seconds?
2. How many miles are there in 5 kilometers?
3. If you run a 5 kilometer race in 21 minutes and 15 seconds, 
   what is your average pace (time per mile in minutes and seconds)?
4. What is your average speed in miles per hour?
5. Suppose the cover price of a book is $19.95, but bookstores get a 25% discount. 
   Shipping costs $2.50 for the first copy and $1 for each additional copy. 
   What is the total wholesale cost for 75 copies?
'''
# Answers

# 1.
print('Number 1');print((21*60)+15)

# 2.
print('Number 2');print(5/1.609344)

# 3.
miles=(5/1.609344)
time=((21*60)+15)
print('Number 3');print((time/60)/miles)

# 4.
miles=(5/1.609344)
time=((21*60)+15)
print('Number 4');print(((time/60)/miles)*(1/60))