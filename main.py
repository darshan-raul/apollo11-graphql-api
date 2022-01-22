from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from fastapi import FastAPI
from graphene.types.objecttype import ObjectType
from graphene import ObjectType as ot
from graphene import String as st
from graphene import Int as int
from graphene import List as li
import graphene

data=[
    {
        "name": "Roni",
        "city": "Cologne",
        "country": "India"

},
{
        "name": "John",
        "city": "London",
        "country": "UK"

},
{
         "name": "Maria",
         "city": "Sydney",
         "country": "Australia"
}
]

class students(ot):
    name=st()
    city=st()
    country=st()

class person(ot):
    student=li(students)
    def resolve_student(self,info):
        return data

app=FastAPI()

schema = graphene.Schema(query=person)

app.add_route("/graphql",GraphQLApp(schema,on_get=make_graphiql_handler())) 


print(graphene.Schema(query=person))
