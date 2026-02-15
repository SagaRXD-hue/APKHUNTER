import os
import re

PATTERNS = [
    r"password\s*=",
    r"token\s*=",
    r"login\(",
]

def scan_m4(source_dir):
    results = []

    for root, _, files in os.walk(source_dir):
        for f in files:
            if f.endswith(".java"):
                path = os.path.join(root, f)

                with open(path, errors="ignore") as file:
                    content = file.read()

                for pat in PATTERNS:
                    if re.search(pat, content):
                        results.append({
                            "title": "Insecure Authentication",
                            "severity": "High",
                            "owasp": "M4",
                            "path": path,
                            "description": "Weak authentication logic",
                            "remediation": "Use secure authentication APIs"
                        })

    return results
