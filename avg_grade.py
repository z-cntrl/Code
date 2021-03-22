################################################################################
# Author: Chloe Weber
# Date: 2/25/2021
# Description: A set of functions that will calculate the average grade from
#a user input of five grades, rejecting invalid ones (above 100 or below 0)
################################################################################

# Write function(s) here get_valid_score, calc_average, determine_grade
def main():
    #should the grade values be determined in main()?

    scores = []
    for i in range(5):
        score = get_valid_score()
        scores.append(score)
        print(f'The letter grade for {score:.1f} is {determine_grade(score):}.')
    print(f'The average score is {calc_average(scores):.2f}.')

def get_valid_score():
    ## Variables above
    while True:
        score = float(input('Enter a score: '))
        if score > 100 or score < 0: #THIS NEEDS A WHILE LOOP SO IT REJECTS
        #AN INVALID UNTIL A VALID IS PUT IN
            print(f'Invalid Input. Please try again.') #super confused how to make 'Invalid' go back
        else:
            return score

def calc_average(numbers):
    total = 0
    count = 0
    for x in numbers:
        total += x
        count += 1
    avg = total/count
    return avg

def determine_grade(score):
#    A = 90
#    B_cutoff = 80
#    C_cutoff = 70
#    D_cutoff = 60
#    F_cutoff = 0
    if score >= 90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


if __name__ == '__main__':
    main()
