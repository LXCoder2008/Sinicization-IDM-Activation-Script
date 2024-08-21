import requests
import hashlib
import random
import re

# 百度翻译API的配置信息 http://api.fanyi.baidu.com/product/111
appid = '你的 ID'
secret_key = '你的 KEY'
api_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

def baidu_translate(query, from_lang='en', to_lang='zh'):
    salt = random.randint(32768, 65536)
    sign = appid + query + str(salt) + secret_key
    sign = hashlib.md5(sign.encode()).hexdigest()
    
    params = {
        'q': query,
        'from': from_lang,
        'to': to_lang,
        'appid': appid,
        'salt': salt,
        'sign': sign
    }
    
    response = requests.get(api_url, params=params)
    result = response.json()
    
    if "trans_result" in result:
        return result['trans_result'][0]['dst']
    else:
        return query  # 如果翻译失败，返回原始内容

# 读取 IAS.cmd 文件内容
input_file_path = "IAS.cmd"
output_file_path = "IAS_translated.cmd"

with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 使用正则表达式找到所有 "call :_color %颜色% "提示"" 形式的内容
matches_prompt = re.findall(r'call :_color\s+(%\S+%)\s+"([^"]+)"', content)

# 翻译找到的内容并替换原文
for match in matches_prompt:
    color_placeholder, text_to_translate = match
    translated_text = baidu_translate(text_to_translate)
    content = content.replace(f'call :_color {color_placeholder} "{text_to_translate}"', f'call :_color {color_placeholder} "{translated_text}"')

manual_translations = {
    "title  IDM Activation Script %iasver%": "title  IDM 激活脚本 %iasver%",
    "This script is NOT working with latest IDM.": "此脚本不适用于最新的 IDM。",
    "[1] Freeze Trial": "[1] 冻结试用期",
    "[2] Activate": "[2] 激活",
    "[3] Reset Activation / Trial": "[3] 重置激活/试用期",
    "[4] Download IDM": "[4] 下载 IDM",
    "[5] Help": "[5] 帮助",
    "[0] Exit": "[0] 退出",
    "Enter a menu option in the Keyboard": "在键盘中输入菜单选项"
}

for english_text, chinese_text in manual_translations.items():
    content = re.sub(re.escape(english_text), chinese_text, content)

# 写入翻译后的内容到新的文件中，并保存为 ANSI 编码
with open(output_file_path, 'w', encoding='mbcs', errors='replace') as file:
    file.write(content)

print(f"请查看 '{output_file_path}' 文件。")
