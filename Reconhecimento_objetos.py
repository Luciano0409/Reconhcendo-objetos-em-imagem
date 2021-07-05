from tkinter import *
import requests
import json

token1 = open('token1.txt','r')
token1 = token1.readlines()

token2 = open('token2.txt','r')
token2 = token2.readlines()

url = open('url.txt','r')
url = url.readlines()

class Application:
    def __init__(self, master=None):

        # Fonte do texto
        self.fontePadrao = ("Arial", "10", "bold")

        # Localização dos widgets
        self.Conteiner1 = Frame(master)
        self.Conteiner1["pady"] = 30
        self.Conteiner1.pack()

        # Largura da tela
        self.Container2 = Frame(master)
        self.Container2["padx"] = 20
        self.Container2.pack()

        # Altura da tela
        self.Container3 = Frame(master)
        self.Container3["pady"] = 10
        self.Container3.pack()

        # Texto apresentado na tela
        self.titulo = Label(self.Conteiner1, text="Analise de materiais de construção")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # Texto apresentado na tela
        self.nome_Label = Label(self.Container2, text="Diretório da imagem: ", font=self.fontePadrao)
        self.nome_Label.pack(side=LEFT)

        # Box que recebe a imagem
        self.texto = Entry(self.Container2)
        self.texto["width"] = 60
        self.texto["font"] = self.fontePadrao
        self.texto.pack(side=LEFT)

        # Botão
        self.buscar = Button(self.Container3)
        self.buscar["text"] = "Analisar"
        self.buscar["font"] = ("Arial", "10")
        self.buscar["width"] = 12
        self.buscar["command"] = self.AnalisarImagem
        self.buscar.pack()

        self.mensagem = Label(self.Container3, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
    def AnalisarImagem(self):
        # url = url # URL do site que analisa a imagem com a imagens que foi passada para IA treinar 

        data = {'files': open(self.texto.get(), 'rb'), 'modelId': ('', token1)}

        # Resultado na analise
        response = requests.post(url, auth= requests.auth.HTTPBasicAuth(token2, ''), files=data)
        result = json.loads(response.text)['result'][0]['prediction'][0]['label']
        self.mensagem["text"] = result
        
  
janela = Tk()
janela.columnconfigure(0, minsize=250)
janela.rowconfigure([0, 1], minsize=300)
Application(janela)
janela.mainloop()

