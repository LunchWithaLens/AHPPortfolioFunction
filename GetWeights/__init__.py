import azure.functions as func
import numpy as np
import json
import math
from numpy import linalg as LA
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    matrix = req_body.get('matrix')
    
    if matrix:
        
        x = matrix.split(',')
        x = [s.replace('1', '1.') for s in x]
        x = [s.replace('A', '3.') for s in x]
        x = [s.replace('B', '6.') for s in x]
        x = [s.replace('C', '9.') for s in x]
        x = [s.replace('a', str(1/3)) for s in x]
        x = [s.replace('b', str(1/6)) for s in x]
        x = [s.replace('c', str(1/9)) for s in x]
        
        a = (np.array(x, dtype='f'))
        dim = int(math.sqrt(a.size))
        a = a.reshape(dim,dim)
        eigenvalues, eigenvector=np.linalg.eig(a)
        maxindex=np.argmax(eigenvalues)
        weights=eigenvector[:, maxindex]
        weights=weights/(np.sum(weights))
        principalEigenValue = eigenvalues[np.argmax(eigenvalues)].real
        matrixWeights = weights.real
        saaty = (0.5247, 0.8816, 1.1086, 1.2479, 1.3417, 1.4057, 1.4499, 1.4854, 1.5140, 1.5365, 1.5551, 1.5713, 1.5838)
        ci = (principalEigenValue - dim)/(dim -1)
        cr = 1. - (ci/saaty[dim-3])
        response = '{"pev":  "' + str(principalEigenValue) + '", "weights" : "' + str(np.round_(matrixWeights,4)) + '", "cr" : "' + str(round(cr,4)) + '"}'
        return func.HttpResponse(response)
    else:
        return func.HttpResponse(
             "Please pass a reciprocal matrix in the request body",
             status_code=400
        )
