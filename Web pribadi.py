"""
Generator website biodata bertema God of War 3.
Cara pakai:
  1. Taruh file ini dan foto kamu (foto.jpg) di folder yang sama.
  2. Edit bagian "DATA KAMU" di bawah.
  3. Jalankan:  python biodata.py
  Website akan dibuat (index.html) lalu terbuka otomatis di browser.
Tidak perlu install apa-apa (hanya library bawaan Python).
"""

import html
import webbrowser
from pathlib import Path

# ============================================================
#                       DATA KAMU
# ============================================================
NAMA = "Farel Widiyanto"
STATUS = "MAHASISWA BARU SISTEM INFORMASI"
MOTTO = "Dari mahasiswa baru menjadi pembangun sistem. Perjalanan ini baru dimulai."
FOTO = "foto.jpg.jpg"  # nama file foto, harus di folder yang sama

DATA_DIRI = {
    "Nama": "Farel Widiyanto",
    "Jurusan": "Sistem Informasi (Mahasiswa Baru)",
    "Kampus": "Universitas Tanjungpura",
    "Asal": "Pontianak",
    "Hobi": "Ngoding, Basket, Desain,",
}

TENTANG = (
    "Saya adalah mahasiswa baru Sistem Informasi yang suka membuat sesuatu dari nol: "
    "aplikasi, tampilan, dan solusi untuk masalah sehari-hari. Saya sedang belajar "
    "menggabungkan logika pemrograman dengan desain yang nyaman dipakai untuk sehari hari."
)

# (nama skill, persen 0-100, keterangan)
SKILL = [
    ("Koding", 60, "HTML, CSS, JavaScript, dasar Python"),
    ("UI/UX Design", 65, "Wireframe, prototype, Figma"),
    ("Basis Data", 55, "MySQL, perancangan tabel dan ERD"),
    ("Analisis Sistem", 50, "Kebutuhan pengguna, diagram UML"),
    ("Kerja Tim", 90, "Komunikasi dan kolaborasi proyek"),
]

TOOLS = ["Git", "VS Code", "Figma", "Canva", "Microsoft Office"]

# (label, teks tampilan, link)
KONTAK = [
    ("EMAIL", "farelwidiyantoanjay@gmail.com", "mailto:farelwidiyantoanjay@gmail.com"),
    ("INSTAGRAM", "@Farel.w", "https://instagram.com/usernamekamu"),
    ("GITHUB", "Farelwwidiyantoanjay", "https://github.com/usernamekamu"),
]

TAHUN = 2026
# ============================================================
#            (di bawah ini tidak perlu diubah)
# ============================================================

CSS = """
:root{--ash:#120a08;--ash2:#1d100c;--blood:#9b1c13;--ember:#e0561f;--gold:#c9a55a;--marble:#ece3d2;--muted:#a89a85}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:radial-gradient(ellipse at 50% -10%,#5a120b 0%,transparent 55%),var(--ash);color:var(--marble);
font-family:'Cormorant Garamond',Georgia,serif;font-size:1.2rem;line-height:1.65}
h1,h2,.nav a{font-family:'Cinzel','Times New Roman',serif}
.key{height:18px;opacity:.75;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='36' height='18'%3E%3Cpath d='M0 17V1h16v12H6V6h6v4' fill='none' stroke='%23c9a55a' stroke-width='2'/%3E%3Cpath d='M20 17V1h16' fill='none' stroke='%23c9a55a' stroke-width='2'/%3E%3C/svg%3E") repeat-x center/auto 18px}
.nav{position:sticky;top:0;z-index:5;display:flex;justify-content:center;gap:clamp(.8rem,4vw,2.5rem);padding:.9rem 1rem;background:rgba(18,10,8,.92);border-bottom:1px solid #3a2118}
.nav a{color:var(--gold);text-decoration:none;font-size:.85rem;letter-spacing:.12em}
.nav a:hover{color:var(--ember)}
.hero{min-height:92vh;display:grid;place-items:center;text-align:center;padding:3rem 1.2rem 2rem;position:relative;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.8;animation:embers 7s linear infinite;
background:radial-gradient(2px 2px at 20% 80%,var(--ember),transparent),radial-gradient(2px 2px at 70% 60%,var(--ember),transparent),radial-gradient(3px 3px at 85% 85%,#ff8a3d,transparent),radial-gradient(2px 2px at 35% 40%,#ff8a3d,transparent),radial-gradient(2px 2px at 55% 90%,var(--ember),transparent)}
@keyframes embers{from{transform:translateY(40px);opacity:0}30%{opacity:.9}to{transform:translateY(-120px);opacity:0}}
.frame{width:min(260px,64vw);aspect-ratio:3/4;margin:0 auto 1.6rem;padding:8px;background:linear-gradient(145deg,var(--gold),#6b4a1c 60%,var(--gold));
clip-path:polygon(0 8%,8% 0,92% 0,100% 8%,100% 92%,92% 100%,8% 100%,0 92%);box-shadow:0 0 60px rgba(155,28,19,.7)}
.frame img,.frame .ph{width:100%;height:100%;object-fit:cover;display:block;background:var(--ash2);clip-path:polygon(0 8%,8% 0,92% 0,100% 8%,100% 92%,92% 100%,8% 100%,0 92%)}
.frame .ph{display:none;place-items:center;text-align:center;padding:1rem;color:var(--muted);font-size:1rem}
.hero h1{font-weight:900;font-size:clamp(2.2rem,8vw,4.8rem);line-height:1.05;text-shadow:0 0 30px rgba(224,86,31,.55),0 3px 0 #4a0f0a}
.sub{font-family:'Cinzel',serif;color:var(--ember);letter-spacing:.2em;font-size:clamp(.8rem,2.6vw,1.05rem);margin-top:.8rem}
.tag{max-width:34ch;margin:1.1rem auto 1.8rem;color:var(--muted);font-style:italic}
.btn{display:inline-block;padding:.8rem 2rem;font-family:'Cinzel',serif;font-weight:700;letter-spacing:.14em;font-size:.9rem;color:var(--marble);text-decoration:none;
background:linear-gradient(180deg,var(--blood),#5f0f09);border:1px solid var(--gold);transition:transform .15s,box-shadow .15s}
.btn:hover{transform:translateY(-2px);box-shadow:0 0 24px rgba(224,86,31,.6)}
section{max-width:900px;margin:0 auto;padding:4.5rem 1.4rem 1rem}
h2{font-size:clamp(1.5rem,5vw,2.2rem);color:var(--gold);text-align:center;letter-spacing:.1em;margin-bottom:.4rem}
.rule{width:120px;height:3px;margin:0 auto 2rem;background:linear-gradient(90deg,transparent,var(--blood),transparent)}
.data{display:grid;grid-template-columns:max-content 1fr;gap:.6rem 1.4rem;background:var(--ash2);border:1px solid #3a2118;border-left:4px solid var(--blood);padding:1.6rem}
.data dt{font-family:'Cinzel',serif;color:var(--gold);font-size:.9rem;letter-spacing:.08em;padding-top:.2rem}
.data dd{margin:0}
.about{margin-top:1.6rem}
.skills{display:grid;gap:1.3rem}
.row{display:flex;justify-content:space-between;font-family:'Cinzel',serif;font-size:.95rem;margin-bottom:.35rem}
.row span:last-child{color:var(--ember)}
.bar{height:14px;background:#000;border:1px solid var(--gold);padding:2px}
.bar i{display:block;height:100%;width:0;background:linear-gradient(90deg,#6a0f08,var(--blood),var(--ember));box-shadow:0 0 12px var(--ember);transition:width 1.6s cubic-bezier(.2,.8,.2,1)}
.skill small{display:block;color:var(--muted);margin-top:.3rem;font-size:1rem}
.chips{display:flex;flex-wrap:wrap;gap:.6rem;justify-content:center;margin-top:2rem}
.chips span{border:1px solid var(--gold);padding:.3rem 1rem;font-family:'Cinzel',serif;font-size:.8rem;background:var(--ash2)}
.contact{display:grid;gap:.8rem;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.contact a{display:block;text-align:center;padding:1rem;color:var(--marble);text-decoration:none;background:var(--ash2);border:1px solid #3a2118;border-top:3px solid var(--blood);word-break:break-word;transition:background .2s,border-color .2s}
.contact a b{display:block;font-family:'Cinzel',serif;color:var(--gold);font-size:.85rem;letter-spacing:.1em}
.contact a:hover{border-top-color:var(--ember);background:#2a1610}
footer{text-align:center;padding:3.5rem 1rem 2rem;color:var(--muted);font-size:1rem}
footer .key{margin-bottom:1.4rem}
@media(max-width:520px){.data{grid-template-columns:1fr;gap:.1rem}.data dd{margin-bottom:.8rem}}
@media(prefers-reduced-motion:reduce){.hero::before{animation:none}.bar i{transition:none}}
"""

JS = """
window.addEventListener('load',function(){setTimeout(function(){
document.querySelectorAll('.bar i').forEach(function(e){e.style.width=e.dataset.v+'%'})},300)});
"""


def e(teks):
    """Amankan teks supaya aman dimasukkan ke HTML."""
    return html.escape(str(teks))


def buat_html():
    data_diri = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in DATA_DIRI.items())

    skill = "".join(
        f'<div class="skill"><div class="row"><span>{e(n)}</span><span>{int(p)}%</span></div>'
        f'<div class="bar"><i data-v="{int(p)}"></i></div><small>{e(ket)}</small></div>'
        for n, p, ket in SKILL
    )

    tools = "".join(f"<span>{e(t)}</span>" for t in TOOLS)

    kontak = "".join(
        f'<a href="{e(link)}" target="_blank" rel="noopener"><b>{e(label)}</b>{e(teks)}</a>'
        for label, teks, link in KONTAK
    )

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Biodata {e(NAMA)}</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Cormorant+Garamond:wght@500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<nav class="nav"><a href="#beranda">BERANDA</a><a href="#tentang">TENTANG</a><a href="#kemampuan">KEMAMPUAN</a><a href="#kontak">KONTAK</a></nav>

<header class="hero" id="beranda"><div>
  <div class="frame">
    <img src="{e(FOTO)}" alt="Foto {e(NAMA)}" onerror="this.style.display='none';this.nextElementSibling.style.display='grid'">
    <div class="ph">Taruh {e(FOTO)}<br>di folder yang sama<br>dengan file ini</div>
  </div>
  <h1>{e(NAMA)}</h1>
  <div class="sub">{e(STATUS)}</div>
  <p class="tag">{e(MOTTO)}</p>
  <a class="btn" href="#kemampuan">LIHAT KEMAMPUAN</a>
</div></header>

<div class="key"></div>

<section id="tentang"><h2>TENTANG SAYA</h2><div class="rule"></div>
  <dl class="data">{data_diri}</dl>
  <p class="about">{e(TENTANG)}</p>
</section>

<section id="kemampuan"><h2>KEMAMPUAN</h2><div class="rule"></div>
  <div class="skills">{skill}</div>
  <div class="chips">{tools}</div>
</section>

<section id="kontak"><h2>HUBUNGI SAYA</h2><div class="rule"></div>
  <div class="contact">{kontak}</div>
</section>

<footer><div class="key"></div>&copy; {TAHUN} {e(NAMA)}. Dibuat dengan semangat Sparta.</footer>
<script>{JS}</script>
</body>
</html>"""


def main():
    folder = Path(__file__).resolve().parent
    hasil = folder / "index.html"
    hasil.write_text(buat_html(), encoding="utf-8")
    print(f"Berhasil! Website dibuat: {hasil}")

    if not (folder / FOTO).exists():
        print(f"Catatan: file '{FOTO}' belum ada di folder ini, taruh fotomu di sana ya.")

    webbrowser.open(hasil.as_uri())


if __name__ == "__main__":
    main()    
