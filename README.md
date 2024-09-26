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
