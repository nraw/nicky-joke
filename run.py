import os
from pathlib import Path

data = os.environ.get(
    "data", "No idea what's happening, but this ain't working"
)
print(data)
print(os.environ)
Path("what.md").write_text(data)
