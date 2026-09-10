import re
import json

with open("input/raw-text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
    print(raw_text)

def is_valid_card(card):
    digits_only = card.replace("-", "").replace(" ", "")
    if len(set(digits_only)) == 1:
        return False
    return True

def hide_card(card):
    digits_only = card.replace("-", "").replace(" ", "")
    last_four = digits_only[-4:]
    stars = "*" * (len(digits_only) - 4)
    return stars + last_four

def is_valid_phone(phone):
    cleaned = phone.replace(" ", "").replace("+", "")
    if cleaned.startswith("0") and len(cleaned) ==10:
        return True
    if cleaned.startswith("250") and len(cleaned) ==12:
        return True
    return False


email_pattern = r"[\w.]+@\w+(?:\.\w+)+"
emails = re.findall(email_pattern, raw_text)

card_pattern = r"\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}"
cards = re.findall(card_pattern, raw_text)

phone_pattern = r"(?:0|\+250)[\d ]{9,12}"
phones = re.findall(phone_pattern, raw_text)

url_pattern = r"https?://[\w.-]+\S*"
urls = re.findall(url_pattern, raw_text)

print("EMAILS:", emails)
print("CARDS:", cards)
print("PHONES:", phones)
print("URLS:", urls)


# test_phones = ["0788123456", "0788 123 456", "+250722556890", "0110009901394"]
# for phone in test_phones:
#     print(phone, ":", is_valid_phone(phone))

valid_phones = [p for p in phones if is_valid_phone(p)]
valid_cards = [hide_card(c) for c in cards if is_valid_card(c)]

print("VALID PHONES:", valid_phones)
print("VALID & HIDDEN CARDS:", valid_cards)


alumni_pattern = r"[\w.]+@alumni\.alueducation\.com"
alumni_emails= re.findall(alumni_pattern, raw_text)

si_pattern = r"[\w.]+@si\.alueducation\.com"
si_emails = re.findall(si_pattern, raw_text)

official_pattern = r"[\w.]+@alueducation\.com"
official_emails_all = re.findall(official_pattern, raw_text)

official_emails = [e for e in official_emails_all if e not in alumni_emails and e not in si_emails]

print("ALUMNI EMAILS:", alumni_emails)
print("SI EMAILS:", si_emails)
print("OFFICIAL EMAILS:",official_emails)

results = {
    "emails": {
        "official": official_emails,
        "alumni":alumni_emails,
        "si": si_emails
    },
    "credit_cards_hidden": valid_cards,
    "phone_numbers": valid_phones,
    "urls": urls
}

with open("output/sample-output.json","w",encoding="utf-8") as f:
    json.dump(results, f, indent=4)
    print("The results are saved to output/sample-output.json")