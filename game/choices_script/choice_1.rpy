label dumb:

 play music "audio/657265__ho52nest__wellcome-supermarket-background-music.ogg"volume 50

 show scene_4
 show scene_3
 show AP1

 ap "Pelo menos estou tentando recuperar o tempo perdido..."
 "Ele pareceu ficar um pouco irritado, mas fez de brincadeira..."
 "Comportamento clássico do Apollo..."
 "Provavelmente a razão pela qual é tão divertido mexer com ele."

 jump continuing

label drama:

 play music "audio/657265__ho52nest__wellcome-supermarket-background-music.ogg"volume 50

 show scene_4
 show scene_3
 show AP1

 ap "Obrigado, minha senhora."
 "Ele se curva dramaticamente para mim antes de começarmos a rir..."
 "A piada é estúpida, mas é sempre divertido brincar quando ele está por perto..."
 
 jump continuing

label mini_game:
    $ randomize_cards()
    call screen memory_mini_game
return
