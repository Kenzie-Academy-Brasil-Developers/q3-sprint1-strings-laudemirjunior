def standardize_names(character_name):
    return character_name.strip().replace(" ", "-")

def standardize_title(title: str):
    return title.title()

def standardize_text(text: str):
    text = text.split(". ")
    output = []
    for i in text:
        i = f"{i[0].upper()}{i[1:]}"
        output.append(i)
    return ". ".join(output)

def title_creator(text):
    h = "--------------------"
    return f"{h}{text.title()}{h}"

def text_merge(text_of_blog_a: str, text_of_blog_b: str):
    if text_of_blog_a[-1] == ".":
        text_of_blog_a = text_of_blog_a[0].upper() + text_of_blog_a[1:-1]
    else:
        text_of_blog_a = text_of_blog_a[0].upper() + text_of_blog_a[1:]
    text_of_blog_a = " ".join(text_of_blog_a.split())
    text_of_blog_b = text_of_blog_b[0].lower() + text_of_blog_b[1:]
    text_of_blog_b = " ".join(text_of_blog_b.split())
    res_a = standardize_text(text_of_blog_a)
    res_b = standardize_text(text_of_blog_b)
    res_b = res_b[0].lower() + res_b[1:]
    return f"{res_a} {res_b}"