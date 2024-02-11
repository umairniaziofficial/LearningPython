# Import the PyPDF2 module for working with PDF files
import PyPDF2

# Specify the path to the PDF file
file_path = "Working_Business_Proposal.pdf"

# Open the PDF file in binary mode using a context manager
with open(file_path, "rb") as file:

    # Create a PdfReader object to read the PDF file
    pdf_reader = PyPDF2.PdfReader(file)

    # Check if the PDF has at least one page
    if len(pdf_reader.pages) > 0:

        # Extract the first page of the PDF
        page_one = pdf_reader.pages[0]

        # Extract text content from the first page
        page_one_text = page_one.extract_text()

        # Print the extracted text from the first page
        print(page_one_text)

    else:
        # Print a message if the PDF has no pages
        print("The PDF has no pages.")

    # Close the file using the context manager
    file.close()
