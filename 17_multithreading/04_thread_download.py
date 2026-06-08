import threading
import time
import requests


def download(url):
    print(f"Starting download from {url}")
    response = requests.get(url)
    print(f"Finish downloading from {url}, size: {len(response.content)} bytes")


urls = [
    "https://img.magnific.com/free-photo/photorealistic-moose-studio_23-2151543575.jpg",
    "https://w7.pngwing.com/pngs/43/168/png-transparent-moose-deer-elk-drawing-deer-antler-animals-monochrome.png",
]


start = time.time()
threads = []

for url in urls:
    t1 = threading.Thread(target=download, args=(url,))
    t1.start()
    threads.append(t1)

for thread in threads:
    thread.join()

end = time.time()

print(f"Pictures Donwload Finished in {end - start:.2f} seconds")
