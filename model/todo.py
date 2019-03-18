from validation import Validator
import datetime
import pymongo


class Todo(object):
    def __init__(self, title, body, created):
        self.validator = Validator()
        self.collection_name = 'collection_name'
        self.fields = {
            "title": "string",
            "body": "string",
            "created": "datetime",
        }
        self.create_required_fields = ["title", "body"]

        self.title = title
        self.body = body
        self.created = created

    def asdict(self):
        return {
            'title': self.title,
            'body': self.body,
            'created': self.created

        }


mytodo = Todo('meghna', 'meghna project phase 1', datetime.date.today().strftime('%y/%m/%d'))
print(mytodo.asdict())

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["test_database"]
# mycol = mydb["todo"]
#
# x = mycol.insert_one(mytodo.asdict())