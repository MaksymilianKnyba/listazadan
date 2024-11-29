# Wybierz oficjalny obraz Pythona jako bazę
FROM python:3.9-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj wszystkie pliki do kontenera
COPY . /app

# Zainstaluj zależności z requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Otwórz port 5000
EXPOSE 5000

# Uruchom aplikację Flask
CMD ["python3", "listazadan.py"]
