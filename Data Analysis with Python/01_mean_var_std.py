import numpy as np

def calculate (number_list):

    #Raise error if list does not contain nine elements
    if len(number_list) != 9:
        raise ValueError(f"List must contain nine numbers.")
    else:
    
        #Turn list into numpy array and reshape it into a 3x3 matrix
        matrix = np.array(number_list).reshape(3,3)
    
        #Perform the mathematical operations while converting these into lists
        #Mean
        mean = [list(matrix.mean(axis=0)),
                list(matrix.mean(axis=1)),
                matrix.mean()]
    
        #Variance 
        var = [list(matrix.var(axis=0)),
               list(matrix.var(axis=1)),
               matrix.var()]
    
        #Standard deviation 
        std_dev = [list(matrix.std(axis=0)),
                   list(matrix.std(axis=1)),
                   matrix.std()]
        
        #Maximum arrays and element
        maximum = [list(matrix.max(axis=0)),
                   list(matrix.max(axis=1)),
                   matrix.max()]
        
        #Minimum arrays and element
        minimum = [list(matrix.min(axis=0)),
                   list(matrix.min(axis=1)),
                   matrix.min()]
    
        #Sum of elements 
        sums = [list(matrix.sum(axis=0)),
                list(matrix.sum(axis=1)),
                matrix.sum()]
    
        #Store results in dicitonary 
        calculations = {'mean' : mean,
                        'variance' : var,
                        'standard deviation' : std_dev,
                        'max' : maximum,
                        'min' : minimum, 
                        'sum' : sums}
        
        return calculations