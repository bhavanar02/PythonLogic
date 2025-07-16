import hashlib
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        """
        size: number of bits in the Bloom filter
        hash_count: number of hash functions
        """
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _get_hashes(self, item):
        """
        generate multiple hash values for the given item
        """
        hashes = []
        item_bytes = item.encode('utf-8')
        for i in range(self.hash_count):
            hash_digest = hashlib.md5(item_bytes + str(i).encode()).hexdigest()
            hash_int = int(hash_digest, 16)
            hashes.append(hash_int % self.size)
        return hashes

    def add(self, item):
        """
        Add item to the Bloom filter.
        """
        for hash_val in self._get_hashes(item):
            self.bit_array[hash_val] = 1

    def __contains__(self, item):
        """
        Check if item is possibly in the Bloom filter.
        """
        #return all(self.bit_array[hash_val] for hash_val in self._get_hashes(item))
        bit_array_final = bitarray(500)
        for hash_val in self._get_hashes(item):
            val = self.bit_array[hash_val]
            bit_array_final.append(val)
        return all(bit_array_final)

def main():

    bloom = BloomFilter(size=500, hash_count=5)
    items_to_add = ["apple", "banana", "grape"]
    for item in items_to_add:
        bloom.add(item)

    test_items = ["apple", "banana", "cherry", "watermelon"]
    for item in test_items:
        if item in bloom:
            print(f"{item} is probably in the set.")
        else:
            print(f"{item} is definitely not in the set.")
    
"""     bit_array = [1, 1, 1, 1, 1, 1]
    all_result = all(bit_array)
    print("daddy code")
    print(all_result) """

if __name__ == "__main__":
    main()




