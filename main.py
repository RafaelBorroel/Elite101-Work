class ChatBot:
    def welcome_user(self):
        print("Hello! Welcome to the Elite 101 Chatbot!")

    def user_info(self):
        name = input("What is your name? ")
        age = input("How old are you? ")
        print(f"Nice to meet you, {name}. You are {age} years old. What can I help you with?")
        return name

    def ask(self, name):
        print(f"{name}, how can I help you today?")

    def menu(self):
        print("Choose an option:")
        print("1. Get information")
        print("2. Ask a question")
        print("3. Talk About Weather")
        print("4. Exit")

    def choose_option(self):
        option = input("Enter a number: ")
        if option == "1":
            print("You chose: Get information.")
        elif option == "2":
            print("You chose: Ask a question.")
        elif option == "3":
            print("You chose: Receive recommendations.")
        elif option == "4":
            print("Goodbye!")
        else:
            print("Sorry, that's not a valid option. Please try again.")

    def run(self):
        self.welcome_user()
        user_name = self.user_info()
        self.ask(user_name)
        self.menu()
        self.choose_option()

# To run the chatbot
bot = ChatBot()
bot.run()

