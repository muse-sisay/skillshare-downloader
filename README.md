# Skillshare video downloader in python

I needed offline access to some skillshare courses I wanted to take while on vacation.
Video download is only available in the skillshare mobile apps and I didn't want to
choose between shaky 3G streaming or watching on a tiny mobile screen so I put together a
quick and dirty video downloader in python.

### Support your content creators, do NOT use this for piracy!

You will need a skillshare premium account to access premium content.
This script will not handle login for you.

1. Log-in to skillshare in your browser and open up the developer console.
(cmd-shift-c for chrome on mac) or go to tools-> web developer -> web console

2. Use it to grab your cookie by typing:
```
document.cookie
```

3. Copy-paste cookie from developer console (without " the quotes if present) into example script.

#### Example:
```
from downloader import Downloader

cookie = """
ADD YOUR COOKIE HERE
"""

# Download path
course_folder = ''

dl = Downloader(cookie=cookie , download_path= course_folder)

# download by class URL:
dl.download_course_by_url('https://www.skillshare.com/classes/Art-Fundamentals-in-One-Hour/189505397')

# or by class ID:
# dl.download_course_by_class_id(189505397)
```

4. (Optionally) run with docker and docker-compose:
```
docker-compose build
docker-compose run --rm ssdl python example.py
```
