# fastapi_mikroservisi

## servis_1

- main.py
- Dockerfile

## servis_2

- main.py
  Dockerfile

## servis_3

- main.py
- Dockerfile

### docker-compose.yml

**Servis_1**

- pokreće igru sa listom [0]
- naizmjenično poziva Servis_2 i Servis_3
- kada lista dosegne 10 elemenata, vraća poruku "Igra gotova"

**Servis_2**

- prima JSON sa listom brojeva (lista_brojeva)
- dodaje neparne brojeve pri svakom pozivu 1, 3, 5...
- vraća ažuriranu listu

**Servis_3**

- prima JSON sa listom brojeva (lista_brojeva)
- dodaje neparne brojeve pri svakom pozivu 2, 4, 6...
- vraća ažuriranu listu
