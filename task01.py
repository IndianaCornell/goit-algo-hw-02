import queue
import random

request_queue = queue.Queue()

def generate_request():
    request_id = random.randint(1, 100)
    print(f"Створено заявку: {request_id}")
    request_queue.put(request_id)

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробка заявки: {request_id}")
    else:
        print("Черга порожня")

for i in range(10):
        generate_request()
        process_request()

 