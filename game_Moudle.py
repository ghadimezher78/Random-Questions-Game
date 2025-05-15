import tkinter as tk

def Question1(root):
    # The Failed Function
    def failed():
        Failed = tk.Label(root, text="You Haved Guessed The Wrong Answer!", font=("Arial", 10))
        Failed.pack()
    # The Question Label
    QuestionLabel = tk.Label(root, text="When Was Lebron James Born?", font=("Arial", 10))
    QuestionLabel.pack(padx=10, pady=10)
    # The Button Questions
    ButtonQuestion1_1 = tk.Button(root, text="February 20, 1991", font=("Arial", 10), command=failed)
    ButtonQuestion1_1.pack()
    ButtonQuestion1_2 = tk.Button(root, text="Jaunuary 23, 2002", font=("Arial", 10), command=failed)
    ButtonQuestion1_2.pack()
    ButtonQuestion1_3 = tk.Button(root, text="February 17, 1963", font=("Arial", 10), command=lambda: Question2(root))
    ButtonQuestion1_3.pack()

def Question2(root):
    # The Failed Function
    def failed():
        Failed = tk.Label(root, text="You Haved Guessed The Wrong Answer!", font=("Arial", 10))
        Failed.pack()
    # The Question Label    
    QuestionLabel = tk.Label(root, text="When was Python Made", font=("Arial", 10))
    QuestionLabel.pack(padx=10, pady=10)
    # The Button Questions
    ButtonQuestion2_1 = tk.Button(root, text="1991", font=("Arial", 10), command=lambda: Question3(root))
    ButtonQuestion2_1.pack()
    ButtonQuestion2_2 = tk.Button(root, text="2000", font=("Arial", 10), command=failed)
    ButtonQuestion2_2.pack()
    ButtonQuestion2_3 = tk.Button(root, text="1959", font=("Arial", 10), command=failed)
    ButtonQuestion2_3.pack()

def Question3(root):
    # The Failed Function
    def failed():
        Failed = tk.Label(root, text="You Haved Guessed The Wrong Answer!", font=("Arial", 10))
        Failed.pack()
    # The Question Label    
    QuestionLabel = tk.Label(root, text="What Is The First ChromeBook?", font=("Arial", 10))   
    QuestionLabel.pack(padx=10, pady=10) 
    # The Button Questions
    ButtonQuestion3_1 = tk.Button(root, text="Cr-48", font=("Arial", 10), command=lambda: Question4(root))
    ButtonQuestion3_1.pack()
    ButtonQuestion3_2 = tk.Button(root, text="Pixel", font=("Arial", 10), command=failed)
    ButtonQuestion3_2.pack()
    ButtonQuestion3_3 = tk.Button(root, text="Pixelbook Go", font=("Arial", 10), command=failed)
    ButtonQuestion3_3.pack()

def Question4(root):
    #The Failed Function
    def failed():
        Failed = tk.Label(root, text="You Haved Guessed The Wrong Answer!", font=("Arial", 10))
        Failed.pack()
    # The Question Label
    QuestionLabel = tk.Label(root, text="What Is 12 x 12 Equal To?", font=("Arial", 10))   
    QuestionLabel.pack(padx=10, pady=10)    
    # The Button Questions
    ButtonQuestion4_1 = tk.Button(root, text="144", font=("Arial", 10), command=lambda: win(root))
    ButtonQuestion4_1.pack()
    ButtonQuestion4_2 = tk.Button(root, text="69", font=("Arial", 10), command=failed)
    ButtonQuestion4_2.pack()
    ButtonQuestion4_3 = tk.Button(root, text="1000", font=("Arial", 10), command=failed)
    ButtonQuestion4_3.pack()

def win(root):
    for widget in root.winfo_children():
        widget.destroy() 
    WinLabel = tk.Label(root, text="You Won!", font=("Arial", 20))
    WinLabel.pack(padx=20, pady=20)