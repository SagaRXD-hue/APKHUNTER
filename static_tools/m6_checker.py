import os

KEYWORDS = [
    "isAdmin",
    "checkRole",
    "hasPermission"
]

def scan_m6(source_dir):
    results = []

    for root, _, files in os.walk(source_dir):
        for f in files:
            if f.endswith(".java"):
                path = os.path.join(root, f)

                with open(path, errors="ignore") as file:
                    content = file.read()

                for k in KEYWORDS:
                    if k in content:
                        results.append({
                            "title": "Insecure Authorization",
                            "severity": "Medium",
                            "owasp": "M6",
                            "path": path,
                            "description": "Weak authorization logic",
                            "remediation": "Enforce server-side authorization"
                        })

    return results
