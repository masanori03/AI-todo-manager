import os

class Task:
    def __init__(self, task, desc):
        self.task = task
        self.priority = None
        self.desc = desc

    def show_data(self):
        print(f"Task title: {self.task}\nTask desc: {self.desc}\n[Priority level: {self.priority}]")


# Every time this function is called, the task is sent to the AI and its priority level is evaluated.
    def update_level_with_ai(self, client):

        response = client.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=[
            {"role": "system", "content": "You are an AI assistant that evaluates the priority level of TODO tasks."},
            {"role": "user", "content": f"Task: {self.task}, Description: {self.desc}. "
                        "Determine the priority level of this task. "
                        "Output only one word: High, Medium, or Low. "
                        "Do not include any additional text."},
            ]
        )

        result = response.choices[0].message.content.strip() # .strip() to remove if there's any extra space
        self.priority = result
  