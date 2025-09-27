# 1) Choisir sa distribution

* **Ubuntu/Kubuntu** (Debian-like, *Apt*): “tout-en-un”, stable, grosses communautés.

  * **Kubuntu** = Ubuntu + **KDE Plasma** (léger, personnalisable, propre). Bon choix généraliste.
* **Linux Mint** (Ubuntu base): très accessible, codecs/préconfig soignés.
* **Fedora** (*dnf*): plus “à jour”, proche des technos Red Hat.
* **Debian**: sobriété, stabilité, moins de “dernier cri”.
* **openSUSE**: outils d’admin avancés (YaST), rolling (Tumbleweed) ou stable (Leap).
* **Arch/Manjaro** (*pacman*): très récent/rolling, plus technique (Manjaro simplifie).

**Si tu débutes** : Kubuntu, Ubuntu, ou Mint.

---

# 2) Télécharger l’ISO

1. Télécharge l’**ISO officiel** (site de la distro).
2. (Optionnel mais recommandé) **Vérifie l’intégrité** : checksum `SHA256` fourni sur la page → compare avec `sha256sum <fichier.iso>`.

---

# 3) Créer la clé USB bootable

## Option 1 — **Balena Etcher** (Windows/macOS/Linux)

1. Installe **Balena Etcher**.
2. **Flash from file** → choisis l’ISO.
3. Sélectionne ta **clé USB (≥8 Go, idéalement USB 3.0)**.
4. **Flash** → **Validate**.
   *(Évite d’avoir la clé montée/ouverte ailleurs.)*

## Option 2 — **Rufus** (Windows)

* Lance Rufus → Sélectionne l’ISO → **Partition scheme**: `GPT` (UEFI) → **Start**.
* Pratique pour faire des clés **UEFI/Secure Boot** propres et ajouter persistance.

## Option 3 — **Terminal** (Linux/mac)

```bash
# Trouve ta clé
lsblk                        # Linux
diskutil list                # macOS

# Écris l’ISO (⚠️ remplace sdX / rdiskN par la bonne cible)
sudo dd if=./linux.iso of=/dev/sdX bs=4M status=progress conv=fsync        # Linux
sudo dd if=./linux.iso of=/dev/rdiskN bs=4m                                # macOS (rdisk = plus rapide)
sync
```

> Astuce: **Ventoy** permet de copier plusieurs ISO sur une seule clé.

---

# 4) Préparer l’UEFI/BIOS

## Accès UEFI/Boot menu

* **Boot menu**: `F12` (Dell/Lenovo), `F8`/`F11`, `Esc` (HP), parfois `F10`.
* **Setup UEFI**: `Del`/`F2` au démarrage.

## Réglages clés

* **Boot Mode** : **UEFI** (préféré).
* **Secure Boot** :

  * Ubuntu/Kubuntu signés → **fonctionnent avec Secure Boot** (shim signé).
  * Si souci (distro non signée, pilotes tiers) → **désactive Secure Boot** ou **enrôle MOK**.
* **Boot Priority** : place **USB** au-dessus du disque **ou** utilise le **Boot menu** (recommandé pour un test ponctuel).
* **Fast Boot** (UEFI) : **désactive** pour faciliter détection USB au boot.
* **CSM/Legacy** : **désactivé** si tu installes en pur **UEFI** (recommandé).

### Si dual-boot avec Windows (préinstallé)

* Dans Windows :

  * **Désactive Fast Startup** (Options d’alimentation > “Choisir l’action des boutons”…).
  * Si **BitLocker** actif → **suspends** le chiffrement avant installation.
  * **Intel RST**: passer en **AHCI** (sinon l’installateur ne voit pas le disque).
* **Shrinker** la partition Windows **depuis Windows** (Gestion des disques) pour éviter des soucis NTFS.

---

# 5) Installation (schéma standard)

1. **Boote sur la clé** (Boot menu → USB).
2. **Essaye en live** (“Try without installing”) pour vérifier Wi-Fi, écran, touchpad.
3. **Install** :

   * **Type d’installation** :

     * **Effacer le disque** (PC dédié Linux)
     * **À côté de Windows** (dual-boot auto)
     * **Manuel (“Something else”)** si tu veux maîtriser les partitions
   * **Partitions conseillées (UEFI)** :

     * **EFI** (FAT32) ~ **300–512 MB** (si non existante)
     * **/** (racine) **30–60 GB** mini
     * **/home** (données) le reste
     * **swap** : fichier auto ok ; sinon partition ~ **RAM** (max 8–16 GB utile pour hibernation)
   * **Chiffrement LUKS** (optionnel) si tu veux protéger les données.
4. Fin d’installation → **retire la clé** → **redémarre**.
5. Dans l’UEFI, vérifie que l’entrée **“ubuntu”** (Kubuntu) est bien en tête si le boot saute.

---

# 6) Après l’installation (Kubuntu)

* **Mises à jour** : `Discover` ou terminal

  ```bash
  sudo apt update && sudo apt full-upgrade -y
  ```
* **Pilotes** : *Driver Manager* (pilotes **NVIDIA** propriétaires si besoin 3D).
* **KDE Plasma** : personnalise thème, panel, raccourcis.
* **Flatpak/Snap** (optionnels) pour apps récentes.

---

# 7) Pourquoi **USB 3.0** (et quand préférer 2.0)

* **USB 3.0** = **débit bien supérieur** → création **et** boot **beaucoup plus rapides** (copie ISO + live session).
* Sur **vieux PC/UEFI capricieux**, un **port USB 2.0** peut parfois mieux booter → essaie les deux si souci.

---

# 8) Pannes courantes & solutions rapides

* **La clé n’apparaît pas dans le boot menu**

  * Recrée la clé (Etcher/Rufus), **désactive Fast Boot**, essaie **autre port** (2.0 vs 3.0), vérifie **UEFI vs Legacy**.
* **“No bootable device”**

  * Mauvais mode (ISO écrite en MBR/Legacy, UEFI exigé), **Secure Boot** bloque la distro non signée, ou **Boot Order** incorrect.
* **L’installateur ne voit pas le disque**

  * **Intel RST** → passe en **AHCI** (et ajoute le pilote NVMe si rare).
* **Écran noir (NVIDIA)**

  * Au menu de boot : options **nomodeset** ou installe ensuite **nvidia-driver-xxx** via *Driver Manager*.
* **Dual-boot absent**

  * Démarre sur **Kubuntu**, `sudo update-grub`. Dans l’UEFI, met l’entrée **ubuntu** en premier.
