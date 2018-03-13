# -*- coding: utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# import tensorflow as tf

DATA_FOLDER = __file__.replace(os.path.basename(__file__), 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'birth_life_2010.txt')

def readBirthLifeData(filename):

    lines = open(filename, 'r').readlines()[1:]
    text = [line[:-1].split('\t') for line in lines]
    data = [(row[1], row[2]) for row in text]
    
if __name__ == "__main__":

    readBirthLifeData(DATA_FILE)