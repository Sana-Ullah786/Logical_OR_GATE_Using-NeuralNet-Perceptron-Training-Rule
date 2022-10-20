import numpy as np,pickle
from prettytable import PrettyTable

def activationFunction(linearUnit):
    if linearUnit <= 0:
        return 0
    else:
        return 1


def orGate(Input, weights, bias):
    return activationFunction(np.dot(weights, Input)+bias)


def printTable(a,b,output):
    myTbale=PrettyTable(["a","b","OR"])
    myTbale.add_row([a,b,output])
    print(myTbale)
if __name__ == '__main__':
    with open('OR.pkl','rb') as f:
            parameters=pickle.load(f)
    while True:
        try: 
            a,b=input("Enter a and b (N to Exit) = ").split()
            if(int(a)<0 or int(a)>1 or int(b)<0 or int(b)>1 ):
                print("Invalid Inputs")
                continue
            printTable(a,b, orGate(np.array([int(a), int(b)]),parameters[0],parameters[1]))
        except:
            break
    
    

