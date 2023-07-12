import uuid
import time
"""
uuid:
    id generation
    unique
"""

# print(uuid.uuid4())

data_set=set()


s=time.time()
for i in range(1_000_000):
    data_set.add(uuid.uuid4())
print(len(data_set))
print(time.time()-s)

"""
table: Post
    id  3c3d8e15-a93c-42bd-8da1-054a0a0d4538
    title
    description
"""

