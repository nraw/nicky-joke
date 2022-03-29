import os
from pathlib import Path

client_payload = os.environ.get(
    "client_payload", "No idea what's happening, but this ain't working"
)
print(client_payload)
print(os.environ)
Path("what.md").write_text(client_payload)
