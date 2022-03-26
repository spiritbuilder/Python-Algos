# -*- coding: utf-8 -*-
import random
from Questions import Question
import django
import uuid
import functools


#print(result) 

print (random.randint(1,2))
# prompts = ["What is the Color of the Nigerian Flag\n(a) Green \n(b) Gold\n(c) Yellow\n(d) Grey",
#              "Who is currently Invading Ukraine\n(a) USA \n(b) Greece\n(c) Afghanistan\n(d) Russia",
#              "Who is the Nigerian President\n(a) Biden \n(b) James Bond\n(c) Buhari\n(d) Osinbajo"]

# questions=[Question(prompts[0], "a"),Question(prompts[1], "d"),Question(prompts[2], "c")]

# def run_test(questions):
#     score  = 0
#     for question in questions:
#         answer = input(question.question + "\nInput your Answer here : ")
#         if answer.lower() ==question.answer:
#             score += 1
#     return "Test is Over, Your Final Score is "+str(score)+" / 3"

# result = run_test(questions)       
# print(result)
d= uuid.uuid4()
print(django.VERSION, d)

arr = [2,4,5,6,7,7]
reduced = functools.reduce(  lambda a,y: y+a, arr)
mapped = list(map(lambda x:x**2, arr))
filtered = list(filter(lambda a: a>3, arr))
sort = sorted(arr,reverse=True)
print("sort ", sort)
print(len("sort"))
print(filtered)
print(mapped)
print(reduced)