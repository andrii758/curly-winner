# Personal Blog Project 

A clean, minimalist personal blog built with the Django framework. This project features a dual-section architecture: a public-facing area for readers and a secure administrative dashboard for content management.


### Guest Section (Public)
* **Home Page**: Displays a curated list of all published articles with snippets and publication dates.
* **Article Page**: A dedicated reading view for full content, optimized for typography and readability.
* **Responsive Design**: Fully compatible with mobile, tablet, and desktop devices via Bootstrap 5.
* **Custom 404 Error Page**: A Google-inspired minimalist error page for better user experience.

### Admin Section (Management)
* **Dashboard**: Integrated directly into the UI, allowing the superuser to manage posts without leaving the site.
* **Add Article Page**: A functional form to publish new content with fields for title, body, and publication date.
* **Edit Article Page**: Seamlessly update existing content with pre-filled forms.
* **Delete Article Page**: A secure confirmation step to prevent accidental deletion of posts.
* **Access Control**: Strict permission checks ensuring only the `Superuser` can access management tools.

##  Tech Stack
* **Backend**: Python 3.x, Django 5.x
* **Frontend**: Bootstrap 5, Django Crispy Forms
* **Database**: SQLite
* **Typography**: Inter Font Family

##  Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/andrii758/curly-winner.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    # .venv\Scripts\activate  # Windows
    ```

3.  **Install dependencies from requirements.txt:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
---
*Developed as part of https://roadmap.sh/projects/personal-blog
