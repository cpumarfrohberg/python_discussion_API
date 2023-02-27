#main.py
from consume_reddit_API import endpoint_data, indexed_endpoint_data

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
#from pymongo import MongoClient
from mongita import MongitaClientDisk


class RedittMessage(BaseModel):
    title: str                  
    key: int

client = MongitaClientDisk()
db = client.db 
reddit_collection = db.reddit_data_collection

app = FastAPI()

@app.get('/')
async def root():
    return {'message':'Hello world!'}

@app.get('/reddit_titles')
async def render_endpoint_data():
    return endpoint_data

@app.get('/reddit_titles_indexed/{reddit_post_id}')
async def render_endpoint_data_by_id(reddit_post_id: int):
    for key in indexed_endpoint_data.keys():
        if key == reddit_post_id:
            return indexed_endpoint_data[key]

@app.post('/reddit_titles')
async def post_message(inserted_message: RedittMessage): 
    reddit_collection.insert_one(inserted_message.dict()) 
    return inserted_message