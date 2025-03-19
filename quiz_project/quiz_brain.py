


class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        questao_atual = self.question_list[self.question_number]
        self.question_number+= 1
        pergunta = input(f"Q - {self.question_number}: {questao_atual.text} (True/False): ")
        self.check_answer(pergunta,questao_atual)
    def still_has_questions(self):
        return self.question_number < len(self.question_list)  
    

    def check_answer(self,resposta,resposta_atual):
        if resposta.lower() == resposta_atual():
            print("Sua respsota esta correta")
        else:
            print(f"Sua resposta esta incorreta, a resposta e - {resposta_atual}")    
        print(f"Seu Score: {(self.score + 1) + "/" + resposta_atual}")

           
