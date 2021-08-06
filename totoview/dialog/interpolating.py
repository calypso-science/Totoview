from ..core.basewindow import BaseWindow
import toto
import matplotlib.pyplot as plt


class InterpWindow(BaseWindow):
    def __init__(self,X, parent=None):
        super(InterpWindow, self).__init__(folder=toto.interpolations,title='Interpolating toolbox',parent=parent)
        self.X0=X[0].copy()
        self.Xs=X.copy()
        self.X=X
        self.refresh_plot()

    # def refresh_plot(self):
    #     with plt.style.context("cyberpunk"):
    #         self.figure.clf()
    #         ax = self.figure.add_subplot(111)

    #         ax.plot(self.X0[self.X[0].keys()[0]],label='original')
    #         ax.plot(self.X[0][self.X[0].keys()[0]],label='interpolated')
    #         plt.grid()
    #         self.figure.autofmt_xdate()
    #         ax.legend()
    #         self.canvas.draw()


    def filter(self):
        idx=self.method_names.currentItem()
        fct_name=idx.text()
        run_ft=self._import_from('toto.interpolations.%s' % fct_name,fct_name)
        opt=self.get_options(self.opt[self.method_names.currentRow()]) # get all option as dict
        #Only play with first file and first variable
        tmp=run_ft(self.X[0][self.X[0].keys()[0]],opt)
        old_index=self.X[0][self.X[0].keys()[0]].index
        if (len(tmp.index) != len(old_index)) or\
               (tmp.index[0]!=old_index[0]):
            self.X[0]=tmp.to_frame()
        else:
            self.X[0][self.X[0].keys()[0]]=tmp
        
        self.refresh_plot()

    def save(self):
        idx=self.method_names.currentItem()
        fct_name=idx.text()
        run_ft=self._import_from('toto.interpolations.%s' % fct_name,fct_name)
        opt=self.get_options(self.opt[self.method_names.currentRow()]) # get all option as dict
        for i in range(0,len(self.Xs)):
            for j,var in enumerate(self.Xs[i].keys()):
                old_index=self.X[i].index

                tmp=run_ft(self.Xs[i][var],opt)
                if (len(tmp.index) != len(old_index)) or\
                       (tmp.index[0]!=old_index[0]):

                    self.X[i]=tmp.to_frame()
                else:
                    self.X[i][var]=tmp


        self.close()
    def reset(self):
        
        self.X[0]=self.X0.copy()
        self.refresh_plot()

    def cancel(self):
        self.X[0]=self.X0
        self.close()
        return None
    
    def exec(self):
        self.exec_()
        return self.X


if __name__ == '__main__':
    app = QApplication(sys.argv)
    import numpy as np
    import pandas as pd
    dates = pd.date_range('1/1/2000', periods=8)
    df = pd.DataFrame(np.random.randn(8, 4),index=dates, columns=['A', 'B', 'C', 'D'])

    main = FiltWindow([df])
    main.setWindowTitle('Filtering toolbox')
    main.show()

    sys.exit(app.exec_())