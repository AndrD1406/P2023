def remove_duplicates(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements
while True:      
        
        try:
            n1 = input("Enter the number of elements:")
            
            input_list = input("Enter the array elements split: ").split()
            input_list = [int(element) for element in input_list]  

            
            result = remove_duplicates(input_list)

            print("Unique elements:", result)
           
            
        except:
             print("the number should have been an integer and as well as the values!")    
        while True:
            choice = input('Do you want to continue (+/-)? ').strip().lower()
            if choice in ('+', '-'):
                break
            else:
                print('Please enter a valid response ("+" or "-").')
        if choice == '-':
            break
