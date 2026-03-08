import os

def save_report(topic, content):

    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    filename = topic.replace(" ", "_") + ".txt"
    path = os.path.join("data", filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path
