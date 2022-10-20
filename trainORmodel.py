
import numpy as np,pickle


def activationFunction(linearUnit):
    if linearUnit <= 0:
        return 0
    else:
        return 1


def orGate(Input, weights, bias):
    return activationFunction(np.dot(weights, Input)+bias)


def updateBias(lr, loss):
    return lr*loss


def updateWeights(lr, loss, input):
    return lr*loss*input


def saveModel(w,b):
    parameters=[w,b]
    with open('OR.pkl','wb') as f:
        pickle.dump(parameters,f)
    print("Model Saved Successfully")


def trainModel(X, y, w, b, lr):
    flag = True
    while flag:
        for i in range(len(X)):
            output = orGate(X[i], w, b)
            if(output != y[i]):
                w[0] += updateWeights(lr, (y[i]-output), X[i][0])
                w[1] += updateWeights(lr, (y[i]-output), X[i][1])
                b += updateBias(lr, (y[i]-output))
                break
        else:
            break
    saveModel(w,b)
    
    


if __name__ == '__main__':
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = [0, 1, 1, 1]
    w = np.array([0.0, 0.0])
    lr = 0.1
    b = -0.7
    trainModel(X, y, w, b, lr)
    
