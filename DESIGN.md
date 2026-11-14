# DESIGN.md – tomekbaczkowski.pl

Wersja 2 (14.11.2026). Akcent i kierunek przyjęte przez Tomka 14.11.2026. Wartości są w `src/static/css/style.css` jako zmienne CSS; strony używają nazw, nie surowych wartości.

Podstawa: brief w Notion (stan 13.11.2026), logo w dwóch wersjach i 66 zdjęć Tomka. Kierunek nie był porównywany z biblioteką prawdziwych stron (UXKIN niepodłączony). Jedyny wzór to iservice.pl z briefu: bierzemy z niego czystość, grube czytelne kroje, sekcje ciemne i jasne na zmianę oraz jeden akcent. Nie bierzemy kolorów, kroju ani układu.

## Zasada

Wszystko, co ozdobne, pochodzi z logo: koło, duża gwiazda z ogonem, mała gwiazda. Przyciski, ramki i linie mają ostre krawędzie jak ramiona gwiazdy. Zdjęcia mają lekko zaokrąglone rogi.

## Kolor

| Nazwa | Wartość | Rola |
| --- | --- | --- |
| `--ink` | #0E1013 | ciemne sekcje, tekst na jasnym, czerń logo |
| `--ink-2` | #181B20 | karty na ciemnym tle |
| `--ink-line` | #2C3138 | linie na ciemnym tle |
| `--paper` | #F4F1EA | jasne sekcje (ciepła biel) |
| `--white` | #FFFFFF | sekcje „czyste” i karty na jasnym tle |
| `--line` | #DAD5C9 | linie na jasnym tle |
| `--text` | #14171A | tekst na jasnym, kontrast 15,9:1 |
| `--text-muted` | #555B63 | tekst pomocniczy na jasnym, 6,1:1 |
| `--on-dark` | #F4F1EA | tekst na ciemnym, 16,9:1 |
| `--on-dark-muted` | #AAB0B8 | tekst pomocniczy na ciemnym, 8,7:1 |
| `--accent` | #F5A800 | jedyny akcent: przycisk główny, mała gwiazda, wyróżnione słowa, sekcja kontaktu |
| `--accent-hover` | #FFBD2E | przycisk główny po najechaniu |
| `--on-accent` | #0E1013 | tekst na akcencie, 9,5:1 |
| `--sea` | #0A2F45 | wyłącznie nakładka na zdjęcia w części o turystyce |

- Akcent to żółty maszyn budowlanych (decyzja Tomka, 14.11.2026): kolor branży klientów, kontrastuje z błękitem zdjęć z morza, nie jest zielenią iService.
- Akcent na jasnym tle nigdy nie jest kolorem tekstu (za słaby kontrast). Na jasnym służy jako wypełnienie, podkreślenie linku i mała gwiazda.
- Strona nie ma osobnego trybu ciemnego. Ciemne i jasne sekcje występują na zmianę.
- Kolory stanu (błąd, sukces) nie są potrzebne: strona nie ma formularzy.

## Typografia

Dwa kroje, hostowane lokalnie (bez Google Fonts, bez zgody na ciasteczka):

- **Archivo** (zmienny: grubość 100–900, szerokość 62–125%) – nagłówki i tekst.
- **IBM Plex Mono 500** – nadtytuły, daty, numery. Kojarzy się z tabliczką znamionową i z systemami.

| Nazwa | Rozmiar | Interlinia | Grubość / szerokość | Użycie |
| --- | --- | --- | --- | --- |
| `--fs-display` | 40–76 px | 1,02 | 800 / 110% | H1 na stronie głównej |
| `--fs-motto` | 30–68 px | 1,05 | 800 / 112% | motto |
| `--fs-h2` | 30–48 px | 1,08 | 800 / 110% | tytuły sekcji |
| `--fs-h3` | 22 px | 1,2 | 700 / 110% | tytuły kart |
| `--fs-lead` | 18–22 px | 1,5 | 400 | wstęp sekcji |
| `--fs-body` | 17 px | 1,6 | 400 | tekst |
| `--fs-small` | 15 px | 1,5 | 400 | podpisy, stopka |
| `--fs-label` | 13 px | 1,3 | Plex Mono 500, wersaliki, odstęp 0,08em | nadtytuły |

- Nagłówki: odstęp między literami −0,02em. Wiersz tekstu do ok. 70 znaków.
- Po jednoliterowych spójnikach i przyimkach twarda spacja.
- Jedno wyróżnienie kolorem akcentu na nagłówek, tylko na ciemnym tle.

## Odstępy i siatka

- Skala 4: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128 px (`--s-1` … `--s-32`).
- Sekcja: 64–120 px od góry i od dołu (`--section-y`).
- Szerokość treści 1200 px (`--wrap`), margines boczny 20–40 px (`--gutter`).
- Progi: 608 px, 896 px, 960 px, 1088 px. Poniżej 1088 px menu chowa się pod przyciskiem „Menu”.

## Kształt i głębia

- `--radius: 0` dla przycisków, ramek i tabel. `--radius-img: 6px` dla zdjęć i kart, w których zdjęcie dochodzi do krawędzi (decyzja Tomka, 14.11.2026).
- Koło: portret w hero, numer w kółku, punkt osi czasu.
- Bez cieni i bez gradientów. Głębię dają kontrast sekcji, linie 1 px i gruba linia 2–3 px nad kartą.

## Kształty z logo

| Element | Skąd | Gdzie |
| --- | --- | --- |
| Portret w kole z małą gwiazdą | układ logo 1:1, zdjęcie w miejscu koła | hero strony głównej |
| Schemat „gwiazda działów” | całe logo: 4 ramiona = serwis, magazyn, marketing, systemy; ogon prowadzi do małej gwiazdy = klient, który wraca | sekcja „Co mnie wyróżnia” |
| Mała gwiazda | mała gwiazda z logo | znacznik nadtytułu i punktora, narożnik zdjęcia, cytat, motto |
| Fragment dużej gwiazdy | duża gwiazda, powiększona i przycięta krawędzią sekcji, krycie 5–7% | sekcje bez zdjęcia w tle (doświadczenie, kontakt) |
| Koło | koło z logo | numery kroków, punkty osi czasu |

Logo w nagłówku i stopce jest jednokolorowe i niezmienione. Kolor akcentu dostaje tylko mała gwiazda użyta jako ozdobnik.

## Zdjęcia

- Zdjęcia „Tło” leżą pod kolorem sekcji: odbarwione, krycie 11% na jasnym, 17% na ciemnym, 26% w części morskiej. Stopka zostawia ciepły kolor zdjęcia nocnego (38%).
- Jedno tło na sekcję, nigdy pod długim tekstem ciągłym bez nakładki.
- Zdjęcia treści mają rogi zaokrąglone o 6 px; 3:2 w kartach, 1:1 w galeriach hobby, 4:5 w nagłówkach podstron.
- Selfie odbite lustrzanie odwracamy (napisy czytelne). Logo obcych marek w tle portretu usuwamy.
- Pliki WebP, szerokość do 1920 px, atrybut `alt` z opisem, `loading="lazy"` poniżej pierwszego ekranu.

| Zdjęcie „Tło” | Sekcja strony głównej |
| --- | --- |
| Tło 1 (pajęczyna z rosą) | Co mnie wyróżnia – sieć połączeń między działami |
| Tło – dwa budynki i statek | Turystyka |
| Tło – próbki grzybni | Poza pracą |
| Tło UTECH – maszyny, zima | Motto |
| Tło – kamper i ciężarówka nocą | Stopka |
| Tło – grzybnia się rozrasta | na razie nieużyte |

## Komponenty

- **Przycisk główny**: tło akcentu, tekst `--on-accent`, 700, min. wysokość 52 px, strzałka. Najechanie: `--accent-hover`. Jeden na ekran.
- **Przycisk drugi**: ramka 2 px w kolorze tekstu, przezroczyste tło. Najechanie: odwrócenie kolorów.
- **Przycisk ciemny**: tylko na sekcji w kolorze akcentu.
- **Link w tekście**: pogrubiony, podkreślenie 3 px w kolorze akcentu.
- **Fokus klawiatury**: obrys 3 px w kolorze akcentu, odsunięty o 3 px (na sekcji akcentu: ciemny).
- **Nadtytuł**: mała gwiazda + Plex Mono wersalikami.
- **Karta**: rogi 6 px, gdy zawiera zdjęcie; na jasnym linia 1 px, na ciemnym tło `--ink-2` i linia akcentu 3 px u góry.
- **Nagłówek podstrony**: ciemna sekcja, ścieżka powrotu, nadtytuł, H1, wstęp; po prawej zdjęcie 4:5 z małą gwiazdą w narożniku.
- **Pasek kontaktu**: sekcja w kolorze akcentu na końcu każdej podstrony (`src/partials/cta.html`).
- **Oś czasu**: linia 2 px, punkty-koła; przerwa zawodowa linią przerywaną; obecna praca punktem w kolorze akcentu.
- **Cytat**: karta z linią u góry; główna rekomendacja na ciemnym tle.
- **Nagłówek strony**: logo + nazwisko, menu, przycisk „Kontakt”. **Stopka**: logo, opis, dwie kolumny linków, nota prawna.

## Czego nie robimy

Gradientów, szkła, cieni, mocno zaokrąglonych kart, emoji zamiast ikon, trzeciego kroju, drugiego akcentu, zdjęć ze stocku.
