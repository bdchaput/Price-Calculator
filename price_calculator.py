import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

class CalcGUI:

    def __init__(self):

        ctk.set_appearance_mode('Dark')
        ctk.set_default_color_theme('green')

        self.root = ctk.CTk()

        self.root.title("Actual Price Calculator")

        # container for the final value
        self.value = tk.StringVar()
        self.value.set('0.00')

        # title
        self.header = ctk.CTkLabel(self.root, text='Actual Price Calculator', font=ctk.CTkFont(size=28))
        self.header.pack(padx=10, pady=20)

        # description
        self.description = ctk.CTkLabel(self.root, text='Type the price of your item into the textbox then select which provice you are shopping in. Next, select how much you would like to add as a tip. When you press submit you will recieve the price of the item with tax and tip added.', font=ctk.CTkFont(size=16), width=50, wraplength=550)
        self.description.pack(padx=10, pady=10)

        # box to input price
        self.price = tk.StringVar()

        self.price_frame = ctk.CTkFrame(self.root, corner_radius=5)
        self.price_frame.columnconfigure(0, weight=1)
        self.price_frame.columnconfigure(1, weight=1)

        
        self.dollar = ctk.CTkLabel(self.price_frame, text='$', font=ctk.CTkFont(size=16))
        self.dollar.grid(row=0,column=0, padx=5, pady=5)
        self.price_input = ctk.CTkEntry(self.price_frame, textvariable=self.price)
        self.price_input.grid(row=0,column=1
, padx=5, pady=5)

        self.price_frame.pack(padx=5, pady=5)

        # Frame for province options
        self.prov_frame = ctk.CTkFrame(self.root, corner_radius=10, border_width=2)
        self.prov_frame.columnconfigure(0, weight=1)
        self.prov_frame.columnconfigure(1, weight=1)
        self.prov_frame.columnconfigure(2, weight=1)
        self.prov_frame.columnconfigure(3, weight=1)

        # province options
        self.prov = tk.IntVar()

        self.alb = ctk.CTkRadioButton(self.prov_frame, text='Alberta', font=ctk.CTkFont(size=12), variable=self.prov, value=1)
        self.alb.grid(row=0,column=0, sticky=tk.W+tk.E, padx=(20, 10), pady=(20, 10))

        self.bc = ctk.CTkRadioButton(self.prov_frame, text='British Columbia', font=ctk.CTkFont(size=12), variable=self.prov, value=2)
        self.bc.grid(row=0,column=1, sticky=tk.W+tk.E, padx=10, pady=(20, 10))

        self.man = ctk.CTkRadioButton(self.prov_frame, text='Manitoba', font=ctk.CTkFont(size=12), variable=self.prov, value=3)
        self.man.grid(row=0,column=2, sticky=tk.W+tk.E, padx=10, pady=(20, 10))

        self.nb = ctk.CTkRadioButton(self.prov_frame, text='New Brunswick', font=ctk.CTkFont(size=12), variable=self.prov, value=4)
        self.nb.grid(row=0,column=3, sticky=tk.W+tk.E, padx=(10, 20), pady=(20, 10))

        self.newf = ctk.CTkRadioButton(self.prov_frame, text='Newfoundland', font=ctk.CTkFont(size=12), variable=self.prov, value=5)
        self.newf.grid(row=1,column=0, sticky=tk.W+tk.E, padx=(20, 10), pady=10)

        self.nwt = ctk.CTkRadioButton(self.prov_frame, text='North West Territories', font=ctk.CTkFont(size=12), variable=self.prov, value=6)
        self.nwt.grid(row=1,column=1, sticky=tk.W+tk.E, padx=10, pady=10)

        self.Nova = ctk.CTkRadioButton(self.prov_frame, text='Nova Scotia', font=ctk.CTkFont(size=12), variable=self.prov, value=7)
        self.Nova.grid(row=1,column=2, sticky=tk.W+tk.E, padx=10, pady=10)

        self.nun = ctk.CTkRadioButton(self.prov_frame, text='Nunavut', font=ctk.CTkFont(size=12), variable=self.prov, value=8)
        self.nun.grid(row=1,column=3, sticky=tk.W+tk.E, padx=(10, 20), pady=10)

        self.ont = ctk.CTkRadioButton(self.prov_frame, text='Ontario', font=ctk.CTkFont(size=12), variable=self.prov, value=9)
        self.ont.grid(row=2,column=0, sticky=tk.W+tk.E, padx=(20, 10), pady=10)

        self.pei = ctk.CTkRadioButton(self.prov_frame, text='PEI', font=ctk.CTkFont(size=12), variable=self.prov, value=10)
        self.pei.grid(row=2,column=1, sticky=tk.W+tk.E, padx=10, pady=10)

        self.que = ctk.CTkRadioButton(self.prov_frame, text='Quebec', font=ctk.CTkFont(size=12), variable=self.prov, value=11)
        self.que.grid(row=2,column=2, sticky=tk.W+tk.E, padx=10, pady=10)

        self.sask = ctk.CTkRadioButton(self.prov_frame, text='Saskatchewan', font=ctk.CTkFont(size=12), variable=self.prov, value=12)
        self.sask.grid(row=2,column=3, sticky=tk.W+tk.E, padx=(10, 20), pady=10)

        self.yuk = ctk.CTkRadioButton(self.prov_frame, text='Yukon', font=ctk.CTkFont(size=12), variable=self.prov, value=13)
        self.yuk.grid(row=3,column=0, sticky=tk.W+tk.E, padx=(20, 10), pady=(10, 20))

        self.prov_frame.pack(padx=10, pady=10)

        # asks if you want to include a tip
        self.tip_prompt = ctk.CTkLabel(self.root, text="How much would you like to tip?", font=ctk.CTkFont(size=12))
        self.tip_prompt.pack(padx=10, pady=10)

        # frame for the tip buttons
        self.tip_frame = ctk.CTkFrame(self.root, corner_radius=10, border_width=2)
        self.tip_frame.columnconfigure(0, weight=1)
        self.tip_frame.columnconfigure(1, weight=1)
        self.tip_frame.columnconfigure(2, weight=1)
        self.tip_frame.columnconfigure(3, weight=1)

        # tip amounts
        self.tip = tk.IntVar()

        self.t_no_tip = ctk.CTkRadioButton(self.tip_frame, text='No Tip', font=ctk.CTkFont(size=12), variable=self.tip, value=1)
        self.t_no_tip.grid(row=0,column=0, padx=(60, 0), pady=10)

        self.t_ten = ctk.CTkRadioButton(self.tip_frame, text='10%', font=ctk.CTkFont(size=12), variable=self.tip, value=2)
        self.t_ten.grid(row=0,column=1, pady=10)

        self.t_fifteen = ctk.CTkRadioButton(self.tip_frame, text='15%', font=ctk.CTkFont(size=12), variable=self.tip, value=3)
        self.t_fifteen.grid(row=0,column=2, pady=10)

        self.t_twenty = ctk.CTkRadioButton(self.tip_frame, text='20%', font=ctk.CTkFont(size=12), variable=self.tip, value=4)
        self.t_twenty.grid(row=0,column=3, padx=(0, 10), pady=10)

        self.tip_frame.pack()

        # displays value
        self.display_text = ctk.CTkLabel(self.root, text="Your Price:", font=ctk.CTkFont(size=12))
        self.display_text.pack(padx=5, pady=5)

        self.display_text = ctk.CTkLabel(self.root, textvariable=self.value, font=ctk.CTkFont(size=20))
        self.display_text.pack(padx=5, pady=5)

        # submit
        self.submit_btn = ctk.CTkButton(self.root, text="Get Price", font=ctk.CTkFont(size=12), command=self.get_price)
        self.submit_btn.pack(padx=5, pady=5)
        
        # asks if you want to close window
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    # function to calculate final price
    def get_price(self):
        tax_amount = self.get_tax_amount()
        tip_amount = self.get_tip_amount()
        price_amount = self.price.get()

        try:
            price_float = float(price_amount)
        except:
            print("error")
            self.no_num()

        if tax_amount == 'no tax selected' or tip_amount == 'no tip selected':
            print("error")
            self.no_select()
        else:
            final_value = price_float + (price_float * tax_amount) + (price_float * tax_amount)
            formated_value = '{:.2f}'.format(final_value)
            self.value.set('$' + str(formated_value))

    # function to determine what tax amount to apply based on selected province
    def get_tax_amount(self):
        match self.prov.get():
            case 1: # Alberta
                return 0.05
            case 2: # BC
                return 0.12
            case 3: # Manitoba
                return 0.12
            case 4: # New Brunswick
                return 0.15
            case 5: # Newfoundland
                return 0.15
            case 6: # North West Territories
                return 0.05
            case 7: # Nova Scotia
                return 0.15
            case 8: # Nunavut
                return 0.05
            case 9: # Ontario
                return 0.13
            case 10: # PEI
                return 0.15
            case 11: # Quebec
                return 0.15
            case 12: # Saskatchewan
                return 0.11
            case 13: # Yukon
                return 0.05
            case other:
                return 'no tax selected'

    # function to determine which tip amount to apply
    def get_tip_amount(self):
        match self.tip.get():
            case 1: # no tip
                return 0
            case 2: # 10%
                return 0.10
            case 3: # 15%
                return 0.15
            case 4: # 20%
                return 0.20
            case other:
                return 'no tip selected'

    # errors that appear when the user fails to provide input

    def no_num(self):
        tk.messagebox.showerror('Error', 'Please enter a number.')

    def no_select(self):
        tk.messagebox.showerror('Error', 'Please select a province and a tip amount.')

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

CalcGUI()