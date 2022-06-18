'''just an attempt for starters'''

from day_data import *
from year_data import *
from source_data import *
from outlier_finder import *
from functions import *
from tkinter import *
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
from numpy import size
from tkcalendar import *

class Application(Tk): 

    def func(self): 

        self.new_path = self.data.get()
        energy_per_year(self.new_path)

    def func1(self): 

        text = str(self.button.get_date())
        t = text.split("-")
        self.new_path = t[0] + t[1] + t[2]
        energy_per_day(self.new_path)

    def func2(self): 
        options = ["Solar", "Wind", "Geothermal", "Biomass", "Biogas", "Small hydro", "Coal", "Nuclear", "Natural gas", "Large hydro", "Batteries", "Imports", "Other"]
        source = self.data.get()
        index = options.index(source)
        self.new_path = index
        source_per_day(self.new_path)
        # text = str(self.button.get())
        # t = text.split("-")
        # self.new_path = t[0] + t[1] + t[2]
        # energy_per_day(self.new_path)
    def func3(self):
        
        data = [self.entry1.get(),self.entry2.get()]
        counter=0
        data_new=[]
        for i in range(len(data)):
            result=checkTime(data[i])
            if result==None:counter+=1
            else:
                data_new.append(int(result[0:2]))
        if counter>0:
            print("Wrong input")
        elif (len(data_new)==2 and data_new[0]>data_new[1]):
            print("End Time must be bigger than Start Time")
        else:
            self.new_path = data_new
            find_outliers(self.new_path)

    def func4(self):
        data = [self.e1.get(),self.e2.get()]
        print(data)
        res1 = checkDate(self.e1.get())
        res2 = checkTime(self.e2.get())
        if res1==None or res1=="WrongDate" or res2==None:
            print("Wrong Input")
        else:
            self.new_path = [res1,res2]
            print(self.new_path) 

    def makeOutlierButton(self):

        if(len(self.dataButtonCanvas.winfo_children())>0):
            for item in self.dataButtonCanvas.winfo_children():
                item.destroy()

        self.data.set("Pick the hours in between you want to find outliers (entries have to be type of xx:00)")
        # self.label = Label(self.dataButtonCanvas, text = "Get Outliers", background = 'pink', font = ('sans-serif', 20))
        # self.label.grid(row = 0)
        print("Get Outliers")
        self.Label1 = Label(self.dataButtonCanvas,text="Put Start Hour(xx:00)",background = 'pink').grid(row=1,column=1)
        self.entry1= Entry(self.dataButtonCanvas)
        self.entry1.grid(row=2,column=1)
        self.Label2 = Label(self.dataButtonCanvas,text="Put End Hour(xx:00)",background = 'pink').grid(row=1,column=2)
        self.entry2= Entry(self.dataButtonCanvas)
        self.entry2.grid(row=2,column=2)

        self.goButton = Button(self.dataButtonCanvas, text = "Go", font = 'sans-serif', command = self.func3)
        self.goButton.grid(row = 2, column = 3)

    def makePredictionButton(self):
        if(len(self.dataButtonCanvas.winfo_children())>0):
            for item in self.dataButtonCanvas.winfo_children():
                item.destroy()
        print("Prediction of energy sources")
        self.Label1 = Label(self.dataButtonCanvas,text="Prediction Date(xxxx-yy-zz)",background = 'pink').grid(row=1,column=1)
        self.e1= Entry(self.dataButtonCanvas)
        self.e1.grid(row=2,column=1)
        self.Label2 = Label(self.dataButtonCanvas,text="Prediction Time(xx:00)",background = 'pink').grid(row=1,column=2)
        self.e2= Entry(self.dataButtonCanvas)
        self.e2.grid(row=2,column=2)

        self.goButton = Button(self.dataButtonCanvas, text = "Go", font = 'sans-serif', command = self.func4)
        self.goButton.grid(row = 2, column = 3)
    
    def makeImportButton(self):
        if(len(self.dataButtonCanvas.winfo_children())>0):
            for item in self.dataButtonCanvas.winfo_children():
                item.destroy()
        print("Import Data File")

    def makeSourceButton(self): 

        if(len(self.dataButtonCanvas.winfo_children())>0):
            for item in self.dataButtonCanvas.winfo_children():
                item.destroy()

        # self.label = Label(self.dataButtonCanvas, text = "Get Graph by Source", background = 'pink', font = ('sans-serif', 20))
        # self.label.grid(row = 0)
        print("Get Graph by Source")
        self.data.set("Pick a source")

        options = ["Solar", "Wind", "Geothermal", "Biomass", "Biogas", "Small hydro", "Coal", "Nuclear", "Natural gas", "Large hydro", "Batteries", "Imports", "Other"]
        self.button = OptionMenu(self.dataButtonCanvas, self.data, *options)
        self.button.grid(row = 2, column = 0)

        self.goButton = Button(self.dataButtonCanvas, text = "Go", font = 'sans-serif', command = self.func2)
        self.goButton.grid(row = 2, column = 1)

    def makeYearButton(self): 

        if(len(self.dataButtonCanvas.winfo_children())>0):
            for item in self.dataButtonCanvas.winfo_children():
                item.destroy()

        # self.label = Label(self.dataButtonCanvas, text = "Get Graph by year", background = 'pink', font = ('sans-serif', 20))
        # self.label.grid(row = 0)
        print("Get Graph by year")
        self.data.set("Pick a year")

        options = ["2019", "2020", "2021"]
        self.button = OptionMenu(self.dataButtonCanvas, self.data, *options)
        self.button.grid(row = 2, column = 0)

        self.goButton = Button(self.dataButtonCanvas, text = "Go", font = 'sans-serif', command = self.func)
        self.goButton.grid(row = 2, column = 1)

    def makeDateButton(self): 

        if(len(self.dataButtonCanvas.winfo_children())>0):
            for item in self.dataButtonCanvas.winfo_children():
                item.destroy()

        print("Get Graph of energy by date")
        # self.label = Label(self.dataButtonCanvas, text = "Get Graph of energy by date", background = 'pink', font = ('sans-serif', 15))
        # self.label.grid(row = 0)
        
        self.data.set("Pick a date")

        self.button = DateEntry(self.dataButtonCanvas, width= 16, highlightbackground = 'pink', background= "magenta3", foreground= "white",bd=0)
        self.button.grid(row = 2, column = 0)

        self.goButton = Button(self.dataButtonCanvas, text = "Go", font = 'sans-serif', command = self.func1)
        self.goButton.grid(row = 2, column = 1)

    def makeButtons(self, xaxisCanvas): 

        self.clicked = BooleanVar()
        self.data = StringVar()
        self.new_path = ""
        self.button = Button()

        button1 = Button(xaxisCanvas, width = 10, text = 'By year', font = 'sans-serif', command = self.makeYearButton)
        button1.grid(row = 0, column = 0, sticky = 'w', padx = (0, 20))

        button2 = Button(xaxisCanvas, width = 10, text = "By day", font = 'sans-serif', command =  self.makeDateButton)
        button2.grid(row = 0, column = 1)

        button3 = Button(xaxisCanvas, width = 10, text = "By source", font = 'sans-serif', command = self.makeSourceButton)
        button3.grid(row = 0, column = 2, sticky = 'e', padx = (30, 0))
        
        label = Label(xaxisCanvas, text = "Modes", background = 'pink', font = ('sans-serif', 20))
        label.grid(row = 3, column = 1)

        button4 = Button(xaxisCanvas, width = 10, text = 'Outlier finder', font = 'sans-serif', command = self.makeOutlierButton)
        button4.grid(row = 4, column = 0, sticky = 'w', padx = (0, 30))

        button5 = Button(xaxisCanvas, width = 15, text = "Predictor of energy", font = 'sans-serif', command =  self.makePredictionButton)
        button5.grid(row = 4, column = 1)

        button6 = Button(xaxisCanvas, width = 10, text = "Import data", font = 'sans-serif', command = self.makeImportButton)
        button6.grid(row = 4, column = 2, sticky = 'e', padx = (30, 0))

        self.dataButtonCanvas = Canvas(self, height = 50, background = 'pink', highlightbackground = 'pink') 
        self.dataButtonCanvas.grid(row = 2, columnspan = 3, sticky = "n")
    
    def makeXAxisCanvas(self): 

        xaxisCanvas = Canvas(self, background = 'pink', highlightbackground = 'pink', height = 150)
        xaxisCanvas.grid(row = 1, column= 0, sticky = "n")
        xaxisCanvas.columnconfigure(0, weight = 1)
        xaxisCanvas.columnconfigure(1, weight = 1)
        xaxisCanvas.columnconfigure(2, weight = 1)
        self.makeButtons(xaxisCanvas)
    
    def makeXAxisCanvas1(self): 

        xaxisCanvas = Canvas(self, background = 'pink', highlightbackground = 'pink', height = 150)
        xaxisCanvas.grid(row = 4, column= 0, sticky = "n")
        xaxisCanvas.columnconfigure(0, weight = 1)
        xaxisCanvas.columnconfigure(1, weight = 1)
        xaxisCanvas.columnconfigure(2, weight = 1)
        self.makeButtons1(xaxisCanvas)
    
    def makeLabelCanvas(self): 

        labelCanvas = Canvas(self, height = 150, background = 'pink', highlightbackground = 'pink')
        labelCanvas.grid(row = 0, column= 0)

        label = Label(labelCanvas, text = "Pick type of graph", background = 'pink', font = ('sans-serif', 20))
        label.grid(row = 0, column = 0)
    
    def __init__(self):
        super().__init__()
        self.geometry("500x300+700+300")
        self.resizable(False, False)
        self.title("an attempt")
        self.configure(bg = 'pink')
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.makeLabelCanvas()
        self.makeXAxisCanvas()


app = Application()
app.mainloop()
