import requests
import time

BASE_URL = "http://127.0.0.1:8000"


def set_key():
    key = input("Enter key: ")
    value = input("Enter value: ")

    response = requests.post(
        f"{BASE_URL}/set",
        json={"key": key, "value": value}
    )

    print("Response:", response.json())


def get_key():
    key = input("Enter key: ")

    response = requests.get(f"{BASE_URL}/get/{key}")

    print("Response:", response.json())


def delete_key():
    key = input("Enter key: ")

    response = requests.delete(f"{BASE_URL}/{key}")

    print("Response:", response.json())


def list_keys():
    response = requests.get(f"{BASE_URL}/keys")
    print("Response:", response.json())


def benchmark():
    start = time.time()

    for i in range(30):
        requests.post(
            f"{BASE_URL}/set",
            json={"key": f"key{i}", "value": f"value{i}"}
        )

    end = time.time()
    print("Time taken:", end - start, "seconds")


def menu():
    print("\n--- PyKV Client ---")
    print("1. SET key")
    print("2. GET key")
    print("3. DELETE key")
    print("4. LIST ALL KEYS")
    print("5. BENCHMARK")
    print("6. EXIT")


if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            set_key()
        elif choice == "2":
            get_key()
        elif choice == "3":
            delete_key()
        elif choice == "4":
            list_keys()
        elif choice == "5":
            benchmark()
        elif choice == "6":
            print("Exiting client...")
            break
        else:
            print("Invalid choice")
