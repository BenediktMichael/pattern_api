import random
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

pattern_list = ["Test1", "Test2", "Test3", "Test4", "Test5"]
available_patterns = ["Test1", "Test2", "Test3", "Test4", "Test5"]
used_patterns = []

working_groups = []

class Pattern(BaseModel):
    name = "Name Pattern"
    group = []




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
    if pattern in working_groups:     
        available_patterns.remove(pattern.name)
        #working_groups[]
        response = {"status": "success", "name": pattern.name, "author": pattern.group}
        return response
    used_patterns.append(pattern.name)
    working_groups.append(pattern)
    response = {"status": "success", "name": pattern.name, "author": pattern.group}
    return response
