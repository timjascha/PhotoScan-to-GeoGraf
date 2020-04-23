from guizero import App, TextBox, PushButton, Text, Window

app = App(title="Converter", height=400)
win = Window(app, title="Copyright")
win.hide()

def main():
    if filename.value=="filename":
        app.error(title="Error!", text="Bitte zuerst eine Datei wählen!")
    if savet.value=="save":
        app.error(title="Error", text="Bitte zuerst einen Speicherpfad wählen!")
    else:
        input = open(filename.value, "r")
        output = open(savet.value + ".xyz", "w")
        n = 1
        for line in input:
            print(n)
            n = n + 1
            i = str(add.value)
            output.write(str(i) + line)
        input.close()
        output.close()
        app.info(title=" ", text="Done!")
def counter():
    if filename.value=="filename":
        app.error(title="Error!", text="Bitte zuerst eine Datei wählen!")
    else:
        input = open(filename.value, "r")
        count = 0
        for line in input:
            count = count + 1
        app.info("Anzahl der Punkte", "Anzahl der Punkte " + str(count))
        input.close()

def copyr():
    win.show()
def file():
    filename.value=app.select_file(title="Select file", folder=".", filetypes=[["All files", "."]], save=False)
    filename.show()
    app.height=500

def save():
    savet.value = app.select_file(title="Select file", folder=".", filetypes=[["All files", "."]], save=True)
    savet.show()
    app.height = 500



 #Content of main window:
loadfile = PushButton(app, text="Datei wählen", command=file, width="fill")
addt = Text(app, text="Additionswert:", width="fill")
add = TextBox(app, width="fill")
convert = PushButton(app,text="Start", command=main, width="fill")
counterb = PushButton(app, text="Punkte zählen", command=counter, width="fill")
copybutton = PushButton(app, text="Copyright", command=copyr, width="fill")
filename = TextBox(app, text="filename", width="fill")
savet = Text(app,text="save", width="fill")
savet.hide()
saveb = PushButton(app, text="Speichern", command=save, width="fill")
exit = PushButton(app, text="Beenden",  command=exit, width="fill")
filename.hide()


copytext = Text(win, text="Copyright by Tim Jascha Fellmeden")
twitter = Text(win, text="Twitter: TimJascha")
github = Text(win, text="Github: timjascha")
webs = Text(win, text="Website; timjascha.com")
app.display()