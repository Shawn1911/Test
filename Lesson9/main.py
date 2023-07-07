import time
import uuid

"""
uuid:
    id generation
    unique
    
"""
data_set = set()
start = time.time()

for i in range(1_000_000_0):
    data_set.add(uuid.uuid4())

print(len(data_set))
print(time.time()-start)
