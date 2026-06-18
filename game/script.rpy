define h = Character("[player_name]")
define hung = Character("Hưng")
define fleiro = Character("Fleiro")

default day = 1
default actions_left = 2
default iq = 80

default hung_friend = 0

######## load sprite
image hungdev normal = "images/character/hungdev/hungdev.png"
image fleiro normal = "images/character/fleiro/fleiro.png"

label start:

    scene black
    with fade
    play music "audio/main.mp3"


    "Oh, chào bạn."
    "Mình là Hưng hay Hungdev, là người tạo ra con game này."
    "Đây chỉ là con game tái hiện 1 Studio trên Scratch lúc năm 2024 - 2025 và nó chưa được hoàn thiện."

    $ player_name = renpy.input("Tên bạn là gì?", length=12)

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Player"

    "Chào [player_name], cùng tiếp tục nhé!"

    play music "audio/realmain.mp3"
    jump main_scene

label main_scene:

    scene bg room
    with dissolve
    image bg room = im.Scale("images/bedroom.jpeg", 1920, 1080)

    h "Hôm nay mình nên làm gì nhỉ?"

    menu:

        "Ra đường":

            scene bg street
            with dissolve
            image bg street = im.Scale("images/street.jpeg", 1920, 1080)

            "Bạn đi dạo ngoài đường..."

            menu:
                "Nói chuyện với Hưng":
                    jump talk_hungdev

                    label talk_hungdev:
                        show hungdev normal:
                            zoom 2
                            yalign 0.6
                            xalign 0.5
                        with dissolve

                        hung "Gì vậy?"

                        menu:
                            "Nói chuyện":
                                hung "Muốn nói gì sao?"
                                menu:
                                    "Tôi muốn tâm sự với bạn.":

                                        hung "Cứ nói đi bro."
                                        "2 người trò chuyện với nhau."
                                        $ hung_friend += 1
                                        "Tăng khả năng thân với nhau."
                                        hung "Ui, tui có chuyện đi rồi, tí nói chuyện tiếp nhé!"
                                    
                                    "Bây giờ là năm bao nhiêu vậy?":
                                        hung "Ông hỏi câu ngớ ngẩn vậy?"
                                        hung "Giờ là Giáng Sinh 2024 chứ gì?"
                                    
                                    "Giúp tôi cài Arch Linux.":
                                        hung "Bro à, hiện giờ tui còn chưa biết cài Arch cơ, tui đang dùng Debian mà bro!"
                                        h "..."
                                    
                                    "Bạn là ai?":
                                        hung "Tui á? Tui là manager của Studio mới gần đây, tui đang có 1 đứa bạn là Cookied á!"
                                    
                            
                            
                            "Không có gì.":
                                hung "Phiền."
                        
                        hide hungdev normal

                        jump main_scene
                
                "Nói chuyện với Fleiro":
                    jump talk_fleiro

                    label talk_fleiro:
                        show fleiro normal:
                            zoom 2
                            yalign 0.6
                            xalign 0.5
                        with dissolve

                        fleiro "Chào :|"

                        hide fleiro normal

                "Về nhà":
                    jump main_scene

            jump main_scene


        "Học tập":

            scene bg study
            with dissolve
            image bg study = im.Scale("images/desk.jpeg", 1920, 1080)

            "Bạn học tập chăm chỉ."

            $ iq += 1
            "IQ của bạn đã được cải thiện."
            

            jump main_scene


        "Đi ngủ":

            jump sleep

label sleep:

    scene black
    with fade

    "Sleepy..."

    $ day += 1
    $ actions_left = 2
    stop music

    "Ngày mới bắt đầu. Ngày  [day]"
    play music "audio/realmain.mp3"

    jump main_scene