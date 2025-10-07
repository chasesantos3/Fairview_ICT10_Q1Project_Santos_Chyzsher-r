from js import document

def submit_order():
    name = document.getElementById("name").value.strip()
    flavor = float(document.getElementById("flavor").value)
    sauce = float(document.getElementById("sauce").value)
    drink = float(document.getElementById("drink").value)
    total = flavor + sauce + drink

    result = f"✨ Order Completed! ✨\n{name}, your total is ₱{total:.2f}."
    document.getElementById("result").innerText = result
