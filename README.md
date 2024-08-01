<div align="center">
    <h1>Argos API</h1>
    <h4>API built with <a href="https://github.com/fastapi/fastapi">FastAPI</a> for translations using <a href="https://github.com/argosopentech/argos-translate">Argos Translate</a>.</h4>
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI Badge"/>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
    <img src="https://img.shields.io/badge/Argos%20Translate-029e74?style=for-the-badge&logo=argo&logoColor=white" alt="Argos Translate Badge"/>
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Badge"/>
</div>

## Overview

This document provides an overview of the Argos API built with [FastAPI](https://github.com/fastapi/fastapi), leveraging the Argos Translate library for translations. For more details on Argos Translate, visit the [Argos Translate GitHub repository](https://github.com/argosopentech/argos-translate).

## Installation and Configuration

### Using Docker

#### Prerequisites

-   Docker
-   Docker Compose

#### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/Jaro-c/Argos-API.git
cd Argos-API
```

2. **Create a `.env` file:**

```env
API_PORT=12448
LANGUAGES="en:ur,en:es"
```

3. **Build and run the Docker containers:**

```bash
docker-compose up --build
```

4. **Access the API:**

Open your browser and go to `http://localhost:12448`

### Without Docker

#### Prerequisites

-   Python 3.12+
-   pip

#### Steps

1.  **Clone the repository:**

```bash
git clone https://github.com/Jaro-c/Argos-API.git
cd Argos-API
```

2.  **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv/Scripts/activate`
```

3.  **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4.  **Create a `.env` file:**

```env
API_PORT=12448
LANGUAGES="en:ur,en:es"
```

5.  **Run the application:**

```bash
uvicorn main:app --host 0.0.0.0 --port 12448
```

6.  **Access the API:**

Open your browser and go to `http://localhost:12448`

## API Endpoints

### `GET /`

Returns the uptime of the API.

### `GET /languages`

Returns the available language pairs for translation. This endpoint is useful to check for updates in supported languages.

### `POST /translate`

Translates text from one language to another. The request body should contain the following fields:

-   `text` (string): The text to be translated.
-   `from_lang` (string): The source language code.
-   `to_lang` (string): The target language code.

# Language Pairs

This document lists the available language pairs for translation.

## From English to Other Languages

-   **English (en)** to Albanian (sq)
-   **English (en)** to Arabic (ar)
-   **English (en)** to Azerbaijani (az)
-   **English (en)** to Bengali (bn)
-   **English (en)** to Bulgarian (bg)
-   **English (en)** to Catalan (ca)
-   **English (en)** to Chinese (Traditional) (zt)
-   **English (en)** to Chinese (Simplified) (zh)
-   **English (en)** to Czech (cs)
-   **English (en)** to Danish (da)
-   **English (en)** to Dutch (nl)
-   **English (en)** to Esperanto (eo)
-   **English (en)** to Estonian (et)
-   **English (en)** to Finnish (fi)
-   **English (en)** to French (fr)
-   **English (en)** to German (de)
-   **English (en)** to Greek (el)
-   **English (en)** to Hebrew (he)
-   **English (en)** to Hindi (hi)
-   **English (en)** to Hungarian (hu)
-   **English (en)** to Indonesian (id)
-   **English (en)** to Irish (ga)
-   **English (en)** to Italian (it)
-   **English (en)** to Japanese (ja)
-   **English (en)** to Korean (ko)
-   **English (en)** to Latvian (lv)
-   **English (en)** to Lithuanian (lt)
-   **English (en)** to Malay (ms)
-   **English (en)** to Norwegian (Bokmål) (nb)
-   **English (en)** to Persian (fa)
-   **English (en)** to Polish (pl)
-   **English (en)** to Portuguese (pt)
-   **English (en)** to Romanian (ro)
-   **English (en)** to Russian (ru)
-   **English (en)** to Slovak (sk)
-   **English (en)** to Slovenian (sl)
-   **English (en)** to Spanish (es)
-   **English (en)** to Swedish (sv)
-   **English (en)** to Tagalog (tl)
-   **English (en)** to Thai (th)
-   **English (en)** to Turkish (tr)
-   **English (en)** to Ukrainian (uk)
-   **English (en)** to Urdu (ur)

## From Other Languages to English

-   **Albanian (sq)** to English (en)
-   **Arabic (ar)** to English (en)
-   **Azerbaijani (az)** to English (en)
-   **Bengali (bn)** to English (en)
-   **Bulgarian (bg)** to English (en)
-   **Catalan (ca)** to English (en)
-   **Chinese (Traditional) (zt)** to English (en)
-   **Chinese (Simplified) (zh)** to English (en)
-   **Czech (cs)** to English (en)
-   **Danish (da)** to English (en)
-   **Dutch (nl)** to English (en)
-   **Esperanto (eo)** to English (en)
-   **Estonian (et)** to English (en)
-   **Finnish (fi)** to English (en)
-   **French (fr)** to English (en)
-   **German (de)** to English (en)
-   **Greek (el)** to English (en)
-   **Hebrew (he)** to English (en)
-   **Hindi (hi)** to English (en)
-   **Hungarian (hu)** to English (en)
-   **Indonesian (id)** to English (en)
-   **Irish (ga)** to English (en)
-   **Italian (it)** to English (en)
-   **Japanese (ja)** to English (en)
-   **Korean (ko)** to English (en)
-   **Latvian (lv)** to English (en)
-   **Lithuanian (lt)** to English (en)
-   **Malay (ms)** to English (en)
-   **Norwegian (Bokmål) (nb)** to English (en)
-   **Persian (fa)** to English (en)
-   **Polish (pl)** to English (en)
-   **Portuguese (pt)** to English (en)
-   **Romanian (ro)** to English (en)
-   **Russian (ru)** to English (en)
-   **Slovak (sk)** to English (en)
-   **Slovenian (sl)** to English (en)
-   **Spanish (es)** to English (en)
-   **Swedish (sv)** to English (en)
-   **Tagalog (tl)** to English (en)
-   **Thai (th)** to English (en)
-   **Turkish (tr)** to English (en)
-   **Ukrainian (uk)** to English (en)
-   **Urdu (ur)** to English (en)

## Other Language Pairs

-   **Portuguese (pt)** to Spanish (es)
-   **Spanish (es)** to Portuguese (pt)
