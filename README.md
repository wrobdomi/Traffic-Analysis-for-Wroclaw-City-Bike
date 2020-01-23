# 13. Wrocławski rower miejski

# Spis treści
+ [Wstęp](#wstęp)
    1. [Opis problemu](#opis-problemu)
    2. [Dane i ich źródła](#dane-i-ich-źródła)
        * [Źródła danych](#źródła-danych)
        * [API WRM](#api-wrm)
        * [API ORS](#api-ors)
    3. [Proponowane rozwiązanie](#proponowane-rozwiązanie)
        * [Model danych](#model-danych)
        * [Algorytm](#algorytm)
    4. [Technologie](#technologie)
+ [Proces wytwarzania oprogramowania](#proces-wytwarzania-oprogramowania)
    1. [Wstępna analiza danych](#wstępna-analiza-danych)
    2. [Przyjęte założenia](#przyjęte-założenia)
    3. [Zliczanie przejazdów w punkcie](#zliczanie-przejazdów-w-punkcie)
    4. [Wstępne przygotowanie QGIS](#wstępne-przygotowanie-qgis)
    5. [Testowe odpalenie skryptu dla 4 stacji](#testowe-odpalenie-skryptu-dla-4-stacji)
+ [Uzyskane wyniki](#uzyskane-wyniki)
    1. [Test 1 29 wybranych do analizy stacji](#test-1-29-wybranych-do-analizy-stacji)
    2. [Test 1 wyniki analizy](#test-1-wyniki-analizy)
    3. [Rozszerzenie modelu na wszystkie stacje](#rozszerzenie-modelu-na-wszystkie-stacje) 
    4. [Test 2 wszystkie 45 stacji](#test-2-wszystkie-45-stacji)
    5. [Test 2 wyniki analizy](#test-2-wyniki-analizy)

# Wstęp

## Opis problemu
Projekt polega na wyznaczeniu na mapie miasta Wrocław najbardziej uczęszczanych
tras przez rowery miejskie. 

Miasto Wrocław posiada własną sieć stacji rowerów 
miejskich, na każdej ze stacji możliwe jest wypożyczenie roweru, a następnie
zwrócenie go na dowolnej innej stacji. Projekt ma pokazać, które z ulic są
najczęściej wybierane przez użytkowników rowerów miejskich. 

Dzięki takim danym możliwe będzie lepsze dostosowanie liczby rowerów na
poszczególnych stacjach, a także zmiana lokalizacji stacji na bardziej korzystne. Innym potencjalnym
zastosowiem może być rozlokowanie reklam dedykowanych dla rowerzystów.

## Dane i ich źródła

### Źródła danych
W projekcie użyto dwóch źródeł danych:
+ API wrocławskiego roweru miejskiego (WRM) - dane dotyczące przejazdów i lokalizacji stacji

https://www.wroclaw.pl/open-data/dataset/przejazdy-wroclawskiego-roweru-miejskiego-archiwalne

https://www.wroclaw.pl/open-data/dataset/nextbikesoap_data

+ API Open Route Service (ORS) - dane dotyczące prawdopodobnej trasy przejazdu z miejsca A do B

https://openrouteservice.org/

### API WRM
API wrocławskiego roweru miejskiego udostępnia dane (te ważne z perspektywy projektu):
+ O lokalizacjach stacji: nazwa stacji, szerokość i długość geograficzna, przykład:

| lat           | lng           | name  |
| ------------- |:-------------:| -----:|
| 51.108004     | 17.039528     | Plac Dominikański (Galeria Dominikańska) |
+ O zarejestrwaonych przejazdach w poprzednich sezonach: skąd (nazwa stacji), dokąd(nazwa stacji), czas startu, czas zakończenia

| Data wynajmu           | Data zwrotu           | Stacja wynajmu  | Stacja zwrotu    |
| ---------------------- |:---------------------:|:---------------:| :--------------: |
| 2015-11-18T17:25:54    | 2015-11-18T17:38:03   | Aleja Bielany   | Zaporska - Wielka|



Do API WRM można wysyłać zapytania, które mają jako parametr zapytanie SQL, co znacznie upraszcza pobieranie danych z tego API.



### API ORS
API Open Route Service udostępnia m.in. dane dla dwóch zadanych poprzez współrzędne geograficzne puktów :
+ O prawdopodobnej trasie pomiędzy tymi punktami (GeoJson - LineString)

Przykładowo dla zapytania o punkty dla współrzędnych dwóch stacji WRM, :

_https:// api.openrouteservice.org /v2/directions/cycling-regular? api_key = 5b3ce3597851110001cf6248782ac85e6e35409582ad067fef1ded89& start = 16.86564,51.15127& end = 16.86627, 51.14323_

Otrzymujemy GeoJson, który nałożony na mapę OpenStreetMap prezentuje prawdopodobną trasę:

![alt text1][logo]

[logo]: img/dok2.PNG "Title Text"


Odpowiadający fragment GeoJson:

```json
 "geometry": {
        "coordinates": [
          [
            16.865657,
            51.151255
          ],
          [
            16.865433,
            51.151154
          ],
          [
            16.865909,
            ...
            ],
        "type": "LineString"
      }
```

+ O prawdopodobnym czasie przejazdu wybranym środkiem transportu na tej trasie

Odpwiadający fragment GeoJson:

```json
"summary": {
          "distance": 983.8,
          "duration": 133.9
        },
```




## Proponowane rozwiązanie
W moim rozwiązaniu chcę dla każdej możliwej trasy, którą wybrali rowerzyści 
(tj. takiej, która została zarejestrowana w bazie danych WRM) wyznaczyć trasę 
przejazdu oraz prawdopodony czas na podstawie danych z ORS.

Następnie wyznaczyć liczbę przejazdów w każdym punkcie tej trasy 
[Zliczanie przejazdów w punkcie](#zliczanie-przejazdów-w-punkcie)

Punkty oraz liczbę wytąpień zapisuje w bazie danych, następnie dane
wyświetlam na mapie OSM w oprogramowaniu QGIS.

Szczegółowy model danych i algorytm opisane są poniżej:

### Model danych

![alt text1][model]

[model]: img/stacja.PNG "Title Text"

![alt text1][model2]

[model2]: img/trasa.PNG "Title Text"

![alt text1][model3]

[model3]: img/punkt.PNG "Title Text"

### Algorytm

![alt text1][algo]

[algo]: img/algo.PNG "Title Text"


## Technologie
Technologie:
+ Kod programu
    - Python 3.7
    - Moduły: requests, psycopg2
+ Baza danych
    - postgresql
    - rozszerzenie PostGIS
+ Narzędzia
    - PyCharm
    - PgAdmin 4
    - IDLE (Python)
    - QGIS (wizualizacja danych z postgresql)
    - excel (konwersja danych excel na csv w celu importu do bazy danych)

# Proces wytwarzania oprogramowania

## Wstępna analiza danych

+ Rozbieżność w danych dotyczących stacji oraz dotyczących przejazdów z WRM. 

W aktualnych danych dotyczących stacji znajduje się 203 stacje rowerowe, 
natomiast dane o zarejestrowanych przejazdach pochodzą z lat 2015/2016 i zawierają tylko około 80
stacji jak widać na poniższych zapytaniach, prawdopodobnie wynika to z tego, że
z upływem czasu miasto decydowało się na wprowadzanie kolejnych stacji, co
potwierdza artykuł z tego linku:
https://www.wroclaw.pl/wroclawski-rower-miejski-podsumowanie-sezonu-2015

Dane aktualne:

![alt text1][roz1]

[roz1]: img/dok99.PNG "Title Text"

Dane z sezonu 2015:

![alt text1][roz2]

[roz2]: img/dok1010.PNG "Title Text"

+ Duża liczba możliwych tras dla całego miasta

Dla danych z 2015 roku zarejestrowano około 5000 różnych tras:

![alt text1][roz3]

[roz3]: img/dok11.PNG "Title Text"

Aby przeanalizować oczekiwaną trasę (z ORS) dla każdej zarejestrowanej potrzebne byłoby
wykonanie ponad 5000 zapytań, ORS nakłada jednak na użytkowników ograniczenia
przez które można wykonać tylko 2000 zapytań dziennie oraz 40 zapytań na minutę.

Ogólny wzór na liczbę tras dla n stacji, to: 

![alt text1][wzor]

[wzor]: img/wzor.PNG "Title Text"

Przyjęto, że trasa z X do Y może być różna od stacji Y do X (np. droga jednokierunkowa). 
Do analizy nie wchodzą stacje z X do X.

+ Duża liczba rekordów przejazdów ma taką samą stację zwrotu jak i wynajmu

Wszystkie rekordy:

![alt text1][all]

[all]: img/dok20.PNG "Title Text"

Rekordy o takiej samej stacji zwynajmu i zwortu:

![alt text1][roz4]

[roz4]: img/dok12.PNG "Title Text"

+ Niektóre ze stacji zmieniły swoje nazwy, np. na skutek podzielenia na mniejsze stacje

Przykładowo stacja Dworzec Główny PKP z danych z roku 2015 nie jest obecna w danych aktualnych stacji.

![alt text1][rozy]

[rozy]: img/dok13.PNG "Title Text"

![alt text1][rozz]

[rozz]: img/dok14.PNG "Title Text"

+ Również bardziej subtelne różnice w nazwach jak np. slash zamiast myślnika:

![alt text1][rozzz]

[rozzz]: img/dok15.PNG "Title Text"

![alt text1][rozxx]

[rozxx]: img/dok16.PNG "Title Text"

## Przyjęte założenia

+ Problem uproszczono do wybrania z obszaru miasta pewnej liczby zbliżonych do siebie
geograficznie stacji i przeprowadzeniu analizy tylko dla nich.  
+ Dodatkowo wybierane stacje będą tymi, które istniały już w 2015 roku aby uzyskać zgodność z danymi 
o zarejestrowanych przejazdach.
+ Z analizy odrzucono przejazdy, które mają taką samą stacje wynajmu i zwrotu

Link do mapy ze wszystkimi stacjami: https://wroclawskirower.pl/mapa-stacji/

## Zliczanie przejazdów w punkcie
Na podstawie rekordów przejazdów w bazie danych zliczamy liczbę przejazdów przez dany punkt.
Licznik jest zwiększamy pod warunkiem, że spełnione jest: 

![alt text1][prob]

[prob]: img/dok17.PNG "Title Text"

Gdzie p jest ustalonym prawdopodobieństwem (współczynnik pewności). 

Przykład

Przyjmując następujące dane:

![alt text1][obl1]

[obl1]: img/obl1.PNG "Title Text"

Stąd pierwszy rekord zostaje zakwalifikowany jako przejazd prawdopodobną trasą:
![alt text1][obl2]

[obl2]: img/obl2.PNG "Title Text"

Drugi z rekordów nie jest zakwalifikowany jako przejazd prawdopodobną trasą:
![alt text1][obl3]

[obl3]: img/obl3.PNG "Title Text"




Wartość p jest zaszyta jako stała w kodzie, a wartość T_O otrzymujemy z ORS, wobec tego liczbę o którą
należy zwiększyć licznik dostajemy z zapytania:

```sql
SELECT count(*) FROM
    (SELECT data_zwrotu, data_wynajmu, EXTRACT(minutes from (data_zwrotu - data_wynajmu))::integer AS m 
    FROM wypozyczenia 
    WHERE stacja_wynajmu = 'Traugutta - Pułaskiego' AND stacja_zwrotu = 'Rynek') AS arr
WHERE abs(m-15) < 3;
```

## Wstępne przygotowanie QGIS
Bazę danych Postresql z rozszerzeniem PostGIS połączono z programem QGIS w celu
wizualizacji punktów tras wraz z etykietami, początkowe testy przyniosły pozytywne
rezultaty:
```sql

CREATE TABLE public.punkty
(
    id bigint NOT NULL DEFAULT nextval('punkty_id_seq'::regclass),
    geom geometry(Point,4326),
    label integer,
    CONSTRAINT punkty_pkey PRIMARY KEY (id)
)

INSERT INTO punkty (geom, label) VALUES (ST_GeomFromText('POINT(17.033499 51.117032)',4326), 1500);
...
```
![alt text1][qgis]

[qgis]: img/dok18.PNG "Title Text"

## Testowe odpalenie skryptu dla 4 stacji
Początkowo skrypt programu odpalono dla 4 wybranych stacji, oto wyniki:
![alt text1][qgistest]

[qgistest]: img/dok19.PNG "Title Text"

# Uzyskane wyniki

## Test 1 29 wybranych do analizy stacji
Do analizy wybrano stacje z centrum miasta. Na poniższym rysunku zaznaczono kolorem zielonym stacje, które wybrano do analizy, kolorem czerwonym zaznaczono stacje, które obecne
są w aktualnych danych wrocławskiego roweru miejskiego (2020), ale nie ma ich w rejestrze przejazdów z roku 2015. W sumie wybrano 29 stacji.
![alt text1][sda]

[sda]: img/stacje_do_analizy.png "Title Text"

Z bazy danych wybrano dane o tych stacjach, następnie dostosowano je do formatu nazw z roku 2015 (zamiana / na - itp.) i utworzono na tej podstawie plik .csv, 
który jest plikiem wsadowym do programu.

```sql
SELECT numer, longitude, latitude, nazwa FROM stacje 
WHERE 
nazwa IN (
	'Rynek',
	'Kościuszki / Pułaskiego',
	'Traugutta / Pułaskiego',
	'Drobnera / Dubois',
	'Legnicka / Wejherowska',
	'Zachodnia / Poznańska',
	'Hallera / Odkrywców',
	'Grabiszyńska / Stalowa',
	'Pereca / Grabiszyńska',
	'Żelazna / Pereca',
	'Grochowa / Jemiołowa,',
	'Zaporoska / Grabiszyńska',
	'Zaporoska / Gajowicka',
	'Komandorska / Kamienna',
	'Gliniana / Gajowa',
	'Traugutta / Kościuszki',
	'Kościuszki / Komuny Paryskiej / Zgodna',
	'Plac Legionów',
	'Wita Stwosza / Szewska',
	'Plac Grunwaldzki / Polaka',
	'Rondo Reagana',
	'Sienkiewicza / Piastowska',
	'Sienkiewicza / Wyszyńskiego',
	'Reymonta / Kleczkowska',
	'Jedności Narodowej / Wyszyńskiego',
	'Nowowiejska / Wyszyńskiego',
	'Żeromskiego / Kluczborska',
	'Mickiewicza / pętla tramwajowa',
	'Olszewskiego / Spółdzielcza'
)
ORDER BY nazwa;
```

Wyświetlenie wybranych stacji w QGIS: 
![alt text1][stacje_wybrane]

[stacje_wybrane]: img/stacje_qgis.PNG "Title Text"

## Test 1 wyniki analizy

Algorytm znalazł 9077 punktów w czasie około 40 minut na komputerze z procesorem CORE i7. Czas ten nie wynika jednak ze złożoności obliczeniowej 
samego algorytmu, ale z faktu, że API ORS nakłada ograniczenie na wysyłanie maksymalnie 40 zapytań na minutę. W związku z tym w algorytmie zastosowano
dwusekundowe opóźnienie po każdym zapytaniu.

![alt text1][wynik1]

[wynik1]: img/wynik1.PNG "Title Text"

![alt text1][wynik2]

[wynik2]: img/wynik2.PNG "Title Text"

![alt text1][wynik3]

[wynik3]: img/wynik3.PNG "Title Text"


## Rozszerzenie modelu na wszystkie stacje

Kolejnym krokiem było rozszerzenie działania programu do jak największej 
możliwej liczby stacji, która mieściłaby się w zakresie dopuszczalnej liczby zapytań do ORS (2000 na dobę).

W tym wykonaliśmy analizę porównawczą stacji obecnych w rekordach z roku 2015 i 2020. Analiza ta
z uwagi na relatywnie małą liczbę stacji została przeprowadzona ręcznie przez przegląd zupełny, zadanie
ułatwiło wybranie stacji z bazy danych oraz z rekordów w kolejności alfabetycznej. 

Wyniki analizy porównawczej przedstawione są poniżej. Kolorem zielonym oznaczono
stacje, które są w aktualnych rekordach stacji, kolorem czerwonym te których już 
nie ma. W kolumnie po prawej opisano aktualną nazwę stacji jeśli uległa ona zmianie.

![alt text1][por1]

[por1]: img/dok21.PNG "Title Text"

![alt text1][por2]

[por2]: img/dok22.PNG "Title Text"

W sumie otrzymaliśmy 45 stacji dla których mogliśmy znaleźć współrzędne geograficzne. 


## Test 2 wszystkie 45 stacji

Kolejny test przeprowadzono dla wszytkich stacji, które obecne są w pomiarach z 2015 roku oraz w aktualnych danych o stacjach
wrocławskiego roweru miejskiego (czyli dla wszystkich tych stacji z 2015 dla których możliwe jest ustalenie współrzędnych geograficznych).
Stacji takich jest 45, ich rozlokowanie prezentuje mapa poniżej:

![alt text1][wszystkie]

[wszystkie]: img/wszystkie.PNG "Title Text"

## Test 2 wyniki analizy

![alt text1][wynik4]

[wynik4]: img/wynik4.PNG "Title Text"

![alt text1][wyniki5]

[wyniki5]: img/wyniki5.PNG "Title Text"

![alt text1][wyniki6]

[wyniki6]: img/wyniki6.PNG "Title Text"

![alt text1][wyniki7]

[wyniki7]: img/wyniki7.PNG "Title Text"

![alt text1][wyniki8]

[wyniki8]: img/wyniki8.PNG "Title Text"

![alt text1][wyniki9]

[wyniki9]: img/wyniki9.PNG "Title Text"
