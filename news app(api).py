from tkinter import *
import requests

api='d7494bb392524150b92b90f2ee7e35c9'

url=f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api}'
response = requests.get(url)
data = response.json()

# print(data)

window=Tk()

window.title("📰 News App")
window.geometry("900x600")
window.configure(bg="white")

news_text=Text(window,
               width=80,
               height=25,
               font="Arial",
               bg="white",)
news_text.pack()



if response.status_code == 200:
    for article in data['articles']:
        title = article['title']
        news_text.insert(END, title + '\n\n')
        content =article.get('content') or 'No content available.'
        news_text.insert(END, content + '\n\n')

        # print(title)
else:
    print("error")


window.mainloop()