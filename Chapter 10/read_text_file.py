filename = "text_files/Python Learning.txt"

with open(filename) as file_object:
    #all at once
    """
    print("all at once")
    contents = file_object.read()
    print(contents)
    print()
    """

    """
    #loop over by line
    print("loop over by line")
    for line in file_object:

        print(line.strip())
    print()
    """

    #store in list
    #print("store in list")
    print("replace method")
    lines = file_object.readlines()
    [print(line.replace("Python","Rust").strip()) for line in lines]
    #[print(line.strip()) for line in lines]
