html = open('hey.html', 'a')
html.write('<TABLE BORDER=0 CELLPADDING=10 CELLSPACING=0>\n    <TR>\n')
atm = 0x000000
for i in range(16):
    for j in range(16):
        string = str(atm)
        html.write('      <TD WIDTH="10" HEIGHT="10" BGCOLOR=#')
        html.write(string)
        html.write('>')
html.close()
