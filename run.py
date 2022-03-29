from pathlib import Path
import os

client_payload = os.environ.get('client_payload')
print(client_payload)
print(os.environ)
Path('what.md').write_text('# hi')
