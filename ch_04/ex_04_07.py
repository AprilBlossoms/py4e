# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade
# that takes a score as its parameter and returns a grade as a string.

score = input('Enter Score')

def computegrade(score):
    try:
        score = float(score)
        if score > 1.0:
            return('Bad Score')
        elif score >= 0.9:
            return('A')
        elif score >= 0.8:
            return('B')
        elif score >= 0.7:
            return('C')
        elif score >= 0.6:
            return('D')
        else:
            return('F')
    except:
        return('Bad score')

print(computegrade(score))
