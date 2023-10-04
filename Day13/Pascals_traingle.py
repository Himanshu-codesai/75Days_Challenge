def pascals_traingle(r,c):
    rows=r-1
    column=c-1
    r_fact=1   
    output=1
    for i in range(rows,0,-1):
        r_fact=r_fact*i
    c_fact=1
    for j in range(column,0,-1):
        c_fact=c_fact*j
    
    rc=rows-column
    rc_fact=1
    for j in range(rc,0,-1):
        rc_fact=rc_fact*j
    
    output=r_fact/(c_fact*rc_fact)
    return output


print(pascals_traingle(5,3))

# n C r
#r-1 O c-1 
