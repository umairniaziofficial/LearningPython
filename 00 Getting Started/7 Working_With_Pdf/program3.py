# Import the PyPDF2 module for working with PDF files
import PyPDF2

# Open the original PDF file in binary mode
file = open("Working_Business_Proposal.pdf", mode="rb")

# Create a PdfReader object to read the original PDF file
pdf_reader = PyPDF2.PdfReader(file)

# Create a PdfWriter object for creating a new PDF
pdf_writer = PyPDF2.PdfWriter()

# Add selected pages (in this case, page 3) from the original PDF to the new PDF
for page_num in range(2, 3):
    page = pdf_reader.pages[page_num]
    pdf_writer.add_page(page)

# Open a new PDF file in binary mode for writing
pdf_output = open("Some_BrandNew_Doc.pdf", mode="wb")

# Write the combined PDF to the new file
pdf_writer.write(pdf_output)

# Close the original and new PDF files
file.close()
pdf_output.close()
