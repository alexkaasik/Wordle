import tkinter as tk
import random

def choose_word():
    with open('wordlist.txt', 'r', encoding='utf-8') as file:
        words = file.readlines()
    return random.choice(words).strip().lower()

def check_guess():
    global current_row
    global current_column
    guess = ''.join(guesses[current_row])
    if guess == secret_word:
        result_label.config(text="Вы угадали слово!")
    else:
        for i, letter in enumerate(guesses[current_row]):
            if letter == secret_word[i]:
                guess_cells[current_row][i].config(bg='green')
            elif letter in secret_word:
                guess_cells[current_row][i].config(bg='yellow')
    current_row += 1
    current_column = 0
    guesses_left_label.config(text="Осталось попыток: {}".format(6 - current_row))

def confirm_guess():
    if current_row < 6:  
        check_guess()
        for i, cell in enumerate(guess_cells[current_row]):
            cell.config(text=guesses[current_row][i])


def clear_guess():
    global current_row
    global current_column
    for row in guess_cells:
        for cell in row:
            cell.config(text='', bg='white')
    current_row = 0
    current_column = 0
    guesses_left_label.config(text="Осталось попыток: {}".format(6))
    result_label.config(text='')

root = tk.Tk()
root.title("Wordle")
root.geometry("600x650")

secret_word = choose_word()
guesses = [[''] * 5 for _ in range(6)]
current_row = 0
current_column = 0


word_display_frame = tk.Frame(root)
word_display_frame.pack(pady=10)
word_display_labels = []
for i in range(len(secret_word)):
    label = tk.Label(word_display_frame, text="", font=("Arial", 20), width=2)
    label.grid(row=0, column=i, padx=5)
    word_display_labels.append(label)

guess_entry_frame = tk.Frame(root)
guess_entry_frame.pack(pady=10)

guess_cells = []
for i in range(6):
    row = []
    for j in range(5):
        cell = tk.Label(guess_entry_frame, text="", font=("Arial", 20), width=2, relief=tk.RIDGE, borderwidth=2, bg='white')
        cell.grid(row=i, column=j, padx=5)
        row.append(cell)
    guess_cells.append(row)

confirm_button = tk.Button(root, text="Подтвердить", command=confirm_guess)
confirm_button.pack()

clear_button = tk.Button(root, text="Очистить", command=clear_guess)
clear_button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

guesses_left_label = tk.Label(root, text="Осталось попыток: {}".format(6))
guesses_left_label.pack()

alphabet_frame = tk.Frame(root)
alphabet_frame.pack(pady=10)
alphabet_rows = ["абвгдеёжзийклм", "нопрстуфхцчшщъ", "ыьэюя"]
alphabet_buttons = {}
for row in alphabet_rows:
    row_frame = tk.Frame(alphabet_frame)
    row_frame.pack()
    for letter in row:
        button = tk.Button(row_frame, text=letter, font=("Arial", 14), width=2, bg='white', command=lambda l=letter: update_cell(l))
        button.pack(side=tk.LEFT, padx=5)
        alphabet_buttons[letter] = button

def update_cell(letter):
    global current_column
    if current_column < 5:
        guess_cells[current_row][current_column].config(text=letter, bg='white')
        guesses[current_row][current_column] = letter
        current_column += 1

root.mainloop()