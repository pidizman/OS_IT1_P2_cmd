# OS_IT1_P2_cmd

## Vypsání běžících procesů 
### Windows
```cmd
tasklist
```

### UNIX (Linux)
```bash
ps ax
```

## Ukončení bežícího procesů
### Windows
```cmd
taskkill <PID>
```

### UNIX (Linux)
```bash
kill <PID>
```

## Zvýšení priority procesů
### Windows
Skrze jméno určitého procesu
```cmd
wmic process where name="<jméno procesu>" CALL setpriority <hodnota priority>
```
Skrz PID určitého procesu
```cmd
wmic process where processid=<PID> CALL setpriority <hodnota priority>
```
Tabulka prioritních hodnot
| **priority level** | **ID** |
|--------------------|--------|
| realtime           | 256    |
| high               | 128    |
| above normal       | 32768  |
| normal             | 32     |
| below normal       | 16384  |
| low                | 64     |

## Nastavení úplného smazání souborů které smažu
### Windows
```cmd
fsutil behavior query DisableDeleteNotify
```

## Rozdělen disků na partition
### Windows + UNIX (Linux)
```
gparted
```

## Zjištění volného místa na disku
### Windows + UNIX (Linux)
```
df
```

## Vypsání aktuální IP adres
### UNIX (Linux) debian
```bash
ip add show
```

## Aktualizace seznamu balíčků ze zrcadel distribuce
### UNIX (Linux) debian
```bash
sudo apt update
```

## Aktualizace systému
### UNIX (Linux) debian
```bash
sudo apt upgrade
```

## Instalace nového balíčku
### UNIX (Linux) debian
```bash
sudo apt install <balíček>
```

## Přihlášení jako root
### UNIX (Linux) debian
```bash
sudo su -
```

## Výpsání kdo je příhlášený
### UNIX (Linux) debian
```bash
w
```
```bash
who
```

## Odeslání souboru
### UNIX (Linux) debian
```bash
scp <zdroj> <cíl>
```
Client -> Server
```bash
scp /etc/hosts student@<ip>:/tmp/
```
Server -> Client
```bash
scp student@<ip>:/etc/hosts /tmp/
```

## Vygenerování ssh klíču na klientovi
### UNIX (Linux) debian
```bash
ssh-keygen
```

## Kopírování ssh klíčů z klienta na server
### UNIX (Linux) debian
```bash
ssh-copy-id <účet>@<ip>
```

## Nastavení přihlášení pouze skrze ssh key
### UNIX (Linux) debian
```bash
nano /etc/ssh/sshd_config
```
Poté nastavit `PasswordAuthentication no` NEZAPOMENOUT ODSTRANIT `#`!!
CTRL+X (uložení změn) a `sudo reboot`
