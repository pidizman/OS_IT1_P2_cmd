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
