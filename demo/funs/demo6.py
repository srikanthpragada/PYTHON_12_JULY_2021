# positional-only arguments

def wish(name, message, /):
    print(f"{message} {name}")


wish("Anders", "Hello")
# wish(message="Good Morning", name="James")  # Keyword

