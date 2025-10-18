# News Explorer

A modern, cross-language news dashboard built with **Python**, **Tkinter**, and **NewsAPI**.
Fetch top articles by category and language, view them in a scrollable, card-style interface, complete with images and clickable links.

---

## **Features**

*  Fetch news in **multiple languages** (English, Greek, German, French, Italian, Spanish).
*  **Extended categories** (business, sports, technology, politics, health, science, travel, lifestyle, music, and more).
*  **Card-style articles** with:

  * Category label
  * Title (clickable, opens in browser)
  * Description
  * Image thumbnail (if available)
*  **Responsive GUI** with hover effects.
*  **Scrollable feed** for multiple articles.
*  **Loading splash screen** while fetching data.
*  **Asynchronous image fetching** for fast display.
*  API key stored securely via **environment variable** or `.env` file.
*  Easy to run in **VSCode**, terminal, or any Python IDE.

---

## **Setup Instructions**

###  Clone the repository

```bash
git clone https://github.com/VasilisKokotakis/NewsAPI-Headlines-Fetcher.git
cd News_Top_Articles
```

---

###  Create and activate a virtual environment

```bash
python3 -m venv env
source env/bin/activate   # Linux/macOS
env\Scripts\activate      # Windows
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

**Requirements file:**

```
requests
pillow
python-dotenv
```

---

### Set your NewsAPI key

#### Option A: Environment variable

```bash
export NEWSAPI_KEY="your_api_key_here"    # Linux/macOS
setx NEWSAPI_KEY "your_api_key_here"      # Windows
```

#### Option B: `.env` file

Create a `.env` file in the project root:

```
NEWSAPI_KEY=your_api_key_here
```

The script will automatically load it using `python-dotenv`.

---

### Run the app

```bash
python News.py
```

> In VSCode: Make sure the **interpreter** is set to your virtual environment (`env/bin/python3`). Then click **Run**.

---

## **Usage**

1. Select a **language** from the dropdown.
2. Select a **category** from the dropdown.
3. Click **Get News**.
4. A new window will open with **scrollable articles**:

   * Click the title or anywhere on the card to open the article in your browser.
   * Images load asynchronously for a smooth experience.

---

## **Optimizations**

* **Asynchronous image fetching** for fast loading.
* **Loading splash screen** while fetching articles.
* **Reduced number of articles** by default (20) to improve performance.
* **Hover effect** on cards for better interactivity.

---

## **Future Improvements**

* Lazy load images for very long feeds.
* Multi-column layout for a real “news portal” feel.
* Export news feed to TXT or PDF.
* Search/filter within fetched articles.

---

## **Screenshots**

<img width="500" height="420" alt="image" src="https://github.com/user-attachments/assets/94d29e31-ae35-4510-a7cd-2a7cf2cd2439" />
<img width="900" height="621" alt="image" src="https://github.com/user-attachments/assets/2d7d9844-ed17-42ac-9e98-01f6956ecbda" />


---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
