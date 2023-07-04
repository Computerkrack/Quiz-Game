x = "not ja"
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


# if playing == "2":
#     status = "making"

#     print("Hier siehts du eine Liste mit bereits gestellten Fragen")
#     print("Frage1: " + )

#     while status == "making":
#         makingquestionnum = input('Welche Frage möchtest du füllen? (Falls du aufhören möchtest tippe quit ein) ')
#         if makingquestionnum == "quit":
#             status = "beginning"
#         if makingquestionnum == "1":
#             questiongood = x
#             while questiongood != "ja":    # ist zwar schon kommentar aber egal kennst du booleans also true und false
#                 Question = input("Was soll die Frage sein? ")
#                 Question1 = Question
#                 questiongood = input("Ist die Frage so gut?: " + Question + " ")

#             answer_good = x
#             while answergood != "ja":
#                 answer = input("Gebe jetzt bitte die Anwort ein: ")
#                 answer1 = answer 
#                 answergood = input("Ist die Antwort so gut?: " + answer + " ")
        
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
                        pass # hier kann man dann checken das die zahl nicht zu groß oder zu klein ist, dafür einfach die var zu einem int machen und dann mit len() die länge der liste nehmen
                        # wenn der index angemessen ist dann deine struktur zum schreiben musst halt auf das richtige listen element gehen
                            # das wäre dann schon ein guter punkt könnte man einen git commit machen
                            # naja ich gehe jetzt auch raus, schreibe mir dann einfach später nochmal
                        # sonst dem user einfach eine fehlermeldung gönnen
                    else:
                        print("Bitte gebe eine Zahl ein!")

# wenn man das nicht versteht dann gibt es das hier: ChatGPT
