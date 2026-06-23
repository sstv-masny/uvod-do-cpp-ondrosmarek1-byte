
# Task 03 — Taxi Fare

**Pricing:** First 2 km cost **4.00 €** total.  
Every additional kilometer (or part of it) costs **1.50 €** per km, **rounded up** to the next km.

**Input:** One non‑negative integer `k` (driven kilometers).  
**Output:** Total fare as a decimal with **two digits** (e.g., `7.00`).

### Interpretation
If `k <= 2` → `4.00`.  
Else → `4.00 + 1.50 * ceil(k - 2)`.

### Samples
```
in: 0      out: 4.00
in: 2      out: 4.00
in: 3      out: 5.50
in: 4      out: 7.00
```

---

# Úloha 03 — Cestovné (taxík)

**Cenník:** Prvé 2 km spolu stoja **4.00 €**.  
Každý ďalší kilometer (alebo jeho časť) stojí **1.50 €** za km, zaokrúhlené nahor na celé kilometre.

**Vstup:** Jedno nezáporné celé číslo `k` (najazdené kilometre).  
**Výstup:** Celková suma ako desatinné číslo s dvoma miestami (napr. `7.00`).

### Interpretácia
Ak `k <= 2` → `4.00`.  
Inak → `4.00 + 1.50 * ceil(k - 2)`.

### Príklady
```
vstup: 0      výstup: 4.00
vstup: 2      výstup: 4.00
vstup: 3      výstup: 5.50
vstup: 4      výstup: 7.00
```
