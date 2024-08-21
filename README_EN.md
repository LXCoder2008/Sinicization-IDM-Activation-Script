# 🌟 Sinicization IDM Activation Script

[简体中文](README.md)

Welcome to the **Sinicization IDM Activation Script** project! This project helps you automate the translation of specific text segments in `.cmd` files using the Baidu Translation API. The script is designed to identify and translate text strings that follow a particular pattern, specifically in the form of `"call :_color %color% "text to be translated""`.

## 🚀 Features

- **Automatic Translation**: Translates text within your `.cmd` files using the Baidu Translation API.
- **Pattern Matching**: Finds and replaces specific text patterns to ensure accurate translation.
- **Manual Overrides**: Preserves custom translations for specific phrases or sentences.

## 🛠 How It Works

1. **Install Dependencies**: Make sure you have Python installed and the `requests` library.
   ```bash
   pip install requests
   ```

2. **Configure API Credentials**: Update the `appid` and `secret_key` in the script with your Baidu Translation API credentials.
3. **Run the Script**: Execute the script to translate your `.cmd` file.
   ```bash
   python translate_script.py
   ```

## 📄 Example

Suppose you have the following line in your `IAS.cmd` file:

```cmd
call :_color %red% "This is an example text."
```

After running the script, it will be translated as:

```cmd
call :_color %red% "这是一个示例文本。"
```

## 📂 Files

- **Sinicization IDM activation script.py**: The main script that handles translation.
- **IAS.cmd**: The input file containing the original commands.
- **IAS_translated.cmd**: The output file with translated text.

## 👨‍💻 Contributing

We welcome contributions! Feel free to fork the repository, submit issues, or create pull requests.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

Special thanks to the developers of the Baidu Translation API and the Python community for their awesome tools and libraries!

---

Happy Coding! 💻🎉



