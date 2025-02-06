from typing import Union
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware


api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("jobs.json", "r") as file:
    jobs_json = json.load(file)


@api.get("/jobs")
def jobs():
    return json.dumps(jobs_json)


@api.get("/job/{job_id}")
def details(job_id: int):
    print("GETTING JOB: ", job_id)
    for job in jobs_json:
        if job["id"] == job_id:
            return json.dumps(job)
        
    return  json.dumps({"error": "Bad Id"})
