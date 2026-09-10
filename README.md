# ALU Regex Data Extraction

## Overview
This program uses regex patterns to find, validate, and extract specific types of data- such as emails, phone numbers, and credit card numbers from raw text. 
## How to Run
To run the program, type python src/main.py in the terminal
## Data Types Extracted
- Emails (including ALU-specific: official, alumni, SI domains)
- Credit card numbers (masked in output)
- Phone numbers(I used the Rwandan format)
- URLs
##  ALU Email Classification
Emails are classified into three categories based on their domain:
- official (@alueducation.com)
- alumni (@alumni.alueducation.com)
- SI (@si.alueducation.com)
  
Separate regex patterns are used for each, and overlapping matches are filtered out so official emails don't include alumni or SI addresses.
## Security Considerations
- Credit cars numbers are masked in the output, showing only the last 4 digits.
- Cards made up of a single repeated digit (eg: 0000-0000-0000-0000) are rejected as fake.
- Phone numbers are validated by exact digit length to avoid false matches
- Malformed or injection-style emails and URLs are naturally rejected because they don't match the strict regex patterns used.
## Output
Results are saved to 'output/sample-output.json'
