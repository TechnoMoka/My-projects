from tkinter import *
import instaloader

moka = Tk()
moka.config(bg="lightskyBlue3")
moka.title("IPD")
moka.geometry('600x500')

def instaget():
    loader = instaloader.Instaloader()
    username = entry_username.get()
    password = entry_password.get()
    target = entry_target.get()
    try:
        loader.login(username , password)
        loader.download_profile(target, profile_pic=True)
        loader.download_post(target)
        status_label.config(text=f"{target} photos downloaded successfully!" , fg='green')
        
    except Exception as e:
        status_label.config(text=f"{target} photos failed to download {str(e)}" , fg='red')


label_username = Label(moka, text = 'username')
label_username.pack(pady = 5)
entry_username = Entry(moka)
entry_username.pack(pady = 10)

label_password = Label(moka, text = 'password')
label_password.pack(pady = 5)
entry_password = Entry(moka)
entry_password.pack(pady = 10)

label_target = Label(moka, text = 'target')
label_target.pack(pady = 5)
entry_target = Entry(moka)
entry_target.pack(pady = 10)

btn = Button(moka , text="Let's go", width=20, height=10 , command=instaget)
btn.pack()

status_label = Label(moka, text="" , bg="lightskyblue3")
status_label.pack(pady=20)

moka.mainloop()