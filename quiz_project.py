import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0

    def update_score(self, points):
        self.score += points
        print(f"{self.name}'s score is now {self.score}")

class Question:
    def __init__(self, question, correct_answer, incorrect_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

    def is_correct(self, answer):
        return answer == self.correct_answer

class Quiz:
    def __init__(self, user):
        self.user = user
        self.questions = []
        self.user_answers = []

    def fetch_questions(self):
        url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json()['results']
            for item in results:
                question = Question(item['question'], item['correct_answer'], item['incorrect_answers'])
                self.questions.append(question)
        else:
            print("Failed to retrieve data from the API")

    def play(self):
        for question in self.questions:
            print(question.question)
            answer = input("Type 'True' or 'False': ").strip()
            self.user_answers.append((question, answer))
            if question.is_correct(answer):
                print("Correct!")
                self.user.update_score(1)
            else:
                print("Incorrect!")

    def show_results(self):
        print(f"\nFinal Score for {self.user.name}: {self.user.score}/{len(self.questions)}")
        print("Your answers:")
        for question, answer in self.user_answers:
            correct = question.correct_answer
            print(f"Q: {question.question} | Your answer: {answer} | Correct answer: {correct}")

def main():
    # Create a user
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    user = User(name, age)

    # Create a quiz
    quiz = Quiz(user)

    # Fetch questions
    quiz.fetch_questions()  # Fixed number of questions (10)

    # Start the quiz
    quiz.play()

    # Show results
    quiz.show_results()

if __name__ == "__main__":
    main()
