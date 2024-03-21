questions = ["what is the capital of india?",
              "who is prime minister of india?",
              "how many states in india?",
              "how many days in august month?",
              "tajmahal is situated in which place?"]
answer = [ "delhi", 
            "narendra modi",
            "29",
            "31",
            "agra"]
score = 0
for i in range (0, len(questions)):
    print(questions[i])
    user_answer = input("Answer: ")
    
    if user_answer == answer[i]:
        print("correct")
        score+= 1
    else:
        print("incorrect")
print("your score is", score)