import whois
from datetime import datetime

def calculate_risk_score(name, email):
    score = 0
    if email == "":
        return -1
    domain = email.split('@')[-1].lower()
    local_part = email.split('@')[0].lower()
    has_name = (name != "")
    if has_name:
        name_parts = name.lower().split()

    summary = []

    free_providers = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'protonmail.com']
    if domain in free_providers:
        score += 40
        summary.append("free domain")

    if has_name:
        found_name_match = name_in_email(name_parts[0], name_parts[1], local_part)
        score += 25 - found_name_match[0]
        if not found_name_match[1]:
            summary.append("doesn't match first name")
        if not found_name_match[2]:
            summary.append("doesn't match last name")

    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:
            days_old = (datetime.now() - creation_date).days
            if days_old < 32:
                score += 35  # Very new domains are high risk
                summary.append("domain is very new")
    except:
        score += 10  # Increase risk slightly if WHOIS is blocked/errors out

    final_score = score

    # normalize score if no first name available
    if not has_name:
        final_score = int(final_score * (100/75))

    return (final_score, summary)


# checks if parts of first and / or last name are in the email
def name_in_email(first_name, last_name, local_part):
    local_part = local_part.lower()
    first_name = first_name.lower()
    last_name = last_name.lower()
    total = 0
    first = False
    last = False

    # Check substrings of first name (length > 2)
    for i in range(len(first_name)):
        for j in range(i + 3, len(first_name) + 1):  # +3 ensures substring length > 2
            if first_name[i:j] in local_part:
                first = True
    if first:
        total += 10

    # Check substrings of last name (length > 2)
    for i in range(len(last_name)):
        for j in range(i + 3, len(last_name) + 1):
            if last_name[i:j] in local_part:
                last = True
    if last:
        total += 15

    # more common to have last name in email than first so weighted higher
    return (total, first, last)