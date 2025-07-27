# ✅ Disnake Verification Bot

Ein einfacher Discord Verifizierungsbot in Python mit `disnake`.  
Alles wird direkt im Code eingestellt — keine Slash Commands, keine externe Konfiguration.

---

## 🚀 Funktionen

- Sendet beim Start automatisch eine Nachricht mit einem „✅ Verify“-Button in einem definierten Kanal.
- Nutzer klicken auf den Button und bekommen eine Rolle.
- Optional wird eine andere Rolle entfernt.
- Einfach zu konfigurieren über Variablen im Code.

---

## ⚙️ Einrichtung & Nutzung

### 1. Bot erstellen & Token holen

- Erstelle deinen Bot im [Discord Developer Portal](https://discord.com/developers/applications).
- Kopiere den Bot-Token.

### 2. Bot konfigurieren

Öffne deine Python-Datei (z. B. `bot.py`) und ändere diese Werte oben im Code:

```python
TOKEN = "DEIN_BOT_TOKEN"

GUILD_ID = 123456789012345678       # Deine Server-ID
CHANNEL_ID = 123456789012345678     # Kanal-ID für die Verifizierungsnachricht
ROLE_TO_ADD_ID = 123456789012345678 # Rolle, die vergeben wird
ROLE_TO_REMOVE_ID = 0               # Optional: Rolle, die entfernt wird (0 = keine)
```

### 3. Abhängigkeiten installieren

```bash
pip install disnake
```

### 4. Bot Starten

```bash
python bot.py # oder wie du dein file gennant hast
```

Bei Fehlern oder Hilfe meinen discord joinen: https://discord.gg/shadowbyteofficial
