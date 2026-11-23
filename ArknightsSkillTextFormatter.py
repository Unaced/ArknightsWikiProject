import html
import re
import tkinter as tk
import ctypes
from tkinter import messagebox, ttk


def convert_header(text):
    image_match = re.search(r"\[\[(.*?)\|width=100%\]\]", text)
    youtube_match = re.search(
        r"\[youtube\(\s*([^,\s)]+)"
        r"(?:\s*,\s*start\s*=\s*([^,\s)]+))?",
        text,
    )
    names_match = re.search(
        r"\{\{\{\+1\s*(.*?)\s*\((.*?)\)\s*\}\}\}",
        text,
    )

    # Find the row containing the recovery and activation types.
    types = []
    for line in text.splitlines():
        matches = re.findall(r">\s*([^<>|]+?)\s*\|\|", line)
        if len(matches) >= 2:
            types = [value.strip() for value in matches[:2]]
            break

    if not image_match or not names_match or len(types) < 2 or not youtube_match:
        raise ValueError(
        "Could not find the image, names, types, or YouTube URL/start position."
        )

    template = html.unescape("""||<&#x74;ablealign=cente&#x72;><&#x74;ablewidth=100&#x30;><&#x77;idth=8&#x30;><&#x68;eight=8&#x30;><&#x74;ablebgcolor=#fff,#2d2f3&#x34;><&#x74;ablecolor=#000,#e0e0e&#x30;><&#x62;gcolor=#ccc,#1c1c1&#x63;><&#x72;owkeepal&#x6C;><&#x63;olkeepal&#x6C;> [[IMAGE_NAME|width=80]] ||<&#x62;gcolor=#eee,#3f3f3&#x66;><&#x63;olor=#000,#ff&#x66;>'''{{{+1 KR_NAME ([include(틀:zh, text=ZH_NAME)])}}}'''[br]{{{#!wiki class="skillTag RECOVERY_SKILLTAG"
'''RECOVERY_TYPE'''}}}{{{#!wiki class="skillTag 발동"
'''ACTIVATION_TYPE'''}}} ||
||<-2><nopad>{{{#!wiki class="skillWrap"
{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv1" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv1,skillSelected"
1}}}{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv2" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv2,skillSelected"
2}}}{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv3" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv3,skillSelected"
3}}}{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv4" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv4,skillSelected"
4}}}{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv5" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv5,skillSelected"
5}}}{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv6" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv6,skillSelected"
6}}}{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv7" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv7,skillSelected"
7}}}{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv8" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv8,skillSelected"
8}}}{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv9" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv9,skillSelected"
9}}}{{{#!wiki class="skillFlex skillTabStyle skillSKILL_NUM skillSKILL_NUMLv10 skillSelected" onclick="remove-class,skillSKILL_NUM,skillSelected;add-class,skillSKILL_NUMLv10,skillSelected"
10}}}}}}||""")

    replacements = {
        "IMAGE_NAME": image_match.group(1).strip(),
        "KR_NAME": names_match.group(1).strip(),
        "ZH_NAME": str((names_match.group(2) or "").strip()),
        "RECOVERY_TYPE": types[0],
        "RECOVERY_SKILLTAG": types[0].replace(" ", ""),
        "ACTIVATION_TYPE": types[1],
        "SKILL_NUM": skill_num.get(),
    }

    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)

    global youtube_url 
    youtube_url = str(youtube_match.group(1).strip())
    global start_pos 
    start_pos = str((youtube_match.group(2) or "0").strip())

    return template


def parse_skill_rows(text):
    rows = []

    for line in text.splitlines():
        if "||" not in line:
            continue

        values = [part.strip() for part in line.split("||") if part.strip()]

        # Skill rows have five values, starting with a numeric level.
        if len(values) == 5 and values[0].isdigit():
            rows.append(values)

    if not rows:
        raise ValueError("Could not find any skill rows with five values.")

    return rows


def convert_all():
    text = input_text.get("1.0", "end")

    try:
        header = convert_header(text)
        rows = parse_skill_rows(text)
    except ValueError as error:
        messagebox.showerror("Input error", str(error))
        return

    skill_template = """{{{#!wiki class="skillDesc skillSKILL_NUM skillSKILL_NUMLvLEVEL hideSELECTED"
## LEVEL레벨
[include(@S@,초기SP=INIT_SP, SP소모=COST_SP, 지속시간=DURATION)]
DESCRIPTION
}}}"""

    skill_template_end = """{{{#!wiki class="skillInfoBox"
{{{#!folding ⠀스킬 범위 [▼]⠀
[[파일:빈 가로 이미지.svg|width=125]]}}}}}} {{{#!wiki class="skillInfoBox"
{{{#!folding ⠀시연 영상 [▼]⠀
||<tablewidth=100%><width=1000><nopad>{{{#!wiki style="aspect-ratio: 16 / 9"
[youtube(YOUTUBE_URL, start=START_POS, width=100%, height=100%)]}}}||}}}}}} ||"""

    skill_blocks = []

    for index, row in enumerate(rows):
        if init_cost_arrangement.get() == "init/cost":
            level, init_sp, cost_sp, duration, desc = row
        elif init_cost_arrangement.get() == "cost/init":
            level, cost_sp, init_sp, duration, desc = row
        selected = " skillSelected" if index == len(rows) - 1 else ""

        replacements = {
        "SKILL_NUM": skill_num.get(),
        "LEVEL": level,
        "SELECTED": selected,
        "INIT_SP": init_sp,
        "COST_SP": cost_sp,
        "DURATION": duration,
        "DESCRIPTION": desc,
    }

        skilldesc_replacements = {
        "#007fff": "#0098dc",
        "#ff7f00": "#f49800",
        "#ff0000": "#ff6237",

        "보호막": "[include(@효과@,이름=보호막)]",
        "인내": "[include(@효과@,이름=인내)]",
        "실드": "[include(@효과@,이름=실드)]",
        "탈취": "[include(@효과@,이름=탈취)]",
        "가호": "[include(@효과@,이름=가호)]",
        "비호": "[include(@효과@,이름=비호)]",
        "저항": "[include(@효과@,이름=저항)]",
        "기운 충만": "[include(@효과@,이름=기운 충만)]",
        "격려": "[include(@효과@,이름=격려)]",
        "위장": "[include(@효과@,이름=위장)]",
        "은신": "[include(@효과@,이름=은신)]",
        "손상 보호막": "[include(@효과@,이름=손상 보호막)]",
        "아츠 충만": "[include(@효과@,이름=아츠 충만)]",
        "대공 가호": "[include(@효과@,이름=대공 가호)]",
        "대미지 감소": "[include(@효과@,이름=대미지 감소)]",
        "기절": "[include(@효과@,이름=기절)]",
        "냉기": "[include(@효과@,이름=냉기)]",
        "빙결": "[include(@효과@,이름=빙결)]",
        "수면": "[include(@효과@,이름=수면)]",
        "정지": "[include(@효과@,이름=정지)]",
        "속박": "[include(@효과@,이름=속박)]",
        "불균형": "[include(@효과@,이름=불균형)]",
        "중상": "[include(@효과@,이름=중상)]",
        "공중 부양": "[include(@효과@,이름=공중 부양)]",
        "전율": "[include(@효과@,이름=전율)]",
        "공포": "[include(@효과@,이름=공포)]",
        "유도": "[include(@효과@,이름=유도)]",
        "마비": "[include(@효과@,이름=마비)]",
        "둔화": "[include(@효과@,이름=둔화)]",
        "지상 결박": "[include(@효과@,이름=지상 결박)]",
        "추방": "[include(@효과@,이름=추방)]",
        "취약": "[include(@효과@,이름=취약)]",
        "물리 취약": "[include(@효과@,이름=물리 취약)]",
        "마법 취약": "[include(@효과@,이름=아츠 취약)]",
        "원소 취약": "[include(@효과@,이름=원소 취약)]",
        "약화": "[include(@효과@,이름=약화)]",
        "무중력": "[include(@효과@,이름=무중력)]",
        "차지": "[include(@효과@,이름=차지)]",
        "과부하": "[include(@효과@,이름=과부하)]",
        "전송": "[include(@효과@,이름=전송)]",
        "이륙": "[include(@효과@,이름=이륙)]",
        "약점 대미지": "[include(@효과@,이름=약점 대미지)]",
        "장비응변": "[include(@효과@,이름=장비응변)]",
        "배치 코스트 하한": "[include(@효과@,이름=배치 코스트 하한)]",
        "촉발성 효과": "[include(@효과@,이름=촉발성 효과)]",
        "쇠약 손상": "[include(@효과@,이름=쇠약 손상)]",
        "소각 손상": "[include(@효과@,이름=소각 손상)]",
        "신경 손상": "[include(@효과@,이름=신경 손상)]",
        "침식 손상": "[include(@효과@,이름=침식 손상)]",
        "광조 손상": "[include(@효과@,이름=광조 손상)]",
        "지속시간=-": "",
        }

        block = skill_template
        for placeholder, value in replacements.items():
            block = block.replace(placeholder, value)

        for placeholder, value in skilldesc_replacements.items():
            block = block.replace(placeholder, value)
        

        skill_blocks.append(block)


    replacements = {
                "YOUTUBE_URL": youtube_url,
                "START_POS": start_pos,
            }
    block = skill_template_end
    for placeholder, value in replacements.items():
        skill_template_end = skill_template_end.replace(placeholder, value)
    
    skill_blocks.append(skill_template_end)

    
    result = header + "\n||<-2>" + "".join(skill_blocks)

    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)

try:
  ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Windows 8.1 이상
except Exception:
  try:
    ctypes.windll.user32.SetProcessDPIAware()  # 이전 Windows 버전 호환
  except Exception:
    pass



root = tk.Tk()
root.title("Arknights Wiki Skill Text Formatter")
root.geometry("950x950")

skill_num = tk.StringVar(value="1")

radio_frame = ttk.LabelFrame(root, text="Skill number")
radio_frame.pack(anchor="w", padx=10, pady=5)

for number in ("1", "2", "3"):
    ttk.Radiobutton(
        radio_frame,
        text=number,
        value=number,
        variable=skill_num,
    ).pack(side="left", padx=8, pady=4)

init_cost_arrangement = tk.StringVar(value="init/cost")

radio_frame = ttk.LabelFrame(root, text="Init/Cost arrangement")
radio_frame.pack(anchor="w", padx=10, pady=5)

for string in ("init/cost", "cost/init"):
    ttk.Radiobutton(
        radio_frame,
        text=string,
        value=string,
        variable=init_cost_arrangement,
    ).pack(side="left", padx=8, pady=4)

ttk.Label(root, text="Paste the source table, followed by the skill level rows:").pack(
    anchor="w", padx=10, pady=(10, 0)
)

input_text = tk.Text(root, height=18, wrap="word")
input_text.pack(fill="both", expand=True, padx=10, pady=5)

ttk.Button(root, text="Convert", command=convert_all).pack(pady=5)

ttk.Label(root, text="Converted output:").pack(anchor="w", padx=10)

output_text = tk.Text(root, height=18, wrap="word")
output_text.pack(fill="both", expand=True, padx=10, pady=(5, 10))

root.mainloop()