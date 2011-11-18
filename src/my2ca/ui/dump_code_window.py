from PySide.QtGui import QDialog, QTextArea

class CodeDumpView(QDialog):
	
	self.code = None
	
	def __init__(self, parent = None):
		QDialog.__init__(self, parent)
		self.textarea = QTextArea()
		self.setCenterWIdget(self.textarea)
		pass
	
	def run(self):
		if code:
			self.textarea.text = code
			self.exec_()
			pass
		pass
	pass

def create_dump_dialog(parent, code):
	dlg = new CodeDumpView(parent)
	dlg.code = code
	dlg.run()
	pass
