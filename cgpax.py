from Tkinter import *
import tkMessageBox
variables = []
num_courses = 13

def widgets(root, irow = 2):
    interface = Frame(root)
    Label(interface, text = 'Current CGPA', bg ='yellow',relief = GROOVE).grid(row = 0, column = 0)
    init_cgpa = Entry(interface, width = 4)
    init_cgpa.grid(row = 0, column = 1, sticky = W)
    Label(interface, text = 'Total Offered Units',bg='yellow', relief = GROOVE).grid(row = 0, column = 2)
    overall_units = Entry(interface, width = 4)
    overall_units.grid(row = 0, column = 3, sticky = W)
    variables.append((init_cgpa, overall_units))
    
    for course in range(num_courses):
        label=Label(interface, width = 6, text = 'GP' + str(course + 1),
                    bg = 'light blue', relief = SUNKEN)
        course_box = Entry(interface)
        lbl = Label(interface, width = 6, text = 'Unit',bg = 'light blue',
                    relief = SUNKEN)
        unit_box = Entry(interface)

        label.grid(row = irow, column = 0)
        course_box.grid(row = irow, column = 1)
        lbl.grid(row = irow, column = 2)
        unit_box.grid(row = irow, column = 3)
        variables.append((course_box, unit_box))
        irow += 1
    interface.grid(row = irow)
    return variables

def event_handler(variables):
    totpts = 0
    totunits = 0
    pts = 0
    units = 0
    for grade in variables:
        try:
            totpts = totpts + (float(grade[0].get()) * float(grade[1].get()))
            totunits += float(grade[1].get())
            
        except(ValueError):
            pass
        
    for pos in range(len(variables)):
        try:
            pts = pts + (float(variables[pos+1][0].get()) * float(variables[pos+1][1].get()))
            units += float(variables[pos+1][1].get())
            
        except(ValueError, IndexError):
            pass
    try:
        cgpa = totpts/totunits
        gpa = pts/units

        if cgpa >= 4.5:
            tkMessageBox.showinfo('RESULT', 'GPA = ' + str(round(gpa, 2)) + '\nCGPA = ' + str(round(cgpa, 2)) + '\n\nTotal Offered Units = ' + str(int(totunits))
                                + '\n\n' + 'First Class Honours'.rjust(30,'-'))
        elif cgpa >= 3.5:
            tkMessageBox.showinfo('RESULT', 'CGPA = ' + str(round(cgpa, 2)) + '\t\tGPA = ' + str(round(gpa, 2)) + '\nTotal Offered Units = ' + str(int(totunits))
                                + '\n\n' + 'Second Class Upper Honours'.rjust(30,'-'))
        elif cgpa >= 2.4:
            tkMessageBox.showinfo('RESULT', 'CGPA = ' + str(round(cgpa, 2)) + '\nTotal Offered Units = ' + str(int(totunits))
                                + '\n\n' + 'Second Class Lower Honours'.rjust(30,'-'))
        elif cgpa >= 1.5:
            tkMessageBox.showinfo('RESULT', 'CGPA = ' + str(round(cgpa, 2)) + '\nTotal Offered Units = ' + str(int(totunits))
                                + '\n\n' + 'Third Class'.rjust(30,'-'))

        elif cgpa >= 1.0:
            tkMessageBox.showinfo('RESULT', 'CGPA = ' + str(round(cgpa, 2)) + '\nTotal Offered Units = ' + str(int(totunits))
                                + '\n\n' + 'Pass'.rjust(30,'-'))
        else:
            tkMessageBox.showinfo('RESULT', 'CGPA = ' + str(round(cgpa, 2)) + '\nTotal Offered Units = ' + str(int(totunits))
                                + '\n\n' + 'Probation'.rjust(30,'-'))
    except(ZeroDivisionError):
        pass

def end():
    if tkMessageBox.askyesno('Quit','Are you sure?'):
        import sys; sys.exit()
    
                     
if __name__ =='__main__':
    root = Tk()
    exe = widgets(root)
    root.title('UNIVERSAL CGPA GENERATOR')
    root.bind('<Return>',(lambda event,e=exe: event_handler(e)))
    
    but = Button(root, text = 'Show Result',command=(lambda e=exe: event_handler(e)))
    but.grid(sticky = W)
    but.config(bg = 'white')
    
    but1 = Button(root, text = 'Exit', command = (lambda e=exe: end()))
    but1.grid(row = 16, sticky = E)
    but1.config(width = 5, bg = 'white')
    root.mainloop()

    
    
        

        
            
            
            
