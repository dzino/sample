from PIL import Image
from hashlib import md5
from os import listdir, remove
from datetime import datetime   #часы
from time import sleep


'''#############################################################################
##                                                                            ##
##             @@@@@@ @@@@@@    @@    @@@@@@ @@  @@ @@@@@@ @@@@@@             ##
##             @@     @@  @@   @@@@   @@  @@ @@  @@   @@   @@                 ##
##             @@     @@@@@@  @@  @@  @@@@@@ @@@@@@   @@   @@                 ##
##             @@  @@ @@ @@  @@@@@@@@ @@     @@  @@   @@   @@                 ##
##             @@@@@@ @@  @@ @@    @@ @@     @@  @@ @@@@@@ @@@@@@             ##
##                                                                            ##
##           ФУНКЦИЯ ОБРАБОТКИ СРИНШОТОВ (РАСПОЗНАВАИЕ СЛОВ И ЧИСЕЛ)          ##
#############################################################################'''

def graphic(_im_, test):
    '''
    @@@@@@  @@@@@@ @@@@@@
    @@   @@ @@     @@
    @@   @@ @@@@@@ @@@@@@
    @@   @@ @@     @@
    @@@@@@  @@@@@@ @@'''

    # Сравнение векторов
    class VectorCompare:
        def magnitude(self,concordance):
            total = 0
            for word,count in concordance.iteritems(): total += count ** 2
            return math.sqrt(total)

        def relation(self,concordance1, concordance2):
            relevance = 0
            topvalue = 0
            for word, count in concordance1.iteritems():
                if concordance2.has_key(word):
                    topvalue += count * concordance2[word]
            return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


    # Функция РАЗМЕТКИ знаков
    def border(imm, list_):
        inletter = False
        foundletter = False
        start = 0
        end = 0
        for y in range(im2.size[0]):
            for x in range(im2.size[1]):
                pix = im2.getpixel((y,x))
                if pix != 255: inletter = True
            if foundletter == False and inletter == True:
                foundletter = True
                start = y
            if foundletter == True and inletter == False:
                foundletter = False
                end = y
                list_.append((start,end))
            inletter=False

    # обрезка по высоте
    def border_(imm):
        inletter = False
        foundletter = False
        start = 0
        end = 0
        for y in range(im2.size[1]):
            for x in range(im2.size[0]):
                pix = im2.getpixel((x,y))
                if pix != 255: inletter = True
            if foundletter == False and inletter == True:
                foundletter = True
                start = y
            if foundletter == True and inletter == False:
                foundletter = False
                end = y
                return (start,end)
            inletter=False


    '''
    @@@@@@  @@@@@@ @@@@@@       @@@@@@ @@@@@@ @@     @@ ФУНКЦИЯ
    @@   @@ @@     @@           @@     @@  @@ @@@   @@@ СРАВНЕНИЯ
    @@   @@ @@@@@@ @@@@@@       @@     @@  @@ @@ @@@ @@
    @@   @@ @@     @@           @@     @@  @@ @@  @  @@
    @@@@@@  @@@@@@ @@     @@@@@ @@@@@@ @@@@@@ @@     @@ '''

    # распознавание каждого знака
    guess = []
    def character_recognition(imageset,guess):
        for image in imageset:
            im3_save = 'screen' + str(count)+".gif"                     # имя временного файла
            im3.save(im3_save)                                          # сохранить полученные символы во временный файл (без сохранения происходила ошибка)
            sleep(0.02)
            com = comparison(im3_save, image, 80, imageset[image])      # ФУНКЦИЯ СРАВНЕНИЯ
            guess.append(com)                                           # знаки прошедшие распознание, добавить в guess

    # Функция СРАВНЕНИЯ
    def comparison(Image_1, Image_2, match_percentage, letter):

        w = 0                                               # переменная ширины
        h = 0                                               # переменная высоты
        def measurement(Imag):                              # замер
            im = Image.open(Imag)
            (width, height) = im.size
            nonlocal w
            w = width
            nonlocal h
            h = height
            im.close()

        list_1 = []                                         # список цветов
        list_2 = []                                         # список цеветов
        stop = 0
        def Image_pixel(Imag, list, a, b):                  # цевета пикселей
            im = Image.open(Imag)
            (width, height) = im.size
            max_w = max(w1, w2)
            max_h = max(h1, h2)
            min_w = min(w1, w2)
            min_h = min(h1, h2)
            w_w = (max_w - min_w) / 2                       # расчет отступа по ширине (обрезка по центру)
            h_h = (max_h - min_h) / 2                       # расчет отступа по высоте (обрезка по центру)
            if min_w/max_w >= 0.5:                                  # если изображения отличаются размером болееб чем в 2 раза - не сравнивать
                for wid in range(min_w):
                    if a == max_w: wid = wid + w_w
                    else: wid = wid

                    for hei in range(min_h):
                        if b == max_h: hei = hei + h_h
                        else: hei = hei

                        im_getpixel = str(im.getpixel((wid, hei)))  # получаем цвет пикселя
                        for ig in im_getpixel: list.append(ig)
            else:                                                   # команда остановить процесс
                nonlocal stop
                stop += 1
            im.close()

        measurement(Image_1)                                # замер изображения
        w1 = w
        h1 = h
        measurement(Image_2)                                # замер изображения
        w2 = w
        h2 = h
        Image_pixel(Image_1, list_1, w1, h1)                # формирование списка пикселей
        Image_pixel(Image_2, list_2, w2, h2)

        if stop == 0:                                           # если процесс не остановлен
            coincidence = 0                                     # совпадения
            le = min(len(list_1), len(list_2))
            for ran in range(le):
                if list_1[ran] == list_2[ran]: coincidence += 1 # СРАВНЕНИЕ ТОЛЬКО ПО ДВУМ ЦВЕТАМ

            percent = coincidence/(len(list_1)/100)
            list_1.clear()                                      # очистить списки
            list_2.clear()
            if percent >= match_percentage:                     # если процент выше порога
                if percent < 100: percent = '0' + str(percent)  # для сортировки все проценты должны быть трехзначными
                return str(percent) + '  ' + str(letter)
            else: return '0'
        else: return '0'



    '''
       @@    @@    @@    @@    @@     @@  @@ @@@@@@ @@@@@@ @@@@@@ Разбивание
      @@@@   @@@   @@   @@@@   @@     @@  @@ @@       @@   @@     на знаки
     @@  @@  @@@@@ @@  @@  @@  @@      @@@@  @@@@@@   @@   @@@@@@ и их
    @@@@@@@@ @@  @@@@ @@@@@@@@ @@       @@       @@   @@       @@ значение
    @@    @@ @@   @@@ @@    @@ @@@@@@   @@   @@@@@@ @@@@@@ @@@@@@ '''


    # Запус шаблонов
    v = VectorCompare()
    iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    imageset = {}
    for letter in iconset:
        for img in listdir('./iconset/%s/'%(letter)):
            if img != "Thumbs.db":                                  # windows папка...
                imageset['./iconset/%s/%s'%(letter, img)] = letter  # адрес:зачение


    # ОТСЕИВАЕМ по цветам
    im = Image.open(_im_)
    im2 = Image.new("P",im.size,255)
    im = im.convert("P")
    temp = {}
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y,x))
            temp[pix] = pix
            if pix == 139 or pix == 69 or pix == 68 or pix == 61 or pix == 96 or pix == 67 or pix == 75:   # цвет текста
                im2.putpixel((y,x),0)


    # РАЗМЕТКА-МАСШТАБИРОВАНИЕ-РАЗМЕТКА

    letter_ = border_(im2)                                       # разметка по высоте
    m = md5()
    im2 = im2.crop(( 0 , letter_[0], im2.size[0], letter_[1] ))  # обрезка по высоте

    letters = []                    # первая разметка
    letters2 = []                   # разметка в масштабе
    border(im2, letters)            # первая разметка
    let = []
    for letter in letters:          # заготовка для нахождения мак высоты
        let.append(im2.size[1])
    working_height = 40             # высота обработки
    wn = working_height / max(let)  # определение множителя
    wn0 = int(im2.size[0]*wn)
    wn1 = int(im2.size[1]*wn)
    im2 = im2.resize( (wn0, wn1) )  # масштабирование изображения
    border(im2, letters2)           # разметка в масштабе


    # ПОСИМВОЛЬНАЯ обрезка

    finish = []                                                         # финальный список процент-значение
    count = 0                                                           # счетчик циклов
    for letter in letters2:
        m = md5()
        im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
        character_recognition(imageset,guess)                           # распознавание каждого знака
        guess.sort(reverse=True)                                        # фильтр большего значения
        if guess[0] != '0': finish.append(guess[0])                     # если знак распознан # добавить в finish (процент-значение)
        count += 1                                                      # счетчик циклов

    finish_word = ''                                                    # финальное слово (число)
    for f in finish: finish_word = finish_word + str(f[-1])             # извлечь значения из списка и добавить их в финальное слово
    return finish_word                                                  #

#abcd = graphic("c3.gif", 0)                                             # адрес скриншота || 1 - тестовый режим
#print(abcd)
