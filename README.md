# Connect Four

Gra „Connect Four” w Pythonie z interfejsem Pygame. Gracz gra przeciwko
botowi, wybierając algorytm myślenia bota (minimax lub minimax z przycinaniem alfa-beta).

Można ustawić głębokość przeszukiwania od 1 do 8. Gra pokazuje czas obliczania
ruchu, co pozwala porównać algorytmy przy tej samej pozycji i głębokości.

## GUI

<img width="700" height="974" alt="Connect Four GUI" src="https://github.com/user-attachments/assets/b8afbed4-ab3c-4ec7-9bdb-1b19680a065a" />


## Uruchomienie

Potrzebny jest Python 3. W terminalu, w folderze projektu:

```bash
python -m pip install pygame
python Gui.py
```

Kliknij kolumnę, aby wrzucić pionek. Przyciski pod planszą zmieniają algorytm
i głębokość, a przycisk Restart rozpoczyna nową partię.

Przy wysokiej głębokości obliczenia mogą długo trwać. W tym czasie okno
nie reaguje na kliknięcia.

## Testy

Z głównego folderu projektu:

```bash
python -m pip install pytest
python -m pytest
```

Testy sprawdzają zasady gry, wybór ruchów bota, cofanie symulowanych ruchów
oraz zgodność ocen minimaxa i alfa-beta.
