
import webbrowser

f = open('summersales.html','w')

message = """<html>
<head></head>
    <body>
        <h1><p>Stay tuned for our amazing summer sale!</p></h1>
    </body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('summersales.html')
