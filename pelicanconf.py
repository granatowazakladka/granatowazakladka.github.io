from os import getenv
from datetime import datetime

# Site settings
AUTHOR = 'Ada Sierocińska'
SITENAME = "Granatowa Zakładka"
SITESUBTITLE = "każda książka ma swój kolor"
SITEURL = getenv("SITEURL", "")
TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = 'pl'
LOCALE = 'pl_PL.UTF-8'
PROFILE_IMAGE = 'theme/images/granatowazakladka.jpg'

# Header settings
# HEADER_COVER = "theme/images/kaer-morhen.jpg"

# Footer settings
COPYRIGHT_YEAR = datetime.now().year
SHOW_CREDITS = True
FOOTER_TEXT = f"Ada Sierocińska &copy; {COPYRIGHT_YEAR}"

# Theme
THEME = 'theme'
THEME_STATIC_DIR = 'theme'

# Content settings
PATH = "content"
STATIC_PATHS = [
    'images',
    'files'
]

ARCHIVES_SAVE_AS = ARCHIVES_URL = 'archives.html'
AUTHORS_SAVE_AS = AUTHORS_URL = 'authors.html'
CATEGORIES_SAVE_AS = CATEGORIES_URL = 'categories.html'
TAGS_SAVE_AS = TAGS_URL = 'tags.html'

ARTICLE_PATHS = ['posts']
ARTICLE_SAVE_AS = 'post/{date:%Y}/{slug}.html'
ARTICLE_URL = 'post/{date:%Y}/{slug}.html'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True
DISPLAY_CATEGORIES_ON_MENU = True

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = "Różności"

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

INSTRAGRAM_LINK = "https://www.instagram.com/granatowazakladka/"
FACEBOOK_LINK = "https://www.facebook.com/GranatowaZakladka/"

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True
