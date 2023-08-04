from LessonPlan import LessonPlan
from SubPlans import Subplans
import openai
import os
openai.api_key = os.environ["OPENAI_API_KEY"]


'''subject = input("Please enter the subject for today's lesson plan \\(e.g. Math, \
Science, Social Studies etc.")
topic = input("Please enter the topic for today's lesson plan, based on the subject you've chosen.")
learning_objective = input("Please describe the learning objectives for today's lesson")
additional_details = input("Please describe any additional details you want to include \
or take into account while generating the lesson plan. Make sure to include \
the order and duration of your daily lessons!")'''


testsp = Subplans()

output = testsp.generate_complete_subplans()
print(output)