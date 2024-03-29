# -*- coding: utf-8 -*-
"""AI_Lab_Task_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/133xExV8rsHtweEseCrETZ9GYs2Q5XVjW

# Lab Task # 2

---


Roll Number: BSCS18030

---


Name: Mubashir Rehman

Q1. Input Total Marks and Obtained Marks from the user and display the percentage of Obtained Marks. (1.5 marks)
"""

totalMarks = int(input("Enter total marks: "))
obtMarks = int(input("Enter obtained marks: "))
print("Percentage of obtained marks: ", (obtMarks/totalMarks)*100, "%")

"""Q2. Input height of a person in centimeters and convert it into feet and inches. (For example, 65cm is equal to 2 feet 2 inches) (3.5 marks)"""

height = int(input("Enter height in centimeters: "))
#1cm = 0.4 inches
inches = height*0.4
feet = int(inches/12)
inches = int(inches-int(feet*12))
print("Height is: ",feet," feet ",inches,"inches")

"""Q3. Take a number as an input from the user and display "Even" if it is an even number and display "Odd" is it is an odd number. (1.5 marks)"""

number = int(input("Enter a number: "))
print("Even") if number%2==0 else print("Odd")

"""Q4. Input X and Y coordinates and determine in which quadrant the coordinate point lies. (3.5 marks)

---


(Quadrant1: X and Y are positive, Quadrant2: X is negative and Y is positive, Quadrant3: X and Y are negative, Quadrant4: X is positive and Y is negative)
"""

x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))
if (x > 0):
  if (y > 0):  print("Quadrant1")
  else: print("Quadrant4")
elif (x< 0):
  if (y > 0): print("Quadrent2")
  else: print("Quadrent3")

"""Q5. Take a Sentence from the user as input and save each word inside a list "Words" using a loop. After this, print the list in reverse order. (5 marks)

"""

sentence = input("Enter your sentence: ")
words = []
for word in sentence.split():
  words.append(word)
print(words[::-1])

"""Q6. Take a range as an input and print prime numbers upto that range. (for example, if I enter 100, the program should print prime numbers between 2 and 100) (5 marks)"""

lowerLimit=int(input("Enter lower bound: "))
upperLimit=int(input("Enter upper bound: "))
print("Prime between ",lowerLimit," and ",upperLimit," numbers are:")
for number in range(lowerLimit,upperLimit):
  if number > 1:
    for i in range(2,number):
      if number % i == 0:
        break
    else:
      print(number)

"""Q7. Take a whole number from the user as an input and determine whether it is a prime number or not. (5 marks)"""

number = int(input("Enter a whole number:"))
isPrime = False
for i in range(2,number):
  if (number%i==0):
    break
  else:
    isPrime=True
print(number," is a Prime number") if isPrime==True else print(number," is not a Prime number")

"""Q8. Take 4 numbers as input and display the largest number. (5 marks)"""

numbers = []
for i in range(4):
  numbers.append(int(input("Enter number a number:")))
numbers.sort()
print("Largest Number is",numbers[-1])

"""Q9. Take 4 numbers as input and display the second largest number. (5 marks)"""

numbers = []
for i in range(4):
  numbers.append(int(input("Enter number a number:")))
numbers.sort()
print("Second Largest Number is",numbers[-2])

"""Q10. Take a number as input and display the total number of digits in the number. (5 marks)"""

number = int(input("Enter a number: "))
digits = 0
while number:
  number=int(number/10)
  digits+=1
print("Number of digits are: ",digits)