import tkinter as tk
import pygame
import webbrowser
import os
import sys
from PIL import Image, ImageTk

if sys.platform == 'win32':
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
else:
    pygame.mixer.init()

is_playing = False
video_opened = False

video_urls = {
    "z": "https://www.youtube.com/watch?v=AFIqSaZM2D0",
    "x": "https://www.youtube.com/watch?v=5H3rxk_oitA",
    "c": "https://youtu.be/6h5LieoWoa4?si=-jSZN45S-aJcAC4C",
    "v": "https://www.youtube.com/watch?v=3qOMafRtQZ0",
    "b": "https://www.youtube.com/watch?v=fLTjpMOruhI"
}

sounds = {
    "s": "Chiken.mp3",

    "q": "Sigma.mp3",
    "w": "Barabulka.mp3",
    "e": "Trator.mp3",
    "r": "Shark.mp3",
    "t": "CuteBoy.mp3",
}

def play_or_stop_sound(event):
    global current_sound

    key = event.keysym.lower()
    if key in sounds:
        audio_file = os.path.join("assets", sounds[key])

        if os.path.isfile(audio_file):
            try:
                if pygame.mixer.music.get_busy() and current_sound == audio_file:
                    pygame.mixer.music.stop()
                    current_sound = None
                else:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(audio_file)
                    pygame.mixer.music.play()
                    current_sound = audio_file
            except Exception as e:
                print(f"Ошибка при воспроизведении {audio_file}: {e}")
        else:
            print(f"Файл {audio_file} не найден!")


def open_video(event):
    key = event.keysym.lower()

def toggle_audio():
    global is_playing
    try:
        if is_playing:
            pygame.mixer.music.stop()
            is_playing = False
        else:
            audio_file = os.path.join("assets", "Chiken.mp3")
            if os.path.isfile(audio_file):
                pygame.mixer.music.load(audio_file)
                pygame.mixer.music.play()
                is_playing = True
            else:
                print(f"Файл {audio_file} не найден!")
    except Exception as e:
        print(f"Ошибка при воспроизведении аудио: {e}")


def open_video(event):
    key = event.keysym.lower() 
    url = video_urls.get(key)
    if url:
        webbrowser.open(url)
    else:
        print(f"Видео для клавиши '{key}' не найдено.")

questions = {
    (1, 0): [("🦁👑", "Король Лев")],
    (2, 0): [("🚀🤠🦖", "История игрушек")],
    (3, 0): [("🏠🎈👴🏼👦", "Вверх")],
    (4, 0): [("🧞‍♂️🕌🐒", "Аладдин")],
    (5, 0): [("🐉👧⚔️", "Мулан")],

    (1, 1): [("Угадайте Песню Q", "Sigma Boy")],
    (2, 1): [("Угадайте Песню W", "Барабулька")],
    (3, 1): [("Угадайте Песню E", "Синий Трактор")],
    (4, 1): [("Угадайте Песню R", "Baby Shark")],
    (5, 1): [("Угадайте Песню T", "Cute Boy")],

    (1, 3): [("Что носят евреи мужчины на голове?", "Кипа"), ("Что идет раньше: Шаббат или Авдала?", "Шаббат"), ("Сколько хал обычно на шаббатнем столе?", "Две")],
    (2, 3): [("Как называется правильное питание у евреев?", "Кошрут"), ("Кто взрослеет раньше, мальчики или девочки?", "Девочки"), ("Как звали жену Адама?", "Ева")],
    (3, 3): [("Кто спас всех животных от потопа?", "Ной"), ("Как звали первого человека?", "Адам"), ("Как звали первого еврея?", "Авраам")],
    (4, 3): [("В какой день недели Шаббат?", "В пятницу"), ("Когда проводят авдалу?", "В течение двух дней после Шаббата"), ("Как называется гимн Израиля?", "Хатиква")],
    (5, 3): [("Сколько было колен Израиля?", "12"), ("Какой Еврейский храм был последний?", "Второй Храм, храм Давида"), ("Как звали короля из свитка Эстер, которого сравнивают с индюком?", "Ахашверош")],
    
    (1, 2): [("Как зовут мадрихов нашей команды?", "Ярик, Слава, Соня, Ариана, Роберта, Сима, Бека")],
    (2, 2): [("Заматайте любого участника вашей команды в туалетку на скорость!", "Молодцы!")],
    (3, 2): [("О чем была прошлая программа?", "Ту би Шват")],
    (4, 2): [("Какая команда активнее станцует - получит баллы S", "Молодцы!")],
    (5, 2): [("Сделайте импровизацию Адам, Ева и яблоко, кто-то Адам, кто-то Ева, кто-то яблоко", "Молодцы!")],

    (1, 4): [("z", "")],
    (2, 4): [("x", "")],
    (3, 4): [("c", "")],
    (4, 4): [("v", "")],
    (5, 4): [("b", "")],
}

current_questions = []
question_index = 0
show_answer = False
category_buttons = {}
current_category = None

def emoji_img(size, text):
    try:
        emoji_folder = "assets/emoji_images"
        emoji_path = os.path.join(emoji_folder, f"{text}.png")
        
        if not os.path.exists(emoji_path):
            print(f"Ошибка: файл эмоджи не найден ({emoji_path})")
            return None
        emoji = Image.open(emoji_path)
        width, height = emoji.size
        if width > height:
            new_width = size * 3
            new_height = int((height / width) * new_width)
        else:
            new_height = size * 3
            new_width = int((width / height) * new_height)
        emoji = emoji.resize((new_width, new_height), Image.Resampling.LANCZOS)

        final_image = Image.new("RGBA", (size * 3, size * 3), (255, 255, 255, 0))
        final_image.paste(emoji, ((size * 3 - new_width) // 2, (size * 3 - new_height) // 2))
        return ImageTk.PhotoImage(final_image)

    except Exception as e:
        print(f"Ошибка загрузки эмоджи: {e}")
        return None

def hide_category_buttons(category):
    if category in category_buttons:
        for button in category_buttons[category]:
            button.grid_forget()

def show_next_question(event, popup_window):
    global question_index, show_answer
    if question_index < len(current_questions):
        if show_answer:
            popup_window.label.config(text=f"Ответ: {current_questions[question_index][1]}")
            question_index += 1
        else:
            popup_window.label.config(text=f"Вопрос: {current_questions[question_index][0]}")

            key = current_category
            emoji_text = current_questions[question_index][0]

            if key in [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]:
                emoji_image = emoji_img(100, emoji_text)
                if emoji_image:
                    popup_window.emoji_label.config(image=emoji_image)
                    popup_window.emoji_label.image = emoji_image  

            else:
                popup_window.emoji_label.config(image="")
                popup_window.emoji_label.image = None

        show_answer = not show_answer
    else:
        popup_window.label.config(text="Все вопросы пройдены!")
        hide_category_buttons(current_category)  
        popup_window.after(500, popup_window.destroy)

def on_button_click(row, col, points):
    global current_questions, question_index, show_answer, current_category
    current_category = (row, col)

    if (row, col) in questions:
        current_questions = questions[(row, col)]
        question_index = 0
        show_answer = False

        popup_window = tk.Toplevel()
        popup_window.title(f"Вопросы категории {row},{col}")
        popup_window.geometry("720x1280")

        window_width = 1280
        window_height = 500
        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        popup_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        popup_window.configure(bg="#1E3F66")

        popup_window.emoji_label = tk.Label(popup_window, bg="#1E3F66")
        popup_window.emoji_label.pack(pady=20)

        popup_window.label = tk.Label(popup_window, text=f"Вопрос: {current_questions[question_index][0]}",
                                      font=("Arial", 20), bg="#1E3F66", fg="white")
        popup_window.label.pack(pady=20)

        popup_window.bind("<space>", lambda event, win=popup_window: show_next_question(event, win))

        show_next_question(None, popup_window)

def create_window():
    global label, category_buttons, frame, current_category
    root = tk.Tk()
    root.title("5x5 Grid Window - Marine Style")
    root.geometry("1920x1080")
    root.configure(bg="#1E3F66")
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
                                bg=button_colors[0], fg="#02051a", 
                                font=("Arial", 18, "bold"))
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

            category_buttons[(i, j)] = category_buttons.get((i, j), []) + [btn]

    label = tk.Label(root, text="", font=("Arial", 22), bg="#1E3F66", fg="white")  
    label.pack(pady=20)

    for key in sounds.keys():
        root.bind(f"<{key}>", play_or_stop_sound)

    for key in video_urls.keys():
        root.bind(f"<{key}>", open_video)

    root.bind("<s>", lambda event: toggle_audio())
    
    root.bind("<z>", open_video)
    root.bind("<x>", open_video)
    root.bind("<c>", open_video)
    root.bind("<v>", open_video)
    root.bind("<b>", open_video)

    
    root.mainloop()

if __name__ == "__main__":
    create_window()
