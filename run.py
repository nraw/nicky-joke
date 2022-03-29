import os
from datetime import date
from pathlib import Path

data = os.environ.get("data")
if data:
    joke = data.get("1604150654")
    today = date.today().strftime("%Y-%m-%d")
    cool_date = data.get("824302638", today)
    date.now
    full_text = f"""
    The joke that was made
    ```
    {joke}
    ```
    on {cool_date}
    """
else:
    full_text = (
        "No idea what's happening, but this ain't working correctly. Blame kaki."
    )


    full_text += """
If you know that he's been funny again, add the new joke [here](https://forms.gle/z8fhvfisUHKKajbv8)
    """
print(data)
Path("what.md").write_text(full_text)
