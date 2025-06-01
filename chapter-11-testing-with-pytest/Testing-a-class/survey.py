class AnonSurvey:
    def __init__(self, question):
        self.question = question
        self.answer = []
    
    def ask_question(self):
        print(self.question)

    def add_answer(self, response):
        self.answer.append(response)

    def print_responses(self):
        print("Responses from the survey:")
        for index, response in enumerate(self.answer):
            print(f'{index} :{response}')
