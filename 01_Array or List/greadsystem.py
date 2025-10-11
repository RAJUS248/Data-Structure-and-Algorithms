def grad_system1(grads):
    
    for grad in grads:
        
        if (grad + 2)% 5 == 0 :
            new_grad = grad + 2 
            
        else:
            new_grad = grad    
        print(new_grad)
        
        
grads = [4,73,67,38,33]
grad_system1(grads)

# new 
def grade_system(grades):
    result = []         # creating new list
    for grade in grades:
        
        if grade < 38:
            result.append(grade)   # insted of  -- > print(grade)  becuse adding the value to new list
            

        else:
            mul_of_5 = ((grade//5)+1) * 5

            if mul_of_5 - grade < 3:
                result.append(mul_of_5) # print(mul_of_5)
            
            else:
                result.append(grade) # print(grade)
        
    for grade in result:
        print(grade)
            
grades = [4,73,67,38,33]
grade_system(grades)



