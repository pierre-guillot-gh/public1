import anyio

async def get_name():
    print("Please enter your name:")
    name = input() # Noncompliant
    return name
