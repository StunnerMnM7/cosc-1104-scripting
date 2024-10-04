
def is_positive(num):
    return isinstance(num, (int, float)) and num > 0

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def gibi_to_giga(gib):
    return gib * 1_073_741_824 / 1_000_000_000

def giga_to_gibi(gb):
    return gb * 1_000_000_000 / 1_073_741_824

if __name__ == "__main__":
    # Test case for is_positive:
    print(is_positive(10))      
    print(is_positive(-5.5))  
    print(is_palindrome("Hello"))                     
    print(is_palindrome("Madam"))  
    print(giga_to_gibi(10))
    print(gibi_to_giga(0.5))

