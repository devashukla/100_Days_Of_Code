studentScores = [120, 112, 134, 142, 123, 154, 172, 165, 129, 119]

totalScore = sum(studentScores)
print(totalScore)

# sum => The sum() function returns a number, the sum of all items in an iterable.

#Using for loop
sum = 0
for score in studentScores:
    sum += score
print(sum)

#Finding the maximum value using for loop
maxScore = 0
for score in studentScores:
    if score > maxScore:
        maxScore = score
print(maxScore)