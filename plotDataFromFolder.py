import os
import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------

colorList = ["b", "g", "r", "c", "m", "y", "k", "w"]

fileDelimiter = '\t'
legendList = []

#-------------------------------------------------------------------------------------------------

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/Data"
folderList = os.listdir(dir_path)

#----------------------------------------------

def plotPlot():
	plt.legend()#loc='upper left')
	plt.xlabel(r'$\phi [\circ]$')
	plt.ylabel('Cp [-]')
	plt.savefig('MyPlot.pdf')
	plt.show()  

def arrangeData(filename, c, l):
	degree_p = filename[:,0]
	degree_s = filename[:,1]

	cp_p = filename[:,2]
	cp_s = filename[:,3]

	tau_p = filename[:,4]
	tau_s = filename[:,5]

	yPlus_p = filename[:,6]
	yPlus_s = filename[:,7]

	plt.plot(degree_p,(cp_p+cp_s[::-1])/2, color = c, label = l)
	plt.plot(degree_s[::-1],(cp_s[::-1]+cp_p)/2, color = c)
	

#----------------------------------------------

def iterateFolderList():
	for i in range(len(folderList)):
		legendList.append(folderList[i])
		arrangeData(np.loadtxt(dir_path + '/' + folderList[i], delimiter = fileDelimiter), colorList[i], folderList[i])

#-------------------------------------------------------------------------------------------------

iterateFolderList()
plotPlot()




















































