""" 
 This file stores an expanded list of key transportation hubs in the Tokyo metro area,
 covering major train and subway hubs. 
 These stations include key JR lines, Tokyo Metro, and other private rail operators.
 The list keeps expanding. 
 """
from typing import Optional

STATION_NAME_DICT = {
    # Major JR Yamanote Line Stations
    "Tokyo": "東京",
    "Shinjuku": "新宿",
    "Shibuya": "渋谷",
    "Ikebukuro": "池袋",
    "Shinagawa": "品川",
    "Akihabara": "秋葉原",
    "Ueno": "上野",
    "Yokohama": "横浜",

    # Additional Major Yamanote Line Stations
    "Ebisu": "恵比寿",
    "Meguro": "目黒",
    "Gotanda": "五反田",
    "Osaki": "大崎",
    "Tamachi": "田町",
    "Hamamatsucho": "浜松町",
    "Kanda": "神田",
    "Nippori": "日暮里",
    "Komagome": "駒込",
    "Sugamo": "巣鴨",
    "Otsuka": "大塚",
    "Mejiro": "目白",
    "Yoyogi": "代々木",

    # Tokyo Metro & Toei Subway Hub Stations
    "Ginza": "銀座",
    "Hibiya": "日比谷",
    "Kasumigaseki": "霞ヶ関",
    "Otemachi": "大手町",
    "Nihombashi": "日本橋",
    "Kayabacho": "茅場町",
    "Roppongi": "六本木",
    "Nogizaka": "乃木坂",
    "Aoyama-Itchome": "青山一丁目",
    "Omotesando": "表参道",
    "Asakusa": "浅草",
    "Ueno-Okachimachi": "上野御徒町",
    "Iidabashi": "飯田橋",
    "Korakuen": "後楽園",
    "Hongo-sanchome": "本郷三丁目",
    "Shimbashi": "新橋",
    "Toranomon": "虎ノ門",
    "Shiodome": "汐留",
    "Monzen-Nakacho": "門前仲町",
    "Kiyosumi-Shirakawa": "清澄白河",

    # Key Private Railway Hubs (Keio, Tokyu, Odakyu, Seibu, Tobu)
    "Kichijoji": "吉祥寺",
    "Mitaka": "三鷹",
    "Nakano": "中野",
    "Koenji": "高円寺",
    "Ogikubo": "荻窪",
    "Asagaya": "阿佐ヶ谷",
    "Nerima": "練馬",
    "Itabashi": "板橋",
    "Ikegami": "池上",
    "Futako-Tamagawa": "二子玉川",
    "Chofu": "調布",
    "Machida": "町田",
    "Tamagawa": "多摩川",
    "Musashi-Kosugi": "武蔵小杉",

    # Major Chuo Line & Sobu Line Stations
    "Ochanomizu": "御茶ノ水",
    "Kanda": "神田",
    "Nakano": "中野",
    "Koenji": "高円寺",
    "Ogikubo": "荻窪",
    "Mitaka": "三鷹",
    "Tachikawa": "立川",

    # Tokyo Bay & Rinkai Line Areas
    "Shin-Kiba": "新木場",
    "Toyosu": "豊洲",
    "Ariake": "有明",
    "Odaiba": "お台場",
    "Shinkiba": "新木場",
    "Kasai": "葛西",
    "Maihama": "舞浜",  # Near Tokyo Disneyland
    "Shin-Urayasu": "新浦安",

    # Tokyo Suburban Expansion (Future Addition)
    "Fuchu": "府中",
    "Hachioji": "八王子",
    "Musashi-Sakai": "武蔵境",
    "Musashi-Koganei": "武蔵小金井",
    "Kunitachi": "国立",
    "Tama-Center": "多摩センター",
    "Kawagoe": "川越",
    "Omiya": "大宮",
    "Matsudo": "松戸",
    "Kashiwa": "柏",
}

def _generate_variants(name: str) -> list[str]:
    """Generate normalized variants for flexible matching."""
    base = name.strip()

    return list({
        base.title(),
        base.replace("-", "").title(),
        base.replace(" ", "").title(),
        base.replace(" ", "-").title(),
    })

def get_japanese_station_name(name: str) -> str:
    """
    Convert English name to Japanese.
    Returns original input if no match is found.
    """
    if not name:
        return name

    for variant in _generate_variants(name):
        if variant in STATION_NAME_DICT:
            return STATION_NAME_DICT[variant]

    return name  # fallback (important for MCP flow)

def is_valid_station(name: str) -> bool:
    """Check if station exists in mapping."""
    return get_japanese_station_name(name) != name
