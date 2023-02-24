#main.py
from consume_reddit_API import endpoint_data, indexed_endpoint_data
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from pymongo import MongoClient

class RedittMessage(BaseModel):
    title: str                  
    key: int

client = MongoClient('localhost')
db = client.db 
reddit_collection = db.reddit_data_collection

app = FastAPI()

@app.get('/')
async def root():
    return {'message':'Consuming reddit API data.'}

@app.get('/reddit_titles')
async def render_endpoint_data():
    endpoint_data = reddit_collection.find({})
    return [
        {key: endpoint_data_element[key] for key in endpoint_data_element if key != '_id'} #A
        for endpoint_data_element in endpoint_data
    ]

@app.get('/reddit_titles_indexed/{reddit_post_id}')
async def render_endpoint_data_by_id(reddit_post_id: int):
    if reddit_collection.count_documents({'id': reddit_post_id}) > 0:
        endpoint_data_element = reddit_collection.find_one({'id': reddit_post_id})
        return {key: endpoint_data_element[key] for key in endpoint_data_element if key != '_id'}
    raise HTTPException(status_code=404, detail=f'No message found with id {reddit_post_id}')

@app.post('/reddit_titles')
async def post_message(inserted_message: RedittMessage): 
    reddit_collection.insert_one(inserted_message.dict()) 
    return inserted_message