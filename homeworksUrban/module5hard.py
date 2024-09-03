import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(),16)

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = self.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
            print("Неверное имя пользователя или пароль")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print("Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if any(v.title == video.title for v in self.videos):
                continue
            self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, покиньте страницу")
                    return

            for second in range(video.time_now + 1, video.duration + 1):
                print(second, end=" ")
                time.sleep(1)
            print("Конец видео")
            return

        print("Видео не найдено")


    def hash_pasword(self, pasword):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

















