from mixpanel import Mixpanel
import re


mp = Mixpanel("4eff0766b8007f63e7192dd2228b486b")


def improve_text(text, user_id):
    # Replace "z" with "s" in appropriate words
    text = re.sub(r"\b(.*?)(iz)(e|ed|ing|es|ation|ationed|ing)\b", r"\1is\3", text)

    # Replace double letters like "bb" with "b"
    text = re.sub(r"bb", "b", text)

    # Convert passive voice to active voice where possible
    text = re.sub(r"\b(is|was|were|been)\b (.*?ed)\b", r"\2", text)

    # Replace weak verbs with stronger alternatives (example: "is" -> "exists as")
    text = re.sub(r"\bis\b", "exists as", text)
    text = re.sub(r"\bare\b", "remain", text)

    # Break up long sentences
    # text = re.sub(r"(\w{10,}), (\w)", r"\1. \2", text)

    # Track the improvement process with Mixpanel
    mp.track(
        user_id,
        "Text Improved",
        {
            "original_text": text,
            "improved_text": text,
        },
    )

    return text


# Example
user_id = "3398116"
input_text = "Up in Pierre, South Dakota, State Historian Doane Robinson, a scholar with patriotism, an extraordinary love for beauty and{17} very little knowledge of magnificent finance, looked at the news photographs of the Stone Mountain project and studied the rotogravure outlines of what the sculptured cliff would look like when Gutzon Borglum finished with it. And he wondered that nobody had ever thought of trying a similar scheme in the mountains of South Dakota, the Black Hills. He wrote a letter to Borglum inquiring why."
ouput_text = improve_text(input_text, user_id)
print(ouput_text)
