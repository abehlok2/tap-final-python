from GenerateActivity import ClassActivity
from LessonPlan import LessonPlan
from GeneralAssistant import Assistant as GaLuna
from Assignment import
from SubPlans import Subplans
import Assignment
import os
openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

# This is the main file, which is the entry point for the program.
# It will call the other files in the program.

# This is the main function, which is the entry point for the program.
def main():
    # Initialize the GeneralAssistant class.
    assistant = GaLuna()
    # Initialize the GenerateActivity class.
    gen_activity = ClassActivity()
    # Initialize the LessonPlan class.
    lesson_plan = LessonPlan()
    # Initialize the SubPlans class.
    sub_plans = Subplans()
    # Initialize the Assignment class.
    assignment = Assignment()

    # Run the main loop of the program.
    while True:
        # Run the assistant.
        assistant.run()
        # Run the GenerateActivity class.
        gen_activity.run()
        # Run the LessonPlan class.
        lesson_plan.run()
        # Run the SubPlans class.
        sub_plans.run()
        # Run the Assignment class.
        assignment.run()

        # If the user wants to quit the program, then break out of the loop.
        if assistant.quit_program:
            break

    # Print a message to the user that the program has ended.
    print("The program has ended.")