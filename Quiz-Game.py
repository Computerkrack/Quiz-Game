x = None
status = "setup"

questions = []

for i in range(10):
    questions.append(None)

while status == "setup":
    try:
        playing = int(input("Möchtest du Fragen beantworten(1) oder welche erstellen(2)? "))
        status = "beginning"
    except ValueError:
        print("Bitte gib eine Zahl ein")
        
if status == "beginning":
    print("Wilkommen zum Quiz Spiel!")

match playing:
    case 2:
        status = "making"

        print('Hier siehst du eine Liste mit bereits gestellten Fragen');

        index = 1
        for i in questions:
            print(f'Frage {index}: {i}')
            index += 1

        while status == "making":
            making_question_num = input('Welche Frage möchtest du füllen? (Falls du aufhören möchtest tippe quit ein) ')
            match making_question_num:
                case "quit":
                    status = "exiting"
                case _:
                    if making_question_num.isnumeric():
                        questions_len = len(questions)
                        question_index = int(making_question_num) - 1

                        if question_index <= 0:
                            print('Bitte gib eine Zahl größer als 0 ein')
                            continue
                        elif question_index + 1 > questions_len:
                            print(f'Die Frage {question_index + 1} existiert nicht!')
                            continue
                        else:
                            question_text = input('Wie soll die Frage lauten? ')
                            question_answer = input('Wie lautet die Antwort? ')

                            questions[question_index] = {
                                'question': question_text,
                                'answer': question_answer
                            }
                        pass
                    else:
                        print("Bitte gebe eine Zahl ein!")

