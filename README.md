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

## Ukončení bežícího procesu
### Windows
```cmd
taskkill <PID>
```

### UNIX (Linux)
```bash
kill <PID>
```

## Zvýšení priority procesu
### Windows
Skrze jméno určitého procesu
```cmd
wmic process where name="<jméno procesu>" CALL setpriority 32
```
Skrz PID určitého procesu
```cmd
wmic process where processid=<PID> CALL setpriority 32
```
