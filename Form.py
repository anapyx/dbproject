from pathlib import Path

from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import Canvas

import re

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\lovea\Documents\python\dbproject\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_Login():
    win.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    Login_path = os.path.join(parent_directory,'assets', 'Login.py')

    subprocess.call(["python", Login_path, 'Login'])

def submeterCadastro():
    user = entrada_nome.get()
    phone = entrada_tel.get()
    email = entrada_email.get()
    senha = entrada_senha.get()
    desconto = temDesconto()
 
    # Chamar funcao para adicionar ao banco

    messagebox.showinfo("LocFlix", "Cadastro realizado!")
    # abrir tela de login e fechar a de cadastro
    open_Login()

def cadastroValido(event=None):
    if  validarNome() and validarEmail() and validarSenha() and validarTelefone():
        submeter_cadastro.configure(state=tk.NORMAL)
    else:
        submeter_cadastro.configure(state=tk.DISABLED)
        

def validarNome():
    user = entrada_nome.get()
    if user:
        if all(s.isalpha() or s.isspace() for s in user) and len(user)>= 3:
            label1.config(
                text="ok",
                foreground="green",
            )
            return True
        elif len(user) == 0:
            label1.config(
                text="Digite seu nome.",
                foreground="red",
            )
            return False
        else:
            label1.config(
                text="Nome inválido.",
                foreground="red",
            )
            return False

def validarEmail():
    email = entrada_email.get()
    if email:
        if re.match('^\S+@\S+$',email):
            label2.config(
                text=f"ok",
                foreground="green",
            )
            return True
        else:
            label2.config(
                text="Email inválido.",
                foreground="red",
            )
            return False
    else:
        label2.config(
            text="Digite seu email.",
            foreground="red",
        )
        return False
    
def validarSenha():
    senha = entrada_senha.get()
    if senha:
        if re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", senha):
            label4.config(
                text=f"",
                foreground="green",
            )
            return True
        else:
            label4.config(
                text="Mínimo 8 characteres, letras e números.",
                foreground="red",
            )
            return False
    else:
        label4.config(
            text="Digite sua senha.",
            foreground="red",
        )
        return False


def validarTelefone():
    tel = entrada_tel.get()
    if tel:
        if re.match('^\(?[1-9]{2}\)? ?(?:[2-8]|9[0-9])[0-9]{3}\-?[0-9]{4}$',tel):
            label3.config(
                text=f"Telefone válido.",
                foreground="green",
            )
            return True
        else:
            label3.config(
                text="Telefone inválido.",
                foreground="red",
            )
            return False
    else:
        label3.config(
            text="",
            foreground="blue",
        )
        return True
    
def temDesconto():
    resposta = entrada_resposta.get()
    answer = re.sub('[^A-Za-z]+','', resposta.lower())
    if answer == 'sim':
        return True
    return False


win = tk.Tk()
win.bind("<Motion>", cadastroValido)
win.wm_attributes("-transparentcolor", 'grey')

win.geometry("1366x740")
win.configure(bg = "#FFFFFF")


canvas = Canvas(
    win,
    bg = "#FFFFFF",
    height = 740,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    600.0,
    100.0,
    950.0,
    600.0,
    fill="#52DFBD",
    outline="")

image_image_1 = tk.PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    750.0,
    315.0,
    image=image_image_1
)

image_image_2 = tk.PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    90.0,
    59.0,
    image=image_image_2
)

canvas.create_rectangle(
    68.0,
    100.0,
    550.0,
    600.0,
    fill="#E7FCF8",
    outline="")

canvas.create_text(
    132.0,
    130.0,
    anchor="nw",
    text="Cadastrar conta",
    fill="#0E795F",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    132.0,
    170.0,
    anchor="nw",
    text="Nome",
    fill="#0E795F",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    132.0,
    230.0,
    anchor="nw",
    text="Email",
    fill="#0E795F",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    132.0,
    290.0,
    anchor="nw",
    text="Senha",
    fill="#0E795F",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    132.0,
    350.0,
    anchor="nw",
    text="Telefone",
    fill="#0E795F",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    132.0,
    410.0,
    anchor="nw",
    text="Você assiste One Piece?",
    fill="#0E795F",
    font=("Inter", 13 * -1)
)

entry_image_1 = tk.PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    235.0,
    205.5,
    image=entry_image_1
)
entrada_nome = tk.Entry(
    bd=0,
    bg="#B7EEE0",
    fg="#000716",
    highlightthickness=0,
    validatecommand=validarNome,
    validate="focusin"
)
entrada_nome.place(
    x=144.5,
    y=190.5,
    width=181.0,
    height=29.0
)

label1 = ttk.Label(win, background="#E7FCF8",text="*")
label1.place(
    x=355.0,
    y=190.0,
    width=181.0,
    height=27.0
)

entry_image_3 = tk.PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_3 = canvas.create_image(
    235.0,
    265.5,
    image=entry_image_3
)
entrada_email = tk.Entry(
    bd=0,
    bg="#B7EEE0",
    fg="#000716",
    highlightthickness=0,
    validatecommand=validarEmail,
    validate="focusout"
)
entrada_email.place(
    x=144.5,
    y=250.5,
    width=181.0,
    height=29.0
)

label2 = ttk.Label(win, background="#E7FCF8", text="*")
label2.place(
    x=355.0,
    y=250.0,
    width=181.0,
    height=29.0
)

entry_image_4 = tk.PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_4 = canvas.create_image(
    235.0,
    325.5,
    image=entry_image_4
)
entrada_senha= tk.Entry(
    bd=0,
    bg="#B7EEE0",
    fg="#000716",
    highlightthickness=0,
    validatecommand=validarSenha,
    validate="focusout"
)
entrada_senha.place(
    x=144.5,
    y=310.5,
    width=181.0,
    height=29.0
)

label4 = ttk.Label(win, background="#E7FCF8", text="*")
label4.place(
    x=355.0,
    y=310.5,
    width=181.0,
    height=29.0
)

entry_image_2 = tk.PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    235.0,
    385.5,
    image=entry_image_2
)
entrada_tel= tk.Entry(
    bd=0,
    bg="#B7EEE0",
    fg="#000716",
    highlightthickness=0,
    validatecommand=validarTelefone,
    validate="focusout"
)
entrada_tel.place(
    x=144.5,
    y=370.0,
    width=181.0,
    height=29.0
)


label3 = ttk.Label(win, background="#E7FCF8", text="")
label3.place(
    x=355.0,
    y=370.0,
    width=181.0,
    height=29.0
)


entry_image_5 = tk.PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_5 = canvas.create_image(
    235.0,
    445.5,
    image=entry_image_5
)
entrada_resposta= tk.Entry(
    bd=0,
    bg="#B7EEE0",
    fg="#000716",
    highlightthickness=0,
)
entrada_resposta.place(
    x=144.5,
    y=430.0,
    width=181.0,
    height=29.0
)


button_image_2 = tk.PhotoImage(
    file=relative_to_assets("button_2.png"))
submeter_cadastro = tk.Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=submeterCadastro,
    state=tk.DISABLED
)
submeter_cadastro.place(
    x=139.0,
    y=500.0,
    width=183.0,
    height=31.0
)


button_image_1 = tk.PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: win.destroy,
    relief="flat"
)
button_1.place(
    x=217.0,
    y=545.0,
    width=36.0,
    height=12.0
)

win.resizable(True, False)
win.mainloop()
