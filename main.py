import os
from dotenv import load_dotenv
from groq import Groq
from todo_manager import Task

#load .env file
load_dotenv()
api_key_from_vault = os.environ.get("GROQ_API_KEY")
client = Groq(api_key =api_key_from_vault)

# main flow
task_list = []

task1 = Task("Coop resume","Fix resume for Coop application")
task2 = Task("Assignment","OOP assignment")
task3 = Task("Laundry", "Do laundry sometimes")

task_list.append(task1)
task_list.append(task2)
task_list.append(task3)

for task in task_list:
    task.update_level_with_ai(client)
    task.show_data()
    print("\n")