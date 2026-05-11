# Getting started (per-folder) / Začnite (po priečinkoch)

This repository contains multiple independent C++ exercises/projects organized into separate folders. Each folder is an independent small project and can be built and run on its own. This README explains how to start and run code separately by folder.

Tento repozitár obsahuje viacero samostatných C++ cvičení/projektov usporiadaných do priečinkov. Každý priečinok predstavuje nezávislý malý projekt, ktorý je možné zostaviť a spustiť samostatne. Tento README vysvetľuje, ako spustiť kód oddelene podľa priečinka.

## How the repo is organized / Ako je repozitár usporiadaný

- Each top-level folder contains one independent C++ task or example.
- Look inside a folder to find source files (e.g. `main.cpp`)
- If a folder already contains its own README, follow the instructions inside that folder.

- Každý vrchný priečinok obsahuje jedno samostatné C++ zadanie alebo príklad.
- Pozrite sa do priečinka, kde nájdete zdrojové súbory (napr. `main.cpp`)
- Ak priečinok už obsahuje vlastný README, riaďte sa pokynmi v ňom.

## Common ways to build & run a single folder / Bežné spôsoby zostavenia a spustenia jedného priečinka

Replace `folder_name` below with the actual folder you want to run.

Nahradiť `folder_name` nižšie skutočným názvom priečinka, ktorý chcete spustiť.

1) Quick compile with g++ (single file or small projects) / Rýchle skompilovanie s g++ (jednosúborové alebo malé projekty)

```bash
cd folder_name
# single source file
g++ -std=c++17 -O2 -Wall -Wextra main.cpp -o main
./main

# or compile all .cpp files in that folder
g++ -std=c++17 -O2 -Wall -Wextra *.cpp -o app
./app
```

4) Visual Studio Code

- Open the folder in VS Code (File → Open Folder).
- Install the C/C++ extension (ms-vscode.cpptools).
- Use the VS Code Run/Debug pane or create a tasks.json/launch.json to build and run.

4) Visual Studio Code

- Otvorte priečinok vo VS Code (File → Open Folder).
- Nainštalujte rozšírenie C/C++ (ms-vscode.cpptools).
- Použite panel Run/Debug v VS Code alebo vytvorte tasks.json/launch.json na zostavenie a spustenie.

## Troubleshooting / Riešenie problémov

- No `main.cpp` / entry point: open the folder and find which source file contains `int main()`.
- Missing dependencies or headers: check the folder README or any provided instructions; install any required libraries.
- Compile errors: enable more verbose output (remove -O2 / add -g) and fix warnings/errors reported by the compiler.

- Žiadny `main.cpp` / vstuponý bod: otvorte priečinok a nájdite zdrojový súbor obsahujúci `int main()`.
- Chýbajúce závislosti alebo hlavičky: skontrolujte README priečinka alebo poskytnuté pokyny; nainštalujte potrebné knižnice.
- Chyby kompilácie: zapnite podrobnejší výstup (odstráňte -O2 / pridajte -g) a opravte varovania/chyby hlásené kompilátorom.
