import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#5da130', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="BD/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="BD/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="BD/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('cod', 'mark', 'sex', 'price', 'kolvo'), height=15, show='headings')

        self.tree.column('cod', width=50, anchor=tk.CENTER)
        self.tree.column('mark', width=180, anchor=tk.CENTER)
        self.tree.column('sex', width=140, anchor=tk.CENTER)
        self.tree.column('price', width=140, anchor=tk.CENTER)
        self.tree.column('kolvo', width=140, anchor=tk.CENTER)

        self.tree.heading('cod', text='ID')
        self.tree.heading('mark', text='Имя игрока')
        self.tree.heading('sex', text='Пол игрока')
        self.tree.heading('price', text='Возраст игрока')
        self.tree.heading('kolvo', text='Результат игрока')

        self.tree.pack()

    def records(self, cod, mark,type, price, kolvo):
        self.db.insert_data(cod, mark,type, price, kolvo)
        self.view_records()

    def update_record(self, cod, mark,type, price, kolvo):
        self.db.cur.execute("""UPDATE users SET cod=?, mark=?,type=?, price=?, kolvo=? WHERE cod=?""",
                            (cod, mark,type, price, kolvo, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE cod=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    # def search_records(self, cod):
    #     cod = ("%" + cod + "%",)
    #     self.db.cur.execute("""SELECT * FROM users WHERE mark LIKE ?""", cod)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, kolvo):
        kolvo = (kolvo,)
        self.db.cur.execute("""SELECT * FROM users WHERE kolvo>?""", kolvo)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=110, y=25)

        label_mark = tk.Label(self, text='Имя')
        label_mark.place(x=50, y=50)
        self.entry_mark = ttk.Entry(self)
        self.entry_mark.place(x=110, y=50)

        label_sex = tk.Label(self, text='Пол')
        label_sex.place(x=50, y=75)
        self.combobox = ttk.Combobox(self, values=[u'Мужской', u'Женский'])
        self.combobox.current(0)
        self.combobox.place(x=110, y=75)

        label_price = tk.Label(self, text='Возраст')
        label_price.place(x=50, y=100)
        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=110, y=100)

        label_kolvo = tk.Label(self, text='Результат')
        label_kolvo.place(x=50, y=125)
        self.entry_kolvo = ttk.Entry(self)
        self.entry_kolvo.place(x=110, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_mark.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_price.get(),
                                                                       self.entry_kolvo.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_mark.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_price.get(),
                                                                          self.entry_kolvo.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('BD/products.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                cod INTEGER PRIMARY KEY AUTOINCREMENT,
                mark TEXT NOT NULL,
               type INTEGER NOT NULL DEFAULT 1,
                price INTEGER,
                kolvo INTEGER
                )""")

    def insert_data(self, cod, mark,type, price, kolvo):
        self.cur.execute("""INSERT INTO users(cod, mark,type, price, kolvo) VALUES (?, ?, ?, ?, ?)""",
                             (cod, mark,type, price, kolvo))
        self.con.commit()

if __mark__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных Сапер")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()