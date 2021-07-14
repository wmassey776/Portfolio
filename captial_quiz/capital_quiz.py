# -*- coding: utf-8 -*-'
# !/usr/bin/env python3
"""
created: 07/5/2021
@author: Will Massey
project: State Capital Quiz
"""
import sys
from random import choice, shuffle


def main():
    # A list of States in alphabetical order:
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
              'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
              'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
              'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New York', 'New Mexico', 'North Carolina',
              'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
              'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
              'Wisconsin', 'Wyoming']

    # A list of corresponding Capitals (!): The indices of `states` and `capitals` match each another!
    # (i.e., capital[0] = Montgomery,  states[0] = Alabama). This is True for all!
    capitals = ['Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover',
                'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka',
                'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'St.Paul', 'Jackson',
                'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Albany', 'Santa Fe',
                'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia',
                'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston',
                'Madison', 'Cheyenne']

    # (!): A list data-type was chosen over a dictionary (hashtable) to conserve on memory size:
    states_and_capitals: list[tuple[str, str]] = list(zip(states, capitals))

    # Start the Quiz!
    start_quiz(states_and_capitals)


def start_quiz(state_capital_list: list[tuple[str, str]]) -> None:
    """
start_quiz(state_capital_list):
    This function takes in a list of tuples containing (states & capitals)
    and asks "What is the capital of (state)?," until the list is exhausted.
    Each question has (4) multiple-choice options to choice from.
    When the quiz is complete, the total CORRECT_ANSWERS is evaluated and a grade given.
    The user will then have an option to play again or quit the quiz.
    Once the quiz begins, there is no option to quit until the quiz ends.

    :param:
        state_capital_list (list[tuple[str, str]]): This is a list of matching (states, capital) tuples (50 total).
    :returns:
        (None): This function only prints.
    """

    # First, let's shuffle the list of states_and_capitals:
    shuffle(state_capital_list)

    # This represents the total of correct answers:
    CORRECT_ANSWERS = 0

    # The enumerate is used to keep track of question number. Starts at question # 1.
    for i, state_capital in enumerate(state_capital_list, start=1):
        # The name of the State:
        STATE: str = state_capital[0]
        # The name of the Capital:
        CAPITAL: str = state_capital[1]
        # This is a list of Capitals which will be used to fill the multi-choice options.
        AVAILABLE_OPTIONS = [i[1] for i in state_capital_list]

        # Setup four (4) MULTIPLE_CHOICE_ANSWERS. 1 correct and 3 incorrect.
        # Now adding 1 correct answer to multiple-choice answers:
        MULTIPLE_CHOICE_ANSWERS = {CAPITAL}  # (!): # The set data-type is used is to ensure no duplicates are added.
        # Now adding 3 incorrect answers to multiple-choice list:
        while len(MULTIPLE_CHOICE_ANSWERS) != 4:  # (!) : This integer sets the number of available choices.
            MULTIPLE_CHOICE_ANSWERS.add(choice(AVAILABLE_OPTIONS))

        # Now create a hashtable of the MULTIPLE_CHOICE_ANSWERS:
        # This is so the user can select a numeric key value to answer the question.
        MULTIPLE_CHOICE_ANSWERS: dict[int: str] = {answer_key: capital for (answer_key, capital) in
                                                   enumerate(MULTIPLE_CHOICE_ANSWERS, start=1)}

        # Start asking the Questions:
        print(f'QUESTION ({i}/{len(state_capital_list)}): ', end='')
        print(f'What is the Capital of {STATE}?')
        # Now display the MULTIPLE_CHOICE_ANSWERS:
        for answer_key, capital in MULTIPLE_CHOICE_ANSWERS.items():
            print(f'  {answer_key} {capital}')
        print('Enter a digit between [1-4]:')

        # Get the user's response:
        while True:
            users_response = input('> ')
            if not users_response.isdigit() or int(users_response) not in range(1, 5):
                print('Invalid response!\nEnter a digit between [1-4]:')
                continue
            else:
                break

        # Evaluate the users_response:
        if MULTIPLE_CHOICE_ANSWERS.get(int(users_response)) == CAPITAL:
            # Add 1 point to CORRECT_ANSWERS if the answer is correct.
            CORRECT_ANSWERS += 1
            print(f'>> Correct!!')
        else:
            print(f'>> Incorrect! The capital of {STATE} is {CAPITAL}!')

    print('The Quiz is complete!')
    # Now evaluate CORRECT_ANSWERS:
    evaluate_score(CORRECT_ANSWERS)

    # Aks the user if they want to play again:
    play_again()


def evaluate_score(answered_correctly: int):
    """This function evaluates the user's score."""
    # This represents percentage of questions answered correctly:
    percentage = answered_correctly / 50 * 100  # 50 states & capitals.
    grade = ''
    feedback = ''
    print('------ QUIZ RESULTS ------')
    print(f'TOTAL CORRECT: ({answered_correctly}/50)')
    if percentage >= 9:
        grade = 'A'
        feedback = 'Excellent job!'
    if 80 <= percentage <= 89:
        grade = 'B'
        feedback = 'Good work!'
    if 70 <= percentage <= 79:
        grade = 'C'
        feedback = 'This is satisfactory.'
    if 60 <= percentage <= 69:
        grade = 'D'
        feedback = 'This is barely passing. You should study some more.'
    if percentage < 59:
        grade = 'F'
        feedback = 'You failed... You need to study some more!'
    print(f'PERCENTAGE: {percentage:.2f}%')
    print(f'GRADE: {grade}')
    print(f'{feedback}')


def play_again():
    while True:
        option = input('Would you like to play again (yes or no?): ')
        if option.isdigit() or not option[0] in 'yn':
            print('Please enter (yes or no?)')
            continue
        if option.lower().startswith('y'):
            return main()
        else:
            print('Thanks for playing!')
            sys.exit()


if __name__ == '__main__':
    main()
