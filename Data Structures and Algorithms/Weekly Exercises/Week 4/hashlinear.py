# Week 4: Exercise 1
# Juho Rekonen

class  HashLinear:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    # Let's first implement the given procedure
    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.size
    
    # Let's also define a function to keep track of available slots in the hash table
    def slots(self):
        return None not in self.table # Returns true if no slots are "None"
    
    # Function to insert values
    def insert(self, data):

        # Check if there are any available slots
        if self.slots():
            # If not, we simply return
            return
        
        value = self.hash(data)

        while self.table[value] is not None:
            # If the Data already exists, we ignore duplicates
            if self.table[value] == data:
                return
            value = (value + 1) % self.size

        self.table[value] = data

    # Function to delete values
    def delete(self, data):
        # Here we just find the correct slot
        for i in range(self.size):
            if self.table[i] == data:
                self.table[i] = None


    # We can do the printing using a cool one liner 
    def print(self):
        output = [value for value in self.table if value is not None]
        print(' '.join(output))


if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1

