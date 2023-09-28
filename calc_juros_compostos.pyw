# Autor : Samuel Vidal Roberto
# Projeto feito em : Janeiro de 2023


import PySimpleGUI as sg

sg.theme("green")



layout = [

[sg.Text("Digite o capital inicial :")],
[sg.Input(key= "cap")],
[sg.Text("Digite a taxa :")],
[sg.Input(key="tax")],
[sg.Text("Digite o tempo decorrido :")],
[sg.Input(key="tempo")],
[sg.Button("Calcular")]

]

janela = sg.Window("Juros Compostos", layout = layout)

while True:
    try:
        events, values = janela.read()
        if events == sg.WIN_CLOSED:
            break
            exit()
        if events == "Calcular":
        
            c = float(values["cap"].replace(",", "."))
            i = float(values["tax"].replace(",", "."))
            t = float(values["tempo"].replace(",", "."))
            formula = c*((1+(i/100))**t)

            

            formula_str = f"{formula:.2f}"

            

            sg.popup(formula_str , title = "Resultado")
    except:
        sg.popup("algo deu errado")
    




