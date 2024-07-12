import time


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname  #имя
        self.password = password  #пароль
        self.age = age  #возраст


class Video:
    title: str

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title  #заголовок
        self.duration = duration  #продолжительность (сек)
        self.time_now = 0  #секунда остановки (изначально 0)
        self.adult_mode = adult_mode  #ограничение по возрасту (по умолчанию False)

    def __eq__(self, other):
        return self.title == other.title

    # def __contains__(self, item):
    #     return item if self.title

class UrTube:
    def __init__(self):
        self.users = []  #список объектов User
        self.videos = []  #список объектов Video
        self.current_user = None  #текущий пользователь

    def log_in(self, login: str, password: str, current_user):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user


    def register(self, nickname: str, password: str, age: int):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, search_keyword):
        keyword_lower = search_keyword.lower()
        matching_videos = [video.title for video in self.videos if keyword_lower in video.title.lower()]
        print(matching_videos)
        return matching_videos

    def watch_video(self, video_title):
        if self.current_user is None:
            print('Войдите в аккаунт чтобы смотреть видео')
            return

        found_video = None
        for video in self.videos:
            if video.title.lower() == video_title.lower():
                found_video = video

        if found_video:
            if self.current_user.age < 18 and found_video.adult_mode:
                print('Вам нет 18-ти, пожалуйста покиньте страницу')
                return

            print(f'Просмотр видео {found_video.title}', found_video.duration)
            for second in range(0, found_video.duration):
                found_video.time_now = second
                print(f'Просмотр на {found_video.time_now} секунде')
                # t.sleep(1)
            print('Конец просмотра')
            found_video.time_now = 0
        else:
            print('Видео не найдено')

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