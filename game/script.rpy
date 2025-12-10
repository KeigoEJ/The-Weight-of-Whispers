# ==========================================
# 1. SETUP & DEFINITIONS
# ==========================================

# --- CHARACTERS ---
# Main Duo
define rk = Character("Raka", color="#00b7ff", what_cps=30)
define ar = Character("Arya", color="#ff9933")

# Friends & Allies
define dm = Character("Dimas", color="#33cc33") # Green for balance
define ns = Character("Nisa", color="#cc99ff")  # Purple for quiet strength

# PERBAIKAN 1: Mengubah 'ibu' menjadi 'i' agar cocok dengan dialog di Scene 3
define i = Character("Ibu", color="#ffcc00")    # Warm Yellow
define ayah = Character("Ayah (Surat)", color="#666666") # Grey/Ghostly
define bl = Character("Bu Lina", color="#aaaaaa")
define pg = Character("Pak Guntur", color="#aaaaaa")

# Antagonists (Orion Group)
define rn = Character("Reno", color="#cc0000") # Red for aggression
define dt = Character("Dita", color="#ff66b2") # Pink for fake sweetness
define yg = Character("Yogi", color="#990000") # Dark Red

# Narrative / Internal
define n = Character(None, color="#dddddd")
define rk_in = Character("Raka (Batin)", color="#aaaaaa") 
define bis = Character("Bisikan", color="#aaaaaa")

# --- TRANSITIONS & AUDIO ---
define vdiss = Dissolve(0.5)

define calm_p = "Calm Piano.wav"
define sad_p = "Sad Piano.wav"
define happy_p = "Happy Piano.wav"
define tension_m = "Tension Piano.wav"

# --- IMAGES ---
# PERBAIKAN 2: Menggunakan spasi (Tagging) agar gambar otomatis terganti (tidak menumpuk)

# Raka
image raka happy   = "images/Characters/Raka Happy.png"
image raka sad     = "images/Characters/Raka Sad.png"
image raka neutral = "images/Characters/Raka Neutral.png"
image raka neutral_flipped = "images/Characters/Raka Neutral (Flipped).png"
# Ini memperbaiki masalah gambar hantu. Karena tag-nya sama ("raka"), 
# saat 'raka grey' muncul, 'raka sad' otomatis hilang.
image raka grey = im.MatrixColor("images/Characters/Raka Sad.png", im.matrix.desaturate())

# Arya
image arya neutral = "images/Characters/Arya Neutral.png"
image arya happy   = "images/Characters/Arya Happy.png"
image arya sad     = "images/Characters/Arya Sad.png" 
image arya angry   = "images/Characters/Arya Angry.png" 

# Dimas
image dimas neutral = "images/Characters/Dimas Neutral.png"
image dimas worried = "images/Characters/Dimas Worried.png" 
image dimas angry   = "images/Characters/Dimas Angry.png"

# Nisa
image nisa neutral = "images/Characters/Nisa Neutral.png"
image nisa shy     = "images/Characters/Nisa Shy.png" # Fallback
image nisa brave   = "images/Characters/Nisa Brave.png" # Fallback

# Antagonists
image reno smirk   = "images/Characters/Reno Smirk.png" # Fallback
image reno angry   = "images/Characters/Reno Angrypng" # Fallback
image dita smile   = "images/Characters/Dita Smile.png" # Fallback
image yogi laugh   = "images/Characters/Yogi Laugh.png" # Fallback

# Backgrounds
image bg parking    = "images/Backgrounds/Parking.jpg"
image bg classroom  = "images/Backgrounds/Classroom.jpg"
image bg house      = "images/Backgrounds/House.png"
image bg house_room = "images/Backgrounds/House.png" # Placeholder for Raka's room
image bg basketball = "images/Backgrounds/Basketball.jpg"
image bg corridor   = "images/Backgrounds/Corridor.jpg" 
image bg stairs     = "images/Backgrounds/Stairs.jpg" 
image bg festival   = "images/Backgrounds/Basketball.jpg" # Placeholder

# --- VARIABLES ---
default a2_points = 0
default b3_points = 0


# ==========================================
# 2. STORY SCRIPT
# ==========================================

label start:
    stop music fadeout 1.0
    $ a2_points = 0
    $ b3_points = 0
    jump scene_1

# ---------------------------------------------------------
# BAB 1: HARI PERTAMA (First Day)
# ---------------------------------------------------------
label scene_1:
    play music calm_p fadein 1.0
    scene bg parking with vdiss

    n "Hari pertama SMA. Buat banyak orang, ini hari penuh harapan."
    
    # Raka enters from left (Slide in)
    # Perhatikan: nama gambar sekarang menggunakan spasi
    show raka neutral with vdiss:
        xalign 0.5 xoffset -300
        linear 0.5 xoffset 0
        
    n "Tapi bagi Raka, yang datang dengan kursi roda, semuanya terasa terlalu besar dan bising."

    rk_in "Kalau aku nggak kuat naik? Kalau aku bikin orang lain repot? Apa aku salah pilih sekolah?"
    
    # Subtle shake/doubt animation
    show raka neutral:
        linear 0.1 xoffset -5
        linear 0.1 xoffset 5
        linear 0.1 xoffset 0

    rk "Tidak. Aku mau coba dulu."

    n "Bu Lina muncul, menatap tangga dengan raut khawatir. Menyarankan pindah ke bawah, tapi Raka menolak halus."
    
    # Arya enters dynamically
    show arya happy with vdiss:
        xalign 1.0 xoffset 300
        linear 0.5 xoffset -100

    ar "Bro! Ayo, kita angkat kursi rodanya bareng. Nggak berat kok."

    n "Ucapan dan gesturnya begitu natural. Dua siswa lain, Dimas dan Nisa, ikut membantu."
    
    # Transition to Class
    scene bg classroom with vdiss
    
    # Group Shot Setup
    show arya neutral at left
    show raka neutral at center
    show dimas neutral at right
    with vdiss

    ar "Selamat datang di 10-B, Rak! Jujur, kamu keren, sih."
    rk "Keren?"
    
    # Arya leans in
    show arya neutral:
        linear 0.3 xoffset 50
    ar "Kamu datang dengan kursi roda, tetap mau sekolah di sini. Itu mental tembok, bro."
    
    rk_in "Kata-kata itu sederhana, tapi menenangkan."
    
    # Nisa enters shyly
    hide dimas
    show nisa shy with vdiss:
        xalign 0.9 xoffset 100
        linear 0.5 xoffset -50
    
    n "Kelompok terbentuk: Arya, Raka, Dimas, dan Nisa. Raka merasa diterima."
    
    jump scene_2

# ---------------------------------------------------------
# BAB 2: HARI PENUH TATAPAN (The Bullying)
# ---------------------------------------------------------
label scene_2:
    stop music fadeout 1.0
    play music sad_p fadein 1.0
    scene bg corridor with vdiss

    n "Namun, hari-hari berikutnya tidak seindah itu. Komentar orang mulai menusuk."
    
    # The Bullies Slide In
    show reno smirk at center with vdiss:
        yoffset -50
        linear 0.5 yoffset 0
    show dita smile at left with vdiss:
        xoffset -100
        linear 0.5 xoffset 0
    show yogi laugh at right with vdiss:
        xoffset 100
        linear 0.5 xoffset 0
    
    rn "Rak, minta sekolah bikin lift pribadi dong. Kita ikut nebeng."
    dt "Atau jangan-jangan kamu jatuh biar dikasih perhatian?"
    
    # Arya slides in to defend, pushing Reno aside visually
    hide dita
    hide yogi
    show reno smirk:
        linear 0.3 xoffset 300
    
    show arya angry at left with vdiss:
        xoffset -300
        linear 0.3 xoffset 0

    ar "Hati-hati, Ra. Terlalu dekat sama dia, kamu ikut dianggap beban."
    
    # Arya steps forward
    show arya angry:
        linear 0.2 xoffset 50
    ar "Kalau itu harga yang harus aku bayar, aku bayar."

    hide reno with vdiss
    hide arya with vdiss
    
    # Raka Alone
    show raka sad at center with vdiss
    rk_in "Apa kehadiranku bikin hidup Arya susah?"

    # The Breakup Scene at Stairs
    scene bg stairs with vdiss
    show raka sad at left
    show arya neutral at right
    
    rk "Arya... kamu nggak capek?"
    ar "Capek? Enggak lah."
    
    # Raka looks away
    # PERBAIKAN PENTING:
    # Karena kita pakai tag "raka sad" dan sekarang "raka grey",
    # Ren'Py akan otomatis mengganti gambar sad dengan grey tanpa menumpuk.
    show raka grey:
        linear 0.5 xoffset -50
    rk "Beberapa hari ke depan... biar aku coba sendiri dulu. Biar kamu nggak makin dijauhi."

    n "Keputusan Raka mengubah segalanya."

    jump scene_3

# ---------------------------------------------------------
# BAB 3: SURAT DARI RUMAH (The Letter)
# ---------------------------------------------------------
label scene_3:
    scene bg house with vdiss
    play music calm_p fadein 1.0
    
    show raka sad at center with vdiss
    
    rk "Bu... Kalau aku... nggak kuat... gimana?"
    
    # Ibu Voice (Variable 'i' sekarang sudah didefinisikan)
    i "Nak... kamu tidak harus kuat setiap hari. Ibu menemukan ini di lemari."
    
    # Visual Effect: Desaturate world while reading letter
    # Hide eksplisit disini aman, tapi tag system juga akan menanganinya
    show raka grey at center with vdiss:
        zoom 1.1
    
    n "Surat dari Ayah."
    
    ayah "Untuk Raka, anakku... Kamu bukan beban. Kamu bukan kesalahan."
    ayah "Dunia kadang mengukur orang dari kaki yang melangkah, padahal yang paling penting adalah hati yang bertahan."
    
    # Zoom back out
    show raka grey:
        linear 1.0 zoom 1.0
    
    rk_in "Ayah..."
    
    jump scene_4

# ---------------------------------------------------------
# BAB 4: RETAKAN (Sports Field Incident)
# ---------------------------------------------------------
label scene_4:
    stop music fadeout 0.5
    play music tension_m fadein 0.5
    scene bg basketball with vdiss
    
    n "Pelajaran olahraga. Raka hanya duduk mencatat di pinggir lapangan."
    
    show reno smirk at center with vdiss:
        xoffset 200
        linear 0.5 xoffset 0
        
    rn "Enak banget ya. Gak lari, gak push-up. Jalur VIP."
    
    # Raka snaps
    show raka sad at left with vdiss:
        xoffset -200
        linear 0.2 xoffset 0
    
    rk "Diam!"
    
    n "Lapangan sunyi. Raka pergi meninggalkan tatapan semua orang."
    hide raka with vdiss
    
    # Dimas & Nisa Stand Up
    show dimas angry at left with vdiss:
        xoffset -300
        linear 0.3 xoffset 0
    
    dm "Berhenti. Kalian nggak lucu."
    rn "Kamu bela anak cacat begitu?"
    
    show nisa brave at right with vdiss:
        xoffset 300
        linear 0.3 xoffset 0
        
    ns "Aku sudah lapor Pak Guntur. Kalau kalian nggak berhenti, kalian akan melukai lebih banyak orang."
    
    n "Reno pergi dengan kesal. Tapi Raka sudah terlanjur pergi dengan luka di hati."

    jump scene_5

# ---------------------------------------------------------
# BAB 5: TIGA HARI TANPA RAKA (Arya's POV)
# ---------------------------------------------------------
label scene_5:
    scene bg classroom with vdiss
    play music sad_p fadein 1.0
    
    n "Sudah tiga hari Raka tidak masuk tanpa kabar."
    
    show arya sad at center with vdiss
    ar "Apa kamu baik-baik saja... Raka?"
    
    # Reno approaches
    show reno smirk at right with vdiss:
        xoffset 200
        linear 0.5 xoffset 0
        
    rn "Oh, mau nengok anak cengeng itu?"
    
    # CHOICE 1
    menu:
        "Balas dengan tegas":
            $ a2_points += 1
            # Arya moves aggressively towards Reno
            show arya sad:
                linear 0.2 xoffset 50
            ar "Kau nggak tahu apa yang dia alami. Jadi diam sebelum kau nyakitin dia lebih jauh."
            n "Reno terdiam melihat keberanian Arya."
        
        "Diam saja":
            $ b3_points += 1
            # Arya shrinks back
            show arya sad:
                linear 0.2 xoffset -30
            ar "..."
            n "Arya terdiam, merasa tak mampu melawan. Kata-kata Reno menusuknya."

    jump scene_6

# ---------------------------------------------------------
# BAB 6: DI KAMAR RAKA (The Critical Moment)
# ---------------------------------------------------------
label scene_6:
    scene bg house_room with vdiss
    
    n "Arya mengunjungi rumah Raka. Kamarnya gelap."
    
    show raka grey at center with vdiss
    
    rk "Aku capek. Aku... nggak kuat, Arya..."
    
    show arya sad at left with vdiss:
        xoffset -200
        linear 0.5 xoffset 0
        
    # CHOICE 2
    menu:
        "Validasi: 'Aku di sini bareng kamu'":
            $ a2_points += 1
            # Arya moves closer
            show arya sad:
                linear 0.5 xoffset 100
            ar "Kamu nggak harus kuat sekarang. Kamu nggak sendirian. Aku di sini... bareng kamu."
            n "Raka menatap Arya. Ada sedikit cahaya di matanya."
            jump scene_7

        "Mundur: 'Aku butuh ruang'":
            $ b3_points += 1
            # Arya moves back
            show arya sad:
                linear 0.5 xoffset -100
            ar "Kalau kamu butuh ruang... aku mundur sedikit."
            rk "...jangan pergi."
            n "Tapi Arya sudah menjauh. Retakan itu membesar."
            jump scene_7

# ---------------------------------------------------------
# BAB 7: BARA DALAM HENING (The Confrontation)
# ---------------------------------------------------------
label scene_7:
    n "Tiba-tiba terdengar gedoran pintu. Reno datang mencari Raka."
    
    show reno angry at right with vdiss:
        xoffset 300
        linear 0.2 xoffset 0
        
    rn "Mana Raka? Anak bandku kurang satu!"
    
    # CHOICE 3
    menu:
        "Usir Reno":
            $ a2_points += 1
            show arya angry at left
            ar "Keluar dari rumah ini. Ini rumah orang."
        
        "Mencoba Meredakan":
            $ b3_points += 1
            show arya sad at left
            ar "Raka sakit. Pulang saja."
            rn "Halah, alasan."

    n "Reno akhirnya pergi, tapi kerusakannya sudah terjadi."
    
    # BRANCHING LOGIC
    if a2_points > b3_points:
        jump ending_a2
    else:
        jump ending_b3

# ==========================================
# ENDINGS
# ==========================================

# --- ENDING A2: GOOD ---
label ending_a2:
    stop music fadeout 2.0
    play music happy_p fadein 2.0
    scene bg house_room with vdiss
    
    n "Esok harinya, Arya datang kembali. Ia mengetuk pintu."
    
    show arya happy at left with vdiss:
        xoffset -100
        linear 0.5 xoffset 0
    show raka neutral at right with vdiss:
        xoffset 100
        linear 0.5 xoffset 0
        
    rk "Aku... belum baik. Tapi aku mau mencoba. Buat diriku."
    ar "Kalau kamu mau mencoba... aku ikut."
    
    # They move closer
    show arya happy:
        linear 0.5 xoffset 50
    show raka neutral:
        linear 0.5 xoffset -50
        
    hide raka
    show raka happy at center with vdiss:
        zoom 1.05
    
    n "Senyum tipis muncul di wajah Raka. Cahaya matahari masuk ke kamarnya."
    n "Mereka berjalan bersama menuju festival sekolah. Saling menyelamatkan."
    
    "ENDING A2: MEREKA SALING MENYELAMATKAN"
    return

# --- ENDING B3: BAD ---
label ending_b3:
    stop music fadeout 2.0
    play music sad_p fadein 2.0
    scene bg house_room with vdiss
    
    n "Malam itu, Raka merasa lilin harapannya sudah padam."
    
    # Animation of Raka fading/leaving
    show raka grey at center
    rk "Aku hanya ingin tenang. Meskipun tenang itu tidak ada di sini."
    
    show raka grey:
        linear 2.0 alpha 0.0
    pause 2.0
    
    scene bg classroom with vdiss
    n "Pagi harinya, Arya datang. Tapi kamar itu kosong."
    
    show arya sad at center with vdiss:
        yoffset 20
    
    ar "Raka?"
    
    n "Hanya ada surat di atas meja."
    
    window show
    "{i}Arya... Aku lelah. Jangan cari aku. Aku tidak akan kembali.{/i}"
    window hide
    
    show arya sad:
        linear 3.0 yoffset 100 alpha 0.5
        
    n "Dunia terasa terlalu sunyi. Satu nyawa sudah pergi."
    
    "ENDING B3: YANG TIDAK AKAN KEMBALI"
    return