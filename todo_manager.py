import os

class Task:
    def __init__(self, task, desc):
        self.task = task
        self.level = None
        self.desc = desc

    def show_data(self):
        print(f"Task title: {self.task}\nTask desc: {self.desc}\n[Priority level: {self.level}]")


#この関数がよばれるたびに毎回各タスクをAIへ渡し、優先度を判定
    def update_level_with_ai(self, client):

        response = client.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=[
            {"role": "system", "content": "あなたはTODOタスクの優先度を判定するAIアシスタントです。"},
            {"role": "user", "content": f"タスク:{self.task}, 詳細：{self.desc}。このタスクの優先度を判定し、余計な言葉は一切入れず必ずHigh, Medium, Low のいずれか1語のみで出力してください。"},
            ]
        )

        result = response.choices[0].message.content.strip() # .strip()は前後の余計な空白を消す関数
        self.level = result
  