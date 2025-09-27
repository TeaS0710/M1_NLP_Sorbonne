# 1) Quick start
## A) Ouvrir & démarrer une VM existante

1. Lance **VirtualBox**.
2. Dans la liste, sélectionne ta VM.
3. Clique **Start ▶️** (ou **Headless Start** si tu n’as pas besoin de fenêtre).

## B) Créer & installer vite une nouvelle VM (depuis un ISO)

1. **New** → Name (ex. `Ubuntu-22.04`) → Type (Linux/Windows) → Version (64-bit).
2. **Memory** : 4–8 GB conseillé pour Linux, 8–16 GB pour Windows (selon ta RAM).
3. **Disk** : Create VDI → Dynamically allocated → 40–80 GB.
4. **Settings > Storage** → clique le lecteur optique → **Choose a disk file…** → sélectionne ton **.iso**.
5. **Settings > System > Boot Order** : mets **Optical** en premier pour l’installation.
6. **Start ▶️** → suis l’installateur de l’OS.
7. Après installation, enlève l’ISO (**Storage** → retire le disque) ou passe **Boot Order** sur **Hard Disk** en premier.
8. (Optionnel) **Devices > Insert Guest Additions CD image…** puis installe dans l’OS invité (meilleure vidéo, copier/coller, etc.).

---

# 2) Commandes utiles (CLI)

> **VBoxManage** (Windows PowerShell / macOS Terminal).

* Lister les VMs :

  ```
  VBoxManage list vms
  VBoxManage list runningvms
  ```
* Démarrer / arrêter :

  ```
  VBoxManage startvm "NomDeVM" --type gui      # ou headless
  VBoxManage controlvm "NomDeVM" acpipowerbutton
  VBoxManage controlvm "NomDeVM" poweroff
  ```
* Réglages rapides :

  ```
  VBoxManage modifyvm "NomDeVM" --memory 8192 --cpus 4
  VBoxManage modifyvm "NomDeVM" --vram 128 --graphicscontroller vmsvga
  VBoxManage storageattach "NomDeVM" --storagectl "SATA" --port 0 --device 0 --type hdd --medium chemin/disque.vdi
  VBoxManage storageattach "NomDeVM" --storagectl "SATA" --port 1 --type dvddrive --medium chemin/image.iso
  ```

---

# 3) Windows — erreurs fréquentes & fixes (console)

## A) “VT-x not available”, “Raw-mode is unavailable courtesy of Hyper-V”

Conflit avec **Hyper-V / WSL2 / Virtual Machine Platform**.

**Désactiver Hyper-V (admin PowerShell) :**

```powershell
bcdedit /set hypervisorlaunchtype off
dism /Online /Disable-Feature:Microsoft-Hyper-V-All
dism /Online /Disable-Feature:VirtualMachinePlatform
dism /Online /Disable-Feature:Windows-Hypervisor-Platform
```

> Redémarre ensuite.
> (Si tu utilises WSL2, tu devras réactiver ces features.)

**Vérifier l’état :**

```powershell
dism /Online /Get-Features /Format:Table | findstr /i "hyper virtual"
```

**Désactiver “Memory Integrity / Core Isolation” (si VT-x toujours bloqué)**
Paramètres Windows → Sécurité Windows → Sécurité de l’appareil → **Intégrité de la mémoire** → OFF → redémarre.

## B) “E_FAIL (0x80004005)” au démarrage

Causes variées. Essaie :

```powershell
# Mettre à jour drivers VirtualBox + Extension Pack (même version)
# Réparer l’adaptateur Host-Only
VBoxManage hostonlyif remove "VirtualBox Host-Only Ethernet Adapter"
VBoxManage hostonlyif create
# Réinitialiser la NVRAM de la VM (UEFI)
VBoxManage setextradata "NomDeVM" "VBoxInternal/Devices/efi/0/Config/ResetNvram" 1
```

## C) Réseau invité KO (pas d’IP)

```powershell
# Recréer l’host-only et rebasculer la VM en "NAT" (simple) :
VBoxManage hostonlyif create
# Dans GUI : Settings > Network > Adapter 1 = NAT
```

## D) Lancement headless/autostart

```powershell
VBoxManage startvm "NomDeVM" --type headless
```

---

# 4) macOS — erreurs fréquentes & fixes (Terminal)

## A) “Kernel driver not installed (rc=-1908)” / Extension non autorisée

1. Ouvre **Réglages Système > Confidentialité et Sécurité** → autorise **Oracle America, Inc.** (kext / extension système), puis **redémarre**.
2. Redémarre le service VirtualBox :

```bash
sudo "/Library/Application Support/VirtualBox/LaunchDaemons/VirtualBoxStartup.sh" restart
```

3. Sinon, réinstalle VirtualBox (même version que l’Extension Pack) et ré-autorise.

## B) Apple Silicon (M1/M2/M3)

* VirtualBox ne fait tourner **que des invités ARM64** (pas d’OS x86).
* Alternatives simples : **UTM** (gratuit) ou **Parallels Desktop**.
* Utilise des **ISOs ARM64** (ex. Ubuntu Server arm64, Windows 11 ARM).

## C) Pas d’affichage / écran noir

```bash
# Forcer le contrôleur vidéo moderne
VBoxManage modifyvm "NomDeVM" --graphicscontroller vmsvga --vram 128
```

## D) Réseau invité KO

```bash
# Recréer host-only et repasser en NAT
sudo VBoxManage hostonlyif create
# Puis, dans l’interface, Settings > Network > Adapter 1 = NAT
```

---

# 5) Bonnes pratiques

* **Alloue raisonnable** (RAM/CPU) : laisse toujours de la marge à l’hôte.
* **Snapshots** avant une manip risquée : **Machine > Take Snapshot**.
* **ISO correct** (x64 vs arm64) et **type d’OS** cohérent.
* **Guest Additions** pour un confort (résolution auto, presse-papier).
* **Extension Pack** (même version) pour USB 2/3, RDP, NVMe.
