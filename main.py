#This code clears up a dataset which contains information about
#bicicle service in mexico city
import os
import pandas as pd

#####         Loading DataSet      ####

'''Loading_DS() access returns '''
def Loading_DS(path):

    path = "/Volumes/Sebastian/Diplomado/DataSets/ecobici/"
    files_namesArray = os.listdir(path)
    files_list = [files_namesArray for files_namesArray in files_namesArray if files_namesArray[:2] == '20']

