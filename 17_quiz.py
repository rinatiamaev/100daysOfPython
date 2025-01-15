# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.follower = 0
#         self.following = 0

#     def follow(self, user):
#         user.follower += 1
#         self.following += 1

# user1 = User("1", "Max")
# user2 = User("2", "Mia")
# user1.follow(user2)

# print(user1.follower)
# print(user1.following)
# print(user2.follower)
# print(user2.following)

question_data = [{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"The very first recorded computer bug; was a moth found inside a Harvard Mark II computer.","correct_answer":"True","incorrect_answers":["False"]},
{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"MacOS is based on Linux.","correct_answer":"False","incorrect_answers":["True"]},
{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"The first dual-core CPU was the Intel Pentium D.","correct_answer":"False","incorrect_answers":["True"]},
{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"The open source program Redis is a relational database server.","correct_answer":"False","incorrect_answers":["True"]},
{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"Windows NT; is a monolithic kernel.","correct_answer":"False","incorrect_answers":["True"]},
{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.","correct_answer":"False","incorrect_answers":["True"]},
{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"Early RAM was directly seated onto the motherboard and could not be easily removed.","correct_answer":"True","incorrect_answers":["False"]},
{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"The first computer bug was formed by faulty wires.","correct_answer":"False","incorrect_answers":["True"]},
{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ","correct_answer":"True","incorrect_answers":["False"]},
{"type":"boolean","difficulty":"medium","category":"Science: Computers","question":"The common software-programming acronym I18; comes from the term Interlocalizatio.","correct_answer":"False","incorrect_answers":["True"]},
]

class Questions:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        

quest_bank = []
for question in question_data:
    quest_text = question["question"]
    quest_answer = question["correct_answer"]
    newQuest = Questions(quest_text, quest_answer)
    quest_bank.append(newQuest)


class QuizzGame:
    def __init__(self, q_list):
        self.quest_nb = 0
        self.quest_list = q_list
        self.score = 0
    
    def nextQuest(self):
        cur_q = self.quest_list[self.quest_nb]
        self.quest_nb += 1
        self.useranswer = input(f"Question{self.quest_nb}: {cur_q.text} (true/false): ")
        self.check_answer(self.useranswer, cur_q.answer)
        

    def still_has_quest(self):
        return self.quest_nb < len(self.quest_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right")
            self.score += 1
        else:
            print("You are wrong")
        print(f"correct answer was {correct_answer}")
        print(f"current score is {self.score}/{self.quest_nb}")
        print("\n")
        


quiz = QuizzGame(quest_bank)
while quiz.still_has_quest():
    quiz.nextQuest()
print(f"final score is {quiz.score}/{quiz.quest_nb}")
    
    



