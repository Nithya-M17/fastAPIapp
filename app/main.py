from fastapi import FastAPI

from routers import company,job
from database import engine,Base
from models import company as company_model,job as job_model
app = FastAPI() 
print(engine)

Base.metadata.create_all(bind=engine) # create the tables in the database if they do not exist already

app.include_router(company.router)
app.include_router(job.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"About": "This is About Page"}

@app.get("/contact")
def read_contact():
    return{"Contact":"This is contact page"}