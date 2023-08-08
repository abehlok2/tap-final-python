from langchain.agents import Tool
from langchain.tools import tool
from GenerateActivity import ClassActivity
from LessonPlan import LessonPlan
from SubPlans import Subplans

lessonplan_gen = LessonPlan()
lessonplan_generator = 

class_activity_gen = ClassActivity()
lessonplan_generator = Tool(
    name="LessonPlan_Generator",
    description="This tool generates lesson plans for teachers based on inputs provided by the user.",
    func=lessonplan_gen.generate_lesson_plan()
)

subplans_gen = Subplans()
subplan_generator = Tool(
    name="Subplan_Generator",
    description="This tool generates substitute teacher plans for substitute teachers based on inputs provided by "
                "the user, the regular teacher.",
    func=subplans_gen.generate_complete_subplans()
)