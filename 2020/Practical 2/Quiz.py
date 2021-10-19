import random
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def __str__(self):
        return f"Question is {self.question}"
class Quiz:
    questions = []
    index_check = []
    score = 0
    def __init__(self):
        while 1:
            self.create_question()
            m = input("Do you want to quit?: ").upper()
            if m == "YES" and len(self.__class__.questions) >= 3:
                break
            elif m == "NO":
                pass
            else:
                input("I shall assume you want to add more!")
        print("Time for a game!")
        while len(self.__class__.index_check) != 3:
            p = random.randint(0, len(self.__class__.questions))
            if p in self.__class__.index_check:
                continue
            print(self.__class__.questions[p])
            self.__class__.index_check.append(p)
            if input("What is the answer: ") == self.__class__.questions[p].answer:
                print('Correct!')
                self.__class__.score += 1
            else:
                print("The correct answer is " + self.__class__.questions[p].answer)
    def create_question(self):
        self.questions.append(Question(input("Enter Question: "), input("Enter Answer: ")))
quiz = Quiz()
