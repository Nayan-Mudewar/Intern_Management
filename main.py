from fastapi import FastAPI
from routes import intern
from routes import task
app=FastAPI()

app.include_router(intern.router, prefix="/intern", tags=["intern"])#same as app.use in mern
app.include_router(task.router, prefix="/task", tags=["task"])
