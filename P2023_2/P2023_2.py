while True:
    try:
        def find_largest_min_among_negative_diagonal(matrix):
            n = len(matrix)
    
        
            negative_diagonal_rows = [i for i in range(n) if matrix[i][i] < 0]
    
       
            if not negative_diagonal_rows:
                return None
    
       
            min_elements = [min(matrix[i]) for i in negative_diagonal_rows]
    
        
            largest_min = max(min_elements)
    
            return largest_min

    
        n = int(input("Enter the matrix's size: "))
        matrix = []

        print("Enter the elements split:")
        for i in range(n):
            row = input().split()
            matrix.append([float(x) for x in row])

        result = find_largest_min_among_negative_diagonal(matrix)
        if result is not None:
            print("The largest element among the minimum elements in rows with negative diagonal elements:", result)
        else:
            print("There are no rows with negative diagonal elements in the matrix.")
    except:
        print("You have probably followed the instructions uncorrectly, please try once more!")












    while True:
        choice = input('Do you want to continue (+/-)? ').strip().lower()
        if choice in ('+', '-'):
            break
        else:
            print('Please enter a valid response ("+" or "-").')

    if choice == '-':
        break