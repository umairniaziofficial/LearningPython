import PyPDF2

file_path = "Working_Business_Proposal.pdf"

with open(file_path, "rb") as file:

    pdf_reader = PyPDF2.PdfReader(file)
    # Check if the PDF has at least one page
    if len(pdf_reader.pages) > 0:
        page_one = pdf_reader.pages[0]
        page_one_text = page_one.extract_text()
        print(page_one_text)
    else:
        print("The PDF has no pages.")
    file.close()
