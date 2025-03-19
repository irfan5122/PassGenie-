#@Author AHMED IRFAN N
from tkinter import*
import random
import pickle
#import ctypes, sys
import os
from tkinter import messagebox as msg
from tkinter import filedialog
from tkinter import ttk
#ctypes.windll.shell32.IsUserAnAdmin()

root = Tk()
root.iconbitmap("passwordgenie.ico")
root.resizable(False,False)

def destroy_window():
	root.destroy()

def open_file():
	def window_2():
		history = Tk()
		history.resizable(False,False)
		history.title("Clear passwords")
		history.iconbitmap("passwordgenie.ico")
		def clear_passwords():
			history.destroy()
			window.destroy()
			question  = msg.askquestion('Clear passwords','All your saved passwords will be cleared are you sure to continue',icon='warning',default='no')
			if question == 'yes':
				os.system(f"del passwords.irf")
				msg.showinfo("Deleted","Passwords deleted successfully")
			else:
				pass

		history.config(bg='black')
		history.geometry("600x300")
		label_warning = Label(history,text="Warning : Clearing saved passwords are not recovarable\nThis is the secure way to remember generated passwords\nThe password file is irf encrypted",bg='black',fg='cyan',font=('',15))
		label_warning.place(x=40,y=50)
		clear_btn = Button(history,text="clear",font=('ROG FONTS',16),bg='black',fg='cyan',command=clear_passwords)
		clear_btn.place(x=40,y=180)
		exit_btn = Button(history,text="exit",font=('ROG FONTS',16),bg='black',fg='cyan',command=history.destroy)
		exit_btn.place(x=460,y=180)


		history.mainloop()

		#file_opened = filedialog.askopenfilename(initialdir=r'C:\Users\ASUS\Desktop',defaultextension=".irf",title="open .irf password file",filetypes=[("Irf password files", "*.irf")])
		#print(file_opened) #Removed this code for security
	check_file = os.path.isfile('passwords.irf')
	if check_file == False:
		with open('passwords.irf','w') as create:
			pass
			
	file = open('passwords.irf','rb')
	global string
	string = ''
	while True:
		try:
			data = pickle.load(file)
			for i in data:
				convert_str = str(i)
				string = string+convert_str
					#print(i,end='')

		except:
			break

	file.close()
	def settings():
		setting = Tk()
		setting.resizable(False,False)
		setting.title("Under Development")
		setting.geometry("300x100")
		setting.config(bg='black')
		coming_soon_lbl = Label(setting,text="Coming Soon",font=("ROG FONTS",20),bg='black',fg='cyan')
		coming_soon_lbl.pack()
		setting.mainloop()


	#print(string)
	window = Tk()
	window.iconbitmap("passwordgenie.ico")
	window.resizable(False,False)
	window.config(bg='black')
	window.title('Password Decrypter')
	window.geometry("400x600")
	mainframe = Frame(window)
	mainframe.config(bg='black')
	mainframe.pack(fill=BOTH, expand=1)
	my_canvas = Canvas(mainframe)
	#my_canvas.config(bg='black')
	my_canvas.pack(sid=LEFT,fill=BOTH,expand=1)
	my_scrollbar = ttk.Scrollbar(mainframe,orient=VERTICAL,command=my_canvas.yview)
	my_scrollbar.pack(side=RIGHT,fill=Y)
	my_canvas.configure(yscrollcommand=my_scrollbar.set)
	my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))
	second_frame = Frame(my_canvas)
	second_frame.config(bg='black')	
	my_canvas.create_window((0,0),window=second_frame,anchor="nw")
	lbl_password = Label(second_frame,text=string,font=('System',20),bg='black',fg='cyan')
	lbl_password.grid(column=0,pady=10,padx=10)
	my_menu = Menu(window)
	sub_menu = Menu(my_menu,tearoff="off")
	sub_menu.add_command(label="Preferences",command=settings)
	sub_menu.add_command(label="History",command=window_2)
	my_menu.add_cascade(label='Edit',menu=sub_menu)
	window.config(menu=my_menu)
	window.mainloop()

	'''except:
					with open('passwords.irf','ab') as create:
						pass '''

		


''''
def on_destroy(e):
	string = '______'
	with open('passwords.irf','ab') as data:
		pickle.dump(string,data)
'''
def copy():
	root.clipboard_clear()
	password_copied = store.get()
	root.clipboard_append(password_copied)
	lbl_pass_cp.config(text='password copied')
	colors = ['red','palegreen','cyan','lemon chiffon','white smoke']
	while True:
		random_color = random.choice(colors)
		lbl_color_now = lbl_pass_cp.cget("fg")   
		if random_color != lbl_color_now:
			lbl_pass_cp.config(fg=random_color)
			#print(random_color)
			break

		else:
			continue
		
count = 0
def generate():
	global count
	import string
	count = count+1
	



	numbers = list(string.digits)
	small_letters = list(string.ascii_lowercase)
	capital_letters = list(string.ascii_uppercase)
	special_characters = list(string.punctuation)
	first_chr = random.choice(capital_letters)
	second_chr = random.choice(small_letters)
	third_chr = str(random.choice(numbers))
	fourth_chr = random.choice(capital_letters)
	fifth_chr = random.choice(capital_letters)
	sixth_chr = random.choice(small_letters)
	seventh_chr = str(random.choice(numbers))
	eighth_chr = random.choice(small_letters)
	nineth_chr = random.choice(capital_letters)
	tenth_chr = random.choice(special_characters)
	password = first_chr+second_chr+third_chr+fourth_chr+fifth_chr+sixth_chr+seventh_chr+eighth_chr+nineth_chr+tenth_chr
	store.set(password)
	string = f"\npassword{count} = "
	string_1 = '\n'
	password_bin = string,first_chr,second_chr,third_chr,fourth_chr,fifth_chr,sixth_chr,seventh_chr,eighth_chr,nineth_chr,tenth_chr,string_1


	'''with open('passwords.irf','ab') as data:
					cwd = os.getcwd()
					file_path = cwd+'\\passwords.irf'
					print(os.path.getsize(file_path))
					file_size = os.path.getsize(file_path)
					if file_size == 0:
						with open('passwords.irf','ab') as data_1:
							pickle.dump(password_bin,data_1)
			
					elif file_size>0:
						print(dir)'''

	with open('passwords.irf','ab') as data:
		pickle.dump(password_bin,data)

	

	if count == 5:
		msg.showinfo("Error","Maximum password limit 5 has reached")
		root.destroy()

root.title('password generator')
root.geometry('350x220') #350x200
root.config(bg='black')
store = StringVar()
lbl_txt = Entry(root,textvariable=store,bd=0,font=('Time of Roman',20),state='readonly',width=12)
b1 = Button(root,bg='black',fg='cyan',text='Generate',font=('ROG FONTS',20),command=generate)
lbl_txt.place(x=55,y=30)
b1.place(x=40,y=90)


def about():
	msg.showinfo("About","Software by AHMED IRFAN N\nPassword_encryption: binary\nversion : 1.0")
	'''
				ls = [0b1010011,0b1101111,0b1100110,0b1110100,0b1110111,0b1100001,0b1110010,0b1100101,0b100000,0b1100010,0b1111001,
					  0b100000,0b1000001,0b1001000,0b1001101,0b1000101,0b1000100,0b100000,0b1001001,0b1010010,0b1000110,0b1000001,
					  0b1001110,0b100000,0b1001110,0b1010,0b1010000,0b1100001,0b1110011,0b1110011,0b1110111,0b1101111,0b1110010,
					  0b1100100,0b1011111,0b1100101,0b1101110,0b1100011,0b1110010,0b1111001,0b1110000,0b1110100,0b1101001,0b1101111,
					  0b1101110,0b111010,0b100000,0b1000010,0b1101001,0b1101110,0b1100001,0b1110010,0b1111001,0b1010,0b1010110,0b1100101,
					  0b1110010,0b1110011,0b1101001,0b1101111,0b1101110,0b111010,0b110001,0b101110,0b110000]
			
				ls_2 = []
				for i in ls:
					type_change = chr(i)
					ls_2.append(type_change)
			
				msg.showinfo("about",ls_2)'''

def help_password():
	import webbrowser
	webbrowser.open("https:\\www.google.com")



def feedback():
	import webbrowser
	webbrowser.open("mailto:irfan512289747@gmail.com")
def website():
	import webbrowser
	webbrowser.open("https:\\app-store-irfan.web.app")




main_menu = Menu(root)
options_menu = Menu(main_menu,tearoff="off")
options_menu.add_command(label='About',command=about)
options_menu.add_command(label='Website',command=website)
options_menu.add_command(label='Feedback',command=feedback)
main_menu.add_cascade(label='options',menu=options_menu)
root.config(menu=main_menu)

copy_btn = Button(root,text='copy',bg='black',fg='red',font=('ROG FONTS',12),command=copy)
copy_btn.place(x=250,y=30)

lbl_pass_cp = Label(root,text='',bg='black',fg='palegreen',font=('Terminal',15))
lbl_pass_cp.place(x=90,y=160)

open_btn = Button(root,text='Open',bg='black',fg='OrangeRed2',font=('ROG FONTS',12),command=open_file)
open_btn.place(x=250,y=155)
#root.bind('<Destroy>',on_destroy)
root.mainloop()