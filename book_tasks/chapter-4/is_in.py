def is_in(str1, str2):
    return True if (str1 in str2 or str2 in str1) else False

# print(is_in("tes", "test"))

def test_is_in(strings1, strings2, results):
    for i in range(0, len(strings1)):
        str1 = strings1[i]
        str2 = strings2[i]
        result = results[i]
        answer = is_in(str1, str2)
        if(answer == result):
            print("Result is as expected")
        else:
            print(f"Unpredictable result for strings {str1} and {str2}, expected result is {result}, but received {answer}")

strings1 = ("test", "abc", "malina", "desire")
strings2 = ("no", "bc", "Comalina", "Undesireable")
result = (False, True, True, True)

test_is_in(strings1, strings2, result)                 
