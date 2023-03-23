# -*- coding=utf-8 -*-
import wx
from random import randint
class my(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="单词V1.0",pos=(100,100),size=(600,300))
        panel = wx.Panel(self)
        self.stopwords = []
        self.keys = []
        self.words = {}
        self.choice = 0  # 选择单词
        self.stopstep()  # 读取文件
        self.wordsstep()
        self.next_button = wx.Button(panel, label="下一个")
        self.next_button.Bind(wx.EVT_BUTTON, self.click_next)
        self.stop_button = wx.Button(panel, label="已学会")
        self.stop_button.Bind(wx.EVT_BUTTON, self.click_stop)
        self.label_E = wx.StaticText(panel, label=f'{self.keys[self.choice].ljust(14,"_")}:')
        self.label_C = wx.StaticText(panel, label='  ***')
        self.label_ok = wx.StaticText(panel, label='是否学会:否')
        self.label_C.Bind(wx.EVT_ENTER_WINDOW,self.show)
        self.label_C.Bind(wx.EVT_LEAVE_WINDOW, self.inshow)
        h1 = wx.BoxSizer(wx.HORIZONTAL)
        h1.Add(self.stop_button, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        h1.Add(self.next_button, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        h2 = wx.BoxSizer(wx.HORIZONTAL)
        h2.Add(self.label_E, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        h2.Add(self.label_C, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        v1 = wx.BoxSizer(wx.VERTICAL)
        v1.Add(h2, proportion=0, flag=wx.ALL|wx.ALIGN_CENTER, border=20)
        v1.Add(h1, proportion=0, flag=wx.ALL|wx.ALIGN_CENTER, border=20)
        v1.Add(self.label_ok, proportion=0, flag=wx.ALL|wx.ALIGN_CENTER, border=20)
        panel.SetSizer(v1)

    def stopstep(self):
        stopflie = open('stopwords.txt', 'r', encoding='utf-8')
        f = stopflie.readlines()
        for i in f:
            i = i.strip()
            if i:
                self.stopwords.append(i)
        stopflie.close()

    def wordsstep(self):
        wordsfile = open('words.txt','r',encoding='utf-8')
        f = wordsfile.readlines()
        for i in f:
            i = i.strip()
            if i is not None:
                if i.split(',')[0] not in self.stopwords:

                    self.words[i.split(',')[0]] = i.split(',')[1]
                    self.keys.append(i.split(',')[0])
                    print(self.keys,self.words)
        wordsfile.close()


    def click_next(self,event):
        self.choice = randint(0, len(self.keys)-1)
        self.label_E.Label = f'{self.keys[self.choice].ljust(14,"_")}:'
        print(self.choice)

    def click_stop(self, event):
        word = self.keys[self.choice]

        f = open('stopwords.txt', "a+",encoding='utf-8')
        f.write(f"\n{word}")

        f.close()
        self.label_ok.Label = '是否学会:是'

    def show(self,event):
        self.label_C.Label = self.words[self.keys[self.choice]]
        print(self.words[self.keys[self.choice]])

    def inshow(self,event):
        self.label_C.Label = '  **'
if __name__ == '__main__':
    app = wx.App()
    frame = my(None, -1)
    frame.Show()
    app.MainLoop()


