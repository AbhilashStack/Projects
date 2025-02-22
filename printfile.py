#file manupulation read and write an new text file
with open('checkfile.txt','r')as file:
    with open('newstub.txt','w') as targetfile:
        for line in file:
            if 'Abhilash' in line:
                targetfile.write(line)
print(("file created"))