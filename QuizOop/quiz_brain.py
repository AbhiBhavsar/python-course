
class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list
    
    def ask_question(self):
        self.question_number+=1
        print(f"Q.{self.question_number}: {self.question_list[self.question_number-1].text}")
        user_answer=input(f'Your answer: ')
        self.check_answer(user_answer,self.question_list[self.question_number-1].answer)
    
    def should_continue(self):
        return self.question_number< len(self.question_list)
    
    def check_answer(self,user_answer,correct_answer):
        if(user_answer.lower()==correct_answer.lower()):
            self.score+=1
            print(f"That's right. Score: {self.score}/{self.question_number}")
        else:
            print(f"That's wrong.")
        
        print(f" Correct ans: {correct_answer} \n Score: {self.score}/{self.question_number}\n")