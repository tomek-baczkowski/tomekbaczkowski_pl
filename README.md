# tomekbaczkowski.pl

Statyczna strona Tomasza Bączkowskiego: aftersales, procesy, wdrożenia systemów i automatyzacje, a także turystyka i hobby.

## Jak to działa

- `src/pages/` – treść każdej podstrony (HTML). Na górze pliku komentarz z ustawieniami: adres (`path`), pozycja menu (`nav`), tytuł i opis dla Google.
- `src/partials/` – powtarzane bloki (`cta.html`: pasek kontaktu na końcu podstron).
- `src/layout.html` – nagłówek, menu, stopka i kształty z logo (SVG) wspólne dla wszystkich stron.
- `src/static/` – CSS, JavaScript, zdjęcia (WebP), kroje pisma, `llms.txt`.
- `build.py` – składa stronę do folderu `_site/` (Python 3, bez dodatkowych bibliotek). Wstawia twarde spacje po jednoliterowych spójnikach, tworzy `sitemap.xml`, `robots.txt` i przekierowania starych adresów (`/aftersales/`, `/kombucha/`).
- `DESIGN.md` – kolory, kroje, odstępy, kształty z logo i komponenty. Nowe elementy projektujemy według niego.

Podgląd lokalnie: `python3 build.py && python3 -m http.server -d _site 8000`, potem http://localhost:8000.

## Mapa strony

| Adres | Plik |
| --- | --- |
| `/` | `index.html` |
| `/skuteczny-aftersales/` | `skuteczny-aftersales.html` |
| `/skuteczny-aftersales/wpisy/` | `wpisy.html` |
| `/dla-firm/` | `dla-firm.html` |
| `/kariera/` | `kariera.html` |
| `/projekty/` | `projekty.html` |
| `/projekty/cogito-crm/` | `cogito-crm.html` |
| `/turystyka/` | `turystyka.html` |
| `/o-mnie/` | `o-mnie.html` |
| `/kontakt/` | `kontakt.html` |
| `/polityka-prywatnosci/` | `polityka-prywatnosci.html` (adres musi zostać: formularze reklam Meta) |

Wersja angielska (`/en/`) powstanie po ukończeniu polskiej.

## Publikacja

Każdy push do gałęzi `main` uruchamia GitHub Actions (`.github/workflows/pages.yml`): budowanie i publikacja na GitHub Pages.
Jednorazowo w ustawieniach repozytorium: Settings → Pages → Source: **GitHub Actions**.

### Domena tomekbaczkowski.pl (jeszcze nieprzepięta)

Do zrobienia przed 19.11.2026, gdy strona jest zaakceptowana:

1. Dodać plik `src/static/CNAME` z jedną linią: `tomekbaczkowski.pl`. Nie dodawać wcześniej: podgląd pod adresem github.io zacząłby przekierowywać na starą stronę.
2. W DNS (cyber_Folks, Edycja strefy DNS): rekordy A dla `tomekbaczkowski.pl` na 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 oraz CNAME `www` → `tomek-baczkowski.github.io`. Rekordów poczty (MX) nie ruszać.
3. W Settings → Pages wpisać domenę i włączyć „Enforce HTTPS”.
4. Sprawdzić, że `/polityka-prywatnosci/` działa pod nowym adresem. Dopiero potem wyłączyć stary hosting. Strefa DNS żyje dziś w tym hostingu: przed jego wyłączeniem przenieść DNS (np. na FreeDNS cyber_Folks) i odtworzyć rekordy.

## Analityka

Brak. Strona nie ma formularzy ani plików cookie do śledzenia.
