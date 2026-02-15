import os
import re

from static_tools.utility.filter import should_ignore

KEYWORDS = [
    "SharedPreferences",
    "MODE_WORLD_READABLE",
    "openFileOutput"
]

def scan_m2(source_dir):
    results = []

    for root, _, files in os.walk(source_dir):
        if should_ignore(root):
            continue
        for f in files:

            if f.endswith(".java"):
                path = os.path.join(root, f)
                print(f"Scanning {path}...")

                with open(path, errors="ignore") as file:
                    content = file.read()

                for key in KEYWORDS:
                    if key in content:
                        results.append({
                            "title": "Insecure Data Storage",
                            "severity": "High",
                            "owasp": "M2",
                            "path": path,
                            "description": f"Possible insecure storage: {key}",
                            "remediation": "Use EncryptedSharedPreferences"
                        })

    return results
