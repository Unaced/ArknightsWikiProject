import html
import re
import tkinter as tk
import ctypes
from tkinter import messagebox, ttk

def convert_all():
    text = input_text.get("1.0", "end")





    replacements = {
        "<tablewidth=100%>": "<tablealign=center><tablewidth=1000>",
        "<table width=100%>": "<tablealign=center><tablewidth=1000>",
        "<tablewidth=1200>": "<tablewidth=1000>",
        "<table width=1200>": "<tablewidth=1000>",

        '{{{#!wiki class="illustBtnWrap""': '{{{#!wiki class="illustBtnWrap"',
        "HIDE": "hide",

        """=== 스탯 ===""": """=== 스탯 ===
{{{#!if 효과 = '틀:명일방주/전투 효과'
}}}""",

        """=== 능력치 ===""": """=== 능력치 ===
{{{#!if 효과 = '틀:명일방주/전투 효과'
}}}""",

        """=== 스킬 ===""": """=== 스킬 ===
{{{#!if S = '틀:명일방주/스킬 정보'
}}}""",

        "#007fff": "#0098dc",
        "#ff7f00": "#f49800",
        "#ff0000": "#ff6237",

        "자동 회복": "자연 회복",


        "[[파일:용문화.png": "[include(틀:명일방주/재화 및 재료, 이름=용문폐)]",
        "[[파일:고원암.png": "[include(틀:명일방주/재화 및 재료, 이름=원암 큐브)]",
        "[[파일:고원암 더미.png": "[include(틀:명일방주/재화 및 재료, 이름=원암 큐브 번들)]",
        "[[파일:정제원암.png": "[include(틀:명일방주/재화 및 재료, 이름=정제 원암)]",
        "[[파일:감미료.png": "[include(틀:명일방주/재화 및 재료, 이름=대체당)]",
        "[[파일:설탕.png": "[include(틀:명일방주/재화 및 재료, 이름=포도당)]",
        "[[파일:설탕 봉지.png": "[include(틀:명일방주/재화 및 재료, 이름=포도당 번들)]",
        "[[파일:설탕 박스.png": "[include(틀:명일방주/재화 및 재료, 이름=포도당 팩)]",
        "[[파일:에스테르.png": "[include(틀:명일방주/재화 및 재료, 이름=에스테르 원료)]",
        "[[파일:폴리에스테르.png": "[include(틀:명일방주/재화 및 재료, 이름=폴리에스테르)]",
        "[[파일:폴리에스테르 세트.png": "[include(틀:명일방주/재화 및 재료, 이름=폴리에스테르 번들)]",
        "[[파일:폴리에스테르 박스.png": "[include(틀:명일방주/재화 및 재료, 이름=폴리에스테르 팩)]",
        "[[파일:이철.png": "[include(틀:명일방주/재화 및 재료, 이름=이철)]",
        "[[파일:이철 조각.png": "[include(틀:명일방주/재화 및 재료, 이름=이철 조각)]",
        "[[파일:이철 결정.png": "[include(틀:명일방주/재화 및 재료, 이름=이철 번들)]",
        "[[파일:이철 덩어리.png": "[include(틀:명일방주/재화 및 재료, 이름=이철 팩)]",
        "[[파일:다이케톤.png": "[include(틀:명일방주/재화 및 재료, 이름=디케톤)]",
        "[[파일:케톤 앰플.png": "[include(틀:명일방주/재화 및 재료, 이름=아케톤 응집체)]",
        "[[파일:케톤 세트.png": "[include(틀:명일방주/재화 및 재료, 이름=아케톤 응집체 번들)]",
        "[[파일:케톤 진열장.png": "[include(틀:명일방주/재화 및 재료, 이름=아케톤 팩)]",
        "[[파일:파손장치.png": "[include(틀:명일방주/재화 및 재료, 이름=파손된 장치)]",
        "[[파일:장치.png": "[include(틀:명일방주/재화 및 재료, 이름=장치)]",
        "[[파일:개조장치.png": "[include(틀:명일방주/재화 및 재료, 이름=리뉴얼 장치)]",
        "[[파일:개량장치.png": "[include(틀:명일방주/재화 및 재료, 이름=개량 장치)]",
        "[[파일:레조에틸렌.png": "[include(틀:명일방주/재화 및 재료, 이름=로식 콜)]",
        "[[파일:에틸렌바이마.png": "[include(틀:명일방주/재화 및 재료, 이름=화이트 호스 콜)]",
        "[[파일:연마석.png": "[include(틀:명일방주/재화 및 재료, 이름=연마석)]",
        "[[파일:오수연마석.png": "[include(틀:명일방주/재화 및 재료, 이름=고급연마석)]",
        "[[파일:망간.png": "[include(틀:명일방주/재화 및 재료, 이름=망간 광석)]",
        "[[파일:깁사이트.png": "[include(틀:명일방주/재화 및 재료, 이름=망간 중합체)]",
        "[[파일:RMA70-12.png": "[include(틀:명일방주/재화 및 재료, 이름=RMA70-12)]",
        "[[파일:RMA70-24.png": "[include(틀:명일방주/재화 및 재료, 이름=RMA70-24)]",
        "[[파일:명일젤라틴.png": "[include(틀:명일방주/재화 및 재료, 이름=젤)]",
        "[[파일:중합젤.png": "[include(틀:명일방주/재화 및 재료, 이름=중합젤)]",
        "[[파일:크리스탈 소자.png": "[include(틀:명일방주/재화 및 재료, 이름=결정 부품)]",
        "[[파일:크리스탈 회로.png": "[include(틀:명일방주/재화 및 재료, 이름=결정 회로)]",
        "[[파일:크리스탈 전자 유닛.png": "[include(틀:명일방주/재화 및 재료, 이름=결정 전자 장치)]",
        "[[파일:전질염 번들.png": "[include(틀:명일방주/재화 및 재료, 이름=합성 소금 번들)]",
        "[[파일:전질염 팩.png": "[include(틀:명일방주/재화 및 재료, 이름= 합성 소금 팩)]",
        "[[파일:소결핵 응집 결정.png": "[include(틀:명일방주/재화 및 재료, 이름=핵결정체 소결물)]",
        "[[파일:갈색 섬유.png": "[include(틀:명일방주/재화 및 재료, 이름=퓨신 섬유)]",
        "[[파일:경화 섬유판.png": "[include(틀:명일방주/재화 및 재료, 이름=경화 섬유판)]",
        "[[파일:고리형 탄화수소 중합체.png": "[include(틀:명일방주/재화 및 재료, 이름=고리탄화수소 응집질)]",
        "[[파일:고리형 탄화수소 프리폼.png": "[include(틀:명일방주/재화 및 재료, 이름=고리탄화수소 프리폼)]",
        "[[파일:화합절삭액.png": "[include(틀:명일방주/재화 및 재료, 이름=중합 절삭유)]",
        "[[파일:절삭원액.png": "[include(틀:명일방주/재화 및 재료, 이름=절삭유 원액)]",
        "[[파일:열합금.png": "[include(틀:명일방주/재화 및 재료, 이름=열합금)]",
        "[[파일:열합금 덩어리.png": "[include(틀:명일방주/재화 및 재료, 이름=열합금 팩)]",
        "[[파일:반자연 용제.png": "[include(틀:명일방주/재화 및 재료, 이름=반합성 용제)]",
        "[[파일:정제된 용제.png": "[include(틀:명일방주/재화 및 재료, 이름=정제된 용제)]",
        "[[파일:D32강.png": "[include(틀:명일방주/재화 및 재료, 이름=D32강)]",
        "[[파일:바이폴라 나노칩.png": "[include(틀:명일방주/재화 및 재료, 이름=바이폴라 나노플레이크 칩)]",
        "[[파일:중합제.png": "[include(틀:명일방주/재화 및 재료, 이름=중합제)]",

        "[[파일:선봉 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=뱅가드 칩)]",
        "[[파일:근위 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=가드 칩)]",
        "[[파일:중장 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=디펜더 칩)]",
        "[[파일:저격 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=스나이퍼 칩)]",
        "[[파일:술사 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=캐스터 칩)]",
        "[[파일:의료 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=메딕 칩)]",
        "[[파일:지원 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=서포터 칩)]",
        "[[파일:특수 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=스페셜리스트 칩)]",
        "[[파일:선봉 칩셋.png": "[include(틀:명일방주/재화 및 재료, 이름=뱅가드 칩셋)]",
        "[[파일:근위 칩셋.png": "[include(틀:명일방주/재화 및 재료, 이름=가드 칩셋)]",
        "[[파일:중장 칩셋.png": "[include(틀:명일방주/재화 및 재료, 이름=디펜더 칩셋)]",
        "[[파일:저격 칩셋.png": "[include(틀:명일방주/재화 및 재료, 이름=스나이퍼 칩셋)]",
        "[[파일:술사 칩셋.png": "[include(틀:명일방주/재화 및 재료, 이름=캐스터 칩셋)]",
        "[[파일:의료 칩셋.png": "[include(틀:명일방주/재화 및 재료, 이름=메딕 칩셋)]",
        "[[파일:지원 칩셋.png": "[include(틀:명일방주/재화 및 재료, 이름=서포터 칩셋)]",
        "[[파일:특수 칩셋.png": "[include(틀:명일방주/재화 및 재료, 이름=스페셜리스트 칩셋)]",
        "[[파일:선봉 듀얼 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=뱅가드 듀얼 칩)]",
        "[[파일:근위 듀얼 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=가드 듀얼 칩)]",
        "[[파일:중장 듀얼 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=디펜더 듀얼 칩)]",
        "[[파일:저격 듀얼 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=스나이퍼 듀얼 칩)]",
        "[[파일:술사 듀얼 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=캐스터 듀얼 칩)]",
        "[[파일:의료 듀얼 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=메딕 듀얼 칩)]",
        "[[파일:지원 듀얼 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=서포터 듀얼 칩)]",
        "[[파일:특수 듀얼 칩.png": "[include(틀:명일방주/재화 및 재료, 이름=스페셜리스트 듀얼 칩)]",

        "[[파일:모듈 데이터 블록.png": "[include(틀:명일방주/재화 및 재료, 이름=모듈 데이터 칩)]",
        "[[파일:데이터 보충 조각.png": "[include(틀:명일방주/재화 및 재료, 이름=데이터 메모리)]",
        "[[파일:데이터 보충 기구.png": "[include(틀:명일방주/재화 및 재료, 이름=데이터 리더기)]",

        "|width=45]]": "]]",
        "|width=50]]": "]]",
        "|width=55]]": "]]",
        "|width=60]]": "]]",
        "|width=65]]": "]]",
        "|width=70]]": "]]",

    }

    replacements_2 = {
        ")]]": ")",
        "||<tablealign=center><tablewidth=1000><width=1000><nopad>": "||<tablewidth=100%><width=1000><nopad>",

        """=== 스탯 ===
{{{#!if S = '효과 = '틀:명일방주/전투 효과'
}}}
{{{#!if S = '효과 = '틀:명일방주/전투 효과'
}}}""": """=== 스탯 ===
{{{#!if S = '효과 = '틀:명일방주/전투 효과'
}}}""",

        """=== 능력치 ===
{{{#!if S = '효과 = '틀:명일방주/전투 효과'
}}}
{{{#!if S = '효과 = '틀:명일방주/전투 효과'
}}}""": """=== 능력치 ===
{{{#!if S = '효과 = '틀:명일방주/전투 효과'
}}}""",
        
        """=== 스킬 ===
{{{#!if S = '틀:명일방주/스킬 정보'
}}}
{{{#!if S = '틀:명일방주/스킬 정보'
}}}""": """=== 스킬 ===
{{{#!if S = '틀:명일방주/스킬 정보'
}}}""",
    }

      
    block = text
    for placeholder, value in replacements.items():
            block = block.replace(placeholder, value)



    for placeholder, value in replacements_2.items():
            block = block.replace(placeholder, value)

    output_text.delete("1.0", "end")
    output_text.insert("1.0", block)


try:
  ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Windows 8.1 이상
except Exception:
  try:
    ctypes.windll.user32.SetProcessDPIAware()  # 이전 Windows 버전 호환
  except Exception:
    pass



root = tk.Tk()
root.title("Arknights Wiki File Text Formatter")
root.geometry("950x950")

input_text = tk.Text(root, height=18, wrap="word")
input_text.pack(fill="both", expand=True, padx=10, pady=5)

ttk.Button(root, text="Convert", command=convert_all).pack(pady=5)

ttk.Label(root, text="Converted output:").pack(anchor="w", padx=10)

output_text = tk.Text(root, height=18, wrap="word")
output_text.pack(fill="both", expand=True, padx=10, pady=(5, 10))

root.mainloop()