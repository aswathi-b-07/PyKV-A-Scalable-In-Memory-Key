import threading
import requests

def replicate(operation, replica_url="http://127.0.0.1:8001"):
    def send():
        try:
            requests.post(f"{replica_url}/replicate", json=operation, timeout=0.2)
        except:
            pass

    threading.Thread(target=send, daemon=True).start()
