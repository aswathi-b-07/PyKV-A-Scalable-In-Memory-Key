from fastapi import FastAPI
from store import KeyValueStore
from models import KeyValueRequest

app = FastAPI()
kv = KeyValueStore(capacity=5)

@app.on_event("startup")
async def startup_event():
    await kv.load_from_disk()

@app.post("/set")
async def set_value(data: KeyValueRequest):
    return await kv.set(data.key, data.value)

@app.get("/get/{key}")
async def get_value(key: str):
    return await kv.get(key)

@app.delete("/{key}")
async def delete_key(key: str):
    return await kv.delete(key)

@app.get("/keys")
async def list_keys():
    return await kv.get_all_keys()
