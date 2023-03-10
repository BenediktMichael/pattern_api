import random
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

pattern_list = []#"Test1", "Test2", "Test3", "Test4", "Test5"
available_patterns = []#"Test1", "Test2", "Test3", "Test4", "Test5"
used_patterns = []

working_groups = {}

class Pattern(BaseModel):
    name = "Name Pattern"
    user = "Name User"


@app.get("/groups")
def show_groups():
    return {"working_groups": working_groups}

@app.get("/pattern")
def show_pattern():
    return {"pattern": random.choice(pattern_list)}


@app.post("/pattern")
def send_pattern(pattern: Pattern):
    if pattern.name not in pattern_list:
        response = {"status": "error", "message": "Pattern unknown"}
        return response
    if (pattern.name in used_patterns) and (pattern.name not in available_patterns):
        response = {"status": "error", "message": "Pattern already taken"}
        return response
    if (pattern.name in used_patterns):     
        working_groups[pattern.name].append(pattern.user)
        if len(working_groups[pattern.name]) == 3:
            available_patterns.remove(pattern.name)
        #working_groups[]
        response = {"status": "success", "name": pattern.name, "author": pattern.user}
        return response
    used_patterns.append(pattern.name)
    working_groups[pattern.name] = [pattern.user]
    response = {"status": "success", "name": pattern.name, "author": pattern.user}
    return response

@app.post("/init",  include_in_schema=False)
def send_pattern_list(patterns: list):
    global pattern_list
    global available_patterns
    pattern_list = patterns
    available_patterns = patterns
    response = {"status": "success", "pattern_list":patterns}
    return response


