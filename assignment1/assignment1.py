# task1 
def hello():
    return("Hello!")


# task2 
def greet(name):
    return f"Hello, {name}!"
 

# task 3
def calc(a, b, operation="multiply"):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "You can't multiply those values!"
    
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "You can't divide by 0!"
    elif operation == "modulo":
        return a % b if b != 0 else "You can't divide by 0!"
    elif operation == "int_divide":
        return a // b if b != 0 else "You can't divide by 0!"
    elif operation == "power":
        return a ** b
    else:
        return "Error: Unknown operation"

# task 4
def data_type_conversion(value, type_name):
    try:
        if type_name == "int":
            return int(value)
        elif type_name == "float":
            return float(value)
        elif type_name == "str":
            return str(value)
        else:
            return f"Unknown type: {type_name}"  
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type_name}."

# task 5
def grade(*args):
    try:
        if not args: 
            return "Invalid data was provided."
        
        avg = sum(args) / len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError): 
        return "Invalid data was provided."

# task 6
def repeat(string, count):
    try:
        if not isinstance(count, int) or count < 0:
            return "Invalid count value."

        result = "" 
        for _ in range(count): 
            result += string 
        return result
    except TypeError:
        return "Invalid input."
        
# task 7
def student_scores(mode, **kwargs):
    try:
        if not kwargs: 
            return "No scores provided."
        
        if mode == "best":
            return max(kwargs, key=kwargs.get)  
        elif mode == "mean":
            return sum(kwargs.values()) / len(kwargs) 
        else:
            return "Invalid mode."
    except (ValueError, TypeError):
        return "Invalid data."

# task 8
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"} 
    
    words = text.split()  
    
    if not words:  
        return ""

    for i, word in enumerate(words):  
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()  
        else:
            words[i] = word.lower()  

    return " ".join(words)

# task 9
def hangman(secret, guess):
    return "".join(char if char in guess else "_" for char in secret)

# Task 10
def pig_latin(text):
    vowels = {"a", "e", "i", "o", "u"}  
    words = text.split()  
    pig_latin_words = [] 

    for word in words:  
        if word[0] in vowels:  
            pig_word = word + "ay"
        elif word.startswith("qu"):  
            pig_word = word[2:] + "quay"
        else:  
            i = 0
            while i < len(word) and word[i] not in vowels:  
                if word[i:i+2] == "qu":  
                    i += 2
                    break
                i += 1
            pig_word = word[i:] + word[:i] + "ay"

        pig_latin_words.append(pig_word)  

    return " ".join(pig_latin_words)  


# Check
print(hello())  # "Hello!"

print(greet("Aida"))  # "Hello, Aida!"
print(greet("Andrew"))  # "Hello, Andrew!"

print(calc(10, 5, "add"))  # 15
print(calc(10, 0, "divide"))  # "You can't divide by 0!"

print(data_type_conversion("42", "int"))  # 42
print(data_type_conversion("abc", "float"))  # "You can't convert abc into a float."

print(grade(90, 95, 100))  # "A"
print(grade(50, 60, 55))  # "F"

print(repeat("hi", 3))  # "hihihi"
print(repeat("test", 0))  # ""

print(student_scores("best", Aida=95, Bob=87, Andrew=92))  # "Aida"
print(student_scores("mean", Aida=95, Bob=87, Andrew=92))  # 91.33

print(titleize("the lion and the mouse"))  # "The Lion and the Mouse"
print(titleize("in the heart of the sea"))  # "In the Heart of the Sea"

print(hangman("alphabet", "ab"))  # "a___ab__"p
print(hangman("mississippi", "sip"))  # "__ssi_ssi__"

print(pig_latin("apple"))  # "appleay"
print(pig_latin("banana"))  # "ananabay"
print(pig_latin("square"))  # "aresquay"
