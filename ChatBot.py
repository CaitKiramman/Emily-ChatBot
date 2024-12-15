# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:32:06 2024
Creating a simple ChatBot
@author: CaitKiramman
"""

import tkinter as tk

responses = {
    "γεια": "Γεια σου! Πώς μπορώ να βοηθήσω;",
    "πώς είσαι": "Είμαι ένα chatbot, οπότε είμαι πάντα καλά! Εσύ;",
    "τι κάνεις": "Είμαι εδώ για να σε βοηθήσω με τις ερωτήσεις σου!",
    "αντίο": "Αντίο! Να έχεις μια υπέροχη μέρα!"
}


def answering(user_input):
    user_input = user_input.lower()
    for key in responses:
      if key in user_input:
          answer_label.config(text=responses[key])  
          return
      else: 
         answer_label.config(text="Συγγνώμη, δεν καταλαβαίνω την ερώτηση. Μπορείς να δοκιμάσεις κάτι άλλο;")  
         
      
    

def button_clicked(event=None):
    user_input = entry.get()  # Παίρνουμε το κείμενο από το πεδίο εισαγωγής
   # answer_label.config(text=user_input)  # Ενημέρωση του Label με το μήνυμα
    answering(user_input)
    entry.delete(0, tk.END)
    return user_input;
   
    

RootWindow = tk.Tk()
RootWindow.title('ChatBot Emily')
RootWindow.geometry('600x400+20+50')
message = tk.Label(RootWindow, text="Γεια ονομάζομαι Emily, είμαι το ChatBot σου. Είμαι εδώ για οτιδήποτε χρειαστείς!")
message.pack()


button = tk.Button(RootWindow, text=' Send ', command=button_clicked)
RootWindow.bind('<Return>', button_clicked)
entry = tk.Entry(RootWindow, width=80)


message_label = tk.Label(RootWindow, text="Τι θα ήθελες να συζητήσουμε σήμερα;")




answer_Frame= tk.Frame(RootWindow,width=500, height=200, bd=1, relief="solid", bg="white")
answer_label = tk.Label(answer_Frame, text=" ", bg="white",  wraplength=496)
answer_Frame.pack_propagate(False)
answer_label.place(x=0, y=0)

  
"""Η update_idletasks() μπορεί να χρησιμοποιηθεί εάν κάνεις ανανεώσεις που αφορούν 
το μέγεθος και την τοποθέτηση του widget μετά την ενέργεια του χρήστη.
"""
RootWindow.update_idletasks()


entry_width = entry.winfo_reqwidth()  # Πλάτος του πεδίου εισαγωγής
window_width = RootWindow.winfo_width()  # Πλάτος παραθύρου
button_width = button.winfo_reqwidth()  # Πλάτος κουμπιού

x_button_position = (window_width - button_width) // 2
button.place(x=x_button_position,y=350) 

x_entry_position = (window_width - entry_width) // 2
entry.place(x=x_entry_position, y=320)

message_label.place(x=x_entry_position, y=290)
answer_Frame.place(x=x_entry_position, y=50)

RootWindow.mainloop()




