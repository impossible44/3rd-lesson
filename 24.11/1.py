import time 
def download(url):
    time.sleep(1)
    return f"Данные с{url}"
start = time.time()
for url in ["site-1", "site-2", "site-3"]:
    print(download(url))
print(f"Ушло {time.time()-start:.1f} c")