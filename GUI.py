import PySimpleGUI as sg

layout = [
    [sg.Text('Fichas iniciales a jugar: '), sg.InputText()],
    [sg.Text('Fichas Máximas a jugar:'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Close Window')],
    [sg.Text("Si no se quiere tener un máximo de fichas para apostar, dejar vacío el segundo apartado")]]

window = sg.Window('CASINO MONOPOLY // JuankiSuela', layout).Finalize()
while True:
    event, values = window.read()
    if event in (None, 'Close Window'):
        break
    else:
        if values[0] == "" or int(values[0]) < 5000:
            print("El valor inicial no puede ser 0, ni menor de 5000. Valor: ", values[0])

        elif values[1] == "" or int(values[1]) >= int(values[0]):
            if int(values[0]) % 5 == 0 and (values[1] == "" or int(values[1]) % 5 == 0) :
                window.close()
                print('Has introducido: ', values)
                fichamin = int(values[0])
                if values[1] != "":
                    fichamax = int(values[1])
                else:
                    fichamax = values[1]
            else:
                print("El número introducido no puede ser transformado en fichas, introduzca un valor múltiple de 5, "
                      "los valores introducidos eran: ", values[0], values[1])
        else:
            print(
                'Las fichas máximas para apostar no pueden ser menores que las fichas iniciales, Introduzca otros '
                'valores')

window.close()
