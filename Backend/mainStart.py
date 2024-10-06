from create_pdf import load_jsonl_test, load_jsonl_names, create_pdf, save_answers
import os


def clean_text(text):
    return text.encode('latin-1', 'replace').decode('latin-1')


def main():
    json_file = 'train.jsonl'
    json_file_name = 'tests.jsonl'
    questions, answers = load_jsonl_test(json_file)
    names, problemSets = load_jsonl_names(json_file_name)
    crete_folder = "Student_Practice"
    rdreams = "Referece_File"
    
    for name_idx in range(len(names)):
        indices_to_include = problemSets[name_idx] 
        if indices_to_include is None:
            continue
        selected_questions = [clean_text(questions[i]) for i in indices_to_include]

        # selected_answers = [answers[i] for i in indices_to_include]
        name = names[name_idx]
        answers_file = f'{name}_answers.txt'
        create_pdf(selected_questions, name, crete_folder)
        save_answers(selected_questions, answers_file, rdreams)


if __name__ == "__main__":
    main()