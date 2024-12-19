#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:26:01 2024

@author: the-brainputer
"""
import random as r
import numpy as np

pathRight = "TestData/Actions/RIGHT/"
pathLeft = "TestData/Actions/LEFT/"


"""-----------------------Read-Data--------------------------------"""

def readData(classToRead: str, testSamples: float):
    """
    Read the Data from one or multiple classes (seperated by comma) and returns to you a sorted (unshuffled) trainingSet and testSet in the ratio you specified.

    Parameters
    ----------
    classToRead : str
        Specify the classes you want to read. Seperate multiple classes by comma.
    testSamples : float
        percantage of test samples you want in range 0 to 1.0

    Returns
    -------
    trainingSet : list
        List of arrays for training pruposes
    testSet : list
        List of arrays for testing purposes

    """
    trainingSet = []
    trainingSetLabel = []
    testSet = []
    testSetLabel = []
    
    #To have the classes seperated
    classToRead = classToRead.replace(" ", "")
    classToRead = classToRead.lower()
    classToRead = classToRead.split(",")
    
    for el in classToRead:
        match el:
            case "right":
                t_trainingSet, t_testSet, t_trainingSetLabel, t_testSetLabel = _readClass(pathRight, testSamples, "right")
                
                trainingSet += t_trainingSet
                testSet += t_testSet
                
                trainingSetLabel += t_trainingSetLabel
                testSetLabel += t_testSetLabel
                
            case "left":
                t_trainingSet, t_testSet, t_trainingSetLabel, t_testSetLabel  = _readClass(pathLeft, testSamples, "left")
                
                trainingSet += t_trainingSet
                testSet += t_testSet
                
                trainingSetLabel += t_trainingSetLabel
                testSetLabel += t_testSetLabel
                
            case _:
                print("Error: Class name not found")
    
    return trainingSet, testSet, trainingSetLabel, testSetLabel
            
def _readClass(path: str, testSamples: float, label: str):
    trainingSet = []
    testSet = []
    trainingSetLabel = []
    testSetLabel = []
    
    file = open(path + 'save.txt', 'r')
    count = int(file.read())
    
    for i in range(count):
        data = np.load(path + "data{}.npy".format(i))
        
        if(r.random() < testSamples):
            testSet.append(data)
            testSetLabel.append(label)
        else:
            trainingSet.append(data)
            trainingSetLabel.append(label)
    return trainingSet, testSet, trainingSetLabel, testSetLabel


"""----------------------Modify-Data-------------------------------"""

def splitComplex(complexArrayToSplit: np.array):
    arrayReal = complexArrayToSplit.real
    arrayImag = complexArrayToSplit.imag
    
    arrayComplex = np.empty((complexArrayToSplit.shape[0], complexArrayToSplit.shape[1], 2))
    arrayComplex[ : , : , 0] = arrayReal
    arrayComplex[ : , : , 1] = arrayImag
    return arrayComplex