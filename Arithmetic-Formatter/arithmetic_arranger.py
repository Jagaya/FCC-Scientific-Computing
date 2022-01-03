def arithmetic_arranger(arr, solving = False):
    arranged_problems = ""
    splitted = [[],[],[],[],[]]

    #splitting the string and looking for errors
    if len(arr)>5:
        arranged_problems = "Error: Too many problems."

    for i in range(len(arr)):
        splitted[i] = arr[i].split()
        if splitted[i][1] != "+" and splitted[i][1] != "-":
            arranged_problems = "Error: Operator must be '+' or '-'."
        try:
            int(splitted[i][0])
            int(splitted[i][2])
        except:
            arranged_problems = "Error: Numbers must only contain digits."

        if len(splitted[i][0])>4 or len(splitted[i][2])>4:
            arranged_problems = "Error: Numbers cannot be more than four digits."

        if arranged_problems:
            break

    #no error found
    if not arranged_problems:
        #build the first line
        for i in range(len(arr)):
            spaces = max(len(splitted[i][0]), len(splitted[i][2]))
            arranged_problems +=(" "*(spaces-len(splitted[i][0])+1) + " " + splitted[i][0])
            if i != len(arr)-1:
                arranged_problems += "    "
                
        #add the second line
        arranged_problems += ("\n")
        for i in range(len(arr)):
            spaces = max(len(splitted[i][0]), len(splitted[i][2]))
            arranged_problems += (splitted[i][1] + " "*(spaces-len(splitted[i][2])+1) + splitted[i][2])
            if i != len(arr)-1:
                arranged_problems += "    "
                
        #add the third line
        arranged_problems +=("\n")
        for i in range(len(arr)):
            spaces = max(len(splitted[i][0]), len(splitted[i][2])) +2
            arranged_problems +=("-"*spaces)
            if i != len(arr)-1:
                arranged_problems += "    "
        
        #add the solution-line
        if solving: 
            arranged_problems += ("\n")
            solved = 0
            for i in range(len(arr)):
                if splitted[i][1] == "+":
                    solved = int(splitted[i][0]) + int(splitted[i][2])
                else:
                    solved = int(splitted[i][0]) - int(splitted[i][2])
                spaces = max(len(splitted[i][0])+2, len(splitted[i][2])+2, len(str(solved)))
                arranged_problems += (" "*(spaces-len(str(solved))) + str(solved))
                if i != len(arr)-1:
                    arranged_problems += "    "
    
    #print("\n" + arranged_problems)
    return arranged_problems