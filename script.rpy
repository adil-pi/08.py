# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define m = Character('Мафия', color="#00ff00")
define s = Character('Убийца', color="#ff0000")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg dark-forest
    with fade

    show spiderman happy at left
    with dissolve


    s "даже в темном лесу мне весело!"

# hide spiderman

    s "Куда же мне пойти дальше?"

    hide spiderman
    with dissolve

    show mafia angry
    with dissolve

    m "Где этот паук я его убью!"

    hide mafia
    with dissolve

    show spiderman happy at left 
    with dissolve

    s "о нет там мафия, мне нужно найти место для укрытия и найти как то оружие"






    s "наконец то я нашел место где спрятатся"

    hide spiderman
    with dissolve

    show mafia angry
    with dissolve

    m "вот блин я почти догнал паука"

    menu:
        "Остатся в лесу":
            jump forest

        "Пойти в город":
            jump city

label forest:
    "..."

    "Персонаж остался в лесу"

    return

label city:

    scene bg city2
    with fade

    "А вот и город..."

    return
