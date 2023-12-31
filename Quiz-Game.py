import json

x = None
status = "setup"

questions = []
with open('questions.json', 'r') as f:
    questions = json.load(f)

while status == "setup":
    try:
        playing = int(input("Möchtest du Fragen beantworten(1) oder welche erstellen(2)? "))
        status = "beginning"
    except ValueError:
        print("Bitte gib eine Zahl ein")
        
if status == "beginning":
    print("Wilkommen zum Quiz Spiel!")

match playing:
    case 1:
        status = "playing"

        score = 0
        total = 0
        wrong = 0
        for i in questions:
            #skip None
            if i == None:
                continue

            print(i['question'])
            answer = input('Antwort: ').lower()

            if answer == i['answer'].lower():
                print('Richtig!')
                score += 1
            else:
                print('Falsch!')
                wrong += 1
            total += 1

        print(f'Du hast {score} von {total} Fragen richtig beantwortet!')
        print(f'Das sind {score / total * 100}%')
    case 2:
        status = "making"

        print('Hier siehst du eine Liste mit bereits gestellten Fragen');

        

        while status == "making":
            making_question_num = input('Welche Frage möchtest du füllen? (Falls du aufhören möchtest tippe quit ein, zum anzeigen aller Fragen list) ')
            match making_question_num:
                case "quit":
                    status = "exiting"

                    with open('questions.json', 'w') as f:
                        json.dump(questions, f)

                case "list":
                    index = 1
                    for i in questions:
                        print(f'Frage {index}: {i}')
                        index += 1
                case _:
                    if making_question_num.isnumeric():
                        questions_len = len(questions)
                        question_index = int(making_question_num) - 1

                        if question_index <= 0:
                            print('Bitte gib eine Zahl größer als 0 ein')
                            continue
                        elif question_index > questions_len:
                            print(f'Die Frage {question_index + 1} existiert nicht!')
                            continue
                        else:
                            question_text = input('Wie soll die Frage lauten? ')
                            question_answer = input('Wie lautet die Antwort? ')

                            question_dict = {
                                'question': question_text,
                                'answer': question_answer
                            }

                            if question_index > questions_len - 1:
                                questions.append(question_dict)
                            else:
                                questions[question_index] = question_dict
                        pass
                    else:
                        print("Bitte gebe eine Zahl ein!")
