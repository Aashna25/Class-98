#creating a function named as countWordsFromFile
def countWordsFromFile():
    # creating a variable named as fileName 
    # which will store the name of the file entered by the user
    fileName =  input("Enter the file name:- ")
    # creating a variable, numberOfWords with the value of 0
    numberOfWords = 0
    # creating a variable- opens the fileName
    file =  open(fileName, 'r')
    # for loop
    for line in file:
        # variable words storing the values from the split function- spliting the lines
        words = line.split()
        # variable numberOfWords incrementing its value
        numberOfWords = numberOfWords + len(words)
    # display the text
    print("Number of words:")
    print(numberOfWords)

#calling the function
countWordsFromFile()
