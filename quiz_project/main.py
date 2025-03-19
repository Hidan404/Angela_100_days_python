from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)




quiz_questoes = QuizBrain(question_bank)

while quiz_questoes.still_has_questions():
    quiz_questoes.next_question()