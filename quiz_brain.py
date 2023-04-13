#asking the questions
#checking if answer was correct
#checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list 
        self.score = 0

    def still_has_q(self):
        return self.question_no < len(self.question_list)
      
        
    def next_question(self):
         current_question = self.question_list[self.question_no]
         self.question_no += 1
         user_ans=input(f"Q.{self.question_no }: {current_question.text} (True/False): ")
         self.check_ans(user_ans, current_question.answer)

    def check_ans(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it right!")

        else:
            print("Oops! Wrong answer")
        
        print(f"Your current score: {self.score}")
        print("\n")