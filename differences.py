
# user_input = input('What is your name?')
# print(user_input)

# def reverseIt(x):
#     return x[::-1] # this is slice statement that means to start at the end and move one step backwards

# myString = reverseIt ("a man, a plan, a canal, frenemies!")

# print(myString)

# a = 10
# b = 30


# a, b = b, a 
# print("a is now " + str(a) + ", and b is now " + str(b))

# numbers = [70, 95, 97, 55, 3, 24, 89, 97, 84, 11]

# total = 1 

# for number in numbers:
#     total = total * number

    
# print('the total is:', total)

# def check_divisible(number):
#     if number % 3 == 0 and number % 5 == 0: # if number 3 is divided by 3 and the remainder is 0 then return x
#         return "Fizzbuzz"
#     elif number % 3 == 0:
#         return "Buzz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else: return str(number)
    
# print(check_divisible(3))   
# print(check_divisible(5))   
# print(check_divisible(15))  
# print(check_divisible(7)) 

# def get_fibonacci(position):
#     if position < 0:
#         return None
    
#     if position <= 1:
#         return position
    
#     prev = 0 
#     current = 1

#     for i in range(2, position + 1):
#         next_num = prev + current 

#         prev = current 
#         current = next_num

#     return current

# print(get_fibonacci(0))  # Returns 0
# print(get_fibonacci(1))  # Returns 1
# print(get_fibonacci(2))  # Returns 1
# print(get_fibonacci(3))  # Returns 2
# print(get_fibonacci(4))  # Returns 3
# print(get_fibonacci(6))  # Returns 8

def fibonacci_nth(n):
   if n < 0:
       return None
   if n <= 1:
       return n
   
   prev = 0 
   current = 1

   for i in range(2, n + 1):
       
       next_num = prev + current

       prev = current
       current = next_num
   return current

print(fibonacci_nth(9))

def search_array(array, value):
    for element in array:
        if element == value:
            return True 
    return False

my_list = [1, 2, 3, 4, 5]
print(search_array(my_list, 3))  # Output: True
print(search_array(my_list, 6))  # Output: Fals

def is_palindrome(str):
    for i in range(len(str)// 2):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))

def has_dupes(arr):
    seen = {}
    for element in arr:
        if element in seen:
            return True
        seen[element] = True
    return False

print(has_dupes([1, 2, 3, 4, 5]))  # Output: False
print(has_dupes([1, 2, 3, 3, 4]))  # Output: True
print(has_dupes(['apple', 'banana', 'orange', 'apple']))  # Output: True
print(has_dupes([10, 20, 30]))  # Output: False