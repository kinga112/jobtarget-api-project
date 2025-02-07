from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Vue FrontEnd
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
    for job in jobs_json:
        if job["id"] == job_id:
            return json.dumps(job)
        
    return  json.dumps({"error": "Bad Id"})
