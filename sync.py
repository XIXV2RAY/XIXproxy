import os
import requests

SUB_URL = os.getenv("SUB_URL")

def fetch():
    r = requests.get(SUB_URL, timeout=15)
    r.raise_for_status()

    lines = r.text.splitlines()

    # حذف خالی + تکراری
    unique = list(dict.fromkeys([x.strip() for x in lines if x.strip()]))

    return "\n".join(unique)

def save(data):
    with open("PROXY.txt", "w", encoding="utf-8") as f:
        f.write(data + "\n")

def main():
    data = fetch()
    save(data)
    print(f"Saved {len(data.splitlines())} proxies")

if __name__ == "__main__":
    main()
