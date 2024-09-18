import google.generativeai as genai


def text_only_gen(promt):
    genai.configure(api_key="AIzaSyAc8RGnoFmSTMFcDuPXLTjtZJuDqS5QBCM")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(promt)
    print(response.text)


def tex_input(promt):
    text = input(promt)
    return text


if __name__ == "__main__":
    while True:
        text = tex_input("Please Enter Your Text: ")
        text_only_gen(text)