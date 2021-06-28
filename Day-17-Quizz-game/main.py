from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_bank.append(
        Question(question['question'], question['correct_answer'])
    )
quizz = QuizBrain(question_bank)
print(len(quizz.question_list))
while quizz.still_has_question():
    quizz.next_question()
    print(quizz.question_number)
print("You've completed the quiz")
print(f"Your final score  was {quizz.score} / {len(question_bank)}")
