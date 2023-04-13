from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_q():
    quiz.next_question()

print("You have completed the quiz :)")
print(f"Your final score is : {quiz.score} ")
print("Come again and play some more")