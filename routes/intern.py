from fastapi import APIRouter
from models.InternModel import InternModel
from config import db
from bson import ObjectId

router=APIRouter()

@router.post("/add")
async def insert_intern(intern: InternModel):

    result=await db["sigma"].insert_one(intern.dict())
    return {"id": str(result.inserted_id)}

@router.get("/")
async def get_all_interns():

    interns=[]

    cursor=db["sigma"].find()

    async for doc in cursor:
      doc["_id"] = str(doc["_id"])
    interns.append(doc)

    return interns

