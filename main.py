from tkinter import *

sec = 60
passage = "Lulu was out for her usual morning walk when she took a wrong turn and found herself in the woods. She tried to retrace her steps, but soon realized she was lost. She began to panic, but then she remembered her training and started using her nose to sniff out a way home. She met all kinds of creatures along the way, but she was too scared to speak to them. Eventually, her nose led her to a house made of dog treats. It looked delicious, but she knew better than to eat anything she found in the woods. Suddenly, an evil witch appeared and tried to trap Lulu in the house. But Lulu was too smart for her and used her nose to find the door and escape. She was finally home safe and sound, and she vowed never to wander off the path again."
final_score = 0
cpm_score_final =0
typed_values = []

# list to str
# passage = passage.join(passage_list)
# print(passage)

# str to list
passage_list = passage.split(" ")
# print(passage_list)

screen1 = Tk()
screen1.geometry("1200x600")
screen1.title("Typing Test Desktop App")
screen1.config(bg="lightblue", padx=300, pady=50)


def start_typing(sec):
    cpm = []
    score = 0
    global final_score
    global cpm_score_final
    global typed_values
    missing_values = []
    if sec !=0:
        screen1.after(1000, start_typing, sec - 1)
        time_left.config(text=sec)
        # print(sec)
        INPUT_value = input.get("1.0", "end-1c")
        # print(INPUT_value)
        INPUT_list = INPUT_value.split(" ")
        for i in range(0,len(INPUT_list)):
            if INPUT_list[i] == passage_list[i]:
                cpm_score = ""
                score += 1
                # print(score)
                final_score = score
                cpm.append(INPUT_list[i])
                # print(cpm)
                cpm_score = cpm_score.join(cpm)
                # print(cpm_score)
                cpm_score_final = len(cpm_score)
            else:
                # print(f"Insted of {passage_list[i]} you typed {INPUT_list[i]}\n\n")
                missing_values.append(f'Instead of "{passage_list[i]}", you typed "{INPUT_list[i]}"\n')
                typed_values = missing_values
                # paragraph.tag_config("start", foreground="red")
                # paragraph.tag_add("start",2.5,2.8)

    else:
        # print(sec)
        screen1.destroy()
        show_score()


def show_score():
    screen2 = Tk()
    screen2.geometry("1200x600")
    screen2.title("Typing Test Desktop App Results")
    screen2.config(bg="lightblue", padx=400, pady=150)

    typing_score = Label(text=f"Your score: {cpm_score_final} CPM (that is {final_score} WPM)",font=("Arial", 20),bg="lightblue",fg="green")
    typing_score.grid_configure(row=2, column=2)

    missed_str =""
    missed_str = missed_str.join(typed_values)
    typed_value = Label(text=missed_str ,font=("Arial", 18),bg="lightblue",fg="red")
    typed_value.grid_configure(row=3, column=2)


title = Label(text="Typing Speed Test", font=("Arial",25,"bold"),bg="lightblue")
title.grid_configure(row=1, column=1)

time_left = Label(text=f"Time left:",font=("Arial", 14))
time_left.grid_configure(row=2, column=2)

time_left = Label(text=sec,font=("Arial", 14),fg="red")
time_left.grid_configure(row=2, column=3)

canvas = Canvas(width=600,height=300,background="white")
canvas_text = canvas.create_text(canvas.winfo_width()+300,canvas.winfo_height()+150,width=580,text=passage,fill="green",font=("Arial", 14))
canvas.grid_configure(row=4,column=1)

input = Text(width=50,height=3,font=("Arial", 14))
# input.bind('<KeyPessed>',start_typing(sec))
input.grid_configure(row=5,column=1)

# paragraph = Text(width=50,height=3,font=("Arial", 14))
# paragraph.insert(END,passage)
# paragraph.grid_configure(row=6,column=1)

note = Label(text="Note: Please click start button and start to type",font=("Arial", 14),fg="red")
note.grid_configure(row=2, column=1)

start = Button(text="start", command=lambda: start_typing(sec),font=("Arial", 14))
start.grid_configure(row=5, column=0)

screen1.mainloop()





