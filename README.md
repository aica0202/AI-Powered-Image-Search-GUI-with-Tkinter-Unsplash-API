# AI-Powered-Image-Search-GUI-with-Tkinter-Unsplash-API

A Python desktop GUI application built with **CustomTkinter** that allows users to search and display high-quality images from the **Unsplash API**. This project features a modern interface, responsive image display, carousel navigation, and search history for a smooth image browsing experience.

## 📌 About the Project

**AI-Powered Image Search GUI** is designed to make image searching simple, fast, and visually interactive. Users can enter a keyword, fetch related images from Unsplash, and browse the results directly inside the desktop application.

This project is created for educational, portfolio, and Python GUI development practice. It also demonstrates API integration, image handling, and user-friendly interface design.

## 🌐 Features

* Search images by keyword
* Fetch images using the Unsplash API
* Display high-quality image results
* Carousel-style image navigation
* Responsive image resizing
* Search history tracking
* Modern desktop interface
* Clean and beginner-friendly layout
* Error handling for empty searches or failed API requests
* Built with Python and CustomTkinter

## 🛠️ Built With

* Python
* CustomTkinter
* Unsplash API
* Requests
* Pillow / PIL
* JSON
* API Integration

## 📁 Project Structure

```text
AI-Powered-Image-Search-GUI-with-Tkinter-Unsplash-API/
│── main.py
│── config.py
│── requirements.txt
│── README.md
│
├── assets/
│   ├── icons/
│   └── images/
│
├── modules/
│   ├── api_handler.py
│   ├── image_viewer.py
│   ├── search_history.py
│   └── carousel.py
```

## 🚀 How to Run the Project

1. Download or clone the repository.
2. Install the required dependencies.
3. Add your Unsplash API access key in `config.py`.
4. Run the main Python file.

```bash
pip install -r requirements.txt
python main.py
```

## 🔑 API Setup

Create a free developer account on Unsplash and generate an API access key.

Add your API key inside `config.py`:

```python
UNSPLASH_ACCESS_KEY = "your_api_key_here"
```

## 🎯 Purpose of the Project

This project was developed to:

* Practice Python GUI development
* Learn how to connect Python apps with external APIs
* Build a modern desktop application using CustomTkinter
* Display and manage images dynamically
* Practice responsive image handling
* Create a portfolio-ready AI-inspired image search project

## 🖼️ Sample Search Flow

```text
Search Keyword: Nature
API Source: Unsplash
Result Type: Image Gallery
View Mode: Carousel
Search History: Saved locally
```

## 🔮 Future Improvements

* Add image download feature
* Add favorite images section
* Add dark and light mode toggle
* Add advanced filters by orientation or color
* Add AI-based image recommendations
* Add offline search history database
* Add pagination for more image results
* Add image preview modal
* Add category-based browsing

## ⚠️ Disclaimer

This project is for educational and portfolio purposes only. Images are fetched from Unsplash through its API and remain owned by their respective creators.

This project is not affiliated with, endorsed by, or officially connected to Unsplash.

## 👨‍💻 Author

Created as a Python GUI project to practice API integration, desktop application design, image handling, and interactive search functionality.

## 📌 License

This project is open for educational, portfolio, and personal learning use.
