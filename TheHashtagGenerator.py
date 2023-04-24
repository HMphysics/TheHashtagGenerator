def generate_hashtag(s):
    if len(s) >= 140 or s == "":
        return False
    
    s = s.lower()
    words = s.split()
    num_alpha = sum(1 for c in s if c.isalpha())
    
    if num_alpha == 0:
        return False
    
    result = "#" + "".join([word.capitalize() for word in words])
    return result if len(result) <= 140 else False
