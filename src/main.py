#Import the regex library (re) and JSON library (json) for pattern and saving output
import re
import json

#Open and read the raw input text file that we are extracting data from
with open("input/raw-text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
    print(raw_text)

#Checks if a credit card number is fake by detecting if all digits are identical (e.g 0000-0000-0000-0000)
def is_valid_card(card):
    digits_only = card.replace("-","").replace(" ", "")
    if len(set(digits_only)) == 1:
        return False
    return True

#Hiding a credit card number, showing only the last 4 digits, to prevent exposing sensitive data
def hide_card(card):
    digits_only = card.replace("-", "").replace(" ", "")
    last_four = digits_only[-4:]
    stars = "*" * (len(digits_only) - 4)
    return stars + last_four

#Validates a phone number by checking its exact length after cleaning, to reject false matches
def is_valid_phone(phone):
    cleaned = phone.replace(" ", "").replace("+", "")
    if cleaned.startswith("0") and len(cleaned) ==10:
        return True
    if cleaned.startswith("250") and len(cleaned) ==12:
        return True
    return False


#Regex pattern to find email addresses in the text
email_pattern = r"[\w.]+@\w+(?:\.\w+)+"
emails = re.findall(email_pattern, raw_text)

#Regex pattern to find credit card numbers and it allows spaces or dashes as separators
card_pattern = r"\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}"
cards = re.findall(card_pattern, raw_text)

#Regex pattern to find Rwandan phone numbers, starting with 0 or +250
phone_pattern = r"(?:0|\+250)[\d ]{9,12}"
phones = re.findall(phone_pattern, raw_text)

#Regex pattern to find URLs starting with http or https
url_pattern = r"https?://[\w.-]+\S*"
urls = re.findall(url_pattern, raw_text)

print("EMAILS:", emails)
print("CARDS:", cards)
print("PHONES:", phones)
print("URLS:", urls)

#Keep only valid phone numbers it rejects fakes like ones leaked from credit cards
#Keep only valid credit cards, and hide them before storing  
valid_phones = [p for p in phones if is_valid_phone(p)]
valid_cards = [hide_card(c) for c in cards if is_valid_card(c)]

print("VALID PHONES:", valid_phones)
print("VALID & HIDDEN CARDS:", valid_cards)

#Find alumni emails ending in @alumni.alueducation
alumni_pattern = r"[\w.]+@alumni\.alueducation\.com"
alumni_emails= re.findall(alumni_pattern, raw_text)

#Finding SI emails ending in @si.alueducation.com
si_pattern = r"[\w.]+@si\.alueducation\.com"
si_emails = re.findall(si_pattern, raw_text)

#Finding official emails ending in @alueducation.com 
official_pattern = r"[\w.]+@alueducation\.com"
official_emails_all = re.findall(official_pattern, raw_text)

#Remove alumni/SI emails from the official list so each email is only counted once
official_emails = [e for e in official_emails_all if e not in alumni_emails and e not in si_emails]

print("ALUMNI EMAILS:", alumni_emails)
print("SI EMAILS:", si_emails)
print("OFFICIAL EMAILS:",official_emails)

#Combine all extracted and validated data into one structured dictionary
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

#Save the results to a JSON file so they're easy to verify.
with open("output/sample-output.json","w",encoding="utf-8") as f:
    json.dump(results, f, indent=4)
    print("The results are saved to output/sample-output.json")
