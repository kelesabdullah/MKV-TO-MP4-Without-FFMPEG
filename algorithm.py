import moviepy.editor as moviepy

from tkinter import *
from tkinter import messagebox,filedialog,ttk


root = Tk()
root.geometry("200x200")
root.resizable(0,0)
root.title("MKV TO MP4 CONVERTER")

#ARKAPLAN FOTO CANVAS
img = PhotoImage(file="indir.png")
width, height = img.width(), img.height()
canvas = Canvas(root, width=width, height=height)
canvas.place(x=0,y=0)
canvas.create_image((0, 0), image=img, anchor="nw")

def convert():
    mkvfile = filedialog.askopenfilename()
    mkvfilepath = mkvfile.replace("/","\\")
    file = moviepy.VideoFileClip(mkvfilepath)
    mp4file = filedialog.asksaveasfilename(initialdir="/",title="Kaydedilecek dizini seçin ve dosyayı adlandırın.(Default olarak mp4 kaydedilir)",defaultextension=".mp4")
    mp4filepath = mp4file.replace("/","\\")
    file.write_videofile(mp4filepath)
    
    messagebox.showinfo("Basarili",f"MKV Dosyası başarıyla dönüştürüldü\n{mp4file}")
    


#CONVERT BUTON
ttk.Button(root,text="Convert to mp4",command=convert).pack(side=TOP,padx=50,pady=50)










root.mainloop()

