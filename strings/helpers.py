HELP_1 = """👤**<u>Perintah Admin:</u>**

Tambahkan **c** di awal perintah untuk menggunakannya untuk saluran.

/pause : Jeda streaming yang sedang diputar.
/resume : Lanjutkan streaming yang dijeda.
/mute : Bisukan streaming yang sedang diputar.
/unmute : Bunyikan streaming yang dibisukan.
/skip : Lewati streaming yang sedang diputar dan mulai streaming lagu berikutnya dalam antrean.
/end atau /stop : Hapus antrean dan akhiri streaming yang sedang diputar.
/shuffle : Acak lagu dalam antrean.
/seek : Cari streaming ke durasi yang diberikan.
/seekback : Mundur cari streaming ke durasi yang diberikan.
/reboot : Mulai ulang bot untuk obrolan Anda.

🥴<u>**Putar Ulang:</u>**

/loop [disable/enable] atau [antara 1:10] 
    : Ketika diaktifkan, bot akan memutar streaming yang sedang diputar dalam loop sebanyak 10 kali atau jumlah loop yang diminta.

😜<u>**Pengguna Auth:</u>**

Pengguna auth dapat menggunakan hak admin di bot tanpa hak admin di obrolan.

/auth [username] : Tambahkan pengguna ke daftar auth bot.
/unauth [username] : Hapus pengguna dari daftar auth.
/authusers : Tampilkan daftar pengguna auth bot."""


HELP_2 = """⏯️<u>**Perintah Putar:</u>**

Perintah yang tersedia = play, vplay, cplay, radio, tv

Perintah forceplay = playforce, vplayforce, cplayforce, radioplayforce, tvplayforce

**c** berarti putar saluran.
**v** berarti putar video.
**force** berarti putar paksa.

/play atau /vplay atau /cplay  : Mulai streaming lagu yang diminta di videochat.

/playforce atau /vplayforce atau /cplayforce : **Putar paksa** menghentikan streaming yang sedang berlangsung dan mulai streaming lagu yang diminta.

/channelplay [username obrolan atau id] atau [disable] : Hubungkan saluran ke grup dan mulai streaming lagu dengan bantuan perintah yang dikirim di grup.

/radio [nama stasiun] : Mulai streaming radio di obrolan suara.

/tv [nama saluran] : Mulai streaming saluran TV di obrolan suara.

🤨**<u>Daftar Putar Server:</u>**

/playlist  : Periksa daftar putar yang disimpan di server.
/deleteplaylist : Hapus lagu yang disimpan dalam daftar putar.
/play  : Mulai memutar dari daftar putar yang disimpan di server."""


HELP_3 = """🤖<u>**Perintah Bot:</u>**

/stats : Dapatkan statistik global 10 lagu teratas, 10 pengguna teratas bot, 10 obrolan teratas bot, 10 lagu teratas yang diputar di obrolan, dan banyak lagi...
/sudolist : Tampilkan pengguna sudo bot musik.
/lyrics [nama lagu] : Cari lirik untuk lagu yang diminta.
/song [nama lagu] atau [tautan yt] : Unduh lagu YouTube dalam format audio atau video.
/player : Dapatkan panel pemutar interaktif.
/queue : Tampilkan daftar lagu dalam antrean."""

HELP_4 = """😴<u>**Perintah Ekstra:</u>**

/start : Mulai bot musik.
/help  : Dapatkan menu bantuan dengan penjelasan perintah.
/ping: Tampilkan ping dan statistik sistem bot.

🧐<u>**Pengaturan Grup:</u>
/settings : Tampilkan pengaturan grup dengan menu inline interaktif."""

HELP_5 = """🥺**<u>Tambah & Hapus Pengguna Sudo:</u>**
/addsudo [username atau balas ke pengguna]
/delsudo [username atau balas ke pengguna].

🥶**<u>Heroku:</u>**
/usage : Tampilkan penggunaan dyno bulan ini.

🤯**<u>Variabel Konfigurasi:</u>**
/get_var : Dapatkan variabel konfigurasi dari Heroku atau .env.
/del_var : Hapus variabel konfigurasi di Heroku atau .env.
/set_var [nama var] [nilai var] : Atur atau perbarui variabel konfigurasi di Heroku atau .env.

🤖**<u>Perintah Bot:</u>**
/restart : Mulai ulang bot Anda.
/update : Perbarui bot dari repositori upstream.
/speedtest : Periksa kecepatan server bot.
/maintenance [enable/disable] 
/logger [enable/disable] : Bot akan mulai mencatat aktivitas yang terjadi di bot.
/get_log [jumlah baris] : Dapatkan log bot Anda [nilai default adalah 100 baris]
/autoend [enable|disable] : Aktifkan auto end streaming jika tidak ada yang mendengarkan.

📋**<u>Perintah Statistik:</u>**
/activevoice : Tampilkan daftar voicechat aktif di bot.
/activevideo : Tampilkan daftar videochat aktif di bot.
/stats : Tampilkan statistik bot saat ini.

😒**<u>Blacklist Obrolan:</u>**
/blacklistchat [chat id] : Blacklist obrolan dari menggunakan bot.
/whitelistchat [chat id] : Whitelist obrolan yang di-blacklist.
/blacklistedchat : Tampilkan daftar obrolan yang di-blacklist.

😤**<u>Blokir Pengguna:</u>**
/block [username atau balas ke pengguna] : Mulai mengabaikan pengguna, sehingga dia tidak bisa menggunakan perintah bot.
/unblock [username atau balas ke pengguna] : Buka blokir pengguna yang diblokir.
/blockedusers : Tampilkan daftar pengguna yang diblokir.

🤬**<u>Fitur Gban:</u>**
/gban [username atau balas ke pengguna] : Ban global pengguna dari semua obrolan yang dilayani dan blacklist dia dari menggunakan bot.
/ungban [username atau balas ke pengguna] : Buka ban global pengguna yang di-ban secara global.
/gbannedusers : Tampilkan daftar pengguna yang di-ban secara global.

🎥**<u>Mode Videochat:</u>**
/set_video_limit [jumlah obrolan] : Atur jumlah maksimum videochat yang diizinkan di bot. [default - 3]
/videomode [download|m3u8] : Jika mode unduh diaktifkan, bot akan mengunduh lagu daripada memutarnya di m3u8.

💔**<u>Bot Pribadi:</u>**
/authorize [chat id] : Izinkan obrolan untuk menggunakan bot.
/unauthorize [chat id] : Tidak mengizinkan obrolan yang diizinkan.
/authorized : Tampilkan daftar obrolan yang diizinkan.

🍒**<u>Fitur Broadcast:</u>**
/broadcast [pesan atau balas ke pesan] : Broadcast pesan ke obrolan yang dilayani bot.

<u>Mode Broadcast:</u>
**-pin** : Pin pesan yang dibroadcast di obrolan yang dilayani.
**-pinloud** : Pin pesan yang dibroadcast di obrolan yang dilayani dan kirim notifikasi ke anggota.
**-user** : Broadcast pesan ke pengguna yang telah memulai bot Anda.
**-assistant** : Broadcast pesan dari akun asisten bot.
**-nobot** : Paksa bot untuk tidak broadcast pesan.

**Contoh:** `/broadcast -user -assistant -pin testing broadcast`"""

HELP_7 = """💌**<u>Fitur Baru:</u>**

/alive : Sekarang Anda dapat memeriksa apakah bot musik Delta hidup atau tidak
/id : Untuk memeriksa id pengguna dan obrolan
/gcast -user -assistant -pin testing broadcast`
/verify : Verifikasi diri Anda di database Delta"""

HELP_8 = """💰**<u>Fitur Langganan Broadcast:</u>**

Sekarang Anda dapat membeli langganan broadcast bulanan dan mingguan dari kami. Kami akan memberikan Anda 3 broadcast untuk mingguan dan 14 broadcast untuk langganan bulanan dengan batas mengirim broadcast setelah dua hari.

**Hanya Pemilik**
/addweekly [user id] : Tambahkan pengguna ke langganan broadcast mingguan.
/addmonthly [user id] : Tambahkan pengguna ke langganan broadcast bulanan.  
/removesub [user id] : Hapus pengguna dari langganan broadcast.
/checksubscription [user id] : Periksa sisa hari langganan pengguna dan jumlah broadcast.
/substats : Periksa jumlah total langganan dengan id mereka dan jenis langganan bersama dengan jumlah broadcast.
/subscription_alert : Kirim pesan peringatan ke pelanggan dengan sisa hari bersama dengan jumlah broadcast.

**Siapa Saja Bisa Menggunakan**
/mysubscription : Anda dapat memeriksa langganan Anda dengan sisa hari dan jumlah broadcast.
/paidbroadcast : Kirim pesan broadcast ke semua pengguna dan grup sekaligus jika Anda memiliki langganan aktif."""
