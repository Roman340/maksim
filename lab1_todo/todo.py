import json, os 
import tkinter as tk 
from tkinter import ttk 
 
DATA_FILE = "todo.json" 
 
def load_tasks(): 
    if os.path.exists(DATA_FILE): 
        with open(DATA_FILE, "r", encoding="utf-8") as f: 
            return json.load(f) 
    return [] 
 
def save_tasks(tasks): 
    with open(DATA_FILE, "w", encoding="utf-8") as f: 
        json.dump(tasks, f, ensure_ascii=False, indent=2) 
 
class TodoApp: 
    def __init__(self, root): 
        self.root = root 
        root.title("Список задач (Docker Edition)") 
        root.geometry("420x380") 
        self.tasks = load_tasks() 
        self.entry = ttk.Entry(root) 
        self.entry.pack(fill="x", padx=10, pady=8) 
        self.entry.bind("<Return>", lambda e: self.add_task()) 
        ttk.Button(root, text="Добавить задачу", 
                   command=self.add_task).pack(pady=2) 
        self.listbox = tk.Listbox(root, height=12) 
        self.listbox.pack(fill="both", expand=True, padx=10, pady=8) 
        ttk.Button(root, text="Удалить выбранную", 
                   command=self.delete_task).pack(pady=2) 
        ttk.Button(root, text="Сохранить и выйти", 
                   command=self.save_and_exit).pack(pady=4) 
        self.refresh() 
        root.protocol("WM_DELETE_WINDOW", self.save_and_exit) 
 
    def refresh(self): 
        self.listbox.delete(0, tk.END) 
        for i, t in enumerate(self.tasks, 1): 
            self.listbox.insert(tk.END, f"{i}. {t}") 
 
    def add_task(self): 
        text = self.entry.get().strip() 
        if text: 
            self.tasks.append(text) 
            self.entry.delete(0, tk.END) 
            self.refresh() 
 
    def delete_task(self): 
        sel = self.listbox.curselection() 
        if sel: 
            self.tasks.pop(sel[0]) 
            self.refresh() 
 
    def save_and_exit(self): 
        save_tasks(self.tasks) 
        self.root.destroy() 
 
if __name__ == "__main__": 
    root = tk.Tk() 
    TodoApp(root) 
    root.mainloop() 