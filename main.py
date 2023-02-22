import requests
from io import BytesIO
from PIL import Image
import tkinter as tk


def get_player_data(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def get_player_skin(username):
    data = get_player_data(username)
    if data is not None:
        uuid = data["id"]
        skin_url = f"https://crafatar.com/skins/{uuid}"
        return (data["name"], skin_url)
    else:
        return None


def show_player_skin(username):
    skin_url = get_player_skin(username)[1]
    response = requests.get(skin_url)
    img = Image.open(BytesIO(response.content))
    img.show()


def show_player_skin_gui():
    window = tk.Tk()
    window.title("Minecraft Player Skin Viewer")

    tk.Label(window, text="Enter player username:").grid(row=0, column=0)
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    def show_skin():
        username = username_entry.get()
        show_player_skin(username)

    tk.Button(window, text="Show Skin", command=show_skin).grid(row=1, column=0, columnspan=2)

    window.mainloop()


if __name__ == "__main__":
    show_player_skin_gui()