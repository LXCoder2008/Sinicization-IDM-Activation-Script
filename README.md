# 🌟 汉化IDM 激活脚本

[English Version](README_EN.md)	

欢迎使用 **汉化IDM 激活脚本** 项目！本项目帮助您通过百度翻译API自动翻译 `.cmd` 文件中的特定文本片段。该脚本设计用于识别并翻译符合特定模式的文本，特别是 `"call :_color %color% "要翻译的文本""` 形式的内容。

## 🚀 功能特色

- **自动翻译**：使用百度翻译API自动翻译 `.cmd` 文件中的文本内容。
- **模式匹配**：查找并替换特定的文本模式，以确保翻译的准确性。
- **手动覆盖**：保留特定短语或句子的自定义翻译。

## 🛠 使用方法

1. **安装依赖**：确保已安装Python和`requests`库。
   ```bash
   pip install requests
   ```

2. **配置API凭证**：将脚本中的 `appid` 和 `secret_key` 更新为你的百度翻译API凭证。
3. **运行脚本**：执行脚本以翻译 `.cmd` 文件。
   
   ```bash
   python translate_script.py
   ```

## 📄 示例

假设你的 `IAS.cmd` 文件中有以下内容：

```cmd
call :_color %red% "This is an example text."
```

运行脚本后，它将被翻译为：

```cmd
call :_color %red% "这是一个示例文本。"
```

## 📂 文件结构

- **translate_script.py**: 处理翻译的主要脚本。
- **IAS.cmd**: 包含原始命令的输入文件。
- **IAS_translated.cmd**: 翻译后的输出文件。

## 👨‍💻 贡献指南

欢迎贡献！随时 fork 本仓库，提交问题或创建 pull request。

## 📝 许可证

此项目采用 MIT 许可证。详情请参见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

特别感谢百度翻译API的开发者和Python社区，他们提供了出色的工具和库！

---

编程愉快！💻🎉



