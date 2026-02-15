SEVERITY_SCORES = {
    "Critical": 20,
    "High": 10,
    "Medium": 5,
    "Low": 2
}


SEVERITY_SCORES = {
    "Critical": 15,
    "High": 8,
    "Medium": 4,
    "Low": 1
}

CONFIDENCE_MULTIPLIER = {
    "High": 1.0,
    "Medium": 0.6,
    "Low": 0.3
}


def calculate_risk(results):

    total = 0
    count = 0


    def extract(data):
        nonlocal total, count

        if not isinstance(data, list):
            return

        for item in data:

            if not isinstance(item, dict):
                continue

            severity = item.get("severity", "Low")
            confidence = item.get("confidence", "Low")

            base = SEVERITY_SCORES.get(severity, 1)
            mult = CONFIDENCE_MULTIPLIER.get(confidence, 0.3)

            score = base * mult

            total += score
            count += 1


    for key in results:
        extract(results[key])


    if total > 100:
        total = 100


    if total >= 70:
        level = "Critical"
    elif total >= 45:
        level = "High"
    elif total >= 20:
        level = "Medium"
    else:
        level = "Low"


    return {
        "score": round(total, 2),
        "level": level,
        "issues_found": count
    }
