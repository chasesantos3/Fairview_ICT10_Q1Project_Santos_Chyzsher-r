from js import document

def generate_message():
    name = document.getElementById("name").value.strip()
    age = document.getElementById("age").value.strip()
    school = document.getElementById("school").value.strip()

    profile = f"""
﹒୨𝑒   ﾟ ˖ Student Profile ﹒୨𝑒   ﾟ ˖
Name    : {name}
Age     : {age}
School  : {school}

Notes:
{name} is currently {age} years old and studies at {school}.
This information was displayed using a multi-line string in Python via PyScript.
"""

    output_div = document.getElementById("output")
    if output_div is not None:
        output_div.innerText = profile
