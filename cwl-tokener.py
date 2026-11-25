with open ("index.cwl","r",encoding="utf-8") as file:
  for line in file:
    for char in line:
      if char=="#":
        state=True
      else: 
        state=False
      if state==True:
        if char=="t":
          typus="text"
        elif char=="i":
          typus="img"
        elif char=="v":
          typus="video"
        elif char=="s":
          typus="style"
        elif char =="c":
          typus="code"
        elif char=="a":
          typus="api"
      
          
