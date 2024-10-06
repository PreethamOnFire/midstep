import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple, Dict

def preprocess_text(text: str) -> str:
    # Convert to lowercase and remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    return text

def extract_numbers(text: str) -> List[float]:
    return [float(num) for num in re.findall(r'-?\d+(?:\.\d+)?', text)]

def cosine_sim(text1: str, text2: str) -> float:
    vectorizer = CountVectorizer().fit_transform([text1, text2])
    return cosine_similarity(vectorizer)[0,1]

def grade_answer(student_answer, correct_answer) -> Tuple[float]:
    student_clean = preprocess_text(student_answer)
    correct_clean = preprocess_text(correct_answer)
    student_numbers = extract_numbers(student_answer)
    correct_numbers = extract_numbers(correct_answer)
    
    similarity = cosine_sim(student_clean, correct_clean)
    number_match = set(student_numbers) == set(correct_numbers)
    score = (similarity*0.5) + (number_match *0.5)
    return score

def grade_test(student_answers, correct_answers) -> Tuple[List[Dict]]:
    results = []
    total_score = 0
    
    for question, (student_ans, correct_ans) in enumerate(zip(student_answers, correct_answers), 1):
        score = grade_answer(student_ans, correct_ans)
        total_score += score
        results.append({
            'question': question,
            'student_answer': student_ans,
            'correct_answer': correct_ans,
            'score': score,
        })
    
    return results
