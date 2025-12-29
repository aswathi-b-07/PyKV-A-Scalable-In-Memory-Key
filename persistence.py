import asyncio
import json
import os

class PersistenceManager:
    def __init__(self, log_file: str = "data.log"):
        self.log_file = log_file
        self.lock = asyncio.Lock()

        # Create log file if it doesn't exist
        if not os.path.exists(self.log_file):
            open(self.log_file, "w").close()

    async def append(self, operation: dict):
        async with self.lock:
            with open(self.log_file, "a") as f:
                f.write(json.dumps(operation) + "\n")

    async def recover(self):
        operations = []

        if not os.path.exists(self.log_file):
            return operations

        with open(self.log_file, "r") as f:
            for line in f:
                if line.strip():
                    operations.append(json.loads(line))

        return operations

    async def compact(self, current_state: dict):
        async with self.lock:
            with open(self.log_file, "w") as f:
                for key, value in current_state.items():
                    record = {
                        "op": "SET",
                        "key": key,
                        "value": value
                    }
                    f.write(json.dumps(record) + "\n")
