
#task1 gramm to ounce
def grams_to_ounces(grams): 
    return 28.3495231 * grams


#task2 farenhait to celcius
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


#task3 chicken and rabbits
def solve(numheads, numlegs):
    for i in range(numheads + 1):
        b = numheads - i
        if 2 * i + 4 * b == numlegs:
            return i, b
    return "No solution"

#task4 checking prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False  
    return True  


def filter_prime(numbers):
    prime_numbers = []  

    for i in numbers:  
        if is_prime(i): 
            prime_numbers.append(i) 

    return prime_numbers  


#task5 permutation
from itertools import permutations

def print_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    for i in perms:
        print(i) 



#task6 reversing
def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

#task7 next 33
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


#task8 finding 007
def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False
[8,0,8,9,0,5,0,7, 7, 8, 6, 0, 0, 7]

import math

#task9 volume of shpere
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

#task10 unique element
def unique_elements(lst):
    unique = []
    for item in lst:
        if lst.count(item) == 1:  
            unique.append(item)
    return unique

#task11 finding palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    s_list = list(s)
    s_list.reverse()
    return s == ''.join(s_list)

#task12 histogramma ****
def histogram(lst):
    for num in lst:
        print('*' * num)


#task13 randon game
import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break




#usage
print(grams_to_ounces(100))
print(fahrenheit_to_celsius(98.6))
print(solve(35, 94))
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print_permutations("abc")
print(reverse_sentence("We are ready"))
print(has_33([1, 3, 3]))
print(spy_game([1,2,4,0,0,7,5]))
print(sphere_volume(5))
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
print(is_palindrome("madam"))
histogram([4, 9, 7])
guess_the_number()
