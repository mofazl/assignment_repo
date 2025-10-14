#STUDENT1: MOHAMMED FAZLUR RAHMAN
#STUDENTID: 426001122
#STUDENT2: Maheep Kaur Rai
#STUDENTID: 751000235
#STUDENT3:
#STUDENTID:
def check_limit(borrowed):
    """
    TASK 1:
    This function takes the argument (borrowed), which refers to the number of books
    borrowed and checks whether the number of books borrowed are within or over limit
    """
    borrowed = int(borrowed) #Converts borrowed into an integer to allow numeric comparisons
    if borrowed < 0:
        return "Error: Invalid number of books" #Uses an if conditional to check if the number of books borrowed is less than 0, and if it is then returns a string stating that the number of books borrowed is invalid
    elif borrowed <= 3:
        return "Within limit" #Uses an elif conditional to check whether the number of books is within limit 
    elif borrowed <= 6:
        return "Over limit: Fine $5" #Uses an elif conditional to check whether the number of books is over limit and the fine is $5
    else:
        return "Over limit: Fine $10" #Uses an else conditional that is used when the number of books borrowed is greater than 6 and returns a string stating that the number of books borrowed is over limit and the fine is $10
def process_borrowers(filename):
    """
    TASK2:
    This function takes an argument (filename), then it opens the given file in read mode and prints the students name and their status.
    It also calls the previous function check_limit to check the status of the given student and uses try and except to check if theres
    invalid inputs in the BooksBorrowed column
    """
    with open(filename,"r") as file: #Uses a with as statement to open the file in read mode. with as is used as it automatically closes the file
        next(file) #Skips the header of the csv file
        for line in file:
            line = line.strip().split(",") #Strips the whitespace and splits the comma separated values into separate tokens
            try:
                name = line[0]
                status = check_limit(line[1]) #check_limit function is called to check the status
                print(name, status)
            except ValueError:
                print("Error: Non-numeric value for",line[0]) #Uses try and except to print the name and status of each entry but if there is an invalid input (number of books borrowed is non-numeric) then it prints out the students name and an error message stating there is a non numeric value associated to their entry

def calculate_average_books(filename):
    """
    This function takes an argument(filenam), it opens the given file and reads the file again and calculates the average number of books 
    borrowed by all students with valid numeric entries. The result is printed rounded of to two decimal places.
    total_books = 0 #
    count = 0
    with open(filename,"r") as f:
        for line in f:
            line = line.strip().split(",")
            if len(line) != 2:
                continue

            try:
                borrowed = int(line[1])
                if borrowed < 0:
                    continue

                total_books += borrowed
                count += 1

            except ValueError:
                continue
    average = total_books / count
    print(f"Average books borrowed:" {average:.2f}")

