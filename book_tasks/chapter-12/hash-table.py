class Int_dict(object):
    #A dictionary with integer keys
    def __init__(self, num_buckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.num_buckets = num_buckets
        for i in range(num_buckets):
            self.buckets.append([])
    
    def add_entry(self, key, dict_val):
        """Assumes key an int. Adds an entry."""
        hash_bucket = self.buckets[key%self.num_buckets]

        for i in range(len(hash_bucket)):
            if hash_bucket[i][0] == key:
                hash_bucket[i] = (key, dict_val)
                return
        hash_bucket.append((key, dict_val))
    
    def get_value(self, key):
        """Assumes key an int.
        Returns value associated with key"""

        hash_bucket = self.buckets[key%self.num_buckets]
        for e in hash_bucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result += f'{e[0] : {e[1]}},'
        return result[:-1] + '}' # result[:-1] omits the last comma

