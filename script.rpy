# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define l = Character('Леон', color="#3c00ffe2")

define is_draw = False

init:
    $ left2 = Position(xalign=0.2, yalign=1.0)
    $ right2 = Position(xalign=0.8, yalign=1.0)

# Игра начинается здесь:
label start:
    scene bg brawlforest
    with fade

    transform fade_in:
        alpha 0.0
        linear 3.0 alpha 1.0

    show leon happy at fade_in

    l "{cps=10}Я так долго появляюсь...{/cps}"

    hide leon
    with dissolve
    l "Почему я растворился"
    transform move_and_fade:
        xpos 0
        alpha 0
        linear 2.0 xpos 0.40 alpha 1.0
    show leon happy at move_and_fade
    l "Оуууу, я появляюсь в движении!"
    hide leon
    with dissolve
    transform bounce:
        ypos 0.5
        linear 0.5 ypos 0.6
        linear 0.5 ypos 0.5
        repeat

    show leon happy at bounce
    with dissolve
    l "Ой, я прыгаю"
    l "ЕЕЕЕЕЕЕлки палки, тепрь с паузами прыгаю"
    # xpos, ypos, xzoom, yzoom, alpha, rotate(1-360)
    # linear, ease, easein, easeout






#     $ valid_name = False

#     while not valid_name:
#         $ name =  renpy.input('Введите имя:')

#         if name.isalpha() and len(name) <= 14:
#             $ valid_name = True
#         else:
#             "Имя должно быть буквами и не превышать 14 символов!"

#     scene bg brawlforest
#     with fade
#     show leon happy at left2
#     with dissolve

#     l "Откуда я взялся? может [name] знает?"

#     menu:
#         "Думаю меня нарисовали...":
#             $ is_draw = True
#             jump label1
#         "Или всё же скачали с интернета...":
#             jump label1

# label label1:    
#     "В любом случае, это не так важно"

#     if is_draw:
#         "Хотя стоит задуматся..."
    
#     "Пора двигатся дальше"
    
#     play sound "metel.wav"

#     l "Что за звуки?"

#     l "Нужно срочно бежать"

#     stop sound

#     return