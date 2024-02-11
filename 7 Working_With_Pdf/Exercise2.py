import PyPDF2
import re

pattern = re.compile(r'\d{3}\.\d{3}\.\d{4}')

file_path = "Find_the_Phone_Number.pdf"

with open(file_path, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)

    if len(pdf_reader.pages) > 0:
        for i in range(len(pdf_reader.pages)):
            page_one = pdf_reader.pages[i]
            page_one_text = page_one.extract_text()

            # Join the words back into a single string
            page_one_text_combined = " ".join(page_one_text.split())

            # Use findall instead of match to find all occurrences
            numbers = pattern.findall(page_one_text_combined)
            string_number = "".join(numbers)
            if numbers:
                print(f"Phone numbers on page {i + 1}: {string_number}")
            else:
                print(f"No phone numbers found on page {i + 1}")
    else:
        print("The PDF has no pages.")
