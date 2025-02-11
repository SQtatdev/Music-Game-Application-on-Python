import tkinter as tk

# Список вопросов и ответов
questions = {
    (1, 3): [
        ("Что носят евреи мужчины на голове?", "Кипа"),
        ("Что идет раньше: Шаббат или Авдала?", "Шаббат"),
        ("Сколько хал обычно на шаббатнем столе?", "Две")
    ],
    (2, 3): [
        ("Как называется правильное питание у евреев?", "Кошрут"),
        ("Кто взрослеет раньше, мальчики или девочки?", "Девочки"),
        ("Как звали жену Адама?", "Ева")
    ],
    (3, 3): [
        ("Кто спас всех животных от потопа?", "Ной"),
        ("Как звали первого человека?", "Адам"),
        ("Как звали первого еврея?", "Авраам")
    ],
    (4, 3): [
        ("В какой день недели Шаббат?", "В пятницу"),
        ("Когда проводят авдалу?", "В течение двух дней после Шаббата"),
        ("Как называется гимн Израиля?", "Хатиква")
    ],
    (5, 3): [
        ("Сколько было колен Израиля?", "12"),
        ("Какой Еврейский храм был последний?", "Второй Храм, храм Давида"),
        ("Как звали короля из свитка Эстер, которого сравнивают с индюком?", "Ахашверош")
    ],
    (1, 2): [
        ("Как зовут мадрихов нашей команды?", "Ярик, Слава, Соня, Ариана, Роберта, Сима, Бека"),
    ],
    (2, 2): [
        ("Заматайте любого участника вашей команды в туалетку на скорость!", "Молодцы!"),
    ],
    (3, 2): [
        ("О чем была прошлая программа?", "Ту би Шват"),
    ],
    (4, 2): [
        ("Какая команда активнее станцует - получит баллы", "Молодцы!"),
    ],
    (5, 2): [
        ("Сделайте импровизацию Адам, Ева и яблоко, кто-то Адам, кто-то Ева, кто-то яблоко", "Молодцы!"),
    ],   
}

# Переменные для текущих вопросов и ответов
current_questions = []
question_index = 0
show_answer = False
category_buttons = {}

def show_next_question(event):
    global question_index, show_answer
    # Проверка, если есть вопросы для отображения
    if question_index < len(current_questions):
        if show_answer:
            label.config(text=f"Ответ: {current_questions[question_index][1]}")
            question_index += 1
        else:
            label.config(text=f"Вопрос: {current_questions[question_index][0]}")
        show_answer = not show_answer
    else:
        label.config(text="Все вопросы пройдены!")
        hide_category_buttons(current_category)  # Прячем кнопки категории, когда все вопросы пройдены

def hide_category_buttons(category):
    # Проверяем, существует ли ключ в category_buttons
    if category in category_buttons:
        for button in category_buttons[category]:
            button.grid_forget()
    else:
        print(f"Ключ {category} не найден в category_buttons!")

def on_button_click(row, col, points):
    global current_questions, question_index, show_answer, current_category
    # Используем кортеж (row, col) для получения правильной категории
    current_category = (row, col)

    # Проверяем, есть ли вопросы в выбранной категории
    if (row, col) in questions:
        current_questions = questions[(row, col)]
        question_index = 0
        show_answer = False
        label.config(text=f"Вопрос: {current_questions[question_index][0]}")
        
    # Если все вопросы пройдены, заменяем кнопку на якорь
    if question_index >= len(current_questions):
        hide_category_buttons(current_category)

def create_window():
    global label, category_buttons, frame, current_category
    root = tk.Tk()
    root.title("5x5 Grid Window - Marine Style")
    root.geometry("1920x1080")
    root.configure(bg="#1E3F66")  # Темно-синий фон
    root.update_idletasks()

    window_width = 1920
    window_height = 1080
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    frame = tk.Frame(root, bg="#1E3F66")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    button_colors = ["#A2D5F2", "#07689F"] 

    headers = ["Пузырьки", "Обратное течение", "Ева с хвостом!", "Адам в океане", "Это мои ноги?"]

    for j in range(5):
        label_header = tk.Label(frame, text=headers[j], width=20, height=4,
                                bg=button_colors[0], fg="#FF7F50", 
                                font=("Arial", 14, "bold"))
        label_header.grid(row=0, column=j, padx=5, pady=5)

    points = [100, 200, 300, 400, 500]  
    for i in range(1, 6): 
        for j in range(5):
            btn_text = f"{points[i-1]}" 
            btn = tk.Button(frame, text=btn_text, width=20, height=4,
                            bg=button_colors[i % 2], fg="white",
                            font=("Arial", 14, "bold"),
                            command=lambda i=i, j=j, points=points[i-1]: on_button_click(i, j, points))
            btn.grid(row=i, column=j, padx=5, pady=5)

            # Добавляем кнопку в словарь
            category_buttons[(i, j)] = category_buttons.get((i, j), []) + [btn]

    label = tk.Label(root, text="", font=("Arial", 22), bg="#1E3F66", fg="white")  
    label.pack(pady=20)
    root.bind("<space>", show_next_question)  

    root.mainloop()

if __name__ == "__main__":
    create_window()
