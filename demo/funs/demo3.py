# Keyword and positional params

def wish(name, message):
    print(f"{message} {name}")


wish("Van", "Hi")    # Positional
wish(message="Good Morning", name="James")  # Keyword
