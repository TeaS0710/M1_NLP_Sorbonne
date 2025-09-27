```bash
# 0) Vérifier l’accès réseau vers le serveur (depuis n’importe quel Wi-Fi)
nc -vz 89.80.61.108 2222

# 1) Nettoyer un port 8080 coincé et arrêter les services (si présents)
fuser -k 8080/tcp 2>/dev/null || true
systemctl --user stop intranet-tunnel sshfs-share 2>/dev/null || true
fusermount -u ~/ServeurShare 2>/dev/null || true

# 2) Relancer à la main (sans systemd) pour tester
ssh -f -N \
  -i ~/.ssh/id_ed25519 \
  -L 8080:127.0.0.1:8000 \
  -o ExitOnForwardFailure=yes \
  -o ServerAliveInterval=15 -o ServerAliveCountMax=3 \
  -p 2222 teas@89.80.61.108

mkdir -p ~/ServeurShare
sshfs -o reconnect \
  -i ~/.ssh/id_ed25519 \
  -p 2222 teas@89.80.61.108:/home/teas/SharedFiles ~/ServeurShare

# 3) Vérifications
ss -lnp | grep ':8080 '
mount | grep ServeurShare
curl -I http://127.0.0.1:8080/ | head -n1
