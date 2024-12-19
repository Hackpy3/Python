#  capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill
b = {"hello","World"}
b.capitalize()
print(b)

# Single quotes
string1 = 'Hello, World!'

# Double quotes
string2 = "Python is great!"

# Triple quotes (for multi-line strings)
string3 = """This is a
multi-line
string."""


greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Alice!

laugh = "Ha" * 3
print(laugh)  # Output: HaHaHa

word = "Python"
print(len(word))  # Output: 6

language = "Python"
first_letter = language[0]
print(first_letter)  # Output: P

substring = language[0:3]
print(substring)  # Output: Pyt

text = "Hello, World!"
print(text.upper())  # Output: HELLO, WORLD!
print(text.lower())  # Output: hello, world!

sentence = "I love Python programming."
position = sentence.find("Python")
print(position)  # Output: 7

new_sentence = sentence.replace("Python", "JavaScript")
print(new_sentence)  # Output: I love JavaScript programming.


multiline = """This is a
multi-line
string."""
print(multiline)

raw_string = r"C:\Users\Alice\Documents"
print(raw_string)  # Output: C:\Users\Alice\Documents


text = "   Python is fun!   "
print(text.strip())  # Output: Python is fun! (removes leading and trailing whitespace)

words = text.split()
print(words)  # Output: ['Python', 'is', 'fun!']

joined_text = " ".join(words)
print(joined_text)  # Output: Python is fun!








