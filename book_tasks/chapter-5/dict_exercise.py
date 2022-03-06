def get_min(d):    
    """d a dict mapping letters to ints       
    returns the value in d with the key that occurs first in the       
    alphabet. E.g., if d = {x = 11, b = 12}, get_min returns 12."""

    min_char_value = min([ord(x) for x in d.keys()])
    return d[chr(min_char_value)]

d = {"x" : 11, "a": 100, "d" : 12}
print(get_min(d))