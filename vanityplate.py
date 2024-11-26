def checkPlates(): 
    plate = input("Enter a plate: ")
    if len(plate) < 2 or len(plate) > 6: 
        print("Usage: plate must be between 2 and 6 characters")
    if validatePlate(plate) == True: 
        print('Plate is valid')
        return True
    else:
        print('Plate is invalid')
        return False
    

def validatePlate(plate): 
    plateLength = len(plate)
    midpoint = calculateMidPoint(plateLength)
    firstdigit = 0
    print(f'Midpoint | {midpoint}')
    print(midpoint)
    if plate[0].isdigit() or plate[1].isdigit():
        print("All vanity plates must start with at least two letters.")
        return False
    if plate[midpoint].isdigit(): 
            print("Numbers cannot be used in the middle of a plate")
            return False
    for i in range(plateLength):
         if plate[i].isdigit(): 
              firstdigit = int(i)
    
    if plate[firstdigit] == 0: 
         print("The first number cannot be a zero")
         return False
    
    if firstdigit > 0 and plate[plateLength - 1].isalpha(): 
         print("Numbers must come at the end of the plate")
         return False
    
    return True

def calculateMidPoint(length: int):
     if length % 2 == 0:
          return (length // 2) - 1
     elif length == 0: 
        print('Provide a positive integer value')
        return False
checkPlates()

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.