from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QHBoxLayout, QVBoxLayout,QComboBox,\
                             QLineEdit,QLabel,QToolButton,QMenu,QWidgetAction,QTextBrowser,QDialogButtonBox,\
                             QCheckBox,QFileDialog,QMainWindow,QDialog,QDateTimeEdit

from PyQt5.QtGui import QIntValidator,QDoubleValidator
from PyQt5.QtCore import Qt
from toto.inputs.cons import CONSfile as reader
import datetime

def xstr(s):
    if s == None:
        return ''
    return str(s)
def strx(s):
    if s == '':
        return None

    return int(s)



class ImportGUI(QDialog):
    def __init__(self,CONSfile,parent,options):
        super(ImportGUI, self).__init__(parent)
        
        self.options=options
        
        Vlayout = QVBoxLayout()
        Hlayout = QHBoxLayout()
        ## number of Headerlines
        Hlayout.addWidget(QLabel('# of line before the data'))
        self.skiprows=QLineEdit(xstr(self.options['skiprows']))
        self.skiprows.setValidator(QIntValidator())
        self.skiprows.setFixedWidth(30)
        Hlayout.addWidget(self.skiprows)
        Vlayout.addLayout(Hlayout)

        ## Header line
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(QLabel('Header line'))
        self.colNamesLine=QLineEdit(xstr(self.options['colNamesLine']))
        self.colNamesLine.setValidator(QIntValidator())
        self.colNamesLine.setFixedWidth(30)
        Hlayout.addWidget(self.colNamesLine)
        Vlayout.addLayout(Hlayout)



        ## Phase unnit
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(QLabel('Phase unit'))
        self.unitPhase = QComboBox()
        items=['degrees','radians']
        for item in items:
            self.unitPhase.addItem(item)
        self.unitPhase.setCurrentIndex(items.index('degrees'))
        Hlayout.addWidget(self.unitPhase)
        Vlayout.addLayout(Hlayout)



        ## skipfooter line
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(QLabel('Footer line'))
        self.skipfooter=QLineEdit(xstr(self.options['skipfooter']))
        self.skipfooter.setValidator(QIntValidator())
        self.skipfooter.setFixedWidth(30)
        Hlayout.addWidget(self.skipfooter)
        Vlayout.addLayout(Hlayout)


        ## Separator line
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(QLabel('Separator'))
        self.sep = QComboBox()
        items=[',',';','tab','\s+']
        for item in items:
            self.sep.addItem(item)
        self.sep.setCurrentIndex(items.index('tab'))
        Hlayout.addWidget(self.sep)
        Vlayout.addLayout(Hlayout)

        ## skipfooter line
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(QLabel('Missing values'))
        self.miss_val=QLineEdit(xstr(self.options['miss_val']))
        self.miss_val.setFixedWidth(100)
        Hlayout.addWidget(self.miss_val)
        Vlayout.addLayout(Hlayout)
               

        self.setLayout(Vlayout)

        self.center_window()
        self.setWindowTitle('Parse data')
    def exec(self):
        self.exec_()
        self.import_input()
        return self.options

    def center_window(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def import_input(self):
        text = str(self.sep.currentText())
        self.options['sep']=text.replace('tab','\t')
        text = str(self.unitPhase.currentText())
        self.options['unit']=text

        self.options['skiprows']=strx(self.skiprows.text())
        self.options['skipfooter']=strx(self.skipfooter.text())
        self.options['colNamesLine']=strx(self.colNamesLine.text())
        self.options['miss_val']=self.miss_val.text()
        self.close()

                        
        return self.options

class parse_cons_GUI(QDialog):
    def __init__(self,CONSfile,parent,options):
        super(parse_cons_GUI, self).__init__(parent)
        
        self.options=options

        colNames=['None']
        colNames+=CONSfile.colNames
        

        mainVL = QVBoxLayout()


        ## Latitude line
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(QLabel('latitude'))
        self.latitude=QLineEdit(xstr(self.options['latitude']))
        self.latitude.setValidator(QDoubleValidator())
        #self.latitude.setFixedWidth(300)
        Hlayout.addWidget(self.latitude)
        mainVL.addLayout(Hlayout)

        ## Latitude line
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(QLabel('Start time'))
        self.min_date=QDateTimeEdit(self.options['min_date'])
        self.min_date.setDisplayFormat("dd/MM/yyyy hh:mm:ss")
        #self.min_date.setFixedWidth(300)
        Hlayout.addWidget(self.min_date)
        mainVL.addLayout(Hlayout)

        ## Latitude line
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(QLabel('End time'))
        self.max_date=QDateTimeEdit(self.options['max_date'])
        self.max_date.setDisplayFormat("dd/MM/yyyy hh:mm:ss")
        #self.max_date.setFixedWidth(30)
        Hlayout.addWidget(self.max_date)
        mainVL.addLayout(Hlayout)

        ## dt
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(QLabel('dt(s)'))
        self.dt=QLineEdit(xstr(self.options['dt']))
        self.dt.setValidator(QIntValidator())
        #self.latitude.setFixedWidth(30)
        Hlayout.addWidget(self.dt)
        mainVL.addLayout(Hlayout)

        ### Multiple column
        labels=['Cons','Amplitude','Phase']
        self.cons_column=[]
        for label in labels:
            Hlayout = QHBoxLayout()
            Hlayout.addWidget(QLabel('%s:' % label))
            qc=QComboBox()
            for colName in colNames:
                qc.addItem(colName)

            idx=[col for col in colNames if col.lower() in label.lower()]
            if idx:
                idx=colNames.index(idx[0])
                qc.setCurrentIndex(idx)
            self.cons_column .append( qc)
            Hlayout.addWidget(qc)
            mainVL.addLayout(Hlayout)

        
       
        self.setLayout(mainVL)
        self.setFixedSize(400, 400)
        self.center_window()
        
        

        self.setWindowTitle('Parse column')
        self.show()
    def exec(self):
        self.exec_()
        self.import_input()
        return self.options
    
    def import_input(self):
        names=['Cons','Amplitude','Phase']
        self.options['col_name']={}
        for i in range(0,len(self.cons_column)):
            if self.cons_column[i].currentText() !="None":
                self.options['col_name'][self.cons_column[i].currentText()]=names[i]

        self.options['latitude']=float(self.latitude.text())
        self.options['dt']=int(self.dt.text())
        self.options['min_date']=self.min_date.text()
        self.options['max_date']=self.max_date.text()

    def center_window(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


class CONSfile():
    def __init__(self,parent,filename):
        
        self.fileparam=lambda:None

        self.parent   =parent
        self.filename     = filename

        options={}

        options['sep']          = '\t'
        options['colNames']     = []
        options['miss_val']    = 'NaN'


        options['colNamesLine'] = 1
        options['skiprows']     = 1
        options['skipfooter'] = 0

        options['unit']='degrees'
        options['col_name']={}

        options['latitude']=-40
        options['min_date']=datetime.datetime(2020,1,1)
        options['max_date']=datetime.datetime(2020,1,9)
        options['dt']=3600

        self.encoding    = None


        # set usr defined parameter
        opt=ImportGUI(filename[0],self.parent,options)
        options=opt.exec()
        Re=reader(filename,**options) 
        Re.reads()   
        # # Parse the date
        opt=parse_cons_GUI(Re.fileparam,self.parent,options)
        options=opt.exec()

        Re.fileparam.col_name=options['col_name']
        Re.cons.latitude=options['latitude']
        Re.cons.min_date=options['min_date']
        Re.cons.max_date=options['max_date']
        Re.cons.dt=options['dt']

        Re.read_cons()
        self.Re=Re

    def _toDataFrame(self):
        return self.Re._toDataFrame()