import tkinter as tk
from tkinter import filedialog, messagebox

def encryption():
    arr = []

    def submit_numbers():
        arr.append(int(public_number1.get()))
        arr.append(int(public_number2.get()))
        arr.append(int(secret_number.get()))

        public_key = (arr[0] ** arr[2]) % arr[1]
        messagebox.showinfo("Public Key", f"Your public key is ready!\nPublic Key: {public_key}\nPublic Number:{arr[0],arr[1]}\nShare them with recipient freely over any public channel.")

        tk.Label(root,text="Enter exchanged public key and browse file to be encrypted").pack()
        other_key_label.pack()
        other_public_key.pack()
        submit_other_key_button.pack(pady=10)
    
    def submit_other_key():
            other_key = int(other_public_key.get())
            file_location = filedialog.askopenfilename()
            text = open(file_location, "r")

            enc = open("Encrypt.txt", "w")
            for line in text:
                for i in line:
                    en = chr(ord(i) ^ ((other_key ** arr[2]) % arr[1]))
                    enc.write(en)
            messagebox.showinfo("Encryption", "Your file is generated")

    root = tk.Tk()
    height=430
    width=530
    x=(root.winfo_screenwidth()//2)-(width//2)
    y=(root.winfo_screenheight()//2)-(height//2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
    root.configure(background='#1F2041')
    root.title("Encryption written by chhavi_rohilla")

    public_number1 = tk.Entry(root,font=font_design_2)
    public_number2 = tk.Entry(root,font=font_design_2)
    secret_number = tk.Entry(root, show="*",font=font_design_2)
    
    tk.Label(root, text="Prefer odd/prime/multiple digits numbers").pack(pady=(40,10))
    
    tk.Label(root, text="Enter first public number:",fg='white',bg="#1F2041",font=font_design).pack()
    public_number1.pack()
    tk.Label(root, text="Enter second public number:",fg='white',bg="#1F2041",font=font_design).pack()
    public_number2.pack()
    tk.Label(root, text="SHH! Enter your private key:",fg='white',bg="#1F2041",font=font_design).pack()
    secret_number.pack()

    submit_numbers_button = tk.Button(root, text="Submit Numbers", command=submit_numbers,bg="#FFC857",font=font_design,border=2,cursor='hand2',highlightthickness=5,height=1,width=15)
    submit_numbers_button.pack(pady=10)
    
    other_key_label = tk.Label(root, text="Enter exchanged public key:",fg='white',bg="#1F2041",font=font_design)
    other_public_key = tk.Entry(root,font=font_design_2)
    submit_other_key_button = tk.Button(root, text="Submit Exchanged Key", command=submit_other_key,bg="#FFC857",font=font_design,border=2,cursor='hand2',highlightthickness=5,height=1,width=20)

    root.mainloop()

def decryption():
    arr = []

    def submit_numbers():
        arr.append(int(public_number1.get()))
        arr.append(int(public_number2.get()))
        arr.append(int(secret_number.get()))

        public_key = (arr[0] ** arr[2]) % arr[1]
        messagebox.showinfo("Public Key", f"Your public key is ready!\nPublic Key: {public_key}\nShare it with sender of encrypted file freely over any public channel.")

        tk.Label(root,text="Enter exchanged public key and browse file to be decrypted").pack()
        other_key_label.pack()
        other_public_key.pack()
        submit_other_key_button.pack(pady=10)
    
    def submit_other_key():
            other_key = int(other_public_key.get())
            file_location = filedialog.askopenfilename()
            text = open(file_location, "r")

            enc = open("Decrypt.txt", "w")
            for line in text:
                for i in line:
                    en = chr(ord(i) ^ ((other_key ** arr[2]) % arr[1]))
                    enc.write(en)
            messagebox.showinfo("Decryption", "Your file is generated")

    root = tk.Tk()
    height=430
    width=530
    x=(root.winfo_screenwidth()//2)-(width//2)
    y=(root.winfo_screenheight()//2)-(height//2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
    root.title("Decryption written by chhavi_rohilla")
    root.configure(background='#1F2041')

    public_number1 = tk.Entry(root,font=font_design_2)
    public_number2 = tk.Entry(root,font=font_design_2)
    secret_number = tk.Entry(root, show="*",font=font_design_2)

    tk.Label(root, text="Prefer odd/prime/multiple digit numbers").pack(pady=(40,10))

    tk.Label(root, text="Enter first public number:",fg='white',bg="#1F2041",font=font_design).pack()
    public_number1.pack()
    tk.Label(root, text="Enter second public number:",fg='white',bg="#1F2041",font=font_design).pack()
    public_number2.pack()
    tk.Label(root, text="SHH! Enter your private key:",fg='white',bg="#1F2041",font=font_design).pack()
    secret_number.pack()

    submit_numbers_button = tk.Button(root, text="Submit Numbers", command=submit_numbers,bg="#FFC857",font=font_design,border=2,cursor='hand2',highlightthickness=5,height=1,width=15)
    submit_numbers_button.pack(pady=10)

    other_key_label = tk.Label(root, text="Enter exchanged public key:",fg='white',bg="#1F2041",font=font_design)
    other_public_key = tk.Entry(root,font=font_design_2)
    submit_other_key_button = tk.Button(root, text="Submit Exchanged Key", command=submit_other_key,bg="#FFC857",font=font_design,border=2,cursor='hand2',highlightthickness=5,height=1,width=20)

    root.mainloop()

def main_menu():
    root = tk.Tk()
    height=430
    width=530
    x=(root.winfo_screenwidth()//2)-(width//2)
    y=(root.winfo_screenheight()//2)-(height//2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
    root.configure(background='#1F2041')
    root.title("Encryption/Decryption written by chhavi_rohilla")

    def open_encryption():
        root.destroy()
        encryption()

    def open_decryption():
        root.destroy()
        decryption()

    tk.Label(root, text="Choose an option:",fg='white',bg="#1F2041",font=font_design).pack(pady=(150,10))

    tk.Button(root, text="Encryption", command=open_encryption,bg="#FFC857",font=font_design,activebackground="#4B3F72",activeforeground='white',border=2,cursor='hand2',highlightthickness=5,height=1,width=10).pack()
    tk.Button(root, text="Decryption", command=open_decryption,bg="#FFC857",font=font_design,activebackground="#4B3F72",activeforeground='white',border=2,cursor='hand2',highlightthickness=5,height=1,width=10).pack(pady=10)

    root.mainloop()

font_design=('Arial',14)
font_design_2=('Arial',11)
main_menu()

