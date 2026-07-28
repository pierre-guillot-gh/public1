class Resource:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        ...

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        ...

async def main():
    resource = Resource()
    with resource:  # Noncompliant: using 'with' in async function when async protocol is available
