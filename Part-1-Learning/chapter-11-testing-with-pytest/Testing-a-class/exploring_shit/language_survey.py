from survey import AnonSurvey

question = "What is your mother tongue?"
my_survey = AnonSurvey(question)

while True:
    print("Press 'q' to quit")
    my_survey.ask_question()
    response = input("Language:")
    print() if response.isalpha():
        if response == 'q':
            print("Gracefully exitting the code")
            break
        else:
            my_survey.add_answer(response)

    else:
        print("Invalid input")
        pass

my_survey.print_responses()


