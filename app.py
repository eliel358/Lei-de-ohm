import customtkinter as ctk
import math
window = ctk.CTk()
window_height = '700'
window_width = '1000'
window.geometry(f'{window_width}x{window_height}+250+250')
window.title('Lei de Ohm')


entry = ctk.CTkEntry(window,width=100,height=10)
entry.place(x=700/4,y=1000/2)

label = ctk.CTkLabel(window,font=('Arial',20),text='Potencia')
label.place(x=700/4,y=450)

entry_1 = ctk.CTkEntry(window,width=100,height=10)
entry_1.place(x=700/2,y=1000/2)

label_1 = ctk.CTkLabel(window,font=('Arial',20),text='Tensão')
label_1.place(x=700/2,y=450)

entry_2 = ctk.CTkEntry(window,width=100,height=10)
entry_2.place(x=525,y=1000/2)

label_2 = ctk.CTkLabel(window,font=('Arial',20),text='Corrente')
label_2.place(x=525,y=450)

entry_3 = ctk.CTkEntry(window,width=100,height=10)
entry_3.place(x=700,y=1000/2)

label_3 = ctk.CTkLabel(window,font=('Arial',20),text='Resistencia')
label_3.place(x=700,y=450)

label_4 = ctk.CTkLabel(window,font=('Arial',20),text='')
label_4.place(x=1000/2,y=250,anchor='center')

def calcular_potencia():
    if entry.get() == '':
        entry.insert(0,'0')
    if entry_1.get() == '':
        entry_1.insert(0,'0')
    if entry_2.get() == '':
        entry_2.insert(0,'0')
    if entry_3.get() == '':
        entry_3.insert(0,'0')

    p = float(entry.get())
    v = float(entry_1.get())
    i = float(entry_2.get())
    r = float(entry_3.get())
    
    if v and r:
        p = (v**2)/r
        return p
    elif v and i:
        p = v*i
        print('2')
        return p
    elif r and i:
        p = r*(i**2)
        print('3')
        return p
    else:
        return p
    
def calcular_tensao():
    if entry.get() == '':
        entry.insert(0,'0')
    if entry_1.get() == '':
        entry_1.insert(0,'0')
    if entry_2.get() == '':
        entry_2.insert(0,'0')
    if entry_3.get() == '':
        entry_3.insert(0,'0')

    p = float(entry.get())
    v = float(entry_1.get())
    i = float(entry_2.get())
    r = float(entry_3.get())
    
    if i and r:
        v = r*i
        return v
    elif p and i:
        v = p/i
        return v
    elif p and r:
        v = math.sqrt(p*r)
        return v
    else:
        return v
    
def calcular_resistencia():
    if entry.get() == '':
        entry.insert(0,'0')
    if entry_1.get() == '':
        entry_1.insert(0,'0')
    if entry_2.get() == '':
        entry_2.insert(0,'0')
    if entry_3.get() == '':
        entry_3.insert(0,'0')

    p = float(entry.get())
    v = float(entry_1.get())
    i = float(entry_2.get())
    r = float(entry_3.get())
    
    if i and v:
        r = v/i
        return r
    elif v and p:
        r = (v**2)/p
        return r
    elif p and i:
        r = (p/(i**2))
        return r
    else:
        return r
    
def calcular_corrente():
    if entry.get() == '':
        entry.insert(0,'0')
    if entry_1.get() == '':
        entry_1.insert(0,'0')
    if entry_2.get() == '':
        entry_2.insert(0,'0')
    if entry_3.get() == '':
        entry_3.insert(0,'0')

    p = float(entry.get())
    v = float(entry_1.get())
    i = float(entry_2.get())
    r = float(entry_3.get())
    
    if v and r:
        i = v/r
        return i
    elif v and p:
        i = p/v
        return i
    elif p and r:
        i = math.sqrt(p/r)
        return i
    else:
        return i
    
def calcular():
    label_4.configure( text = 'Potencia: '+str(calcular_potencia()) +'\nTensão: '+str(calcular_tensao())+'\nResistencia: '+str(calcular_resistencia())+'\nCorrente: '+str(calcular_corrente()))
bt_calcular = ctk.CTkButton(window,width=200,height=50,font=('Arial',35),text_color='black',text='Calcular',command=calcular)
bt_calcular.place(x=1000/2,y=650,anchor='center')


window.mainloop()