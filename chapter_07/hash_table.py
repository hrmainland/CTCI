def hash(input):
    res = 0
    for char in input:
        res += ord(char)
    return res


class LLNode:
    def __str__(self):
        res = "X"
        current = self
        while current.next:
            res += " -> " + current.next.val[0] + " "
            current = current.next
        return res

    def __init__(self, val, next):
        self.val = val
        self.next = next


class HashMap:

    def __str__(self):
        return ", ".join([str(elem) for elem in self.array])

    def __init__(self, n):
        self.n = n
        self.array = []
        for _ in range(n):
            self.array.append(LLNode(None, None))

    def add(self, key, value):
        key_hash = hash(key)
        index = self._get_index(key_hash)
        node = LLNode((key, value), None)
        current = self.array[index]
        while current.next:
            current = current.next
        current.next = node

    def get(self, key):
        key_hash = hash(key)
        index = self._get_index(key_hash)
        current = self.array[index]
        while current:
            if current.val and current.val[0] == key:
                return current.val[1]
            current = current.next
        return None

    def _get_index(self, hash):
        if not isinstance(hash, int):
            raise ValueError("Hash must be an integer")
        return hash % self.n


hash_map = HashMap(10)
hash_map.add("abc", 10)
hash_map.add("abc", 10)
hash_map.add("abc", 10)
hash_map.add("abc", 10)
hash_map.add("abc", 10)
print(hash_map)
res = hash_map.get("abc")
print(res)
