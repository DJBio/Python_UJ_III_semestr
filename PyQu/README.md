# PyQu
PyQu jest małym programem konsolowym, pozwalający tworzyć odrębne pule pytań
oraz przeprowadzać quiz z nich.
## Ten program pozwała na:
1. Stworzenie własnych pul zamkniętych pytań jednokrotnego wyboru w odrębnych 
kategoriach (dane formatu json) z możliwością wprowadzenia dowolnej liczby 
możliwych wariantów odpowiedzi
1. Program, na podstawie wybranej kategorii (z pliku Pytania\TEMATY.json),
przeprowadza test.
1. Punktacja liczy się następująco:
	1. 2 pkt za poprawną odpowiedź
	1. -1 pkt za błędną
	1. Użytkownik na początku dostaje 0 pkt. 
	1. Uzyskana ilość punktów zachowuje się w następnej rundzie
	(w razie kontynuacji quizu)


## Instalacja i wykorzystywanie

1. Pobierz całą zawartość katalogu [PuQu][url_1].
1. Uruchomienie programu:
	- uruchom plik START.py
		
		bądź
		
	- wydaj polecenie w konsoli (z katalogu gdzie znajduje się plik START.py)
	```bash
	>py .\START.py
	```
1. Wszystkie opisane wyżej możliwości programu są realizowane przez 
wydawanie odpowiednich poleceń w konsoli wg wyświetlanych instrukcji


## Struktura programu
1. Program składa się z:
	- *START.py* (główny moduł programu, z jego poziomu realizowane są
	wszystkie f-je)
	- *ask_module.py* (moduł zawierający klasę AskModule, tworząca instancję 
	wg imienia użytkownika)
	- *add_question.py* (moduł przeprowadzający dodawanie pytań do 
	istniejących pul	bądź tworzenie nowych)
	- Pytania\
		- *TEMATY.json*
		- *(pytania wg nazwy tematyki).json*
1. Dodatkowe wymagania modułowe Python:
	- json, tabulate

## Licencja
[MIT](https://choosealicense.com/licenses/mit/)

[url_1]: https://github.com/DJBio/Python_UJ_III_semestr/tree/main/PyQu
