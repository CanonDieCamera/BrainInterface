#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:06:42 2024

@author: canan gallitschke
"""
#Imports
import tensorflow as tf
from tensorflow.keras import layers, models
import DataReader as dr

#Konstanten
num_classes = 2;    #anzahl der Klassen



#__________________________________________________________________
#
#                   Einlesen der Daten
#__________________________________________________________________

dataSet, dataSetLabel = dr.readData("right, left")
print("Data size: " + str(len(dataSet)) + " " + str(len(dataSetLabel)))


#__________________________________________________________________
#
#                   Anpassen der komplexen Daten
#__________________________________________________________________

dataSetComplex = []

for i in range(len(dataSet)):
    dataSetComplex.append(dr.splitComplex(dataSet[i]))
    
print("Data Size after splitting: " + str(len(dataSet)) + " " + str(len(dataSetLabel)))

                                                    
#__________________________________________________________________
#
#                   Shuffeln der Daten
#__________________________________________________________________


#__________________________________________________________________
#
#                   Splitten in Trainings und Tesdaten
#__________________________________________________________________




#__________________________________________________________________
#
#                   Definieren des Models
#__________________________________________________________________

"""     Option 1: CNN (als 2D-Daten)"""
model1 = models.Sequential([
    layers.Input(shape=(16,129, 2)),   #2D-Daten mit Channel Dimension (z.B. für graustufenbilder, auch wenn es sich hierbei nicht um bilder handelt)
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation = 'relu'),
    layers.Flatten(),
    layers.Dense(128, activation = 'relu'),
    layers.Dense(num_classes, activation='softmax')
    ])

model1.compile(optimizer='adam', loss='categorial_crossentropy', metrics=['accuracy'])
model1.summary()


"""     Option 2: CNN + LSTM """
# Analyse von Sequenzmustern innerhalb der Frequenzen
model2 = models.Sequential([
    #CNN Part: extraction of local pattern inside the frequence
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(16, 129, 2)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Reshape((16, -1)), #Transform to (Channels, Features)
    
    #LSTM-Teil: Have a look at the patterns accross the Channels
    layers.LSTM(64, return_sequences=False),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
    ])

model2.compile(optimizer='adam', loss='categorial_crossentropy', metrics=['accuracy'])
model2.summary()

"""     Option 3: Nur LSTM/Transformer (als Sequenzdaten) """
# Verwendung von Frequenzen als Sequenz pro Channel
model3 = models.Sequential([
    #LSTM-layer for every channel
    layers.TimeDistributed(layers.LSTM(64, return_sequences=True), input_shape=(16, 129, 2)),
    layers.TimeDistributed(layers.LSTM(32, return_sequences=False)),
    
    #Dense-Layer for Classification
    layers.LSTM(64, return_sequences=False),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax') 
    ])    
    

model3.compile(optimizer='adam', loss='categorial_crossentropy', metrics=['accuracy'])
model3.summary()


#__________________________________________________________________
#
#                   Trainieren der Daten
#__________________________________________________________________

#__________________________________________________________________
#
#                   Ausgabe der Trainingsdaten
#__________________________________________________________________

#__________________________________________________________________
#
#                   Testen der Daten
#__________________________________________________________________

#__________________________________________________________________
#
#                   Ausgabe der Testdaten
#__________________________________________________________________


#__________________________________________________________________
#
#                   Funktionen
#__________________________________________________________________




















