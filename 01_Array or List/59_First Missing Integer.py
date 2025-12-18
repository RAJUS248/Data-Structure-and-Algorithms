def firstMissingPositive(A):
        
        n = len(A)
        
        # Step 1: Place numbers in their correct spots
        for i in range(n):
            # While A[i] is a valid positive number AND it is not in the correct spot
            # We keep swapping it to its correct spot (A[i] - 1)
            while 1 <= A[i] <= n and A[A[i] - 1] != A[i]:
                correct_idx = A[i] - 1
                # Swap A[i] with A[correct_idx]
                A[i], A[correct_idx] = A[correct_idx], A[i]
                
        # Step 2: Scan for the first mismatch
        for i in range(n):
            if A[i] != i + 1:
                return i + 1,A
                
        # If all spots [1...N] are filled, the missing number is N + 1
        return n + 1
            
A = [3,1,4,-1,1,1]
print(firstMissingPositive(A))