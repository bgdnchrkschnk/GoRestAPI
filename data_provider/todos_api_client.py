from randomuser import RandomUser
import random
from random import randint
import datetime


class TodosDataProvider:

    @staticmethod
    def get_post_todo_datamodel():
        title = RandomUser().get_username()
        status = random.choice(["pending", "completed"])
        if random.choice([True, False]):
            due_on = str(datetime.date(randint(1930,2025), randint(1,12),randint(1,28)))
        else:
            due_on = None
        yield dict(title=title, status=status, due_on=due_on if due_on else None)


print(TodosDataProvider.get_post_todo_datamodel().__next__())
