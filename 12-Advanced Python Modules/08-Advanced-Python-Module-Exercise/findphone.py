import os
import re


def find_phone_numbers(start_path):
    # Regex pattern for a phone number
    phone_number_pattern = r'\b(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})\b'

    for root, dirs, files in os.walk(start_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as file:
                content = file.read()
                match = re.search(phone_number_pattern, content)
                if match:
                    print(f"File: {file_path}")
                    print("Phone Number:", '-'.join(match.groups()))


# Get the current working directory
current_dir = os.getcwd()
start_subdirectory = 'unzip_me_for_instructions/extracted_content'
start_path = os.path.join(current_dir, start_subdirectory)

# Call the function to find phone numbers
find_phone_numbers(start_path)
