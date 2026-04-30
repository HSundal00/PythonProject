import functions
import FreeSimpleGUI as SG

label = SG.Text("Type in a to-do")
input_box = SG.InputText(tooltip="Enter todo")
add_button = SG.Button("Add")

window = SG.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()

