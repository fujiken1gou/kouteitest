from flask import Flask
import openpyxl as px
import tkinter
import tkinter.filedialog

app = Flask(__name__)

@app.route('/')
def kouteitesut():

    root = tkinter.Tk()
    root.withdraw()

    #file = tkfd.askopenfilename(
        #title = "ファイルを選びましょう。",
        #filetypes =[("TEXT", ".xlsx")] #開けるファイルの種類。
    #)

    idir = 'C:\\python_test'
    file_path = tkinter.filedialog.askopenfilename(initialdir = idir)

    wbw = px.load_workbook(file_path,data_only=True)
    wsw = wbw['test']

    for row in wsw.values:
        cellstr = ""
        for value in row:
            if value is None:
                value = "None"
            cellstr += " %s " % value
        print(cellstr)

if __name__ == '__main__'
    app.run()
