# PyQu
PyQu jest małym programem konsolowym, pozwalający tworzyć odrębne pule pytań oraz
przeprowadzać quiz z nich.

**Ten program pozwała na:**
1. Stworzenie własnej puli zamkniętych pytań jednokrotnego wyboru w odrębnych 
kategoriach (dane formatu json) z możliwością wprowadzenia dowolnej liczby 
możliwych wariantów odpowiedzi
1. Program, na podstawie wybranej kategorii (pula pytań, odrębny plik .json w katalogu /Pytania), przeprowadza test.


**Instalacja**

1. Pobierz całą zawartość katalogu [PuQu][url_1].
1. Urochom programu:
	- uruchom plik START.py
		
		bądź
		
	- wydaj polecenie w konsoli (z katalogu gdzie znajduje się plik START.py)

```bash
>py .\START.py
```

## Wykorzystywanie
Wszystkie opisane wyżej możliwości programu są realizowane uruchomiając START.py

## Struktura programu
1. Program składa się z:
	- *START.py* (główny moduł programu, z jego poziomu realizowane są wszytkie f-je)
	- *ask_module.py* (moduł zawierający klasę AskModule, tworząca instancję 
	wg imienia użytkownika)
	- *add_question.py* (moduł przeprowadzający dodawanie pytań do 
	istnijacych pul	bądź tworzenie nowych)
	- Pytania\
		- *TEMATY.json*
		- *(pytania wg nazwy tematyki).json*
1. Dodatkowe wymagania modułowe Python:
	- json, tabulate

## Licencja
[MIT](https://choosealicense.com/licenses/mit/)

[url_1]: https://github.com/DJBio/Python_UJ_III_semestr/tree/main/PyQu
