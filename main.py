import os
from dotenv import load_dotenv
from groq import Groq
from todo_manager import Task
import json

#load .env file
load_dotenv()
api_key_from_vault = os.environ.get("GROQ_API_KEY")
client = Groq(api_key =api_key_from_vault)

# main flow
task_list = []

#load tasks.json
if os.path.exists("tasks.json"):
    with open("tasks.json", "r", encoding="utf-8") as f:
        load_data = json.load(f)

    for data in load_data:
        task = Task(data["task"], data["desc"])
        task.priority = data["priority"]
        task_list.append(task)
    print("Todo list loaded")


print("--- Todo Manager Tool ---\n")

while True:
    
    user_selection = input("1: Add Todo\n2: Show list with level\n3: Finish\nType Number: ")
    print("\n")
    
    # Add Todo
    if user_selection == "1":
        print("--- Input the info below ---\n")
        input_task = input("Task title: \n")
        input_desc = input("Task descritption: \n")
        new_task = Task(input_task, input_desc) # Make new instance
        task_list.append(new_task)
        print("Task added!\n")

    # AI Sort and show Todo
    elif user_selection == "2":
        print("--- Todo list with priority level ---\n")
        for task in task_list:
            task.update_level_with_ai(client)

        # this automatically calls __lt__ method in Todo class
        task_list.sort()
        
        for task in task_list:
            task.show_data()
            print("\n")

    # Finish the program and save it to json file
    elif user_selection == "3":
        
        save_data = []
        for task in task_list:
            save_data.append(task.to_dict())

        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(save_data, f, indent=4)

        print("Data saved to json file")
        break
    
    else: # error handling
        print("Invalid number! Please enter 1, 2 or 3.\n")

