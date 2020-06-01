from pywinauto import application
app1=application.Application()
app1.Start("Notepad.exe")
app1.Notepad.edit.TypeKeys("This ")
app1.Notepad.MenuSelect("File->Save")
app1.SaveAs.edit.Save.click()
app1.Notepad.Close()