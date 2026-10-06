# 1. Создаём три набора слов
positive_words = ['хороший', 'отличный', 'быстрый', 'красивый', 'нравится', 'супер']
negative_words = ['плохой', 'медленный', 'ужасный', 'ломается', 'греется', 'дорогой']
neutral_words = ['экран', 'батарея', 'камера', 'память', 'процессор', 'корпус']

# 2. Функция анализа отзыва
def analyze_review(text):
    # Переводим в нижний регистр
    text = text.lower()
    
    # Убираем знаки препинания (заменяем на пустоту)
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace('-', '')
    
    # Делим текст на слова
    words = text.split()
    
    # Создаём пустые списки для результатов
    positive = []
    negative = []
    neutral = []
    
    # Проверяем каждое слово
    for word in words:
        if word in positive_words:
            positive.append(word)
        elif word in negative_words:
            negative.append(word)
        elif word in neutral_words:
            neutral.append(word)
    
    # Считаем количество
    pos_count = len(positive)
    neg_count = len(negative)
    
    # Определяем общую оценку
    if pos_count == 0 and neg_count == 0:
        overall = "Нейтральный отзыв"
    elif pos_count > neg_count:
        overall = "Положительный отзыв"
    elif neg_count > pos_count:
        overall = "Отрицательный отзыв"
    else:
        overall = "Смешанный отзыв"
    
    # Выводим результат
    print("Положительные характеристики:", positive)
    print("Отрицательные характеристики:", negative)
    print("Нейтральные характеристики:", neutral)
    print("Общая оценка:", overall)

# 3. Главная часть — ввод отзывов
print("Введите отзыв (или 'выход' для завершения):")

while True:
    review = input("Отзыв: ")
    if review == 'выход':
        break
    analyze_review(review)
    print("-" * 40)