import os
import re

directory = r'c:\Users\AA5123\Desktop\RFD40-RFD 90 Handled Reader MqqT reference\operation_descriptions'

# Define patterns to remove: the headers and everything following them until the next header or end of file
# Actually, the user wants these specific sections removed along with their content.
# Usually these are at the end of the file.

patterns = [
    r'##\s+MQTT Command Payload.*?(?=\s##|$)',
    r'##\s+Error Codes.*?(?=\s##|$)',
    r'##\s+Response Codes.*?(?=\s##|$)'
]

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Clean up trailing whitespace/newlines
    content = content.strip() + '\n'
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

if __name__ == "__main__":
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            if clean_file(os.path.join(directory, filename)):
                print(f"Cleaned: {filename}")
                count += 1
    print(f"Total files updated: {count}")
