#🔹 Array Implementation in Python
class MyArray:
    def __init__(self):
        self.data = []

    # 1. Traverse
    def traverse(self):
        for item in self.data:
            print(item, end=" ")
        print()

    # 2. Insert
    def insert(self, index, value):
        if index < 0 or index > len(self.data):
            print("Invalid index")
        else:
            self.data.insert(index, value)

    # 3. Delete
    def delete(self, index):
        if index < 0 or index >= len(self.data):
            print("Invalid index")
        else:
            removed = self.data.pop(index)
            print(f"Deleted: {removed}")

    # 4. Search
    def search(self, value):
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        return -1

    # 5. Size
    def size(self):
        return len(self.data)

    # 6. Get
    def get(self, index):
        if index < 0 or index >= len(self.data):
            print("Invalid index")
        else:
            return self.data[index]

    # 7. Set
    def set(self, index, value):
        if index < 0 or index >= len(self.data):
            print("Invalid index")
        else:
            self.data[index] = value

    # 8. Clear
    def clear(self):
        self.data = []

    # 9. Reverse
    def reverse(self):
        self.data.reverse()

    # 10. Sort
    def sort(self):
        self.data.sort()

    # 11. Min
    def min(self):
        return min(self.data)

    # 12. Max
    def max(self):
        return max(self.data)

    # 13. Sum
    def sum(self):
        return sum(self.data)

    # 14. Average
    def average(self):
        return sum(self.data) / len(self.data)

    # 15. Copy
    def copy(self):
        return self.data

    # 16. Count
    def count(self, value):
        return self.data.count(value)

    # 17. Index
    def index(self, value):
        return self.data.index(value)

    # 18. Pop
    def pop(self):
        return self.data.pop()

    # 19. Extend
    def extend(self, other):
        self.data.extend(other) 

#Using the Array Class
# Create an array
arr = MyArray()

# Insert elements
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
arr.insert(3, 40)
arr.insert(4, 50)

print("Array after insertion:")
arr.traverse()   # 10 20 30 40 50

# Delete element at index 2
arr.delete(2)    # Deletes 30
print("Array after deletion:")
arr.traverse()   # 10 20 40 50

# Search element
pos = arr.search(40)
if pos != -1:
    print(f"Element found at index {pos}")
else:
    print("Element not found")
