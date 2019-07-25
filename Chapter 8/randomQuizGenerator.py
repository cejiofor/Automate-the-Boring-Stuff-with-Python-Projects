##! python3
#randomQuizGenerator.py - Creates quizzes with questions and answer in random order, along with an answer key
# Project 1 from Chapter 7 of Automate the Boring Stuff with Python

import random
import os

#Quiz data, with the states as keys and capitals as values
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Set a loop to creat 35 unique quizzes fot the students
for quizNum in range(3):
    #Create a text file with th quiz number in the name of the file
    quiz = open(f"quiz{quizNum+1}.txt", 'w')

    # Write quiz header information to the file then close it 
    quiz.write("Name: \nDate: \nPeriod: \n")
    quiz.write(f'\t\tState Capital Quiz: Form {quizNum+1}\n\n')    
    quiz.write('Please select one of the four options for each question\n\n')
    quiz.close()

    #create a text file for the answer key to the quiz matching the quiz number file
    answer = open("quiz"+f"{quizNum+1}_key.txt", 'w')

    #write answer key header information to the file then close it
    answer.write(f'Key for Quiz Form {quizNum+1}.\n\n')
    answer.close()
    
    # ref: https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python
    states = list(capitals.keys())
    random.shuffle(states)
    questionNum = 1

    multiChoice = 'ABCD'

    for state in states:
        quiz = open(f"quiz{quizNum+1}.txt", 'a')
        answer = open(f"quiz{quizNum+1}_key.txt", 'a')

        quiz.write(f"\nQuestion {questionNum}: What is the capital of {state}?\n")
        correctAnswer = capitals[state]
        
        #Temporary copy of list of states, with current/working state removed so only other citys reamin in random selection for multiple choice options
        _states = states.copy()
        _states.remove(state)
        answerOptions = []

        for i in range(3):
            randomState = random.choice(_states)
            answerOptions.append(capitals[randomState])
            _states.remove(randomState)

        answerOptions.append(correctAnswer)
        random.shuffle(answerOptions)

        for i in range (len(multiChoice)):
            quiz.write(f"\t{multiChoice[i]}: {answerOptions[i]} \n")
            if answerOptions[i] == correctAnswer:
                answer.write(f'Question {questionNum}: {multiChoice[i]} - {correctAnswer}\n')
        questionNum +=1
    answer.close()
    quiz.close()

#TODO: Create 50 multiple-choice questions for each quiz in random order, providing correct answer and 3 random wrong answers for each question

#TODO: Write quiz to 35 text files

#TODO: Write Answer key to 35 text files
