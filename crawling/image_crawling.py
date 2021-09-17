from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

argument = {"keywords":"short sleeve dress", "limit":300, "print_urls":True, "chromedriver":"chromedriver.exe", "format":"jpg"}
paths = response.download(argument)
print(paths)