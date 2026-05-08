# A decorator in Python is a function that takes another function and extends its
# behavior without explicitly modifying it. Think of it as a wrapper that adds
# "extra features" to a function, such as logging, security checks, or timing,
# while keeping the original code clean.

def changeCase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@changeCase
def myFunc():
    return "hello world"

print(myFunc())

