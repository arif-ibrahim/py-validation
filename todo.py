from validation import Validator
from database import Database


class Todo(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()

        self.collection_name = 'todo'

        self.fields = {
            "title": "string",
            "body": "string",
        }

        self.create_required_fields = ["title", "body"]

        # Fields optional for CREATE
        self.create_optional_fields = []

        # Fields required for UPDATE
        self.update_required_fields = []

        # Fields optional for UPDATE
        self.update_optional_fields = []

    def create(self, todo):
        # Validator will throw error if invalid
        self.validator.validate(todo, self.fields, self.create_required_fields, self.create_optional_fields)
        res = self.db.insert(todo, self.collection_name)
        return "Inserted Id " + res
