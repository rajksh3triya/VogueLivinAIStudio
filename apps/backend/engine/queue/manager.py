from collections import deque
from engine.generation.job import GenerationJob

_queue = deque()

def enqueue(job: GenerationJob):
    _queue.append(job)

def dequeue():
    if _queue:
        return _queue.popleft()
    return None

def size():
    return len(_queue)
