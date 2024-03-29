# print(1+1) # 2
# print() # 

# print(2 + 1) # 3 # plus
# print(2 - 1) # 1 # minus
# print(2 * 2) # 4 # multiply
# print(2 / 3) # 0.6666666666666666 # divide
# print(7 % 4 ) # 3 # Modulo
# print((-7) % 3) # 2
# print(2 ** 3) # 8 # power

# print(0.1+0.2) # 0.30000000000000004 # approximation with decimal
# print(round(2.675, 2)) # 2.67 # round the value 2.675 to two decimal places

# from decimal import Decimal
# print(Decimal(2.675)) # to see the exact value
# # Decimal('2.67499999999999982236431605997495353221893310546875')

# a = 5
# print(a) # 5
# a =  a + a 
# print(a) # 10
# print(type(a)) # <class 'int'> # return type of a variable
# a = 3.2 # example of dynamic typing
# print(type(a)) # <class 'float'>

# income = 3
# tax_rate = 0.2
# tax_amount = income * tax_rate
# print(tax_amount) # 0.6000000000000001

# print('hello, this is a string') 
# print("I'm learning python. ") # take advantage of single or double quotes
# print('hello\nworld') # have a new line in a string
# # hello
# # world
# print('hello\tworld') # hello   world # have a tab in a string
# print(len('hello round')) # 11 # length of string

# s = "Hello World!"
# print(s[0]) # H # get a char out of string
# print(s[-3]) # l # reverse indexing
# print(s[2:]) # llo World! # get substr starting at idx=2
# print(s[:2]) # He # get the substr up to but exclusive idx=2
# print(s[2:5]) # llo # get the substr start at idx=2 and ends at idx=5 (exclusive)
# print(s[::]) # Hello World! # get the whole string, with step size unspecified
# print(s[::2]) # HloWrd # get the whole string with step size=2
# print(s[2:7:2]) # loW # get the substring idx = [2, 7) with step size=2. [start:stop:step size]
# print(s[::-1]) # !dlroW olleH # reverse the string

# name = 'Sam'
# # name[0] = 'P' # TypeError due to string is immutable. So if want to change it, will need to create a new string
# # ---------------------------------------------------------------------------
# # TypeError                                 Traceback (most recent call last)
# # /var/folders/bn/yypl5g397pz61ngtbr4xsbrc0000gn/T/ipykernel_78033/1930518064.py in 
# # ----> 1 name[0] = 'P' # TypeError due to string is immutable
# #       2 # So if want to change it, will need to create a new string.

# # TypeError: 'str' object does not support item assignment
# name2 = 'P' + name[1:] # string concatenation
# print(name2) # Pam
# name3 = name * 5 # multiplication of strings
# print(name3) # SamSamSamSamSam
# print(name.upper()) # SAM # convert to upper case. Returns the new string
# print("NAME".lower()) # name # convert to lower case
# print("Hello World!".split()) # ['Hello', 'World!'] # split a string by space, return a list
# print("Hello World!".split("o")) # ['Hell', ' W', 'rld!'] # split by specified string
# print("Hello World!".split("o ")) # ['Hell', 'World!'] # split by specified string

# print('This is a string {}'.format('INSERTED')) # This is a string INSERTED # String interpolation (insert a var into a string)
# print('The {} {} {}'.format('round1', 'round2', 'round3')) # The round1 round2 round3
# print('The {2} {1} {0}'.format('round1', 'round2', 'round3')) # The round3 round2 round1 # reorder
# print('The {0} {0} {0}'.format('round1', 'round2', 'round3')) # The round1 round1 round1 # repeat
# print('The {r1} {r2} {r3}'.format(r1='round1', r2='round2', r3='round3')) # The round1 round2 round3 # assign keywords

# result = 100/777
# print(result) # 0.1287001287001287
# print("The result was {}".format(result)) # The result was 0.1287001287001287
# print("The result was {r}".format(r=result)) # The result was 0.1287001287001287
# print("The result was {r:1.3f}".format(r=result)) # The result was 0.129 # {value[:width][.precision]f}
# print("The result was {r:10.3f}".format(r=result)) # The result was      0.129
# print("The result was {r:0.3f}".format(r=result)) # The result was 0.129
# print("The result was {r:2.5f}".format(r=result)) # The result was 0.12870

# name = 'Jose'
# print(f'Hello, his name is {name}') # introduced in Python 3.6
# name = "Sam"
# age = 3
# print(f"{name}'s age is {age}") # Sam's age is 3

# my_list = [1, 2, 3]
# my_list = ["string", 100, 32.2] # can combine datatypes in list
# print(len(my_list)) # 3 # return length of list

# my_list = ['one', 'two', 'three']
# print(my_list[0]) # 'one'
# print(my_list[1:]) # ['two', 'three'] # slicing of list works like slicing of string 

# another_list = ['four', 3.5]
# new_list = my_list + another_list
# print(new_list) # ['one', 'two', 'three', 'four', 3.5]

# new_list[0] = 100 # you can mutate a list, unlike a string
# print(new_list) # [100, 'two', 'three', 'four', 3.5]
# new_list.append("six") # append a new element to end of list
# print(new_list) # [100, 'two', 'three', 'four', 3.5, 'six']
# new_list.pop() # remove an elem from the end of list
# print(new_list) # [100, 'two', 'three', 'four', 3.5]
# print(new_list.pop()) # 3.5 # pop() returns the val got popped out
# print(new_list.pop(0)) # 100 # remove an elem of specified index
# print(new_list.pop(-2)) # three # reverse index works for lists too

# new_list = ['a', 'e', 'x', 'b', 'c']
# num_list = [4, 1, 8, 3]
# new_list.sort() # sort the list in-place, so return nothing
# print(new_list) # ['a', 'b', 'c', 'e', 'x']
# print(sorted(new_list)) # ['a', 'b', 'c', 'e', 'x'] # this returns the sorted list
# num_list.sort()
# print(num_list) # [1, 3, 4, 8]
# num_list.reverse()
# print(num_list) # [8, 4, 3, 1]

# my_dict = {'key1':'value1', 'key2':'value2'} # initialize a dict
# print(my_dict) # {'key1': 'value1', 'key2': 'value2'}
# print(my_dict['key2']) # value2 # retrieve a value based on its key

# prices_lookup = {'apple':2.99, 'oranges':1.99, 'milk':5.80}
# print(prices_lookup['apple']) # 2.99

# prices_lookup = {'apple':2.99, 100:'test', 'milk':5.80} # no restriction on data types
# print(prices_lookup[100]) # test

# d = {'k1':123, 'k2':[0, 1, 2], 'k3':{'nestedKey':20}} # no restriction on data types, even nested dict or lists
# print(d['k3']['nestedKey']) # 20
# print(d['k2'][1]) # 1
# d['k4'] = 100 # add key-value pair to dictionary
# print(d) # {'k1': 123, 'k2': [0, 1, 2], 'k3': {'nestedKey': 20}, 'k4': 100}
# d['k2'] = 'Hi' # update value of a key in a dict
# print(d) # {'k1': 123, 'k2': 'Hi', 'k3': {'nestedKey': 20}, 'k4': 100}
# print(d.keys()) # dict_keys(['k1', 'k2', 'k3', 'k4']) # show all keys of the dict
# print(d.values()) # dict_values([123, 'Hi', {'nestedKey': 20}, 100]) # show all values of the dict
# print(d.items()) # dict_items([('k1', 123), ('k2', 'Hi'), ('k3', {'nestedKey': 20}), ('k4', 100)]) # show all pairs in the form of tuples

# t = (1, 2, 3)
# mylist = [1, 2, 3]
# print(type(t)) # <class 'tuple'>
# print(type(mylist)) # <class 'list'>
# print(len(t)) # 3 # return length of tuple

# t = ('One', 2, [1, 2, 3]) # no restriction to data types
# print(t[1]) # 2 # index a tuple
# print(t[-1]) # [1, 2, 3] # can also use reverse index

# t = ('a', 'a', 'b', 'z')
# print(t.count('a')) # 2 # return how many times 'a' exists in the tuple
# t.index('a') # 2 # return the index where 'a' appears for the first time in tuple
# # t.index('hi') # will return error the value we look for does not exist

# mylist[0] = 'New'
# print(mylist) # ['New', 2, 3]
# # t[0] = 'New' # expect an error, because of immutability

# myset = set() # initialize a set
# myset.add(1) # add an element to this set
# print(myset) # {1}
# myset.add('Hi')
# print(myset) # {1, 'Hi'}
# myset.add(1) # re-adding existing elem will not cause err, will not dup either. 

# mylist = [5, 'Hello', 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4]
# myset = set(mylist) # cast a list to a set, could de-dup
# print(myset) # {1, 2, 3, 4, 5, 'Hello'}

# print(True) # True
# # print(true) # lowercase is not accepted
# # Traceback (most recent call last):
# #   File "/Users/lisa/Desktop/python/temp.py", line 175, in <module>
# #     print(true)
# # NameError: name 'true' is not defined
# print(type(False)) # <class 'bool'>
# print(1 > 2) # False # comparison operators returns a boolean
# print(1 == 1) # True
# b = None
# print(b) # None

# myfile = open('myfile.txt') # if file not exist, will get error
# myfile.read() # return a string of everything in the text file
# myfile.read() # return nothing because cursor is at the end of the file
# myfile.seek(0) # reset the cursor
# myfile.read() # return a string of everything in the text file
# myfile.seek(0)
# myfile.readlines() # return a list with each line as a string
# myfile.close() # close the file

# # best practice, so you don't need to close this file by yourself
# with open('myfile.txt') as f:
#     contents = f.read()
# print(contents) # a string of everything in the text file

# with open('myfile.txt', mode = 'r') as f:
#     contents = f.read()
# # open function has different modes, default is r (read only)
# # could also be: 
# # w (write only, overwrite existing files or create new), 
# # a (append only), 
# # r+ (read and write), 
# # w+ (write and read, overwrites existing file or create new)

# with open('myfile.txt', mode = 'a') as f:
#     f.write('this is the 4th line') # add a new line

# with open('myfile.txt', mode = 'r') as f:
#     print(f.read())

# with open('newfile.txt', mode = 'w') as f:
#     f.write("This is a new file\nLine2") # create a new file and write to it

# with open('newfile.txt', mode = 'r') as f:
#     print(f.read())


# print('Hello' == 'Hi') # False
# print('hi' == 'Hi') # False
# print(2 == '2') # False
# print(2.0 == 2) # True
# print(1 < 2 and 2 < 3) # True # and, or, not
# print(not True) # False


# hungry = False
# if hungry: 
#   print('Feed dog!')
# else:
#   print('Dog not hungry. ')

# loc = 'Bank'
# if loc == 'Auto Shop':
#   print('loc is Auto Shot')
# elif loc == 'Bank':
#   print('loc is Bank')
# else:
#   print('I have no idea')

# mylist = [1, 2, 3, 4]
# for num in mylist:
#   print(num)
# # 1
# # 2
# # 3
# # 4

# for num in mylist:
#   if num % 2 == 0: # check for even
#     print(num)
#   else:
#     print(f'Odd Number: {num}')
# # Odd Number: 1
# # 2
# # Odd Number: 3
# # 4

# mystr = 'Hello World'
# for letter in mystr:
#   print(letter) # print each char on each line

# for _ in 'Hi': # use low dash if don't need the var
#   print('Cool')
# # Cool
# # Cool

# tup = (1, 2, 3)
# for item in tup: # can iterate over tuple
#   print(item)

# mylist = [(1, 2), (3, 4), (5, 6)]
# for item in mylist:
#   print(item)
# # (1, 2)
# # (3, 4)
# # (5, 6)

# for (a, b) in mylist: # tuple unpacking
#   print(a)
#   print(b)
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6

# for a, b in mylist: # tuple unpacking
#   print(b)
# # 2
# # 4
# # 6

# d = {'k1':1, 'k2':2, 'k3':3}
# for item in d: # by default, only loop over keys in a dict
#   print(item)
# # k1
# # k2
# # k3
# for item in d.items(): # output key-value pair
#   print(item)
# # ('k1', 1)
# # ('k2', 2)
# # ('k3', 3)
# for key, val in d.items(): # output key-value pair using tuple unpacking
#   print(val)
# # 1
# # 2
# # 3
# for val in d.values(): # output only values
#   print(val)
# # 1
# # 2
# # 3

# x = 0
# while x < 5:
#     print(f'The cur val of x is {x}')
#     x += 1
# else:
#     print('x is not less than 5')
# # The cur val of x is 0
# # The cur val of x is 1
# # The cur val of x is 2
# # The cur val of x is 3
# # The cur val of x is 4
# # x is not less than 5

# x = [1, 2, 3]
# for item in x:
#     # if nothing in this part, then will have error
#     pass # this does nothing, but help avoid syntax error
#     # it can act as a place holder for your function content

# mystring = 'sammy'
# for letter in mystring:
#     if letter == 'a':
#         continue # Python has continue statement
#     print(letter)
# # s
# # m
# # m
# # y

# mystring = 'sammy'
# for letter in mystring:
#     if letter == 'a':
#         break # Python has break statement
#     print(letter)
# # s

# for num in range(10): # means range [0, 10)
#     print(num)

# for num in range(3, 10, 2): # means range [3, 10), step of 2
#     print(num)

# print(list(range(0, 11, 2))) # [0, 2, 4, 6, 8, 10] # cast a range to a list

# idx = 0
# for letter in 'abcde':
#     print('at idx {} the letter is {}'.format(idx, letter))
#     idx += 1
# # at idx 0 the letter is a
# # at idx 1 the letter is b
# # at idx 2 the letter is c
# # at idx 3 the letter is d
# # at idx 4 the letter is e

# word = 'abcde'
# for item in enumerate(word): # use enumerate to do same as above cell
#     print(item) # each item is a tuple
# # (0, 'a')
# # (1, 'b')
# # (2, 'c')
# # (3, 'd')
# # (4, 'e')

# # now add tuple unpacking
# word = 'abcde'
# for idx, letter in enumerate(word): 
#     print(idx, letter) 
# # 0 a
# # 1 b
# # 2 c
# # 3 d
# # 4 e

# mylist1 = [1, 2, 3, 4, 5]
# mylist2 = ['a', 'b', 'c']
# mylist3 = ['h', 'i']
# for item in zip(mylist1, mylist2): # zip function produces a "collection" of tuples
#     print(item)
# # (1, 'a')
# # (2, 'b')
# # (3, 'c')
# for item in zip(mylist1, mylist2, mylist3): # zip() takes many inputs, output length is same with the shortest one
#     print(item)
# # (1, 'a', 'h')
# # (2, 'b', 'i')

# print(list(zip(mylist1, mylist2))) # [(1, 'a'), (2, 'b'), (3, 'c')] # cast the output of zip() to a list
# print(zip(mylist1, mylist2, mylist3)) # <zip object at 0x7fb8a01d6240> # produces nothing if you do not cast it

# print('x' in [1, 2, 3]) # False # the "in" operator
# print('x' in ['x', 'y', 'z']) # True # "in" works for a list
# print('abc' in 'xabcdef') # True # "in" also works for string
# print('mykey' in {'key1': 100, 'key2': 200})  # False # "in" works in dict
# print('mykey' in {'mykey': 100, 'key2': 200}) # True

# d = {'mykey': 100, 'key2': 200}
# print(100 in d.values()) # True

# mylist = [1, 3, 4, 5, 5]
# print(min(mylist)) # 1 # return min val in a list
# print(max(mylist)) # 5

# from random import shuffle # import a library
# mylist = [1, 2, 3, 4, 5, 6, 7, 8]
# shuffle(mylist) # shuffle the list in place
# print(mylist) # [8, 1, 6, 3, 4, 2, 5, 7]

# from random import randint
# print(randint(0, 100)) # 96 # return a random integer in range [0, 100]

# my_val = input('What is your name?') # ask for user input, get a string
# print(my_val) # Lisa

# mystring = 'hello'
# mylist = []
# for letter in mystring: # The old way of creating a list
#     mylist.append(letter)
# print(mylist) # ['h', 'e', 'l', 'l', 'o']

# mylist = [letter for letter in mystring] # using list comprehension
# print(mylist) # ['h', 'e', 'l', 'l', 'o']

# mylist = [num for num in range(0, 11)] # using list comprehension
# print(mylist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mylist = [num**2 for num in range(0, 11)] # using list comprehension
# print(mylist) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# mylist = [num for num in range(0, 11) if num%2 == 0] # using list comprehension, only return even numbers
# print(mylist) # [0, 2, 4, 6, 8, 10]

# mylist = [num**2 for num in range(0, 11) if num%2 == 0] # using list comprehension, only return even numbers then square
# print(mylist) # [0, 4, 16, 36, 64, 100]

# celsius = [0, 10, 20, 35.1]
# fahrenheit = [(9/5*temp + 32) for temp in celsius] # more complex calcs
# print(fahrenheit) # [32.0, 50.0, 68.0, 95.18]

# results = [x if x%2==0 else 'Odd' for x in range(0, 11)] # not recommended, hard to read
# print(results) # [0, 'Odd', 2, 'Odd', 4, 'Odd', 6, 'Odd', 8, 'Odd', 10]

# mylist = []
# for x in [2, 4, 6]:
#     for y in [1, 10, 100]:
#         mylist.append(x*y) 
# print(mylist) # [2, 20, 200, 4, 40, 400, 6, 60, 600]

# mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 100]]
# print(mylist) # [2, 20, 200, 4, 40, 400, 6, 60, 600]

# def say_hello():
#     print("Hello")
#     print("Round! ")
# say_hello()

# def say_hello(name):
#     print(f"Hello {name}")
# say_hello("Lisa")

# def say_hello(name='Default name'): # provide a default val for argument
#     print(f"Hello {name}")
# say_hello()

# def add_num(num1, num2): # a function that returns something
#     return num1 + num2
# my_sum = add_num(1, 2)
# print(my_sum)
# add_num('a', 'b') # ab # when inputs are not numbers # Python is dynamically typed, so if create a function that other people use, better check the datatype first

# def even_check(number): # check whether a number is even
#     return number % 2 == 0
# print(even_check(4)) # True
# print(even_check(5)) # False

# def even_check_list(num_list): # check whether list has a num that is even
#     for num in num_list:
#         if num % 2 == 0:
#             return True
#     return False
# print(even_check_list([1, 3, 5])) # False

# def return_even_vals(num_list): # return vals in a list that is even
#     result = []
#     for num in num_list:
#         if num % 2 == 0:
#             result.append(num)
#     return result
# print(return_even_vals([1, 2, 3, 5, 7, 8])) # [2, 8]

# stock_prices = [('APPL', 200), ('GOOG', 300), ('MSFT', 100)]
# for ticker, price in stock_prices: # use tuple unpacking
#     print(ticker)
# # APPL
# # GOOG
# # MSFT
# def price_check(stock_prices_list): # return the tuple with max price
#     cur_max = 0
#     max_ticker = ''
#     for ticker, price in stock_prices_list:
#         if price > cur_max:
#             cur_max = price
#             max_ticker = ticker
#     return (max_ticker, cur_max)
# print(price_check(stock_prices)) # ('GOOG', 300)
# ticker_name, price = price_check(stock_prices) # get result using tuple unpacking, could get error if num of items in tuple not match the num of vars on the left hand side

# my_list = [1, 2, 3, 4, 5, 6, 7]
# from random import shuffle
# shuffle(my_list) # shuffle the list in-place, so returns nothing
# def shuffle_list(input_list): # a function that returns shuffled result
#     shuffle(input_list)
#     return input_list
# print(shuffle_list(my_list)) # [4, 5, 2, 1, 6, 7, 3]

# # in below function, a and b are positional arguments
# def myfunc(a, b): # return 5% of (a+b)
#     return sum((a, b)) * 0.05
# print(myfunc(40, 60)) # 5.0

# # *args allows to take multiple arguments, and internally convert into a tuple
# def myfunc(*args):
#     return sum(args) * 0.05
# print(myfunc(40, 60, 100)) # 10.0

# # it is the * that matters, you can use other names, 
# # but it is best practice to use *args for readability
# def myfunc(*vals):
#     return sum(vals) * 0.05

# # **kwargs allows to take a key-val pairs, and internally convert to a dictionary
# def myfunc(**kwargs):
#     if 'fruit' in kwargs:
#         print(f"My fruit is {kwargs['fruit']}")
#     else: 
#         print('no fruit')
# print(myfunc(fruit='apple')) # My fruit is apple
# print(myfunc(fruit='apple', veggie='cabbage')) # # My fruit is apple

# def myfunc(*args, **kwargs): # you can use both of them in one function
#     print(f"I would like {args[0]} {kwargs['food']}. ")
# print(myfunc(1, 2, 3, food='sandwich', fruit='orange')) # I would like 1 sandwich. # note that args should come ahead of kwargs, because location of both of them is defined

# def square(num):
#     return num**2
# my_nums = [1, 2, 3, 4, 5]
# for item in map(square, my_nums): # apply the func to each elem in the array
#     print(item)
# # 1
# # 4
# # 9
# # 16
# # 25
# print(list(map(square, my_nums))) # [1, 4, 9, 16, 25] # return the result as a list

# def check_even(num):
#     return num%2 == 0
# my_nums = [1, 2, 3, 4, 5, 6]
# print(list(filter(check_even, my_nums))) # [2, 4, 6] # filter takes a func that returns true or false

# # lambda expression (anonymous function)
# print(lambda num: num**2) # <function __main__.<lambda>(num)>
# list(map(lambda num:num**2, my_nums)) # [1, 4, 9, 16, 25, 36]
# list(filter(lambda num: num%2 == 0, my_nums)) # [2, 4, 6]

# name = 'a global string' # global var
# def greet():
#     name = "Sammy"  # enclosing function local
#     def hello(): 
#         name = 'Lisa' # local var
#         print(f"hello {name}")
#     hello()
# greet() # hello Lisa

# name = 'a global string' # global var
# def greet():
#     name = "Sammy"  # enclosing function local
#     def hello(): 
#         print(f"hello {name}")
#     hello()
# greet() # hello Sammy

# name = 'a global string' # global var
# def greet():
#     def hello():
#         print(f"hello {name}")
#     hello()
# greet() # hello a global string

# x = 50
# def func():
#     global x # declare x as global, so you can reach out to global namespace
#     print(f'val of x is {x}')
#     x = 200
#     print(f'val of x is updated globally to {x}')
# func()
# # val of x is 50
# # val of x is updated globally to 200
# print(f'val of x is finally {x}')
# # val of x is finally 200

# # To avoid accidentally overriding global keyword in a large script, 
# # recommend to avoid using global keyword, 
# # and write the function to be like x = func(x) to update x. 

# class Sample():
#     pass
# my_sample = Sample() # create an instance of this class
# print(type(my_sample)) # <class '__main__.Sample'> # return the type of the instance

# class Dog():
#     def __init__(self, breed):
#         self.breed = breed # initialize an attribute for this class
# # my_dog = Dog() # wil return error if do not pass the param breed
# my_dog = Dog(breed='Lab') # create an instance of this class
# print(type(my_dog)) # <class '__main__.Dog'> # return the type of this class
# print(my_dog.breed) # Lab # return the breed attribute of the instance

# class Dog():
#     def __init__(self, breed, name, spots): # more attributes
#         self.breed = breed # initialize an attribute for this class
#         self.name = name
#         self.spots = spots
# my_dog = Dog(breed='lab', name='sammy', spots=False)
# print(my_dog.spots) # False

# class Dog():
#     animal_type = 'mammal' # class object attribute, same for all instances of this class
#     def __init__(self, breed, name, spots): # more attributes
#         self.breed = breed # initialize an attribute for this class
#         self.name = name
#         self.spots = spots
# my_dog = Dog(breed='lab', name='sammy', spots=False)
# print(my_dog.animal_type) # mammal

# class Dog():
#     animal_type = 'mammal' # class object attribute, same for all instances of this class
#     def __init__(self, breed, name, spots): # more attributes
#         self.breed = breed # initialize an attribute for this class
#         self.name = name
#         self.spots = spots
#     def bark(self): # a method of this class
#         print("Woof!")
# my_dog = Dog(breed='lab', name='sammy', spots=False)
# my_dog.bark() # Woof!

# class Dog():
#     animal_type = 'mammal' # class object attribute, same for all instances of this class
#     def __init__(self, breed, name, spots): # more attributes
#         self.breed = breed # initialize an attribute for this class
#         self.name = name
#         self.spots = spots
#     def bark(self): # a method of this class, uses the class attribute
#         print(f"Woof! My name is {self.name}")
# my_dog = Dog(breed='lab', name='sammy', spots=False)
# my_dog.bark() # Woof! My name is sammy

# class Dog():
#     animal_type = 'mammal' # class object attribute, same for all instances of this class
#     def __init__(self, breed, name, spots): # more attributes
#         self.breed = breed # initialize an attribute for this class
#         self.name = name
#         self.spots = spots
#     def bark(self, my_number): # a method of this class, takes a variable
#         print(f"Woof! My name is {self.name}, and my number is {my_number}")
# my_dog = Dog(breed='lab', name='sammy', spots=False)
# my_dog.bark(3) # Woof! My name is sammy, and my number is 3

# class Circle():
#     PI = 3.14
#     def __init__(self, radius=1): # radius has a default value
#         self.radius = radius
#     def get_circumference(self):
#         return self.radius * self.PI * 2
# my_circle = Circle() # use default radius value
# my_circle.get_circumference() # 6.28
# my_circle = Circle(2) # use customized value
# my_circle.get_circumference() # 12.56

# class Circle():
#     PI = 3.14
#     def __init__(self, radius=1): # radius has a default value
#         self.radius = radius
#         self.area = self.PI * radius * radius
#     def get_circumference(self):
#         return self.radius * self.PI * 2
# my_circle = Circle(2) # use customized value
# my_circle.area # 12.56

# class Circle():
#     PI = 3.14  # can use Circle instead of self to refer class attribute
#     def __init__(self, radius=1): # radius has a default value
#         self.radius = radius
#         self.area = Circle.PI * radius * radius
#     def get_circumference(self):
#         return self.radius * Circle.PI * 2

# class Animal():
#     def __init__(self):
#         print("Animal created. ")
#     def who_am_i(self):
#         print("I am an animal. ")
#     def eat(self):
#         print("I am eating. ")
# my_animal = Animal() # Animal created. 
# my_animal.eat() # I am eating. 
# class Dog(Animal): # derive the Animal class
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created. ")
#     def who_am_i(self):
#         print("I am a dog!")
#     def bark(self):
#         print("Woof! ")
# mydog = Dog()
# # Animal created. 
# # Dog created. 
# mydog.eat() # this dog instance can reuse the animal methods via inheritance
# # I am eating. 
# mydog.who_am_i() # it can overwrite the animal methods
# # I am a dog!
# mydog.bark() # it can add new methods
# # Woof! 

# class Dog():
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name + " says woof! "
# class Cat():
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name + " says meow! "
# niko = Dog("Niko")
# felix = Cat("felix")
# for pet in [niko, felix]: # example of polymorphism
#     print(pet.speak())
# # Niko says woof! 
# # felix says meow! 
# def pet_speak(pet):
#     print(pet.speak())
# pet_speak(niko)
# pet_speak(felix)
# # Niko says woof! 
# # felix says meow!

# class Animal(): # abstract class
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         raise NotImplementedError("this is an abstract method")
# my_animal =  Animal('fred')
# # my_animal.speak() # NotImplementedError 
# class Dog(Animal):
#     def speak(self):
#         return self.name + ' says woof! '
# fido = Dog('Fido')
# fido.speak() # 'Fido says woof! '

# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def __str__(self): # return the string representation of the object
#         return f"{self.title} by {self.author}"
#     def __len__(self):
#         return self.pages
# mybook = Book('mytitle', 'myauthor', 100)
# print(mybook) # mytitle by myauthor # this calls the __str__(self) 
# print(str(mybook)) # mytitle by myauthor # this also calls __str__(self)
# print(len(mybook)) # 100 # this calls __len__(self)
# del mybook # delete the instance of this Book object, works without __del__() defined

# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def __str__(self): # return the string representation of the object
#         return f"{self.title} by {self.author}"
#     def __len__(self):
#         return self.pages
#     def __del__(self):
#         print("A book object has been deleted. ")
# mybook = Book('mytitle', 'myauthor', 100)
# del mybook # A book object has been deleted. # now also calls __del__() , and delete the instance

# def add(n1, n2):
#     print (n1 + n2)
# num1 = 1
# num2 = '2'
# try: 
#     add(num1, num2)
# except:
#     print('Error adding two numbers!')
# # Error adding two numbers!
# try: 
#     add(num1, num2)
# except: # runs if try block has error
#     print('Error adding two numbers!')
# else: # runs if try block had no issue
#     print("Add went well!")
# finally:
#     print("I run anyway!")
# # Error adding two numbers!
# # I run anyway!

# try: 
#     f = open('testfile.txt', 'w') # write mode
#     f.write("Write a test line")
# except TypeError:
#     print("There was a type error! ")
# except OSError:
#     print("You have an OS Error! ")
# finally:
#     print('I always run!')
# # I always run!

# try: 
#     f = open('testfile.txt', 'r') # read mode
#     f.write("Write a test line")
# except TypeError:
#     print("There was a type error! ")
# except OSError:
#     print("You have an OS Error! ")
# except: # catch anything else
#     print("All other exceptions! ")
# finally:
#     print('I always run!')
# # You have an OS Error! 
# # I always run!

# def ask_for_int():
#     try: 
#         result = int(input('Please provide a number: '))
#     except:
#         print("That is not a number. ")
#     finally: 
#         print("End of the block. ")
# ask_for_int() # provide 20 as input
# # End of the block.
# ask_for_int() # provide a as input
# # That is not a number. 
# # End of the block.  

# def ask_for_int():
#     while True:
#         try: 
#             result = int(input('Please provide a number: '))
#         except:
#             print("That is not a number. ")
#             continue
#         else: 
#             print('Yes, thank you')
#             break
#         finally:
#             print('End of one loop')
# ask_for_int() # provide 20
# # Yes, thank you
# # End of one loop
# ask_for_int() # provide a, then 2
# # That is not a number. 
# # End of one loop
# # Yes, thank you
# # End of one loop



















# def create_cubes_v1(n): # generates the list in memory as a whole
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result

# print(create_cubes_v1(10)) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# def create_cubes_v2(n): # the memory efficient way
#     for x in range(n):
#         yield x**3

# for x in create_cubes_v2(10):
#     print(x)

# print(list(create_cubes_v2(10)))  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# def gen_fib(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a+b

# print(list(gen_fib(10))) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# def simple_gen():
#     for x in range(3):
#         yield x

# for x in simple_gen(): # 0 1 2
#     print(x)

# g = simple_gen()
# print(next(g)) # 0
# print(next(g)) # 1
# print(next(g)) # 2
# # print(next(g)) # StopIteration Error. Note we don't get this error in "for loop" because it automatically catches the error. 

# s = 'hello'
# for letter in s: # h e l l o
#     print(letter)

# # next(s) # TypeError: 'str' is not an iterator
# s_iter =  iter(s)
# print(next(s_iter)) # h
# print(next(s_iter)) # e

# from collections import Counter
# my_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 'abc', 'a', 'a']
# c = Counter(my_list)
# print(c) # Counter({3: 8, 1: 4, 2: 2, 'a': 2, 'abc': 1})
# print(c.most_common()) # [(3, 8), (1, 4), (2, 2), ('a', 2), ('abc', 1)]. Orders by most common elements
# print(c.most_common(2)) # [(3, 8), (1, 4)]. Orders by most common elements, list 2. 
# print(list(c)) # [1, 2, 3, 'abc', 'a']. convert keys to a list


# d = {'a':10} # this is a regular dictionary
# print(d['a']) # 10. prints the value of key 'a'
# print(d['wrong']) # returns error, because key does not exist

# from collections import defaultdict
# d = defaultdict(lambda: 0) # set default value of this dict
# d['a'] = 10
# print(d['a']) # 10
# print(d['wrong']) # returns 0, because key does not exist, so use default value

# my_tuple = (1, 2, 3)
# print(my_tuple[0]) # 1

# from collections import namedtuple
# Dog = namedtuple('Dog', ['age', 'breed', 'name'])
# sammy = Dog(age=5, breed = 'Husky', name = 'Sam')
# print(type(sammy)) # <class '__main__.Dog'>
# print(sammy) # Dog(age=5, breed='Husky', name='Sam')
# print(sammy.breed) # Husky
# print(sammy[1]) # Husky

# f = open('practice.txt', 'w+')
# f.write('This is a test string')
# f.close()

# import os
# print(os.getcwd()) # returns current working directory
# print(os.listdir()) # returns list of items as strings in cur dir
# print(os.listdir('/Users/lisa/Desktop')) # returns list of items as strs in this dir
# os.unlink('practice.txt') # delete this file
# os.rmdir('/Users/lisa/Desktop/my_folder') # delete this folder

# import shutil
# shutil.move('practice.txt', '/Users/lisa/Desktop') # move this file to this folder
# shutil.rmtree('/Users/lisa/Desktop/my_folder') # delete all files and folders in this folder

# import send2trash # pip install send2trash
# send2trash.send2trash('practice.txt') # sends file to trash bin, instead of permanent removal

# # recursively visit each nested dirs and files in this folder
# for folder, sub_folders, files in os.walk('/Users/lisa/Desktop/my_folder'):
#     print(f"Currently looking at {folder}\n")
#     print('The subfolders are: ')
#     for sub_folder in sub_folders:
#         print(f'\t Subfolder: {sub_folder}')
#     print('\nThe files are:')
#     for f in files:
#         print(f'\t File: {f}')

# import datetime
# my_time = datetime.time(2, 20) # hr, min, second, microsecond in 24 hr format
# print(my_time.minute) # 20
# print(my_time.hour) # 2
# print(my_time) # 02:20:00

# my_time = datetime.time(13, 20, 1, 20)
# print(my_time) # 13:20:01.000020
# print(type(my_time)) # <class 'datetime.time'>

# today = datetime.date.today()
# print(today) # 2023-03-20
# print(today.year) # 2023
# print(today.ctime()) # Mon Mar 20 00:00:00 2023

# from datetime import datetime
# my_datetime = datetime(2023, 3, 20, 15, 46, 12)
# print(my_datetime) # 2023-03-20 15:46:12
# my_datetime = my_datetime.replace(year=2024)
# print(my_datetime) # 2024-03-20 15:46:12

# from datetime import date
# date1 = date(2023, 3, 20)
# date2 = date(2024, 4, 20)
# print(date2 - date1) # 397 days, 0:00:00
# print(type(date2 - date1)) # <class 'datetime.timedelta'>

# datetime1 = datetime(2023, 3, 20, 3)
# datetime2 = datetime(2024, 4, 20, 4)
# print(datetime2 - datetime1) # 397 days, 1:00:00
# print(type(datetime2 - datetime1)) # <class 'datetime.timedelta'>
# print((datetime2 - datetime1).total_seconds()) # 34304400.0

# import math
# value = 4.35
# print(math.floor(value)) # 4
# print(math.ceil(value)) # 5
# print(round(4.5)) # 4 (round toward the even number if half way)
# print(round(5.5)) # 6 (round toward the even number if half way)
# print(math.pi) # 3.141592653589793
# print(math.e) # 2.718281828459045
# print(math.log(math.e)) # 1.0
# print(math.log(100, 10)) # 2.0
# print(math.inf) # inf
# print(math.nan) # nan
# print(math.sin(10)) # -0.5440211108893698
# print(math.degrees(math.pi/2)) # 90.0
# print(math.radians(180)) # 3.141592653589793

# from math import pi
# print(pi) # 3.141592653589793

# import random
# print(random.randint(0, 100)) # return an int within [0, 100]
# random.seed(42) # if start with a fixed seed, will always use the same rand vals, no matter how many times you run it
# print(random.randint(0, 100)) # 81
# print(random.randint(0, 100)) # 14
# print(random.randint(0, 100)) # 3

# my_list = list(range(0, 20))
# print(random.choice(my_list)) # randomly choose a val from my_list

# print(random.choices(population=my_list, k=10)) # sample 10 elems with replacement
# print(random.sample(population=my_list, k=10)) # sample 10 elems without replacement
# random.shuffle(my_list) # shuffle the list in place
# print(my_list)
# print(random.uniform(a=0, b=100)) # choose a real number between a and b, each number have same likelihood of being chosen
# print(random.gauss(mu=0, sigma=1)) # choose a real number between a and b, distribution is gauss distribution

# import pdb
# x = [1, 2, 3]
# y = 2
# z = 3
# result = y + z
# pdb.set_trace() # set the trace before error line, press q to quit debugger
# # command line:
# # (Pdb) result
# # 5
# # (Pdb) y
# # 2
# # (Pdb) x
# # [1, 2, 3]
# result2 = x + y # should get an error, cannot add integer to a list

# text = "The agent's phone number is 408-555-1234. Call soon!"
# print('phone' in text) # returns True

# import re
# pattern = 'not in text'
# print(re.search(pattern, text)) # None
# pattern = 'phone'
# print(re.search(pattern, text)) # <re.Match object; span=(12, 17), match='phone'>
# match = re.search(pattern, text) # will only get the first match
# print(match.span()) # (12, 17)
# print(match.start()) # 12
# print(match.end()) # 17

# text = "phone once, phone twice"
# matches = re.findall('phone', text) # find all patterns in a string
# print(matches) # ['phone', 'phone']
# for match in re.finditer('phone', text): # find each match
#     print(match)
# # returns: 
# # <re.Match object; span=(0, 5), match='phone'>
# # <re.Match object; span=(12, 17), match='phone'>

# import re
# text = 'My phone number is 123-456-7890'
# phone = re.search('123-456-7890', text)
# print(phone) # <re.Match object; span=(19, 31), match='123-456-7890'>
# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text) # need r before string pattern
# print(phone) # <re.Match object; span=(19, 31), match='123-456-7890'>
# print(phone.group()) # 123-456-7890

# phone = re.search(r'\d{3}-\d{3}-\d{4}', text) # need r before string pattern
# print(phone) # <re.Match object; span=(19, 31), match='123-456-7890'>
# print(phone.group()) # 123-456-7890

# phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # '()-()-()' groups 3 regex
# results = re.search(phone_pattern, text)
# print(results.group()) # 123-456-7890
# # access each of the 3 groups, idx starts from 1: 
# print(results.group(1)) # 123
# print(results.group(2)) # 456
# print(results.group(3)) # 7890

# import re
# print(re.search(r'cat', 'The cat is here')) # <re.Match object; span=(4, 7), match='cat'>
# print(re.search(r'cat|dog', 'The dog is here')) # <re.Match object; span=(4, 7), match='dog'> # the pipe operator, for "or" operation
# print(re.findall(r'at', 'The cat in the hat sat there.')) # ['at', 'at', 'at']
# print(re.findall(r'.at', 'The cat in the hat sat there.')) # ['cat', 'hat', 'sat'] # wildcard operator
# print(re.findall(r'...at', 'The cat in the hat sat there.')) # ['e cat', 'e hat'] # wildcard operator
# print(re.findall(r'^\d', '2 is a number')) # ['2'] # search for the number that starts the string, ^ means starts with
# print(re.findall(r'\d$', '2 is a number, so is 3')) # ['3'] # search for the number that ends the string, $ means ends with
# phrase = 'there are 3 numbers 34 inside 5 this sentence'
# pattern = r'[^\d]+' # exclude single/continuous digits, [] are often used for excludes
# print(re.findall(pattern, phrase)) # ['there are ', ' numbers ', ' inside ', ' this sentence']

# phrase = 'This is a string! But it has punctuation. We need to remove them. '
# print(re.findall(r'[^!.?]+', phrase)) # ['This is a string', ' But it has punctuation', ' We need to remove them', ' ']
# words = re.findall(r'[^!.? ]+', phrase) # ['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'We', 'need', 'to', 'remove', 'them'] # also removes spaces, and return a list
# print(words) 
# print(' '.join(words)) # This is a string But it has punctuation We need to remove them

# text = 'Only find the dash-words in this sentence. But you do not know how long-ish they are. '
# pattern = r'[\w]+'
# print(re.findall(pattern, text)) # ['Only', 'find', 'the', 'dash', 'words', 'in', 'this', 'sentence', 'But', 'you', 'do', 'not', 'know', 'how', 'long', 'ish', 'they', 'are'] # return all alphanumerics. 
# pattern = r'[\w]+-[\w]+' # alphanumerics-alphanumerics
# print(re.findall(pattern, text)) # ['dash-words', 'long-ish']

# text = 'Hello, would you like some catfish? or catnap? or caterpillar?'
# pattern = r'cat(fish|nap|claw)' # use () for a group of or operations
# print(re.search(pattern, text)) # <re.Match object; span=(27, 34), match='catfish'>

# def func_one(n):
#     return [str(num) for num in range(n)]

# print(func_one(10)) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# def func_two(n):
#     return list(map(str, range(n)))

# print(func_two(10)) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# # method 1: use time difference. Problem: precision is not good enough for fast code
# import time
# start_time =  time.time()
# result = func_one(1000000)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time) # 0.06716489791870117 # unit is in seconds

# start_time =  time.time()
# result = func_two(1000000)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time) # 0.06970787048339844 

# # method 2: use the timeit module. 
# import timeit
# statement = '''
# func_one(100)
# ''' # the statement to test performance, in the form of a string
# setup = '''
# def func_one(n):
#     return [str(num) for num in range(n)]
# ''' # the function used in the statement
# avg_time = timeit.timeit(statement, setup, number=1000000)
# print(avg_time) # 5.778604458086193
# statement = '''
# func_two(100)
# ''' # the statement to test performance, in the form of a string
# setup = '''
# def func_two(n):
#     return list(map(str, range(n)))
# ''' # the function used in the statement
# avg_time = timeit.timeit(statement, setup, number=1000000)
# print(avg_time) # 5.254787957994267

# f = open('file1.txt', 'w+')
# f.write('one file')
# f.close()

# f = open('file2.txt', 'w+')
# f.write('two file')
# f.close()

# import zipfile # this has to put file into zip one by one
# comp_file = zipfile.ZipFile('comp_file.zip', 'w') # write items to this zip file
# comp_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()

# zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
# zip_obj.extractall('extracted_content') # unzip to this folder

# import shutil # this can do a dir into a zip all at once
# dir_to_zip = '/mypath/extracted_content'
# output_filename = 'example'
# shutil.make_archive(output_filename, 'zip', dir_to_zip) # will zip source dir into example.zip file 
# shutil.unpack_archive('example.zip', 'folder_to_unzip', 'zip') # unzip to this folder

# import requests
# result = requests.get("http://www.example.com")
# print(type(result)) # requests.models.Response
# print(result.text) # return the html document contents # '<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'

# import bs4 # beautifulSoup library can obtain info from html string
# soup = bs4.BeautifulSoup(result.text, "lxml") # lxml is the engine to use to parse the html text
# print(soup) # # makes it easy to read, in indented format, with multiple lines
# soup.select('title') # grab things from the html document, based on tag name, returns a list # [<title>Example Domain</title>]
# soup.select('p') # 
# # [<p>This domain is for use in illustrative examples in documents. You may use this
# #      domain in literature without prior coordination or asking for permission.</p>,
# #  <p><a href="https://www.iana.org/domains/example">More information...</a></p>]
# soup.select('title')[0].getText() # getText() method removes the tag name in the specified bs4 object element # 'Example Domain'
# soup.select('div') # returns all elements with a 'div' tag
# soup.select('#my_id') # returns elements with this id
# soup.select('.my_class') # returns elements with this class
# soup.select('div span') # returns elements with tag name 'span' within a 'div' element
# soup.select('div > span') # returns elements with tag name 'span' directly within a div element, with nothing in between

# import requests
# import bs4
# res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup.select('div .vector-toc-text'))
# # Output exceeds the size limit. Open the full output data in a text editor
# # [<div class="vector-toc-text">(Top)</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">1</span>Early life and education</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2</span>Career</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2.1</span>World War II</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2.2</span>UNIVAC</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2.3</span>COBOL</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2.4</span>Standards</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">3</span>Retirement</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">4</span>Post-retirement</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">5</span>Anecdotes</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">6</span>Death</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">7</span>Dates of rank</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">8</span>Awards and honors</div>,
# # ...
# #  <span class="vector-toc-numb">13</span>References</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">14</span>Further reading</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">15</span>External links</div>]
# print(soup.select('div .vector-toc-text')[1].text) # '\n1Early life and education'
# for item in soup.select('div .vector-toc-text'):
#     print(item.getText())
# # Output exceeds the size limit. Open the full output data in a text editor
# # (Top)

# # 1Early life and education

# # 2Career

# # 2.1World War II

# # 2.2UNIVAC

# # 2.3COBOL

# # 2.4Standards

# # 3Retirement

# # 4Post-retirement

# # 5Anecdotes

# # 6Death

# # 7Dates of rank

# # 8Awards and honors
# # ...

# # 14Further reading

# # 15External links


# import requests
# import bs4
# res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# list_of_img_tags = soup.select('img')
# # print(list_of_img_tags[3]) # shows an image tag
# list_of_img_tags = soup.select('.thumbimage')
# # print(list_of_img_tags)
# link1_text = list_of_img_tags[0]['src']
# print(link1_text)
# img_link = requests.get('https:' + link1_text)
# print('https:' + link1_text)
# f = open('image.jpg', 'wb') # write binary for this image
# f.write(img_link.content)
# f.close()

# from PIL import Image # pip install pillow
# image_file = Image.open('cat.jpg')
# # image_file.show() # this opens the image to view
# print(image_file.size) # (481, 480) # print out the size of the image
# print(image_file.filename) # cat.jpg 
# print(image_file.format_description) # JPEG (ISO 10918)
# image_file.crop((0, 0, 100, 200)).show() # origin is top left corner. start from origin, width = 100px, and hight = 200px. returns the cropped file. 
# cropped_file = image_file.crop((50, 50, 100, 200))
# image_file.paste(im=cropped_file, box=(0, 0)) # put cropped_file at origin of the image_file, modify image_file in-place
# image_file.show()
# image_file.resize((2000, 300)).show() # stretch this file, return a stretched file
# image_file.rotate(90).show() # rotate this image by 90 deg, return a new file

# red = Image.open('red.jpg') # opens a red image
# blue = Image.open('blue.jpg') # opens a blue image
# blue.putalpha(128) # changes the transparency of this image in place. 0 is complete transparent, 255 is not transparent at all
# red.putalpha(128) 
# blue.paste(im=red, box=(0, 0)) # paste red on top of blue, now blue is a purple image
# blue.save('purple.png') # save this image as file, overwrite if already exists

# import csv
# data = open('example.csv', encoding='utf-8')
# csv_data = csv.reader(data)
# data_lines = list(csv_data) # a col list of row val lists
# for line in data_lines[:5]:
#     print(line) # print the first 5 rows
# # write to a csv file: 
# output_file = open('saved-file.csv', mode='w', newline='')
# csv_writer = csv.writer(output_file, delimiter=',')
# csv_writer.writerow(['a', 'b', 'c']) # write a single row
# csv_writer.writerows(['1', '2', '3'], ['4', '5', '6']) # write multiple rows
# output_file.close()
# f = open('saved-file.csv', mode='a', newline='') # append to this file
# csv_writer = csv.writer(f)
# csv_writer.writerow(['a2', 'b2', 'c2']) 
# f.close()

# import PyPDF2 # pip install PyPDF2
# f = open('test.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
# print(pdf_reader.numPages) # show num of pages in the pdf file
# page0 = pdf_reader.getPage(0) # grab the first page
# page0_text = page0.extractText() # extract text as string
# print(page0_text)
# f.close()

# # write to a new pdf file
# f = open('test.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
# page0 = pdf_reader.getPage(0) 
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(page0)
# f_out = open('newfile.pdf', 'wb')
# pdf_writer.write(f_out)
# f_out.close()

# import smtplib
# smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_obj.ehlo() # greets the server, need to be immediately after obj creation
# smtp_obj.starttls() # initiate TLS encryption
# import getpass
# email = getpass.getpass("Email: ") # will hide your input
# pwd = getpass.getpass("App Password: ") 
# smtp_obj.login(email, pwd)
# from_address = email
# to_address = email
# subject =  "This is my subject"
# message = "This is my message"
# msg = "Subject: " + subject + '\n' + message # construct the email text
# smtp_obj.sendmail(from_address, to_address, msg)
# smtp_obj.quit() # close the connection

# import imaplib
# M = imaplib.IMAP4_SSL('imap.gmail.com')
# import getpass
# email = getpass.getpass("Email: ")
# pwd = getpass.getpass("App Password: ") 
# M.login(email, pwd)
# M.list() # shows everything you can check in your email
# M.select('inbox')
# my_type, my_ids = M.search(None, 'SUBJECT "This is my subject"')
# id1 = my_ids[0] # the id of the first email in the search result
# print(id1)
# result, email_data = M.fetch(id1, '(RFC822)')
# print(email_data) # all sorts of info, including email subject and content
# raw_email = email_data[0][1]
# raw_email_string = raw_email.decode('utf-8')
# import email # parses the raw_email_string
# email_message = email.message_from_string(raw_email_string)
# for part in email_message.walk():
#     if part.get_content_type() == 'text/plain':
#         body = part.get_payload(decode=True)
#         print(body) # b'This is my message\r\n'
# M.close()

# print(hex(12)) # 0xc
# print(bin(3)) # 0b11
# print(pow(2, 3)) # 8
# print(abs(-2)) # 2
# print(round(3.1)) # 3
# print(round(3.141592, 2)) # 3.14

# s = 'hello world'
# print(s.capitalize()) # Hello world # capitalizes the first word in the str
# print(s.upper()) # HELLO WORLD
# print(s.lower()) # hello world
# print(s.count('o')) # 2 # count num of letter o in the str
# print(s.find('o')) # 4 # find the first idx of o
# print(s.center(20, '-')) # ----hello world----- # center the string between dashes, total length is 20
# s = 'hello'
# print(s.isalnum()) # True # checks if all chars in str are alpha-numeric 
# print(s.isalpha()) # True # checks if all chars in str are alphabetic 
# print(s.islower()) # True # checks if all chars in str are lowercase
# print(s.isupper()) # False # checks if all chars in str are uppercase
# print(s.isspace()) # False # checks if all chars in str are whitespace
# print(s.istitle()) # False # checks if each word start with an upper case letter
# print(s.endswith('o')) # True
# print(s.split('e')) # ['h', 'llo'] # separate at every occurrence
# print(s.partition('l')) # ('he', 'l', 'lo')

# s = set()
# s.add(1)
# s.add(2)
# s.add(2)
# print(s) # {1, 2}
# s.clear()
# print(s) # set()
# s = {1, 2, 3}
# sc = s.copy() # copy is a deep copy
# print(sc) # {1, 2, 3}
# s.add(4)
# print(sc) # {1, 2, 3}
# print(s.difference(sc)) # {4} # shows the difference between two sets
# s.difference_update(sc) # {4} # remove from s the duplicates between s and sc
# print(s)
# s = {1, 2, 3, 4}
# s.discard(2)
# print(s) # {1, 3, 4} 
# s1 = {1, 2, 3}
# s2 = {1, 2, 4}
# print(s1.intersection(s2)) # {1, 2}
# s1.intersection_update(s2) # update s1 as the intersection
# print(s1) # {1, 2}
# s1 = {1, 2}
# s2 = {1, 2, 4}
# s3 = {5}
# print(s1.isdisjoint(s2)) # False # if have no common elems
# print(s3.isdisjoint(s2)) # True
# print(s1.issubset(s2)) # True
# print(s2.issuperset(s1)) # True
# print(s1.union(s2)) # {1, 2, 4}
# s1.update(s2) # s1 becomes the union of both

# d = {'k1': 1, 'k2': 2}
# print({x:x**2 for x in range(10)}) # using list comprehension to create a dict
# # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# print({k:v**2 for k,v in zip(['a', 'b', 'c'], range(10))})
# # {'a': 0, 'b': 1, 'c': 4}
# for pair in d.items():
#     print(pair)
# # ('k1', 1)
# # ('k2', 2)
# for k in d.keys():
#     print(k)
# # k1
# # k2
# for v in d.values():
#     print(v)
# # 1
# # 2

# l = [1, 2, 3]
# l.append(4)
# print(l) # [1, 2, 3, 4]
# print(l.count(3)) # 1 # count num of occurrences of 3
# l.append([4, 5])
# print(l) # [1, 2, 3, 4, [4, 5]]
# l.extend([6, 7]) # append one by one from the iterable
# print(l) # [1, 2, 3, 4, [4, 5], 6, 7]
# print(l.index(7)) # 6 # will get error if val not exist
# l.insert(2, 'inserted') # insert at idx 2
# print(l) # [1, 2, 'inserted', 3, 4, [4, 5], 6, 7]
# print(l.pop()) # 7 # pop last elem out of the list
# print(l) # [1, 2, 'inserted', 3, 4, [4, 5], 6]
# print(l.pop(0)) # 1 # pop the indexed elem out of the list
# print(l) # [2, 'inserted', 3, 4, [4, 5], 6]
# l.remove('inserted') # remove the first occurrence of 'inserted'
# print(l) # [2, 3, 4, [4, 5], 6]
# l = [1, 2, 3]
# l.reverse()
# print(l) # [3, 2, 1]
# l.sort()
# print(l) # [1, 2, 3]






