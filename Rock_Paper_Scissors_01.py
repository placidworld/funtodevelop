# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:56:43 2020

@author: heart
"""

"""
This is a 
multi-line
comment!
Codeacademy - Learn Python
Rock Paper Scissors
"""
from random import randint
options = ["ROCK", "PAPER", "SCISSORS"]
message = {"tie": "Yawn it's a tie!",
           "won": "Yay you won!",
           "lost": "Aww you lost!"
          }

def decide_winner(user_choice, computer_choice):
	print ("You selected: %s" % user_choice)
	print ("Computer selected: %s" % computer_choice)
	if user_choice == computer_choice: 
 		print (message["tie"])
	elif user_choice == options[0] and computer_choice == options[2]:
		print (message["won"])
	elif user_choice == options[1] and computer_choice == options[0]:
		print (message["won"])
 	elif user_choice == options[2] and computer_choice == options[1]:
		print (message["won"])
	else:
		print (message["lost"])
def play_RPS():
	user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
	user_choice = user_choice.upper()
	computer_choice = options[randint(0, 2)]
	decide_winner(user_choice, computer_choice)
 
play_RPS()



lloyd = {
  "name" : "Lloyd",
  "homework" : [],
  "quizzes" : [],
  "tests" : []
}

alice = {
  "name" : "Alice",
  "homework" : [],
  "quizzes" : [],
  "tests" : []
}

tyler = {
  "name" : "Tyler",
  "homework" : [],
  "quizzes" : [],
  "tests" : []
}


lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]
for student in students:
  print student["name"]
  print student["homework"]
  print student["quizzes"]
  print student["tests"]

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  
  total = homework *.1 + quizzes * .3 + tests * .6
  return total

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"
  
print get_letter_grade(get_average(lloyd))


def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)


avg = get_class_average(students)
print(avg)
print(get_letter_grade(avg))