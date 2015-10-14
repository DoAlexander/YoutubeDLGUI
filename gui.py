import sys
import os
import json
import urllib.request
from PyQt4 import QtCore, QtGui
from form import Ui_Dialog
from bs4 import BeautifulSoup
import pprint

 
class MyDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.dl)
		self.ui.lineEdit.textChanged.connect(self.labeler)
		
	def labeler(self):
		s = ""
		with urllib.request.urlopen(self.ui.lineEdit.text()) as url:
			s += str(url.read())
		soup = BeautifulSoup(s, 'html.parser')
		#print(soup.prettify())
		souper = soup.findAll(name='img')
		if 'data-thumb' in souper[1].string:
			print("True")
		#print(souper)
		#self.ui.label.setText(soup.title.string)
		#self.ui.label.repaint()
	
	def dl(self):
		print(self.ui.lineEdit.text())
		if self.ui.checkBox.isChecked():
			os.system('youtube-dl.exe -x --audio-format mp3 '+ self.ui.lineEdit.text())
		else:
			os.system('youtube-dl.exe -e --get-description '+ self.ui.lineEdit.text())
			#os.system('youtube-dl.exe -f mp4 '+ self.ui.lineEdit.text())
 
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyDialog()
	myapp.show()
	sys.exit(app.exec_())