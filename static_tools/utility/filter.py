IGNORE_PACKAGES = [
    "com/google/",
    "androidx/",
    "kotlin/",
    "kotlinx/",
    "com/google/android/gms/",
    "google/",
    "okhttp3/",
    "retrofit2/",
    "org/apache/",
    "com/facebook/",
    "com/firebase/",
    "com/squareup/"
]


def should_ignore(path: str) -> bool:
    
    path = path.replace("\\", "/").lower()

    return any(pkg in path for pkg in IGNORE_PACKAGES)
