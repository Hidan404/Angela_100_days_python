from question_model import Question
from data import questoes_interativo
from quiz_brain import QuizBrain
import json
import flet as ft




question_bank = []

def abrir_arquivo():
    with open("quiz_project/dados.json", "r") as f:
        dados = json.load(f)
        return dados

dadso_arquivo = abrir_arquivo()

def questoes():
    for question in dadso_arquivo["results"]:
        text = question["question"]
        answer = question["correct_answer"]
        new_question = Question(text, answer)
        question_bank.append(new_question)




quiz_questoes = QuizBrain(question_bank)
def main():
    questoes()
    while quiz_questoes.still_has_questions():
        quiz_questoes.next_question()

        if quiz_questoes.still_has_questions() == False:
            print("Quiz finalizado")
            print(f"Seu score final foi de {quiz_questoes.score}/{quiz_questoes.question_number}")

            
if __name__ == "__main__":
    main()            