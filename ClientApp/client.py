import requests
import time
import sys

url = "http://webapp:5000/"

print("🚀 Клиент запущен. Ожидание инициализации веб-сервера (5 сек)...", flush=True)
time.sleep(5)

while True:
    try:
        response = requests.get(url)
        print(f"[УСПЕШНО] Статус: {response.status_code} | Ответ: {response.text.strip()}", flush=True)
    except Exception as e:
        print(f"[ОШИБКА] Не удалось подключиться к {url}. Причина: {e}", flush=True)
    
    time.sleep(3)
