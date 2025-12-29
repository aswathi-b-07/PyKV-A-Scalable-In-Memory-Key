import asyncio
from lru_cache import LRUCache
from persistence import PersistenceManager

class KeyValueStore:
    def __init__(self, capacity: int = 5):
        self.cache = LRUCache(capacity)
        self.lock = asyncio.Lock()
        self.persistence = PersistenceManager()

    async def load_from_disk(self):
        operations = await self.persistence.recover()
        for op in operations:
            if op["op"] == "SET":
                self.cache.put(op["key"], op["value"])
            elif op["op"] == "DEL":
                self.cache.delete(op["key"])

    async def set(self, key: str, value: str):
        async with self.lock:
            await self.persistence.append({
                "op": "SET",
                "key": key,
                "value": value
            })
            self.cache.put(key, value)
            return {"status": "success", "message": f"{key} stored"}

    async def get(self, key: str):
        async with self.lock:
            value = self.cache.get(key)
            if value is None:
                return {"status": "error", "message": "Key not found"}
            return {"status": "success", "value": value}

    async def delete(self, key: str):
        async with self.lock:
            await self.persistence.append({
                "op": "DEL",
                "key": key
            })
            self.cache.delete(key)
            return {"status": "success", "message": f"{key} deleted"}

    async def get_all_keys(self):
        async with self.lock:
            return {"status": "success", "keys": self.cache.keys()}

    async def compact_log(self):
        async with self.lock:
            current_state = self.cache.cache
            await self.persistence.compact(current_state)
