import matplotlib.path as mplPath
import PIL.Image
from PIL import ImageTk 

from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import sys
import json
from time import strftime

def log ():
    log = strftime("%D - %H:%M:%S | ")
    return str(log)

class DATABASEK:
    def __init__(self, master):
        self.settings_folder = os.path.join(os.getcwd(), "Settings") 
        if not os.path.exists(self.settings_folder): 
            print(log()+"settings folder not identified, creating settings' parameters...")
            self.previous_year_var = False
            self.int_val = 40
            self.px_val = 60
            print(log()+"settings folder not identified, settings' parameters created successfully.") 
            os.makedirs('Settings')
            print(log()+"settings folder created, initializing settings' parameters save...") 
            Settings = {
                    "int_val": 40, 
                    "previous_year": bool(self.previous_year_var),
                    "px_val": 60
                }
            print(log()+f"data created in int_val: " + str(self.int_val) +"\ndata created in previous_year_var: " + str(self.previous_year_var) + "\ndata created in self.px_val: " + str(self.px_val))
            with open(self.settings_folder + '/' + 'Settings.json', 'w') as outfile:
                json.dump(Settings, outfile)
                print(log()+'settings folder created and settings saving successful.')
        else:
            print(log()+'settings folder identified, settings loading')
            with open(self.settings_folder + '/' + 'Settings.json', 'r') as f:
                data = json.load(f)
            self.int_val = data['int_val']
            self.previous_year_var = data['previous_year']
            self.px_val = data['px_val'] 
        global text
        self.master = master
        master.title("WINDOW TITLE")
        self.master.tkraise()
        self.msre_record = os.path.join(os.getcwd(), "Measurements")
        if not os.path.exists(self.msre_record):
            os.makedirs(self.msre_record)
        w = 650
        h = 300
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        self.x = (ws / 2) - (w / 2)
        self.y = (hs / 2) - (h / 2)
        self.original_dimensions = master.geometry('%dx%d+%d+%d' % (w, h, self.x, self.y))
        self.x_dimension = self.master.winfo_width()
        self.y_dimension = self.master.winfo_height()
        self.master.wm_minsize(600, 300)
        w_style = ttk.Style()
        w_style.configure ('TFrame', background = 'black')
        f_style = ttk.Style()
        f_style.configure('TButton', font = ('calibri', 12), background = 'black', width = 14)
        f2_style = ttk.Style()
        f2_style.configure('TButton2', font = ('calibri', 12), background = 'black', width = 25)
        s_style = ttk.Style()
        s_style.configure('TScale', background = 'black', foreground = '#FFFFFF')
        c_style = ttk.Style()
        c_style.configure('Grey.TCheckbutton', sticky = 'W', background = 'black', foreground = '#FFFFFF', highlightcolor = 'blue') 
        # create notebook with tabs
        self.notebook = ttk.Notebook(master, width = master.winfo_screenwidth(), height = master.winfo_screenheight())
        self.notebook.grid(row=0, column=0, columnspan=4) 
        ####Create Measure frame
        self.Measure = Frame(self.notebook, background = 'black')
        self.Measure.grid(row=0, column=0)
        self.Measure.grid_propagate(False) 
        self.settings_folder = os.path.join(os.getcwd(), "Settings") 
        ######background universal image
        self.background = ImageTk.PhotoImage(PIL.Image.open('preto.png'))
        
        ######background measure set
        image_black_measure_label = Label(self.Measure, image = self.background, bg = 'black')
        image_black_measure_label.place(x = 0, y = 0) 
        ######Measure Frame black column
        black_image = ImageTk.PhotoImage(PIL.Image.open('preto.png'))
        black_canvas = Canvas(self.Measure, width = 150, height = 1200, background = 'black', highlightbackground = 'black')
        black_canvas.create_image (0,0, image = black_image, anchor = 'n')
        black_canvas.image = black_image
        black_canvas.place(x = 0, y = 0)
        black_canvas.grid_propagate (False) 
        ####Create Settings frame
        self.Settings = Frame(self.notebook, background = 'black')
        self.Settings.grid(row=0, column=1)
        self.Settings.grid_propagate(False) 
        ######background Settings set
        image_settings_label = Label(self.Settings, image = self.background, bg = 'black')
        image_settings_label.place(x = 0, y = 0)
        list_1 = Label(self.Settings, text = '1', bg = 'black', fg = 'white')
        list_1.grid (row = 0, column = 0, padx = 5)
        
        ######Settings Frame black column
        black_image = ImageTk.PhotoImage(PIL.Image.open('preto.png'))
        black_canvas = Canvas(self.Settings, width = 2500, height = 210, background = 'black', highlightbackground = 'black')
        black_canvas.create_image (0,0, image = black_image, anchor = 'n')
        black_canvas.image = black_image
        black_canvas.place(x = 0, y = 0)
        black_canvas.grid_propagate (False) 
        ####Create Credits frame
        self.Credits = Frame(self.notebook, background = 'black')
        self.Credits.grid(row=0, column=2)
        self.Credits.grid_propagate(False) 
        ######background Credits set
        image_settings_label = Label(self.Credits, image = self.background, bg = 'black')
        image_settings_label.place(x = 0, y = 0) 
        ######Credits Frame black column
        black_image = ImageTk.PhotoImage(PIL.Image.open('preto.png'))
        black_canvas = Canvas(self.Credits, width = 2500, height = 80, background = 'black', highlightbackground = 'black')
        black_canvas.create_image (0,0, image = black_image, anchor = 'n')
        black_canvas.image = black_image
        black_canvas.place(x = 0, y = 0)
        black_canvas.grid_propagate (False) 
        self.notebook.add(self.Measure, text="Measure")
        self.notebook.add(self.Settings, text="Settings")
        self.notebook.add(self.Credits, text = "Credits")

        global mLs 
        mLs = 0
        cLs = 0
        sLs = 0 
        self.image_label = Label(self.Measure, background = 'grey')
        self.image_label.place (x = 60, y = 15)
        #self.image_label.grid (row = 1, column = 1)
        self.image_label.grid_propagate(False) 
        self.btn_strt = ttk.Button(self.Measure, text = 'Start', command = lambda: (self.year_measure(), self.mtd_strt()), style = 'TButton')
        self.btn_strt.grid (row = mLs, column = 0, sticky = 'W', padx = 15, pady = 7)
        btn_exit = ttk.Button(self.Measure, text = 'Exit', command = sys.exit, style = 'TButton')
        btn_exit.grid (row = mLs + 7, column = 0, sticky = 'W', padx = 15, pady = 8) 
        #Settings Frame
        lenght_mssg = Label(self.Settings, text = "Threshold for minimum pixels segmment length in true edges detection:", fg = '#FFFFFF')
        lenght_mssg.configure (background = 'black')
        lenght_mssg.grid (row = sLs, padx = 15, pady = 15, sticky = 'W')
        
        px_mssg = Label(self.Settings, text = "Pixel line extent for true edges detected:", fg = '#FFFFFF')
        px_mssg.configure (background = 'black')
        px_mssg.grid (row = sLs + 3, padx = 15, pady = 15, sticky = 'W') 
        def sld_vle_update(val):
            self.int_val = int(float(val))
            self.sld_vle.configure(text=str(int(self.int_val)) + " pixels")
            
        self.sld_vle = Label(self.Settings, text = str(self.int_val), background = 'black', fg = '#FFFFFF')
        self.sld_vle.grid (row = sLs, column = sLs + 2, padx = 15, sticky = 'W')
        
        self.length = tk.DoubleVar()
        self.sld = ttk.Scale(self.Settings, from_ = 0, to = 100, variable = self.length, orient = 'horizontal', command = sld_vle_update)
        self.sld.set(str(self.int_val))
        self.sld.grid (row = sLs, column = sLs + 1, padx = 15, sticky = 'W') 
        #################################### 
        #self.px_val = 60
        def sld_px_update(val_px):
            self.px_val = int(float(val_px))
            self.sld_px.configure(text=str(int(self.px_val)) + " pixels")
            
        self.sld_px = Label(self.Settings, text = str(self.px_val), background = 'black', fg = '#FFFFFF')
        self.sld_px.grid (row = sLs + 3, column = sLs + 2, padx = 15, sticky = 'W')
        
        self.px_length = tk.DoubleVar()
        self.sld_px1 = ttk.Scale(self.Settings, from_ = 0, to = 100, variable = self.px_length, orient = 'horizontal', command = sld_px_update)
        self.sld_px1.set(str(self.px_val))
        self.sld_px1.grid (row = sLs + 3, column = sLs + 1 , padx = 15, sticky = 'W')
        self.sld_px1.grid_propagate (False) 
        #################################### 
        #End of the stuff in Settings Frame
        #Measure Frame
        
        self.inpt_box_flnm_text = Label(self.Measure, text = "Instrument ID", fg = 'White')
        self.inpt_box_flnm_text.grid (row = mLs + 3, column = 0, sticky = 'W', padx = 15)
        self.inpt_box_flnm_text.configure (bg = 'black') 
        self.inpt_box_flnm = ttk.Entry(self.Measure)
        self.inpt_box_flnm.grid (row = mLs + 4, column = 0, sticky = 'W', padx = 16)
        self.inpt_box_flnm.configure (background = 'black', width = 20)
        self.inpt_box_flnm.focus() 
        self.inpt_box_OS_text = Label(self.Measure, text = "Service Order Number", fg = 'White')
        self.inpt_box_OS_text.grid (row = mLs + 5, column = 0, sticky = 'W', padx = 15)
        self.inpt_box_OS_text.configure (background = 'black') 
        self.inpt_box_OS = ttk.Entry(self.Measure)
        self.inpt_box_OS.grid (row = mLs + 6, column = 0, sticky = 'W', padx = 15)
        self.inpt_box_OS.configure (background = 'black', width = 20)
        
        def chk_img_chkbtn():
            if self.img_mtd_chk.instate(['selected']):
                self.cam_mtd_chk.configure(state = 'disabled')
                self.btn_strt.configure (state = 'enabled')
            else:
                self.cam_mtd_chk.configure(state = 'enabled')
                btn_strt_routine() 
        self.img_mtd_chk_var = BooleanVar(value = False)
        self.img_mtd_chk = ttk.Checkbutton(self.Measure, text = "Image Method", variable = self.img_mtd_chk_var, style = 'Grey.TCheckbutton', command = chk_img_chkbtn)
        self.img_mtd_chk.grid (row = mLs + 1, column = mLs, padx = 25, sticky = 'W') 
        def chk_cam_chkbtn():
            if self.cam_mtd_chk.instate(['selected']):
                self.img_mtd_chk.configure (state = 'disabled')
                self.btn_strt.configure (state = 'enabled')
            else:
                self.img_mtd_chk.configure (state = 'enabled')
                btn_strt_routine() 
        self.cam_mtd_chk_var = BooleanVar(value = False)
        self.cam_mtd_chk = ttk.Checkbutton(self.Measure, text = "Camera Method", variable = self.cam_mtd_chk_var, style = 'Grey.TCheckbutton', command = chk_cam_chkbtn)
        self.cam_mtd_chk.grid (row = mLs + 2, column = mLs, padx = 25, sticky = 'W') 
        if not self.cam_mtd_chk.instate(['selected']) and not self.img_mtd_chk.instate(['selected']):
                self.btn_strt.configure (state = 'disabled') 
        def btn_strt_routine ():
            if not self.cam_mtd_chk.instate(['selected']) and not self.img_mtd_chk.instate(['selected']):
                self.btn_strt.configure (state = 'disabled') 
        self.canvas_test = tk.Canvas(self.Measure) 
        self.crd_mssg = Label(self.Credits, text = "DATABASEK, 28-09-2025", fg = 'White', bg = 'black')
        self.crd_mssg.grid (row = cLs, column = 0, padx = 15, pady = 15, sticky = 'W')
        self.crd_mssg.configure (bg = 'black')
        self.crd_mssg2 = Label(self.Credits, text = "CASTRO,2025", fg = 'White', bg = 'black')
        self.crd_mssg2.grid (row = cLs + 1, column = 0, sticky = 'W', padx = 15)
        self.crd_mssg2.configure (bg = 'black')
        
    def save_routine_Db(self):
        print(log()+'save routine initialized') 
        self.settings_folder = os.path.join(os.getcwd(), "Settings") 
        if os.path.exists(self.settings_folder): 
            print(log()+'settings folder identified, saving in progress...')
            Settings = {
                        "int_val": int(self.sld.get()), 
                        "previous_year": bool(self.previous_year_var),
                        "px_val": int(self.sld_px1.get())
                }
            with open(self.settings_folder + '/' + 'Settings.json', 'w') as outfile:
                json.dump(Settings, outfile)
                print(log()+'settings saving successful')
    
open_wdw = Tk()
software = DATABASEK(open_wdw)
open_wdw.mainloop()
