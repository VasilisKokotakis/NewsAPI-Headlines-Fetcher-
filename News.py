import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import io
import webbrowser
import threading
import os

API_KEY = os.environ.get("NEWSAPI_KEY")
if not API_KEY:
    raise ValueError("Please set the NEWSAPI_KEY environment variable!")

EVERYTHING_URL = "https://newsapi.org/v2/everything"

LANGUAGES = {
    "English": "en",
    "Greek": "el",
    "German": "de",
    "French": "fr",
    "Italian": "it",
    "Spanish": "es",
}

CATEGORIES = [
    "general", "business", "entertainment", "health",
    "science", "sports", "technology", "politics",
    "world", "finance", "education", "travel",
    "environment", "fashion", "food", "gaming",
    "lifestyle", "music", "culture", "automotive"
]

CATEGORY_COLORS = {
    "general": "#95a5a6", "business": "#2ecc71", "entertainment": "#e67e22",
    "health": "#1abc9c", "science": "#9b59b6", "sports": "#3498db",
    "technology": "#f39c12", "politics": "#e74c3c", "world": "#34495e",
    "finance": "#16a085", "education": "#8e44ad", "travel": "#d35400",
    "environment": "#27ae60", "fashion": "#c0392b", "food": "#e67e22",
    "gaming": "#9b59b6", "lifestyle": "#2980b9", "music": "#d35400",
    "culture": "#7f8c8d", "automotive": "#34495e"
}


def get_articles(category, language_code, page_size=20):
    """Fetch articles (limited for faster loading)"""
    query_parameters = {
        "q": category,
        "language": language_code,
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": API_KEY,
    }
    response = requests.get(EVERYTHING_URL, params=query_parameters)
    if response.status_code != 200:
        messagebox.showerror("Error", f"API request failed: {response.status_code}")
        return []
    return response.json().get("articles", [])


def open_url(url):
    webbrowser.open_new_tab(url)


def fetch_image(url, max_size=(150, 100)):
    """Fetch and resize image from URL"""
    if not url:
        return None
    try:
        response = requests.get(url, timeout=5)
        img_data = response.content
        img = Image.open(io.BytesIO(img_data))
        img.thumbnail(max_size)
        return ImageTk.PhotoImage(img)
    except:
        return None


def display_articles(articles, category, language):
    """Display articles in scrollable card layout"""
    if not articles:
        messagebox.showinfo("No Articles", f"No {category} articles found in {language}.")
        return

    results_window = tk.Toplevel(root)
    results_window.title(f"{language} - {category} News")
    results_window.geometry("900x600")
    results_window.configure(bg="#f4f4f9")

    canvas = tk.Canvas(results_window, bg="#f4f4f9", highlightthickness=0)
    scrollbar = ttk.Scrollbar(results_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f4f4f9")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    image_refs = []

    for article in articles:
        card = tk.Frame(scrollable_frame, bg="white", bd=1, relief="solid")
        card.pack(fill="x", padx=15, pady=10)
        card.bind("<Enter>", lambda e, c=card: c.configure(bg="#ecf0f1"))
        card.bind("<Leave>", lambda e, c=card: c.configure(bg="white"))

        title = article.get("title", "No Title")
        url = article.get("url", "")
        description = article.get("description", "No Description")
        image_url = article.get("urlToImage", "")

        cat_color = CATEGORY_COLORS.get(category, "#95a5a6")
        tk.Label(card, text=category.upper(), bg=cat_color, fg="white", font=("Helvetica", 10, "bold"), padx=5, pady=2).pack(anchor="w", padx=5, pady=5)

        content_frame = tk.Frame(card, bg="white")
        content_frame.pack(fill="x", padx=5, pady=5)

        # Load image asynchronously
        def load_image_async(frame, img_url):
            img = fetch_image(img_url)
            if img:
                img_label = tk.Label(frame, image=img, bg="white")
                img_label.image = img
                img_label.pack(side="left", padx=(0, 10))
                image_refs.append(img)

        threading.Thread(target=lambda f=content_frame, u=image_url: load_image_async(f, u), daemon=True).start()

        text_frame = tk.Frame(content_frame, bg="white")
        text_frame.pack(fill="both", expand=True, side="left")

        title_label = tk.Label(text_frame, text=title, font=("Helvetica", 14, "bold"), fg="#2c3e50", cursor="hand2", wraplength=700, justify="left")
        title_label.pack(anchor="w")
        tk.Label(text_frame, text=description, font=("Helvetica", 12), fg="#7f8c8d", wraplength=700, justify="left").pack(anchor="w", pady=(2, 0))

        if url:
            card.bind("<Button-1>", lambda e, link=url: open_url(link))
            for child in card.winfo_children():
                child.bind("<Button-1>", lambda e, link=url: open_url(link))
            for sub_child in content_frame.winfo_children():
                sub_child.bind("<Button-1>", lambda e, link=url: open_url(link))
            for sub_child in text_frame.winfo_children():
                sub_child.bind("<Button-1>", lambda e, link=url: open_url(link))

    results_window.image_refs = image_refs  # keep references alive


def fetch_news():
    selected_lang = language_var.get()
    selected_cat = category_var.get()

    if not selected_lang or not selected_cat:
        messagebox.showwarning("Missing input", "Please select both language and category!")
        return

    # Show loading splash
    loading = tk.Toplevel(root)
    loading.title("Loading...")
    tk.Label(loading, text="Fetching news articles...", font=("Helvetica", 14)).pack(padx=20, pady=20)
    loading.geometry("300x100")
    loading.transient(root)
    loading.grab_set()

    lang_code = LANGUAGES[selected_lang]

    # Fetch articles in a background thread
    def background_fetch():
        articles = get_articles(selected_cat, lang_code)
        root.after(0, lambda: display_articles(articles, selected_cat, selected_lang))
        root.after(0, loading.destroy)  # close loading splash

    threading.Thread(target=background_fetch, daemon=True).start()


# GUI setup
root = tk.Tk()
root.title("🌐 News Explorer")
root.geometry("500x400")
root.configure(bg="#f4f4f9")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TCombobox", padding=5, relief="flat", font=("Helvetica", 12))
style.map("TCombobox",
          fieldbackground=[('readonly', 'white')],
          selectbackground=[('readonly', '#cce6ff')],
          selectforeground=[('readonly', '#000')])

tk.Label(root, text="🌐 News Explorer", font=("Helvetica", 22, "bold"), bg="#f4f4f9", fg="#2c3e50").pack(pady=15)

tk.Label(root, text="Select Language:", font=("Helvetica", 12), bg="#f4f4f9").pack(pady=(5, 0))
language_var = tk.StringVar()
language_menu = ttk.Combobox(root, textvariable=language_var, values=list(LANGUAGES.keys()), state="readonly", width=30)
language_menu.pack(pady=5)

tk.Label(root, text="Select Category:", font=("Helvetica", 12), bg="#f4f4f9").pack(pady=(10, 0))
category_var = tk.StringVar()
category_menu = ttk.Combobox(root, textvariable=category_var, values=CATEGORIES, state="readonly", width=30)
category_menu.pack(pady=5)

fetch_button = tk.Button(root, text="Get News", command=fetch_news, bg="#4a90e2", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5, activebackground="#357ABD", activeforeground="white")
fetch_button.pack(pady=20)

root.mainloop()
