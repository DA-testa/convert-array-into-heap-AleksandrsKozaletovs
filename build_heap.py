# python3

def build_heap(data):
    swaps = []
    loopCount = len(data) -1 
    parentElements = 0
    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    while loopCount != 0:
        lastElement = loopCount
        if lastElement != 0:
            parentElements = int((lastElement-1)/2)                
            if data[lastElement] < data[parentElements]: 
                data[lastElement],data[parentElements] = data[parentElements],data[lastElement]
                swaps.append([parentElements,lastElement])
            lastElement = parentElements

        loopCount -= 1
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    
    actionChoose = input()
    if  "i" in actionChoose.lower():        
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    elif "f" in actionChoose.lower():
        openFilename = input()
        if "a" in openFilename.lower():
            return
        else:
            with open("./tests/" + openFilename, mode = "r") as f:
                # input from keyboard
                n = int(f.readline())
                data = list(map(int, f.readline().split()))

            # calls function to assess the data 
            # and give back all swaps
    else:
        return
            # checks if lenght of data is the same as the said lenght
    assert len(data) == n
            
    # calls function to assess the data  and give back all swaps
    swaps = build_heap(data)            
    
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
