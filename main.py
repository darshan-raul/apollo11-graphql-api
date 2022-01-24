import os
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from fastapi import FastAPI
from graphene import ObjectType as ot
from graphene import String as st
from graphene import List as li
import graphene

data = [
    {"name": "Roni", "city": "Cologne", "country": "India"},
    {"name": "John", "city": "London", "country": "UK"},
    {"name": "Maria", "city": "Sydney", "country": "Australia"},
]


class Students(ot):
    name = st()
    city = st()
    country = st()


class Person(ot):
    student = li(Students)

    def resolve_student(self, info):
        return data


app = FastAPI()

schema = graphene.Schema(query=Person)

app.add_route("/graphql", GraphQLApp(schema, on_get=make_graphiql_handler()))


@app.get("/health")
def get_health():
    return "pong"


@app.get("/ready")
def get_readiness_status():
    return "yes"


@app.get("/startup")
def get_startup_status():
    return "healthy"


@app.get("/secret")
def get_secret():
    with open("/etc/secrets/fastapi-name", "r") as file:
        data = file.read().rstrip()
    return data
