from queue import Queue
import random
import time

queue = Queue()

request_id= 1

def generate_request():
    global request_id
    request = f"Request №{request_id}"
    queue.put(request)
    print(f"New request was generated: {request}")
    request_id += 1

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing request: {request}")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate processing time
        print(f"Request {request} processed.")
    else:
        print("The queue is empty. No requests to process.")

def main():
    try:
        while True:

            if random.choice([True, False]):  # Randomly decide whether to generate a new request
                generate_request()

            process_request()

            time.sleep(random.uniform(0.5, 2)) # Pause to simulate real-world timing
            print("\n Press Control + c to stop.")
    except KeyboardInterrupt:
        print("\n Program stopped by the user.")

if __name__ == "__main__":
    main()
