import json
from fpdf import FPDF
import os
from datetime import datetime

def load_jsonl_test(jsonl_file):
    questions = []
    answers = []
    
    with open(jsonl_file, 'r') as f:
        for line in f:
            entry = json.loads(line.strip())
            questions.append(entry.get("question"))
            answers.append(entry.get("answer"))
    
    return questions, answers

def load_jsonl_names(file_name):
    name = []
    problem_sets = []
    
    with open(file_name, 'r') as f:
        for line in f:
            entry = json.loads(line.strip())
            name.append(entry['test_name'])
            problem_sets.append(entry['questions']) 

    return name, problem_sets


def create_pdf(selected_questions, pdf_file, crete_folder):
    pdf = FPDF()
    locations = []
    pdf.set_auto_page_break(auto=True, margin=15)
    

    pdf.add_page()    

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, "Name: " + "_" * 10, ln=True, align='R')
    pdf.cell(0, 10, datetime.now().strftime('%m/%d/%Y'), ln=True, align='R')
    pdf.ln(3)  


    pdf.set_font("Arial", 'B', size=16)
    pdf.cell(0, 10, pdf_file, ln=True, align='C')
    pdf.ln(5) 

    pdf.set_font("Arial", size=12)
    for i, q in enumerate(selected_questions, start=1):
        pdf.multi_cell(0, 10, f"{i}. {q}")
        pdf.rect((pdf.get_x()), (pdf.get_y()), 180, 30)
        
        locations.append((pdf.page, pdf.get_y()))
        pdf.ln(30) 

    os.makedirs(crete_folder, exist_ok=True)
    pdf_path = os.path.join(crete_folder, pdf_file)
    pdf.output(pdf_path)


    cache_answer_loc = 'loc_cache.txt'
    with open(cache_answer_loc, 'w') as f:
        for page, loc in locations:
            f.write(f'{page}, {loc:.6f}\n') 

def save_answers(selected_questions, answers_file, crete_folder):

    os.makedirs(crete_folder, exist_ok=True)
    pdf_path = os.path.join(crete_folder, answers_file)

    with open(pdf_path, 'w') as f:
        for q in selected_questions:
            f.write(f"{q}\n")
