import json
from fpdf import FPDF
import os
from datetime import datetime

def load_jsonl(jsonl_file):
    questions = []
    answers = []
    
    with open(jsonl_file, 'r') as f:
        for line in f:
            entry = json.loads(line.strip())
            # Append question and answer to their respective lists
            questions.append(entry.get("question"))
            answers.append(entry.get("answer"))
    
    return questions, answers

def create_pdf(selected_questions, pdf_file, author):
    pdf = FPDF()
    locations = []
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add the first page
    pdf.add_page()    

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, "Name: " + "_" * 10, ln=True, align='R')
    pdf.cell(0, 10, datetime.now().strftime('%m/%d/%Y'), ln=True, align='R')
    pdf.ln(3)  

    # Title
    pdf.set_font("Arial", 'B', size=16)
    pdf.cell(0, 10, pdf_file, ln=True, align='C')
    pdf.ln(5) 

    pdf.set_font("Arial", size=12)
    for i, q in enumerate(selected_questions, start=1):
        pdf.multi_cell(0, 10, f"{i}. {q['question']}")
        pdf.rect((pdf.get_x()), (pdf.get_y()), 180, 30)
        
        # Store the location as a tuple of (page number, y-coordinate)
        locations.append((pdf.page, pdf.get_y()))
        pdf.ln(30) 

    pdf.output(pdf_file)

    # Write the locations to the cache file
    cache_answer_loc = 'loc_cache.txt'
    with open(cache_answer_loc, 'w') as f:
        for page, loc in locations:
            f.write(f'{page}, {loc:.6f}\n')  # Format loc to six decimal places

def save_answers(selected_questions, answers_file):
    with open(answers_file, 'w') as f:
        for q in selected_questions:
            f.write(f"{q['question']}\n")
            f.write(f"Answer: -- {q['answer']} -- \n\n")
