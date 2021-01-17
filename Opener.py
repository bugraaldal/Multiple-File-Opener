import tkinter as tk
from tkinter import filedialog, Text
import os
os.chdir("c:/Users/Buğra//Desktop/Python/Opener")
root = tk.Tk()  # Creating the main window
apps = []
resultList = []
colour = "green"
root.title("One For All")  # Name of the main window


root.configure(background=colour)  # Background of the main window


if os.path.isfile("OneForAllSave.txt"):
    with open("OneForAllSave.txt", "r", encoding="utf-8") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]


def click():  # Defining the function of "Search" button
    entered_text = entry.get()  # Getting searched words
    # Looping through the  C and D disks and appending the fitting results into a list(resultList):
    os.chdir("C:/Users/Buğra/")
    for _, _, files in os.walk(os.getcwd()):
        for f in files:
            if entered_text.lower() in f.lower():
                resultList.append(f)
    os.chdir("D:/Users/Buğra/")
    for _, _, files in os.walk(os.getcwd()):
        for f in files:
            if entered_text.lower() in f.lower():
                resultList.append(f)
    # Looping through the resultList to count how many files were found
    count = len(resultList)
    top = tk.Toplevel()  # Creating a pop-up window to show the results
    tk_resultsfound_label = tk.Label(
        top, text=f"{count} results found.", font="none 17 bold")
    # Telling how many results were found
    tk_resultsfound_label.pack(side="top")

    def clickedAdd(res):
        os.chdir("/home/buura")
        with open("OneForAllSave.txt", "a") as s:
            s.write(res + ",")
    for result in resultList:
        addbuttonsearch = tk.Button(
            top, text=result, command=lambda: clickedAdd(result))
        addbuttonsearch.pack()

# Adding apps to open


def addApp():
    os.chdir("/home/buura")
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


# Fundtion of "Run the Files". Runs the files -duh


def runApps():
    for app in apps:
        os.popen(app)


# Adding the "Search a File" label at the top:
search = tk.Label(root, text="Search a file:        ", bg="green",
                  fg="white", font="none 12 bold")
search.pack(side="top")
entry = tk.Entry(root, width=60, bg="white")  # Creating the search bar
entry.pack()
# Creating the "Search button"
searchbutton = tk.Button(root, text="Search", width=50, command=click)
searchbutton.pack()

# Adding the big white box -which shows the files- in the middle
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# The "Add a File Manually" button:
addFile = tk.Button(root, text="Add a File Manually", padx=310,
                    pady=5, fg="white", bg="green", command=addApp)
addFile.pack(side="bottom")
# The "Run the files" button:
runFile = tk.Button(root, text="Run the Files", padx=302,
                    pady=5, fg="white", bg="green", command=runApps)
runFile.pack(side="bottom")

for app in apps:  # Looping through the apps list and creating a label with each of them
    label = tk.Label(frame, text=app)
    label.pack()
root.mainloop()

with open("OneForAllSave.txt", "w") as f:  # Creating a save file
    for app in apps:
        f.write(app + ",")
