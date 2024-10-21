sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
chunk1 = sample_list[:3]
chunk2 = sample_list[3:6]
chunk3 = sample_list[6:]

chunk1.reverse()
chunk2.reverse()
chunk3.reverse()

print(f"Chunk-1 = {chunk1}")
print(f"Chunk-2 = {chunk2}")
print(f"Chunk-3 = {chunk3}")
