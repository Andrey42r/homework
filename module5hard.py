from time import sleep


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname  #имя
        self.password = hash(password)  #пароль
        self.age = age  #возраст


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title  #заголовок
        self.duration = duration  #продолжительность видео в секундах
        self.time_now = 0  #секунда остановки, изначально равна нулю
        self.adult_mode = adult_mode  #ограничение по возрасту, изначально False


class UrTube:
    def __init__(self):
        self.users = []  #список пользователей
        self.videos = []  #список видео
        self.current_user = None  #текущий пользователь

    def log_in(self, nickname: str, password: str, current_user):
        for user in self.users:  #перебираем пользователей в списке self.users
            if nickname == user.nickname and password == user.password:  #сравниваем ники и пароли в UrTube и User
                self.current_user = user  #при совпадении ника и пароля текущий пользователь меняется меняется на user

    def register(self, nickname: str, password: str, age: int):
        password = hash(password)  #Хешируем пароль, значит его нельзя изменить
        for user in self.users:  #перебираем пользователей в списке self.users
            if nickname == user.nickname:  #если ник существует - пишем что пользователь уже зарегистрирован
                print(f'Пользователь {nickname} уже зарегистрирован!')
                return
        new_user = User(nickname, password, age)  #новый пользователь
        self.users.append(new_user)  #добавляем нового пользователя в список self.users
        self.current_user = new_user  #текущий пользователь меняется на new_user
        print(f'Пользователь {nickname} зарегистрирован!')

    def log_out(self):
        self.current_user = None  #метод, скидывающий текущего пользователя

    def add(self, *args):
        for movie in args:  #перебираем видео в бесконечном списке
            if movie not in self.videos:  #если видео нет в self.videos, то добавляем его в список
                self.videos.append(movie)


    def get_videos(self, search_keyword):
        list_film = []
        for video in self.videos:
            if search_keyword.upper() in video.title.upper():
                list_film.append(video.title)
        return list_film

    def watch_video(self, videos_title):
        if self.current_user is None:  #если текущий пользователь None, то видео не запускается
            print('Для просмотра видео нужно авторизироваться!')
            return

        found_video = None  #текущее видео
        for video in self.videos:  #перебираем видео в списке self.videos
            if video.title.lower() == videos_title.lower():  #проверяем точное совпадение заголовка
                found_video = video  #если заголовок совпал то текущее видео меняется на video

        if found_video:  #если заголовок совпал, проверяем возраст
            if self.current_user.age < 18 and found_video.adult_mode:  #проверяем возраст юзера, должен быть 18+
                print('Вам нет 18-ти лет, пожалуйста покиньте страницу')
                return


            for i in range(video.duration):
                print(f'{i + 1}', end='-')
                sleep(1)
                video.time_now += 1
            video.time_now = 0
            print('Конец видео')
            sleep(2)
        # else:
        #     print('Видео не найдено')


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
