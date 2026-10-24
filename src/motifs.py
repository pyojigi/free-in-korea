"""언어별 배경과 색.

- SKY: 화면 아래에 깔리는 전통 가옥 그림 (200x110 한 칸이 가로로 반복). 직접 그린 색칠 도형.
- PAT: 바탕에 아주 옅게 깔리는 전통 무늬 (언어 색으로 칠해짐).
- COLORS: 언어별 대표색(버튼·탭). 밝은 화면 / 어두운 화면 두 벌.
"""
from urllib.parse import quote

SKY = {
    # 한옥: 검은 기와, 단청 띠(빨강·청록), 흰 벽, 나무 기둥, 돌 기단
    "hanok": '''
<rect y="96" width="200" height="14" fill="#a9a59c"/>
<rect x="54" y="58" width="92" height="38" fill="#f3ead8"/>
<rect x="66" y="70" width="24" height="26" fill="#d9c6a3"/><rect x="110" y="70" width="24" height="26" fill="#d9c6a3"/>
<path d="M66 78 H90 M66 86 H90 M78 70 V96 M110 78 H134 M110 86 H134 M122 70 V96" stroke="#b39770" stroke-width="1.2"/>
<rect x="54" y="62" width="6" height="34" fill="#8a5a34"/><rect x="97" y="62" width="6" height="34" fill="#8a5a34"/><rect x="140" y="62" width="6" height="34" fill="#8a5a34"/>
<rect x="50" y="57" width="100" height="4" fill="#b23a2e"/><rect x="50" y="61" width="100" height="3" fill="#2e7d6b"/>
<path d="M8 60 Q28 58 38 47 L60 33 H140 L162 47 Q172 58 192 60 Q166 63 150 58 H50 Q34 63 8 60 Z" fill="#3a3f4b"/>
<path d="M56 30 H144 L141 34 H59 Z" fill="#23262e"/>
<path d="M44 46 H156 M36 52 H164" stroke="#555b69" stroke-width="1.2"/>''',
    # 중국 누각: 황금 기와, 붉은 기둥, 흰 기단
    "pagoda": '''
<rect y="96" width="200" height="14" fill="#e3dccd"/>
<rect x="98" y="6" width="4" height="18" fill="#c9962b"/><circle cx="100" cy="6" r="3" fill="#c9962b"/>
<rect x="90" y="30" width="20" height="18" fill="#b8322a"/>
<rect x="86" y="54" width="28" height="20" fill="#b8322a"/><rect x="96" y="60" width="8" height="14" fill="#5a1a14"/>
<rect x="80" y="80" width="40" height="16" fill="#b8322a"/><rect x="95" y="84" width="10" height="12" fill="#5a1a14"/>
<path d="M70 30 Q82 28 86 22 H114 Q118 28 130 30 Q114 32 110 30 H90 Q86 32 70 30 Z" fill="#c9962b"/>
<path d="M58 54 Q76 51 82 44 H118 Q124 51 142 54 Q120 56 114 54 H86 Q80 56 58 54 Z" fill="#c9962b"/>
<path d="M46 80 Q70 76 78 68 H122 Q130 76 154 80 Q126 82 118 80 H82 Q74 82 46 80 Z" fill="#c9962b"/>
<path d="M84 29 H116 M80 53 H120 M76 79 H124" stroke="#2f6b5a" stroke-width="2"/>''',
    # 사원 지붕(제비꼬리 용마루): 주황 기와, 청록 장식, 붉은 벽돌
    "swallowtail": '''
<rect y="96" width="200" height="14" fill="#b9a993"/>
<rect x="50" y="60" width="100" height="36" fill="#a33b2b"/>
<rect x="86" y="70" width="28" height="26" fill="#3a2320"/><rect x="60" y="70" width="16" height="14" fill="#d9a53a"/><rect x="124" y="70" width="16" height="14" fill="#d9a53a"/>
<path d="M28 62 L42 50 H158 L172 62 Z" fill="#c4552d"/>
<path d="M22 28 Q34 40 52 46 H148 Q166 40 178 28 Q172 44 160 50 H40 Q28 44 22 28 Z" fill="#c4552d"/>
<path d="M30 36 Q40 44 54 47 H146 Q160 44 170 36" stroke="#2e8b8b" stroke-width="3" fill="none"/>
<circle cx="100" cy="42" r="4" fill="#d9a53a"/>''',
    # 일본: 후지산 + 주홍 도리이
    "torii": '''
<rect y="96" width="200" height="14" fill="#9fb59a"/>
<path d="M-10 100 L38 58 Q46 52 54 58 L102 100 Z" fill="#5b7fa6"/>
<path d="M26 69 L38 58 Q46 52 54 58 L66 69 Q58 64 52 70 Q46 64 40 70 Q34 64 26 69 Z" fill="#f4f6f8"/>
<rect x="116" y="44" width="8" height="56" fill="#d9472b"/><rect x="170" y="44" width="8" height="56" fill="#d9472b"/>
<rect x="106" y="54" width="82" height="5" fill="#d9472b"/>
<path d="M96 38 Q148 30 198 38 L196 45 Q148 38 98 45 Z" fill="#d9472b"/>
<path d="M94 35 Q148 26 200 35 L199 39 Q148 31 95 39 Z" fill="#2a2a2a"/>''',
    # 베트남: 논라(삿갓), 연꽃, 물
    "nonla": '''
<rect y="96" width="200" height="14" fill="#7fb3c8"/>
<path d="M0 98 Q25 94 50 98 T100 98 T150 98 T200 98" stroke="#a9d0de" stroke-width="2" fill="none"/>
<path d="M14 84 L44 54 L74 84 Q44 90 14 84 Z" fill="#e0c27a"/><path d="M44 54 L74 84 Q60 87 50 87 Z" fill="#c9a75a"/>
<path d="M30 82 Q44 86 58 82" stroke="#a6863f" stroke-width="1.2" fill="none"/>
<path d="M120 84 L150 54 L180 84 Q150 90 120 84 Z" fill="#e0c27a"/><path d="M150 54 L180 84 Q166 87 156 87 Z" fill="#c9a75a"/>
<path d="M100 96 V80" stroke="#4f8a4b" stroke-width="2.5"/>
<ellipse cx="88" cy="94" rx="10" ry="3" fill="#4f8a4b"/>
<path d="M100 80 Q88 70 92 56 Q100 66 100 80 Z" fill="#e27aa0"/><path d="M100 80 Q112 70 108 56 Q100 66 100 80 Z" fill="#e27aa0"/>
<path d="M100 80 Q93 64 100 50 Q107 64 100 80 Z" fill="#f2a6c2"/>''',
    # 태국 사원: 빨강·초록 겹지붕, 금색 처마 장식, 흰 벽
    "wat": '''
<rect y="96" width="200" height="14" fill="#d8cdb8"/>
<rect x="56" y="76" width="88" height="20" fill="#f1ece2"/>
<rect x="90" y="80" width="20" height="16" fill="#d4a32a"/>
<path d="M32 78 L100 32 L168 78 Z" fill="#2f7a4a"/>
<path d="M40 76 L100 36 L160 76 Z" fill="#b3322b"/>
<path d="M50 64 L100 18 L150 64 Z" fill="#2f7a4a"/>
<path d="M56 62 L100 22 L144 62 Z" fill="#b3322b"/>
<path d="M32 78 Q24 70 28 62 L36 70 Z M168 78 Q176 70 172 62 L164 70 Z M50 64 Q44 57 47 51 L54 58 Z M150 64 Q156 57 153 51 L146 58 Z M100 18 L97 8 L100 4 L103 8 Z" fill="#d4a32a"/>''',
    # 루마 가당: 검은 야자섬유 지붕, 붉은 갈색 벽, 금색 조각 띠, 기둥
    "gadang": '''
<rect y="96" width="200" height="14" fill="#a68a64"/>
<rect x="54" y="88" width="6" height="10" fill="#5b3a22"/><rect x="140" y="88" width="6" height="10" fill="#5b3a22"/><rect x="97" y="88" width="6" height="10" fill="#5b3a22"/>
<rect x="44" y="66" width="112" height="22" fill="#9b3b2a"/>
<rect x="44" y="66" width="112" height="5" fill="#d6a53a"/>
<path d="M50 76 l6 -4 6 4 6 -4 6 4 6 -4 6 4 6 -4 6 4 6 -4 6 4 6 -4 6 4 6 -4 6 4 6 -4 6 4" stroke="#d6a53a" stroke-width="1.5" fill="none"/>
<rect x="92" y="74" width="16" height="14" fill="#3b2a20"/>
<path d="M8 24 Q30 56 60 50 Q78 40 100 50 Q122 40 140 50 Q170 56 192 24 Q186 58 158 68 H42 Q14 58 8 24 Z" fill="#3b2f2a"/>''',
    # 이즈바: 통나무집, 파란 창틀, 붉은 굴뚝
    "izba": '''
<rect y="96" width="200" height="14" fill="#c9c3b0"/>
<rect x="128" y="28" width="10" height="20" fill="#a4402e"/>
<rect x="52" y="58" width="96" height="38" fill="#a0693a"/>
<path d="M52 64 H148 M52 70 H148 M52 76 H148 M52 82 H148 M52 88 H148" stroke="#7c4e27" stroke-width="1.4"/>
<path d="M44 60 L100 26 L156 60 Z" fill="#6f7d84"/>
<path d="M58 58 L100 32 L142 58 Z" fill="#a0693a"/>
<rect x="64" y="66" width="22" height="20" fill="#3f6fb6"/><rect x="68" y="69" width="14" height="14" fill="#fdf7e6"/>
<rect x="114" y="66" width="22" height="20" fill="#3f6fb6"/><rect x="118" y="69" width="14" height="14" fill="#fdf7e6"/>
<rect x="92" y="40" width="16" height="12" fill="#3f6fb6"/><rect x="95" y="42" width="10" height="8" fill="#fdf7e6"/>''',
    # 게르: 흰 펠트, 파랑·빨강 문양 띠, 주황 문
    "ger": '''
<rect y="96" width="200" height="14" fill="#a7b878"/>
<path d="M40 100 V72 Q40 54 100 46 Q160 54 160 72 V100 Z" fill="#f2efe8"/>
<path d="M40 72 Q40 54 100 46 Q160 54 160 72" stroke="#c9c3b6" stroke-width="2" fill="none"/>
<rect x="40" y="74" width="120" height="6" fill="#2c5aa0"/>
<path d="M40 77 h120" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="4 4"/>
<rect x="92" y="40" width="16" height="8" fill="#c0392b"/>
<rect x="89" y="80" width="22" height="20" fill="#d2552a"/>
<path d="M93 84 H107 V96 H93 Z" stroke="#f2c14e" stroke-width="1.4" fill="none"/>''',
}

SKY["barn"] = '''
<rect y="96" width="200" height="14" fill="#8fae6b"/>
<path d="M0 84 H44 M0 92 H44 M156 84 H200 M156 92 H200" stroke="#f4f1ea" stroke-width="2.5"/>
<path d="M6 80 V98 M20 80 V98 M34 80 V98 M166 80 V98 M180 80 V98 M194 80 V98" stroke="#f4f1ea" stroke-width="3"/>
<path d="M50 58 L66 36 H134 L150 58 V98 H50 Z" fill="#a8322b"/>
<path d="M46 60 L64 33 H136 L154 60 L150 62 L133 38 H67 L50 62 Z" fill="#5a5f66"/>
<path d="M80 62 H120 V98 H80 Z" fill="#7a221d"/>
<path d="M80 62 L120 98 M120 62 L80 98 M80 62 H120 V98 H80 Z" stroke="#f4f1ea" stroke-width="2.5" fill="none"/>
<path d="M90 42 H110 V54 H90 Z" fill="#f4f1ea"/><path d="M93 45 H107 V51 H93 Z" fill="#7a221d"/>
'''

PAT = {
    "lattice": '<path d="M0 24 H48 M24 0 V48 M0 0 L48 48 M48 0 L0 48" stroke="#000" stroke-width="1.6" fill="none"/>',
    "cloud": '<path d="M10 30 a6 6 0 1 1 10 -6 a6 6 0 1 1 10 2 a5 5 0 1 1 6 8 H12 a4 4 0 0 1 -2 -4 Z" stroke="#000" stroke-width="1.6" fill="none"/>',
    "square": '<path d="M8 8 H40 V40 H8 Z M16 16 H32 V32 H16 Z" stroke="#000" stroke-width="1.6" fill="none"/>',
    "seigaiha": '<g stroke="#000" stroke-width="1.6" fill="none"><path d="M0 24 a24 24 0 0 1 48 0 M8 24 a16 16 0 0 1 32 0 M16 24 a8 8 0 0 1 16 0"/><path d="M-24 48 a24 24 0 0 1 48 0 M24 48 a24 24 0 0 1 48 0"/></g>',
    "lotus": '<path d="M24 38 Q14 28 18 16 Q24 26 24 38 Z M24 38 Q34 28 30 16 Q24 26 24 38 Z M24 38 Q20 24 24 10 Q28 24 24 38 Z" stroke="#000" stroke-width="1.4" fill="none"/>',
    "diamond": '<path d="M24 4 L44 24 L24 44 L4 24 Z M24 14 L34 24 L24 34 L14 24 Z" stroke="#000" stroke-width="1.6" fill="none"/>',
    "kawung": '<g stroke="#000" stroke-width="1.6" fill="none"><ellipse cx="24" cy="12" rx="6" ry="10"/><ellipse cx="24" cy="36" rx="6" ry="10"/><ellipse cx="12" cy="24" rx="10" ry="6"/><ellipse cx="36" cy="24" rx="10" ry="6"/></g>',
    "folk": '<path d="M24 6 V42 M6 24 H42 M12 12 L36 36 M36 12 L12 36" stroke="#000" stroke-width="1.6" fill="none"/><circle cx="24" cy="24" r="5" fill="#000"/>',
    "stars": '<path d="M24 8 L27.5 18.5 H38.5 L29.5 25 L33 35.5 L24 29 L15 35.5 L18.5 25 L9.5 18.5 H20.5 Z" stroke="#000" stroke-width="1.4" fill="none"/>',
    "knot": '<path d="M12 12 H36 V36 H12 Z M18 6 V42 M30 6 V42 M6 18 H42 M6 30 H42" stroke="#000" stroke-width="1.6" fill="none"/>',
}

# 언어 → (그림, 무늬, 밝은 화면 대표색, 어두운 화면 대표색)
BY_LANG = {
    "ko": ("hanok", "lattice", "#1f4e8c", "#86aee8"),      # 단청의 청색
    "en": ("barn", "stars", "#2a3d66", "#a3b6e0"),       # 미국: 데님 네이비
    "zh": ("pagoda", "cloud", "#b8322a", "#f08a7f"),       # 붉은 기둥
    "tw": ("swallowtail", "square", "#b4462a", "#f0956f"),  # 사원 기와
    "ja": ("torii", "seigaiha", "#2b4a7f", "#93b3e8"),     # 쪽빛
    "vi": ("nonla", "lotus", "#b23c6e", "#f093b9"),        # 연꽃
    "th": ("wat", "diamond", "#8a5d00", "#e8c25c"),        # 사원 금빛
    "id": ("gadang", "kawung", "#8b4513", "#e3a676"),      # 바틱 갈색
    "ru": ("izba", "folk", "#a8232a", "#f08a8f"),          # 민속 빨강
    "mn": ("ger", "knot", "#1d5fa8", "#82b4ec"),           # 하늘 파랑
}


def _url(svg, w, h):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{" ".join(svg.split())}</svg>'
    return 'url("data:image/svg+xml,' + quote(s, safe=" =:/,;-.") + '")'


def css():
    light, dark = [], []
    for lang, (sky, pat, c_light, c_dark) in BY_LANG.items():
        sel = f'[data-motif="{lang}"]'
        light.append(f'{sel}{{--sky:{_url(SKY[sky], 200, 110)};--pat:{_url(PAT[pat], 48, 48)};--accent:{c_light};--accent-ink:#ffffff}}')
        dark.append(f'{sel}{{--accent:{c_dark};--accent-ink:#111418}}')
    d = "\n".join(dark)
    d_media = "\n".join(x.replace('[data-motif', ':root:not([data-theme="light"]) [data-motif', 1) for x in dark)
    d_attr = "\n".join(x.replace('[data-motif', ':root[data-theme="dark"] [data-motif', 1) for x in dark)
    return "\n".join(light) + "\n@media (prefers-color-scheme:dark){\n" + d_media + "\n}\n" + d_attr


# ---------------------------------------------------------------------------
# 장면: 대표 건물 1채 + 전통 의상 남녀 (얼굴은 그리지 않고 의상·실루엣만)
# 400x150 한 장, 바닥선 y=130
# ---------------------------------------------------------------------------
B = 130
SKIN = "#efc7a2"
HAIR = "#2b2522"
SHOE = "#3a2f2a"


def _p(d, fill):
    return f'<path d="{d}" fill="{fill}"/>'


def _sleeves(cx, w, top, color, wide):
    if wide:
        l = f"M{cx-w+1} {B-48} L{cx-w-8} {B-25} L{cx-w+1} {B-25} Z"
        r = f"M{cx+w-1} {B-48} L{cx+w+8} {B-25} L{cx+w-1} {B-25} Z"
    else:
        l = f"M{cx-w+1} {B-48} L{cx-w-4} {B-28} L{cx-w-1} {B-27} L{cx-w+2} {B-43} Z"
        r = f"M{cx+w-1} {B-48} L{cx+w+4} {B-28} L{cx+w+1} {B-27} L{cx+w-2} {B-43} Z"
    hands = f'<circle cx="{cx-w-2.5 if not wide else cx-w-3}" cy="{B-26}" r="2" fill="{SKIN}"/><circle cx="{cx+w+2.5 if not wide else cx+w+3}" cy="{B-26}" r="2" fill="{SKIN}"/>'
    return hands + _p(l + " " + r, color)


def _head(cx, hair="short"):
    h = B - 56
    out = ""
    if hair == "braid":
        out += _p(f"M{cx+3} {h+2} Q{cx+9} {h+14} {cx+6} {h+28} L{cx+3.5} {h+28} Q{cx+6} {h+14} {cx+1} {h+4} Z", HAIR)
    if hair == "lowbun":
        out += f'<circle cx="{cx+5.5}" cy="{h+3}" r="3.2" fill="{HAIR}"/>'
    if hair == "topbun":
        out += f'<circle cx="{cx}" cy="{h-8}" r="3.4" fill="{HAIR}"/>'
    out += f'<rect x="{cx-2}" y="{h+5}" width="4" height="4" fill="{SKIN}"/>'
    out += f'<circle cx="{cx}" cy="{h}" r="6.5" fill="{SKIN}"/>'
    if hair == "bob":
        out += _p(f"M{cx-7} {h+3} Q{cx-8} {h-8} {cx} {h-7.5} Q{cx+8} {h-8} {cx+7} {h+3} L{cx+5} {h+3} Q{cx+5} {h-3} {cx} {h-3} Q{cx-5} {h-3} {cx-5} {h+3} Z", HAIR)
    else:
        out += _p(f"M{cx-6.6} {h} Q{cx-6} {h-7.5} {cx} {h-7} Q{cx+6} {h-7.5} {cx+6.6} {h} Q{cx+3} {h-3} {cx} {h-3.2} Q{cx-3} {h-3} {cx-6.6} {h} Z", HAIR)
    return out


def _hat(cx, kind, color):
    h = B - 56
    if kind == "gat":   # 갓
        return (f'<ellipse cx="{cx}" cy="{h-5}" rx="13" ry="2.4" fill="{color}" opacity=".85"/>'
                + _p(f"M{cx-5} {h-5} L{cx-4} {h-13} H{cx+4} L{cx+5} {h-5} Z", color))
    if kind == "cone":  # 논라
        return _p(f"M{cx-14} {h-3} L{cx} {h-17} L{cx+14} {h-3} Q{cx} {h} {cx-14} {h-3} Z", color)
    if kind == "kokoshnik":
        return _p(f"M{cx-8} {h-3} Q{cx-9} {h-15} {cx} {h-17} Q{cx+9} {h-15} {cx+8} {h-3} Q{cx} {h-6} {cx-8} {h-3} Z", color)
    if kind == "peci":
        return _p(f"M{cx-6.5} {h-3} L{cx-6} {h-9} H{cx+6} L{cx+6.5} {h-3} Z", color)
    if kind == "khandong":  # 베트남 남성 터번형 모자
        return _p(f"M{cx-7} {h-2} Q{cx-7} {h-9} {cx} {h-9} Q{cx+7} {h-9} {cx+7} {h-2} Q{cx} {h-4} {cx-7} {h-2} Z", color)
    if kind == "cowboy":
        return (f'<ellipse cx="{cx}" cy="{h-5}" rx="12" ry="2.6" fill="{color}"/>'
                + _p(f"M{cx-6} {h-5} Q{cx-6} {h-14} {cx-2} {h-13} Q{cx} {h-11} {cx+2} {h-13} Q{cx+6} {h-14} {cx+6} {h-5} Z", color))
    if kind == "bonnet":
        return _p(f"M{cx-8.5} {h+4} Q{cx-10} {h-11} {cx} {h-11} Q{cx+10} {h-11} {cx+8.5} {h+4} L{cx+6} {h+3} Q{cx+6} {h-6} {cx} {h-6} Q{cx-6} {h-6} {cx-6} {h+3} Z", color)
    if kind == "mongol":
        return (_p(f"M{cx-7} {h-3} Q{cx-6} {h-14} {cx} {h-15} Q{cx+6} {h-14} {cx+7} {h-3} Z", color)
                + f'<rect x="{cx-8}" y="{h-5}" width="16" height="3" fill="#2b2522"/>'
                + f'<circle cx="{cx}" cy="{h-16}" r="1.6" fill="#c0392b"/>')
    return ""


def woman(cx, top, bottom, sash=None, shape="bell", sleeve="narrow", hair="lowbun", hat=None, hat_color="#222",
          sleeve_color=None, trousers=None, trim=None):
    out = ""
    if hair == "long":  # 긴 머리는 몸보다 먼저(뒤쪽에) 그려서 어깨 뒤로 내려오게
        h = B - 56
        out += _p(f"M{cx-7} {h} Q{cx-10} {h+14} {cx-9} {h+24} H{cx+9} Q{cx+10} {h+14} {cx+7} {h} Z", HAIR)
    if trousers:
        out += f'<rect x="{cx-6}" y="{B-16}" width="12" height="15" fill="{trousers}"/>'
    if shape == "bell":       # 한복 치마처럼 풍성
        out += _p(f"M{cx-5} {B-40} Q{cx-18} {B-18} {cx-18} {B} H{cx+18} Q{cx+18} {B-18} {cx+5} {B-40} Z", bottom)
    elif shape == "robe":     # 발목까지 내려오는 겉옷
        out += _p(f"M{cx-8} {B-49} L{cx-12} {B} H{cx+12} L{cx+8} {B-49} Z", bottom)
    elif shape == "slim":     # 치파오·사롱처럼 몸에 붙는
        out += _p(f"M{cx-7} {B-49} L{cx-8} {B} H{cx+8} L{cx+7} {B-49} Z", bottom)
    elif shape == "aodai":    # 아오자이: 긴 상의 + 바지
        out += _p(f"M{cx-7} {B-49} L{cx-10} {B-5} H{cx+10} L{cx+7} {B-49} Z", bottom)
    out += _sleeves(cx, 7.5, B - 49, sleeve_color or top, sleeve == "wide")
    short = shape == "bell"
    out += _p(f"M{cx-7.5} {B-49} H{cx+7.5} L{cx+8} {B-(38 if short else 34)} H{cx-8} Z", top)
    if trim:
        out += _p(f"M{cx} {B-49} L{cx+4} {B-49} L{cx-2} {B-40} Z", trim)
    if sash:
        out += f'<rect x="{cx-8.5}" y="{B-39}" width="17" height="{5 if shape != "bell" else 3}" fill="{sash}"/>'
        if shape == "bell":
            out += _p(f"M{cx+1} {B-38} L{cx+4} {B-24} L{cx+2} {B-24} L{cx} {B-36} Z", sash)
    out += _head(cx, hair)
    if hat:
        out += _hat(cx, hat, hat_color)
    out += f'<ellipse cx="{cx-4}" cy="{B}" rx="3.5" ry="1.5" fill="{SHOE}"/><ellipse cx="{cx+4}" cy="{B}" rx="3.5" ry="1.5" fill="{SHOE}"/>'
    return out


def man(cx, top, bottom, sash=None, shape="jacket", sleeve="narrow", hair="short", hat=None, hat_color="#222",
        sleeve_color=None, trim=None):
    out = ""
    out += _p(f"M{cx-8} {B-32} L{cx-9} {B} H{cx-1.5} L{cx} {B-22} L{cx+1.5} {B} H{cx+9} L{cx+8} {B-32} Z", bottom)
    if shape == "robe":
        out += _p(f"M{cx-8.5} {B-49} L{cx-11.5} {B-2} H{cx+11.5} L{cx+8.5} {B-49} Z", top)
    out += _sleeves(cx, 8.5, B - 49, sleeve_color or top, sleeve == "wide")
    if shape == "jacket":
        out += _p(f"M{cx-8.5} {B-49} H{cx+8.5} L{cx+9.5} {B-27} H{cx-9.5} Z", top)
    if shape == "robe":
        out += _p(f"M{cx-8.5} {B-49} H{cx+8.5} L{cx+9} {B-34} H{cx-9} Z", top)
    if trim:
        out += _p(f"M{cx-1} {B-49} H{cx+3} L{cx+3} {B-30} H{cx+1} Z", trim)
    if sash:
        out += f'<rect x="{cx-9.5}" y="{B-35}" width="19" height="4" fill="{sash}"/>'
    out += _head(cx, hair)
    if hat:
        out += _hat(cx, hat, hat_color)
    out += f'<ellipse cx="{cx-5}" cy="{B}" rx="4" ry="1.6" fill="{SHOE}"/><ellipse cx="{cx+5}" cy="{B}" rx="4" ry="1.6" fill="{SHOE}"/>'
    return out


# 언어별 장면: (건물, 바닥색, 여성, 남성)
SCENES = {
    "hanok": ("#a9a59c",  # 한복: 노랑 저고리 + 분홍 치마 / 하늘색 저고리 + 흰 바지 + 갓
              lambda x: woman(x, "#f2d16b", "#e8789a", sash="#c0392b", shape="bell", hair="lowbun"),
              lambda x: man(x, "#a9c6e0", "#f4f1ea", shape="jacket", hat="gat", hat_color="#1e1e1e")),
    "pagoda": ("#e3dccd",  # 한푸: 넓은 소매 겉옷
               lambda x: woman(x, "#d9534f", "#d9534f", sash="#f2c14e", shape="robe", sleeve="wide", hair="topbun", sleeve_color="#e7807c"),
               lambda x: man(x, "#2f6b8f", "#2f6b8f", sash="#c9962b", shape="robe", sleeve="wide", hair="topbun")),
    "swallowtail": ("#b9a993",  # 치파오 / 장삼
                    lambda x: woman(x, "#1f7a8c", "#1f7a8c", shape="slim", hair="bob", trim="#f2c14e"),
                    lambda x: man(x, "#6b4a3a", "#3a2f2a", shape="robe", trim="#d9a53a")),
    "torii": ("#9fb59a",  # 기모노(오비) / 하카마
              lambda x: woman(x, "#c94c6a", "#c94c6a", sash="#f2c14e", shape="robe", sleeve="wide", hair="topbun", sleeve_color="#d97089"),
              lambda x: man(x, "#2b4a7f", "#5a5a6e", shape="robe", sleeve="wide", sash="#1e1e1e")),
    "nonla": ("#7fb3c8",  # 아오자이 + 논라 / 남성 아오자이 + 모자
              lambda x: woman(x, "#d64545", "#d64545", shape="aodai", hair="long", hat="cone", hat_color="#e0c27a", trousers="#f6f3ec"),
              lambda x: man(x, "#2c5aa0", "#f6f3ec", shape="robe", hat="khandong", hat_color="#2b2522")),
    "wat": ("#d8cdb8",  # 사바이 + 파신 / 라차빠땐 재킷 + 쫑끄라벤
            lambda x: woman(x, "#d4a32a", "#7a2a5e", sash="#d4a32a", shape="slim", hair="topbun", sleeve_color=SKIN),
            lambda x: man(x, "#f4f1ea", "#2c5aa0", shape="jacket", trim="#d4a32a")),
    "gadang": ("#a68a64",  # 끄바야 + 바틱 사롱 / 바틱 셔츠 + 페치
               lambda x: woman(x, "#f4e3c3", "#8b4513", shape="slim", hair="lowbun", trim="#b5651d"),
               lambda x: man(x, "#b5651d", "#2b2522", shape="jacket", hat="peci", hat_color="#1e1e1e", trim="#6b3410")),
    "izba": ("#c9c3b0",  # 사라판 + 코코시닉 / 코소보로트카 + 허리띠
             lambda x: woman(x, "#b22222", "#b22222", shape="robe", hair="braid", hat="kokoshnik", hat_color="#d4a32a", sleeve_color="#f6f3ec"),
             lambda x: man(x, "#f4f1ea", "#3a4a6b", shape="jacket", sash="#b22222", trim="#b22222")),
    "barn": ("#8fae6b",  # 프레리 드레스 + 보닛 / 카우보이 모자 + 체크 셔츠 + 청바지
             lambda x: woman(x, "#6f8fbf", "#6f8fbf", sash="#f4f1ea", shape="robe", hair="long", hat="bonnet", hat_color="#f4f1ea"),
             lambda x: man(x, "#c0392b", "#3d5a8a", shape="jacket", hat="cowboy", hat_color="#8a5a34", trim="#f4f1ea")),
    "ger": ("#a7b878",  # 델 + 모자
            lambda x: woman(x, "#2c5aa0", "#2c5aa0", sash="#f2c14e", shape="robe", hair="braid", hat="mongol", hat_color="#2c5aa0", trim="#f2c14e"),
            lambda x: man(x, "#b03a2e", "#b03a2e", sash="#f2c14e", shape="robe", hat="mongol", hat_color="#b03a2e", trim="#f2c14e")),
}


def scene_svg(building):
    ground, w, m = SCENES[building]
    import re
    tile = re.sub(r'<rect y="(96|100)" width="200"[^>]*/>', "", SKY[building])  # 건물 그림의 자체 바닥은 빼고 전체 바닥 하나로
    return (f'<rect y="{B}" width="400" height="20" fill="{ground}"/>'
            f'<g transform="translate(46 30)">{tile}</g>'
            f'{w(276)}{m(312)}')


def css2():
    out = []
    for lang, (sky, pat, c_light, c_dark) in BY_LANG.items():
        out.append(f'[data-motif="{lang}"]{{--scene:{_url(scene_svg(sky), 400, 150)};--ground:{SCENES[sky][0]}}}')
    return "\n".join(out)
