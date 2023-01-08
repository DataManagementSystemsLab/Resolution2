import pytesseract
import PyPDF2

# Open the PDF file
with open('files/1_Gh5XSGA2X3Em6l0UaOweIs8CfmIQ_KT.pdf', 'rb') as f:
    pdf = PyPDF2.PdfReader(f)
    
    # Iterate through all of the pages in the PDF
    for i in range(pdf.getNumPages()):
        # Extract the text from the page
        text = pytesseract.image_to_string(pdf.page[i])
        
        # Print the text
        print(text)