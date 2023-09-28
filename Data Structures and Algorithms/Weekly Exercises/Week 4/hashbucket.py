# Week 4: Exercise 2
# Juho Rekonen

class HashBucket:
    def __init__(self, size, bucket):
        self.size = size
        self.bucket = bucket
        self.table = [[] for _ in range(bucket)]  # Initialize the hash table as a list of lists
        self.overflow = []  # Initialize the overflow array as an empty list

    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.size

    def insert(self, data):
        hash_value = self.hash(data)
        bucket_value = hash_value % self.bucket  # Use hash value to get the bucket value

        # Check if data already exists in the table
        if data in self.table:
            return
        
        # Check if the bucket has available slots
        if len(self.table[bucket_value]) < self.size / self.bucket:
            self.table[bucket_value].append(data)
            
        else:
            # Bucket is full, add data to the overflow array
            self.overflow.append(data)

    def delete(self, data):
        # Search for the data in the buckets
        for i in range(self.bucket):
            if data in self.table[i]:
                self.table[i].remove(data)
                return

        # Data not found in buckets, remove it from the overflow array
        if data in self.overflow:
            self.overflow.remove(data)

    def print(self):
        result = []

        # First we print the contents of the table
        for bucket in self.table:
            result.extend(bucket)

        print(" ".join(result), end=' ')

        # And then add the overflow array
        for item in self.overflow:
            print(item, end=' ')

        print()


if __name__ == "__main__":
    table = HashBucket(10, 5)
    table.insert("buttermilk")
    table.insert("shim")
    table.insert("resolvend")
    table.insert("cheiromegaly")
    table.insert("premillennialise")
    table.insert("finebent")
    table.print() # buttermilk shim resolvend premillennialise cheiromegaly finebent
    table.delete("buttermilk")
    table.delete("cores")
    table.delete("cheiromegaly")
    table.delete("iodations")
    table.print() # shim resolvend premillennialise finebent

    table.insert("iodations")
    table.insert("tirrlie")
    table.insert("comous")
    table.insert("discursiveness")
    table.insert("flabbergasts")
    table.insert("rename")
    table.insert("softhead")
    table.print() # iodations discursiveness softhead comous rename shim resolvend premillennialise flabbergasts finebent tirrlie


