#Linear search is searching through a list in a linear fashion, element after element 

# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

#1. write the statement in your words when you understand it in term of python.
#(Turn the problem in python logic)
#For example: We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.

# Cards >>>>> list 
# Query(Target Number) >>>>> any num in the list
# Position >>>>> index of the query in the list
#So, inputs >>>>> cards (i.e., [13,12,11,10,7,5,4,3,2]), query (lets suppose, 7)
# output >>>>> index = 4 

#STEP 2: List all CASES
# CASE no.1: The query number is present in the list.
# CASE no.2: What if The query number is not present in the list.
# CASE no.3: What if The list is empty.
# CASE no.4: What if The query number is the first item in the list.
# CASE no.5: What if The query number is the last item in the list.
# CASE no.6: What if The query number is in the last portion of the list.
# CASE no.7: What if The query number is in the first portion of the list.
# CASE no.8: What if There is only one number in the list, and it is the query number.
# CASE no.9: What if All the numbers in the list are repeating except query number.
# CASE no.10: What if The query number is repeating multiple times in the list.

#Step 3: Create an empty list to store the results of each case.
tests = []
#Step 4: Create dictionaries according to all cases (input, output)
tests.append({
    "input":{
        "cards":"[17,16,15,14,13,7,5,3]",
        "query": 15
    },
    "output": 2
})
tests.append({
    "input":{
        "cards":"[17,16,15,14,13,7,5,3]",
        "query": 20
    },
    "output": -1
})
tests.append({
    "input":{
        "cards":"[]",
        "query": 15
    },
    "output": -1
})
tests.append({
    "input":{
        "cards":"[17,16,15,14,13,7,5,3]",
        "query": 17
    },
    "output": 0
})
tests.append({
    "input":{
        "cards":"[17,16,15,14,13,7,5,3]",
        "query": 3
    },
    "output": 7
})
tests.append({
    "input":{
        "cards":"[17,16,15,14,13,7,5,3]",
        "query": 5
    },
    "output": 6
})
tests.append({
    "input":{
        "cards":"[17,16,15,14,13,7,5,3]",
        "query": 16
    },
    "output": 1
})

tests.append({
    "input":{
        "cards":"[15]",
        "query": 15
    },
    "output": 0
})
tests.append({
    "input":{
        "cards":"[17,17,17,17,15,14,14,14,14,13,13,13,3,3,3]",
        "query": 15
    },
    "output": 2
})
tests.append({
    "input":{
        "cards":"[17,15,15,15,15,15,14,13,3]",
        "query": 15
    },
    "output": 2
})


#You may not have to create this much edge cases in the interview if you have short time, but you should aim for at least 5 edge cases, it has a good impact on the interviewer as well

#You should be able to have done this in 2 to 3 minutes by the time with practice 

#Step 4:
#State the algorithm in your own words in plain english

def card_locate(cards, query):
    #Create a variable "position" equal to zero
    position = 0
    #Create a loop for repitition
    while True:
        #Check if element at current position equals to query
        if cards[position] == query:
            #If answer found, return and exit 
            return position
    #Otherwise, increment position value
    position += 1
    #Check whther we have reached the end of array
    if position == len(cards):
        #Number not found, return -1 
        return -1

result = card_locate(tests["input"]["query"])
result == output
print(result)







