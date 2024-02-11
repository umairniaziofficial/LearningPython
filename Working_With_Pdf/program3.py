import PyPDF2

file = open("Working_Business_Proposal.pdf", mode="rb")
pdf_reader = PyPDF2.PdfReader(file)
pdf_writer = PyPDF2.PdfWriter()

# Add all pages from the original PDF
for page_num in range(3, 4):
    page = pdf_reader.pages[page_num]
    pdf_writer.add_page(page)

# Output the combined PDF to a new file
pdf_output = open("Some_BrandNew_Doc.pdf", mode="wb")
pdf_writer.write(pdf_output)

file.close()
pdf_output.close()
