import random

hero_hp = 100
monster_hp = 80

print("======================")
print("     HERO VS MONSTER")
print("======================")

nama = input("Masukkan nama hero: ")

while hero_hp > 0 and monster_hp > 0:

    print("\n----------------------")
    print(nama)
    print("HP Hero    :", hero_hp)
    print("HP Monster :", monster_hp)

    print("\n1. Serang")
    print("2. Minum Potion")
    print("3. Kabur")

    pilihan = input("Pilih: ")

    if pilihan == "1":

        damage = random.randint(10, 25)
        monster_hp -= damage

        print(f"\n⚔️ Kamu menyerang monster sebesar {damage} damage!")

        if monster_hp <= 0:
            break

        serangan_monster = random.randint(5, 20)
        hero_hp -= serangan_monster

        print(f"👹 Monster menyerang balik {serangan_monster} damage!")

    elif pilihan == "2":

        heal = random.randint(15, 30)
        hero_hp += heal

        if hero_hp > 100:
            hero_hp = 100

        print(f"\n❤️ Kamu minum potion +{heal} HP")

        serangan_monster = random.randint(5,20)
        hero_hp -= serangan_monster

        print(f"👹 Monster menyerang {serangan_monster} damage!")

    elif pilihan == "3":
        print("\n🏃 Kamu kabur dari pertarungan!")
        break

    else:
        print("\nPilihan tidak valid!")

print("\n======================")

if monster_hp <= 0:
    print("🎉 SELAMAT!")
    print("Monster berhasil dikalahkan!")

elif hero_hp <= 0:
    print("💀 GAME OVER")
    print("Hero telah gugur.")