import qrcode
import customtkinter as ctk
from PIL import Image

class QrCode():
    def generator(self, link:str, name):
        image = qrcode.make(f'{link}')
        image.save(f'.\\QRCode\\QRCode - {name}.png')

class Interface():
    def configures(self):
        pass

ctk.set_appearance_mode('light')
app = ctk.CTk()
app.geometry("400x500")
app.title('Gerador de QRCode')
app.resizable(False, False)

#  Variaveis
qr = QrCode()
img = ctk.CTkImage(Image.open('.\\img\\refresh.png'), size=(16, 16))

# Funções
def get_link():
    global qr
    lab_qr.configure(image=None)
    name = ent_name.get()
    link = ent_link.get()

    qr.generator(link, name)
    result.pack(pady=10)
    result.configure(text='QRCODE GERADO')

    view_qrcode(name)

def view_qrcode(name):
    qrcode_generate = ctk.CTkImage(Image.open(f'.\\QRCode\\QRCode - {name}.png'), size=(170, 170))
    lab_qr.configure(image=qrcode_generate)
    lab_qr.pack(pady=10)

def reset():
    for widget in app.winfo_children():
        if isinstance(widget,ctk.CTkEntry):
            widget.delete(0,'end')
        result.pack_forget()
        lab_qr.pack_forget()

# Campos
btn_reset = ctk.CTkButton(app, width=30, text=None, command=lambda:reset(), text_color='black', fg_color='#96989A', image=img)
btn_reset.pack(pady=10)

ent_name = ctk.CTkEntry(app, width=200, placeholder_text='INSIRA O NOME DO QRCODE')
ent_name.pack(pady=10)

lab_link = ctk.CTkLabel(app, text='DIGITE SEU LINK ABAIXO:')
lab_link.pack(pady=10)

ent_link = ctk.CTkEntry(app, width=250, placeholder_text='INSIRA O LINK')
ent_link.pack(pady=10)

btn = ctk.CTkButton(app, text="GERAR QRCODE", command=get_link)
btn.pack(pady=10)

result = ctk.CTkLabel(app, text="")
result.pack_forget()

lab_qr = ctk.CTkLabel(app, text='')
lab_qr.pack_forget()

app.mainloop()