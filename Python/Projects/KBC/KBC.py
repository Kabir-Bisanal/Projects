questions = [
["Who is the current prime minister of India?", "Narendra modi","Rahul gandhi","Priya desai","Draupati murmu", 1],
["What is the capital of canada?","bejieng","oklahoma","ottawa","moscow", 3],
["Which animal/bird is the fastest in the world?","Cheetah","Flacon eagle","hippopotamus","elephant", 2]
]
for question in questions:
    print(question[0])
    print(f"Option 1 :{question[1]}")
    print(f"Option 2 :{question[2]}")
    print(f"Option 3 :{question[3]}")
    print(f"Option 4 :{question[4]}")

    a=int(input("Enter your choice: \n"))
    if (a==question[5]):
        print("Saaath karoooddd")
    else:
        print(f"Aap mumbai nahi aa skte the correct option was {question[5]} ")
        break