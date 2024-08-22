Kuhan_pituus = float(input("Kerro kuhan pituus cm:"))

Kuhan_kasvettava = 37 - Kuhan_pituus

if Kuhan_pituus >= 37:
    print("Sopivan kokoinen")
else: print(f"Laske kuha takaisin järveen. Sen tulee kasvaa vielä: {Kuhan_kasvettava:.2f}CM")