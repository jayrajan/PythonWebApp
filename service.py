#  Code written by Jerin Rajan on 15th April 2020
# service.py - converts the request into a response
import models

class ToDoService:
    def __init__(self):
        self.model = models.ToDoModel()

    def create(self, params):
        self.model.create(params["Title"], params["Description"])

    def list(self):
        response = self.model.list_items()
        return response
