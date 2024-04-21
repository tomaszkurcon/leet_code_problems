from queue import Queue
def removeElement(nums, val: int) -> int:
    n = len(nums)
    counter = 0
    q = Queue()
    for i in range(n):
        if nums[i] == val:
            counter += 1
            q.put(i)
        else:
            if not q.empty():
                index = q.get()
                nums[index], nums[i] = nums[i], nums[index]
                q.put(i)
    return n - counter, nums

print(removeElement([2,3,2,5,7,2], 2))
