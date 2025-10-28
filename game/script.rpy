# The Weight Of Whispers

# DEFINE CHARACTERS
define rk = Character("Raka", color="#00b7ff", what_cps=30)
define ar = Character("Arya", color="#00b7ff")
define n = Character(None, color="#dddddd")

define rk_in   = Character("Raka", color="#aaaaaa")
define i    = Character("Perkataan Ibu", color="#aaaaaa")
define bis = Character("Bisikan", color="#aaaaaa")

define vdiss = Dissolve(0.5)

# DEFINE MUSICS
define calm_p = "Calm Piano.wav"
define sad_p = "Sad Piano.wav"
define happy_p = "Happy Piano.wav"

# DEFINE IMAGES
image raka_happy   = "images/Characters/Raka Happy.png"
image raka_sad     = "images/Characters/Raka Sad.png"
image raka_neutral = "images/Characters/Raka Neutral.png"
image raka_neutral_flipped = "images/Characters/Raka Neutral (Flipped).png"
image raka_sad_grey = im.MatrixColor("images/Characters/Raka Sad.png", im.matrix.desaturate())
image raka_sad_grey_flipped = im.MatrixColor("images/Characters/Raka Neutral (Flipped).png", im.matrix.desaturate())

image arya_neutral  = "images/Characters/Arya Neutral.png"
image arya_happy = "images/Characters/Arya Happy.png"

image bg_parking    = "images/Backgrounds/Parking.jpg"
image bg_classroom  = "images/Backgrounds/Classroom.jpg"
image bg_house      = "images/Backgrounds/House.png"
image bg_basketball = "images/Backgrounds/Basketball.jpg"

 
# SCRIPT GAMEPLAY
label start:
    stop music fadeout 1.0
    jump scene_1

label scene_1:
    play music calm_p fadein 1.0
    scene bg_house with vdiss

    n "Di rumah ini, Raka adalah Raka. Dikelilingi kasih. Tapi di balik senyum tenangnya, sebuah pertanyaan terus berputar."

    show raka_neutral at left with vdiss
    rk "Aku... harus buktikan... bahwa aku bisa."

    show raka_neutral:
        linear 0.5 xoffset 200
    n "Ibunya masuk, membawakan teh, menatapnya dengan tatapan yang Raka kenali... campuran antara cemas dan bangga."

    hide raka_neutral with vdiss
    show raka_sad_grey at center with vdiss:
        xoffset -460
    rk_in "Mengingat percakapan tadi pagi 'Aku sudah putuskan, Bu. Aku mau masuk SMA Negeri 5. Sekolah umum.'"

    show raka_sad_grey:
        linear 0.5 xoffset -345
    rk_in "Aku harus tahu. Apa aku bisa diterima... apa aku pantas bahagia seperti orang lain?"

    show raka_sad_grey:
        linear 0.5 xoffset -230
    n "Raka teringat jawaban ibunya. Kata-kata yang selalu jadi pegangannya."

    show raka_sad_grey:
        linear 0.5 xoffset -115
    n "Ingat, kamu bukan kurang, Raka. Kamu hanya berbeda cara melangkahnya."

    show raka_sad_grey:
        linear 0.5 xoffset 0
    rk_in "Aku memegang kata-kata itu erat-erat."

    show raka_sad_grey at center
    hide raka_sad_grey with vdiss
    show raka_sad at center with vdiss
    n "Kata-kata itu memberinya kekuatan, sekaligus pertanyaan baru..."

    rk "Haruskah Aku..."
    show raka_sad:
        linear 0.5 yoffset 170

    menu:
        "Pembuktian diri.":
            stop music fadeout 1.0
            play music happy_p fadein 1.0
            hide raka_sad with vdiss
            show raka_happy with vdiss:
                yoffset 170
            show raka_happy:
                linear 0.5 yoffset 0
            rk "Aku harus buktikan pada mereka... dan pada diriku sendiri... bahwa aku bisa."
            show raka_happy:
                linear 0.5 xoffset 200
            n "Tekadnya mengeras. Ini adalah tentang pembuktian."
            jump scene_1_end
        "Penerimaan.":
            stop music fadeout 1.0
            play music sad_p fadein 1.0
            show raka_sad:
                linear 0.5 yoffset 0
            rk "Aku hanya ingin... merasakan jadi bagian dari mereka. Diterima apa adanya."
            show raka_sad:
                linear 0.5 xoffset 200
            n "Hatinya berdesir. Ini adalah tentang penerimaan."
            jump scene_1_end

label scene_1_end:
    hide raka_sad with vdiss
    stop music fadeout 1.0
    jump scene_2

# SCENE 2

label scene_2:
    play music calm_p fadein 1.0
    scene bg_parking with vdiss

    n "Hari pertama di SMA Negeri 5. Area parkir itu terasa ramai, penuh tawa dan derap langkah yang asing."

    show raka_neutral at center with vdiss
    n "Raka sudah menduga akan ada tatapan. Tatapan kasihan, tatapan penasaran."
    show raka_neutral:
        linear 0.5 xoffset 200
    n "Seorang guru menghampirinya dengan wajah serba salah, menjelaskan bahwa kelasnya, 10-B, ada di lantai dua. Dan tidak ada lift atau jalur landai."

    hide raka_neutral with vdiss
    show raka_sad_grey with vdiss:
        xoffset 850
    rk_in "Sudah kuduga. Ini akan terjadi. Tantangan pertamaku."

    hide raka_sad_grey with vdiss
    show raka_neutral with vdiss:
        xoffset 850
    n "Siswa-siswa lain hanya melihat sekilas. Beberapa berbisik, lalu lanjut berjalan, termasuk ketua kelas, Dimas, dan siswi pintar, Nisa. Mereka ragu, tidak menolak, tapi juga tidak mendekat."

    show arya_neutral at left with vdiss
    ar "Woi! Mau ke kelas? 10-B kan? Bareng aja!"

    hide raka_neutral with vdiss
    show raka_neutral_flipped with vdiss:
        xoffset 850
    rk "Eh? Nggak usah, nanti repot..."

    show arya_neutral:
        linear 0.5 xoffset 200
    ar "Repot apaan? Kaki kamu boleh beda, tapi tanganmu kuat, kan? Pegangan! Kita ke atas!"

    hide raka_neutral_flipped with vdiss
    show raka_neutral with vdiss:
        xoffset 850
    
    show arya_neutral:
        linear 0.5 xoffset 400
    n "Arya sudah memegang pegangan kursi roda Raka, siap mendorong."
    show arya_neutral:
        linear 0.5 xoffset 400 yoffset 170
    show raka_neutral:
        linear 0.5 xoffset 850 yoffset 170

    menu:
        "Pegang erat-erat.":
            stop music fadeout 1.0
            play music happy_p fadein 1.0
            hide raka_neutral with vdiss
            hide arya_neutral with vdiss
            show raka_happy with vdiss:
                xoffset 200 yoffset 170
            show arya_happy with vdiss:
                xoffset 400 yoffset 170

            show raka_happy:
                linear 0.5 xoffset 200 yoffset 0
            show arya_happy:
                linear 0.5 xoffset 400 yoffset 0

            rk "Aku... aku percaya padanya."

            show raka_happy:
                linear 0.5 xoffset 400
            show arya_happy:
                linear 0.5 xoffset 600
            n "Raka mencengkeram erat sandaran tangannya. Jantungnya berdebar, tapi ini langkah pertamanya."
            jump scene_2_end

        "Menolak dengan halus.":
            stop music fadeout 1.0
            play music sad_p fadein 1.0 
            show raka_neutral:
                linear 0.5 xoffset 850 yoffset 0
            show arya_neutral:
                linear 0.5 xoffset 400 yoffset 0
            rk "T-tunggu! Aku bisa minta tolong guru saja..."
            ar "Halah, keburu bel! Udah ayo!"

            show raka_neutral:
                linear 0.5 xoffset 1050 yoffset 0
            show arya_neutral:
                linear 0.5 xoffset 600 yoffset 0
            n "Arya tidak memberinya pilihan lain dan langsung mendorongnya."
            jump scene_2_end

label scene_2_end:
    stop music fadeout 1.0
    jump scene_3

# SCENE 3

label scene_3:
    play music calm_p fadein 1.0
    scene bg_classroom with vdiss

    n "Setiap pagi, Arya atau satpam sekolah membantunya naik. Tapi 'bantuan' itu punya harga."

    show raka_sad at center with vdiss
    n "Di dalam kelas, Raka mulai mendengar suara-suara yang tak pernah ditujukan langsung padanya, tapi cukup keras untuk menembus telinga."

    hide raka_sad with vdiss
    show raka_sad_grey at center with vdiss
    bis "Kasihan banget, ya."
    hide raka_sad_grey with vdiss
    show raka_sad_grey_flipped with vdiss
    bis "Kenapa sih sekolah nggak kasih dia kelas di bawah aja?"
    hide raka_sad_grey_flipped with vdiss
    show raka_sad_grey with vdiss
    bis "Jadi ribet, deh. Kita nggak bisa cepet-cepet pulang kalau mau bantu dia."

    hide raka_sad_grey with vdiss
    show raka_sad with vdiss
    n "Raka mencoba mencari dukungan dari ketua kelas, Dimas. Tapi dia pura-pura sibuk, menghindari tatapan Raka."
    rk "Aku ingin diterima, bukan dikasihani... Tapi bahkan dia pun mulai menjauh."

    show raka_sad at center with vdiss
    n "Bisikan itu terasa lebih menusuk daripada tatapan kasihan."
    show raka_sad:
        linear 0.5 yoffset 170

    menu:
        "Fokus pada pelajaran.":
            stop music fadeout 1.0
            play music happy_p fadein 1.0 
            hide raka_sad with vdiss
            show raka_happy with vdiss:
                yoffset 170
            show raka_happy:
                linear 0.5 yoffset 0
            rk "Aku di sini untuk belajar. Bukan untuk mendengarkan mereka."
            n "Raka menunduk lebih dalam, memaksa dirinya untuk fokus pada buku di depannya."
            jump scene_3_end
        "Mencari Arya.":
            stop music fadeout 1.0
            play music sad_p fadein 1.0 
            show raka_sad:
                linear 0.5 yoffset 0
            rk "Di mana Arya? Setidaknya dia..."
            show raka_sad:
                linear 0.5 xoffset 200
            n "Raka mengedarkan pandangannya, tapi bangku Arya hari ini kosong."
            hide raka_sad with vdiss
            show raka_sad_grey with vdiss:
                xoffset 850
            n "Dia benar-benar sendirian."
            jump scene_4_end

label scene_3_end:
    rk_in "Ini... mungkin akan menjadi awal yang baik."
    stop music fadeout 1.0

    n "Bersambung..."

    return

label scene_4_end:
    rk_in "Ini... akan jauh lebih sulit dari yang kubayangkan."
    stop music fadeout 1.0

    n "Bersambung..."

    return
