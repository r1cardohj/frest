from flask import Flask
from pydantic import BaseModel
from frest import restful

app = Flask(__name__)

class Person(BaseModel):
    name: str
    age: int


@app.get("/person")
@restful
def list_person():
    person = Person(name='jun', age=24)
    return person


@app.post("/person")
@restful
def create_person(person: Person):
    # creating...
    return person



if __name__ == '__main__':
    app.run(debug=True)