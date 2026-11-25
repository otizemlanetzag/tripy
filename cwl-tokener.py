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
          lined=line.strip("#t")
        elif char=="i":
          typus="img"
          lined=line.strip("#i")
        elif char=="v":
          typus="video"
          lined=line.strip("#v")
        elif char=="s":
          typus="style"
          lined=line.strip("#s")
        elif char =="l":
          typus="logic"
          lined=line.strip("#l")
        elif char=="a":
          typus="api"
          lined=line.strip("#a")
      
