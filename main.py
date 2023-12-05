import os

def dev():
    os.system('clear')
    print("""
\033[32m ╔╦╗╔═╗╦  ╦╔═╗╦  ╔═╗╔═╗╔═╗╦═╗
\033[32m  ║║║╣ ╚╗╔╝║╣ ║  ║ ║╠═╝║╣ ╠╦╝
\033[32m ═╩╝╚═╝ ╚╝ ╚═╝╩═╝╚═╝╩  ╚═╝╩╚═
\033[32m
\033[32m Developer: LazyDev
\033[32m From: DefacerPh | Philippine Cyber Alliance        
""")

def crtdp():
    os.system('clear')
    print("""
\033[32m ╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╔╦╗╔═╗
\033[32m ║  ╠╦╝║╣ ╠═╣ ║ ║╣  ║║╠═╝
\033[32m ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝═╩╝╩  
          
""")
    cn = input("[ENTER YOUR CODENAME] > ")
    imglink = input("[ENTER IMAGE LINK] > ")
    filename = input("[ENTER DEFPAGE FILE NAME] > ")
    css = """
<style>
  body{
    background-color: black;
  }

  font{
    font-family: 'Courier New', Courier, monospace;
  }

</style>  
"""
    dp = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Hacked by {}</title>
</head>
{}
<body>
  <center>
    <div class="output">
      <br>
      <br>
      <img src="{}" width="200px">
      <br>
      <font id="cursor" color="white" size="6px"> ./Hacked by </font>
      <font id="codename" color="green" class="lol" size="6px"> 
 {} </font>
      <br>
      <br>
      <font size="5px" color="green">
        Hello Admin, I want to inform you that your website<br>
        is too vulnerable. Please patch your website to avoid data breach. Thankyou!
      </font>
    </div>

    <script>
      alert('{} was here')
    </script>
  </center>
</body>

</html>""".format(cn, css, imglink, cn, cn)
    finalf = filename+'.html'
    open(finalf, 'a+').write(dp)
    print("\033[32m Defpage successfuly created!")


def cmd():
    while True:
        cmd = input("\033[32m [root@dpcreator] > ")
        if cmd == "1":
          crtdp()
        elif cmd == "2":
          dev()
        elif cmd == "":
           print("\033[31m Please enter something!")
        else:
          print("\033[31m Please enter the right command!")

def main():
    os.system('clear')
    print("""
\033[32m ╔╦╗╔═╗╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
\033[32m  ║║╠═╝║  ╠╦╝║╣ ╠═╣ ║ ║ ║╠╦╝
\033[32m ═╩╝╩  ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝╩╚═          

\033[32m 1. Create DefacePage
\033[32m 2. Developer
\033[32m 4. Exit   
""")
    cmd()

main()