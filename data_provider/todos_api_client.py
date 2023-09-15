from randomuser import RandomUser
import random


class TodosDataProvider:

    @staticmethod
    def get_post_todo_datamodel():
        title = RandomUser().get_username()
        status = random.choice(["pending", "completed"])
        return dict(title=title, status=status)

print(TodosDataProvider.get_post_todo_datamodel())