from main import question_data, question_bank
from question_model import Question


class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        questao_atual = self.question_list[self.question_number]
        self.question_number+= 1
        pergunta = input(f"Q - {self.question_number}: {questao_atual.text} (True/False): ")