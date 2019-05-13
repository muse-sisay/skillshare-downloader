from downloader import Downloader

cookie = ''

# Download path
course_folder = ''

dl = Downloader(cookie=cookie , download_path= course_folder)

# download by class URL:
dl.download_course_by_url('https://www.skillshare.com/classes/Art-Fundamentals-in-One-Hour/189505397')

# or by class ID:
# dl.download_course_by_class_id(189505397)
