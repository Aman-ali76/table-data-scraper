# 🔍 Table Data Scraper (with Pagination & Resume)

A Python-based web scraper that extracts tabular data from [scrapethissite.com](https://www.scrapethissite.com/pages/forms/) and saves each page's content into separate CSV files. It includes a smart resume mechanism to continue scraping from the last saved page if interrupted.

## 🌐 Website Target

* `https://www.scrapethissite.com/pages/forms/?page_num=1`

## ✨ Key Features

* Extracts structured data from HTML tables across multiple pages
* Handles pagination automatically
* Saves each page’s data in the `CSV/` directory (e.g., `1.csv`, `2.csv`, ...)
* Resume capability via a `num.txt` tracker file — continues from last page after interruption
* Graceful termination on user interrupt

## 💡 Real-Life Use Case

Ideal for scraping datasets displayed in paginated tables, such as:

* Economic indicators from statistics portals
* Sports statistics listings
* Public government or open data platforms

## 💪 Key Strength

Even if the scraper is stopped (e.g., using Ctrl+C), it saves progress in `num.txt` and upon next run begins from the next page, ensuring no data duplication or loss.

## 💻 Technologies & Modules

* Python
* BeautifulSoup (HTML parsing)
* requests (HTTP requests)
* pandas (data handling)
* os (file system operations)

## ⚙️ How to Run

1. Ensure Python 3.x is installed.
2. Install dependencies:

   ```bash
   pip install beautifulsoup4 requests pandas
   ```
3. Place `main.py` in your project folder and run:

   ```bash
   python main.py
   ```

## 📂 Output

* **CSV files**: `CSV/1.csv`, `CSV/2.csv`, …
* **Tracker file**: `num.txt` records the last scraped page number

## 📁 Suggested Repo Structure

```
table-data-scraper/
├── main.py
├── README.md
└── CSV/            # Generated output
    ├── 1.csv
    └── ...
```

---
