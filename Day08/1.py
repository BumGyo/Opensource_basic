from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# 테이블 생성 함수
def create_table():
    con = sqlite3.connect('./test.db')
    cur = con.cursor()
    # 계속 만들면 안되므로 예외 처리
    cur.execute('''CREATE TABLE IF NOT EXISTS userTable (
                    id CHAR(4),
                    username CHAR(15),
                    email CHAR(15),
                    birthYear INT)''')
    con.commit()
    con.close()

# 입력 함수
def insert_data():
    email = entry_id.get() + entry_email.get()
    con = sqlite3.connect('./test.db')
    cur = con.cursor()
    cur.execute("INSERT INTO userTable VALUES (?, ?, ?, ?)",
                (entry_id.get(), entry_name.get(), email, entry_year.get()))
    con.commit()
    con.close()
    messagebox.showinfo("성공", "데이터가 성공적으로 입력되었습니다.")
    display_data()

# 조회 함수
def display_data():
    con = sqlite3.connect('./test.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM userTable")
    rows = cur.fetchall()
    con.close()

    for row in tree.get_children():
        tree.delete(row)

    for row in rows:
        tree.insert("", "end", values=row)

root = Tk()
root.title("GUI 데이터 입력")

# 입력 필드
Label(root, text="사용자ID").grid(row=0, column=0)
Label(root, text="사용자이름").grid(row=0, column=1)
Label(root, text="이메일").grid(row=0, column=2)
Label(root, text="출생년도").grid(row=0, column=3)

entry_id = Entry(root)
entry_id.grid(row=1, column=0)
entry_name = Entry(root)
entry_name.grid(row=1, column=1)
entry_email = Entry(root)
entry_email.grid(row=1, column=2)
entry_year = Entry(root)
entry_year.grid(row=1, column=3)

# 버튼
Button(root, text="입력", command=insert_data).grid(row=1, column=4)
Button(root, text="조회", command=display_data).grid(row=1, column=5)

# 트리뷰 설정
cols = ('사용자ID', '사용자이름', '이메일', '출생년도')
tree = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    tree.heading(col, text=col)
tree.grid(row=2, column=0, columnspan=6)

# 테이블 생성 및 초기 데이터 표시
create_table()
display_data()

# GUI 실행
root.mainloop()