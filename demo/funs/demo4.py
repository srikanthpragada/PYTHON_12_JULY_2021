# Default value for parameter - Default parameters

def wish(name, message="Hi"):
    print(f"{message} {name}")


wish("Van")  # Positional
wish("Anders", "Hello")
wish(message="Good Morning", name="James")  # Keyword
wish("Larry", message="Hello")
