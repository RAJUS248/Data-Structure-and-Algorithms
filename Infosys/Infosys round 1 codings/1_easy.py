import sys

def solve():
    # Read all inputs from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    # Parse N and the array
    n = int(data[0])
    nums = [int(x) for x in data[1:n+1]]
    
    total_operations = 0
    prev_val = 0  # Tracks the previous element's value (0 for the first element)
    
    for i in range(n):
        factor = i + 1
        
        # Lower bound constraint to keep it strictly increasing and >= original value
        lower_bound = max(nums[i], prev_val + 1)
        
        # Find the smallest multiple of 'factor' that is >= lower_bound
        if lower_bound % factor == 0:
            target_val = lower_bound
        else:
            target_val = ((lower_bound // factor) + 1) * factor
            
        # Add the operations needed for the current element
        total_operations += (target_val - nums[i])
        
        # Update prev_val for the next iteration
        prev_val = target_val
        
    print(total_operations)

if __name__ == '__main__':
    solve()
