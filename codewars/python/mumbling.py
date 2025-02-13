def accum(st): # Start of accum function
    a=0 # Number for the letter you want from st
    ans = "" # Declare ans
    for x in st: # Start a for loop
        b = st[a] * (a+1) # Set b to st[a] a+1 times
        b = b.capitalize() # Capitalize b
        ans = ans + b + "-" # Set ans to previous ans + b + "-"
        a += 1 # Add one to a before restarting for loop
    ans = ans[:-1] # Remove last char from ans
    return(ans) # Return ans