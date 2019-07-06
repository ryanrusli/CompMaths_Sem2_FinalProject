
def bisection(f,x1,x2,dGoal):
    
    xs = x1
    xe = x2
    xm = (xs+xe)/2
    xm1 = (xs+xe)/2
    
    if (f(xs) * f(xe) > 0):
        print("Value not found between the bounds")
        return None
    
    if (f(xs)>0):
        
        while (True):
            if (f(xm) > 0):
                xs = xm 
                
            elif (f(xm) < 0):
                xe = xm      
            xm1  = (xs + xe)/2
            
            if (abs(f(xm1) - f(xm)) <= dGoal):
                return xm1
            xm = xm1
    
    
    elif (f(xs)<0):
        while (True):
            if (f(xm) > 0 ):
                xe = xm 
                
            elif (f(xm) < 0):
                xs = xm
            
            xm1  = (xs + xe)/2
            
            if (abs(f(xm1) - f(xm)) <= dGoal):
                return xm1
            xm = xm1
            


            
        
        
        
        
         