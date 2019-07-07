import numpy as np
import matplotlib.pyplot as plt


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
            

def mylagrange(x,y,val):
    
    l_val = []
    for i in range(0,len(x)):
        l_val.append(1)
        
    y_fin = 0
    
    for i in range(0,len(x)):
        for j in range(0,len(x)):
            
            if (i != j):
                l_val[i] *= (val - x[j])/(x[i]-x[j])
        
    for i in range(0,len(y)):
        y_fin += y[i] * l_val[i]
    
    return y_fin
            
        

def f_diff_central(f, x, h, level):
    if (level == 1):
        return (f(x + h) - f(x - h)) / 2 * h
    elif (level == 2):
        # return (f_diff_forward(x,h, 1) - f_diff_backward(x,h))  /h
        return (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2
    elif (level == 3):
        return (-1 * f(x - 2 * h) + 2 * f(x - h) - 2 * f(x + h) + f(x + 2 * h)) / 2 * h ** 3
    elif (level == 4):
        return (f(x - 2 * h) - 4 * f(x - h) + 6 * f(x) - 4 * f(x + h) + f(x + 2 * h)) / h ** 4
    else:
        return 0

def centralNumDifferentiation(f,level):

    x = 1
    n = 10

    h_data = np.linspace(0.00001, 0.64, n)

    f_central = []
    f_central_2 = []
    f_central_3 = []
    f_central_4 = []

    for h in h_data:

        f_central.append(f_diff_central(f, x, h, 1))
        f_central_2.append(f_diff_central(f, x, h, 2))
        f_central_3.append(f_diff_central(f, x, h, 3))
        f_central_4.append(f_diff_central(f, x, h, 4))


    print("Central 1st", f_central)
    print("\n")
    print("Central 2nd", f_central_2)
    print("\n")
    print("Central 3rd", f_central_3)
    print("\n")
    print("Central 4th", f_central_4)
    print("\n")

    x_values = np.linspace(0, 100, 10)

    plt.style.use('ggplot')

    fig3 = plt.figure(1)
    plt.clf()
    ax3 = fig3.add_subplot(1, 1, 1)
    ax3.set_title("Central")
    ax3.plot(x_values, f_central, label='Central 1st')
    ax3.plot(x_values, f_central_2, label='Central 2nd')
    ax3.plot(x_values, f_central_3, label='Central 3rd')
    # ax2.plot(x_values, f_backward_4,label='Backward 4')
    ax3.legend()
    
    plt.savefig('result.png')
