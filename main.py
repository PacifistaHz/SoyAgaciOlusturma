import tkinter as tk
from tkinter import messagebox
import graphviz
import os

class SoyağacıUygulaması:
    def __init__(self, root):
        self.root = root
        self.root.title("Soyağacı Uygulaması")

        self.tree = graphviz.Digraph(comment="Soyağacı")

        self.label = tk.Label(root, text="Aile bireyinin adını girin:")
        self.label.pack()

        self.entry_name = tk.Entry(root)
        self.entry_name.pack()

        self.label_parent = tk.Label(root, text="Ebeveyn adını girin (yoksa boş bırakın):")
        self.label_parent.pack()

        self.entry_parent = tk.Entry(root)
        self.entry_parent.pack()

        self.button_add = tk.Button(root, text="Ekle", command=self.add_member)
        self.button_add.pack()

        self.button_create = tk.Button(root, text="Soy ağacını oluştur", command=self.create_tree)
        self.button_create.pack()

    def add_member(self):
        name = self.entry_name.get().strip()
        parent = self.entry_parent.get().strip()

        if not name:
            messagebox.showerror("Hata", "Lütfen bir isim girin.")
            return

        if parent:
            self.tree.node(name)
            self.tree.edge(parent, name)
        else:
            self.tree.node(name)

        self.entry_name.delete(0, tk.END)
        self.entry_parent.delete(0, tk.END)

        messagebox.showinfo("Başarılı", f"{name} başarıyla eklendi.")

    def create_tree(self):
        try:
            self.tree.render("soy_agaci", format="png", cleanup=True)
            messagebox.showinfo("Başarılı", "Soy ağacı 'soy_agaci.png' olarak oluşturuldu.")
        except Exception as e:
            messagebox.showerror("Hata", f"Soy ağacı oluşturulurken bir hata oluştu: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SoyağacıUygulaması(root)
    root.mainloop()
