from extract_answers import extract_answers
# from free_check_answers import grade_test_bert
from check_students import grade_test
from create_pdf import load_jsonl, create_pdf, save_answers


def main():
    json_file = 'train.jsonl'
    questions, answers = load_jsonl(json_file)

    indices_to_include = range(0,12)
    selected_questions = [questions[i] for i in indices_to_include]
    selected_answers = [answers[i] for i in indices_to_include]
    
    # pdf_file = 'KindergardenIHS.pdf'
    # answers_file = 'answers.txt'
    # create_pdf(selected_questions, pdf_file, "Soham Jain")
    # save_answers(selected_questions, answers_file)

    pdf_file = 'KindergardenIHS-answers.pdf'
    # read_file = 'page_read.txt'
    # output_folder = 'cropped_images'  
    box_file = "loc_cache.txt"
    open(box_file, 'w')

    student_answers = extract_answers(pdf_file, box_file)

    results = grade_test(student_answers, selected_answers)
    for result in results:
        print(f"Question {result['question']}:")
        print(f"Student answer: {result['student_answer']}")
        print(f"Correct answer: {result['correct_answer']}")
        print(f"Score: {result['score']}")
        print()


if __name__ == "__main__":
    main()