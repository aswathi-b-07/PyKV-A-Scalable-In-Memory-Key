from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from store import KeyValueStore
from models import KeyValueRequest

app = FastAPI()

# ✅ Enable CORS (IMPORTANT FOR UI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow all origins (safe for academic project)
    allow_credentials=True,
    allow_methods=["*"],        # allow GET, POST, DELETE, OPTIONS
    allow_headers=["*"],
)

# Initialize key-value store with LRU capacity = 5
kv = KeyValueStore(capacity=5)

# Load data from disk on server startup (crash recovery)
@app.on_event("startup")
async def startup_event():
    await kv.load_from_disk()

# Store a key-value pair
@app.post("/set")
async def set_value(data: KeyValueRequest):
    return await kv.set(data.key, data.value)

# Retrieve value by key
@app.get("/get/{key}")
async def get_value(key: str):
    return await kv.get(key)

# Delete a key
@app.delete("/{key}")
async def delete_key(key: str):
    return await kv.delete(key)

# List all keys
@app.get("/keys")
async def list_keys():
    return await kv.get_all_keys()
