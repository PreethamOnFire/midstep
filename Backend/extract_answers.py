import pdfplumber
from fpdf import FPDF
from datetime import datetime
import pdfplumber
from PIL import Image
import pytesseract
import os


# Function to read box positions from a text file
def read_box_positions(file_path):
    box_positions = {}
    with open(file_path, 'r') as f:
        for line in f:
            page, y_coord = line.strip().split(',')
            page = int(page.strip()) 
            y_coord = float(y_coord.strip())
        
            if page not in box_positions:
                box_positions[page] = []
            box_positions[page].append(y_coord)

    return box_positions


def extract_answers(pdf_file, box_file, output_folder=None, read_file=None):
    answeres = []
    box_positions = read_box_positions(box_file)
    with pdfplumber.open(pdf_file) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            # this is where the problem begins I think
            img = page.to_image(resolution=300).original
            
            x_box = 10
            if page_number in box_positions:
                for y_box in box_positions[page_number]:
                    # The bounding box is kinda... cuz the numbers lose their meanings after to_image
                    y_box *= 11.5
                    y_bottom = y_box + (img.height/8.5)  
                    box = (int(x_box), int(y_box), img.width, y_bottom)
                    
                    
                    cropped_img = img.crop(box)
                    # This really helps visualize what is getting cropped
                    # cropped_img_path = os.path.join(output_folder, f'cropped_image_{page_number}_{y_box}.png')
                    # cropped_img.save(cropped_img_path)
                    
                    answer_text = pytesseract.image_to_string(cropped_img)
                    

                    if answer_text.strip():
                        answeres.append(answer_text.strip())
                        # print(f"Recognized Answer: '{answer_text.strip()}'")
                        # with open(read_file, 'a') as f:
                        #     f.write(answer_text + "\n\n")
    return answeres

# A full page scan could also work

# def extract_answers(pdf_file, output_folder):

#     os.makedirs(output_folder, exist_ok=True)

#     with pdfplumber.open(pdf_file) as pdf:
#         for page in pdf.pages:
#             print(page.width)
#             print(page.height)

#             img = page.to_image(resolution=300).original
#             answer_text = pytesseract.image_to_string(img)

#             # if answer_text.strip():
#             #     with open(read_file, 'a') as f:
#             #         f.write(answer_text + "\n\n")