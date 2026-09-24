from locale import str
import os
from file import File
from encryption import Crypt
import requests
import json
import webbrowser

class Func:

    @staticmethod
    # pyrefly: ignore [not-a-type]
    def AddHook(url: str):
        if not url.find("https://discord.com/api/webhooks/"):
            if not os.path.exists("data/hooks"):
                File.Write('create',"data/hooks")
            try:
                webhook_name = Func.get_webhook_name(url)
            except:
                webhook_name = 'error'
            key = Func.GetKey()
            enc_url = Crypt.Encrypt(url,key)
            data = webhook_name+'[/hook/%context%/]'+enc_url.decode("utf-8")
            File.Add(data,"data/hooks")
        else:
            print("not a webhook")

    @staticmethod
    def GetKey():
        keyList = File.Read("data/key.db")
        key = Crypt.Decrypt64(keyList[0])
        return key

    @staticmethod
    # pyrefly: ignore [not-a-type]
    def get_webhook_name(webhook_url:str) -> str:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            data = response.json()
            return data.get('name', 'Webhook Name Not Found')
        else:
            return 'Error'

    @staticmethod
    def GetHooks():
        hooksList = File.Read("data/hooks")
        if hooksList != ['null']:
            splitHooks = [hook.split("[/hook/%context%/]") for hook in hooksList]

            processedHooks = []
            for hook in splitHooks:
                if len(hook) >= 2:
                    key = Func.GetKey()
                    decrypted = Crypt.Decrypt(hook[1], key)
                    processedHooks.append([hook[0], decrypted])
                else:
                    processedHooks.append(hook)

            return processedHooks
        return 'null'

    @staticmethod
    # pyrefly: ignore [not-a-type]
    def DelHook(url: str):
        str_url = str(url)
        str_url = str_url.replace('\n','')
        dataList = Func.GetHooks()
        key = Func.GetKey()
        string= ''
        for x in range(len(dataList)):
            #print(dataList[x][1]+'?='+str_url)
            if dataList[x][1] != str_url:
                #print(dataList[x][1]+'!='+str_url)
                enc_url = Crypt.Encrypt(dataList[x][1],key)
                string +='[/bin/%context%/]'+dataList[x][0]+"[/hook/%context%/]"+enc_url.decode("utf-8")
        File.Write(string, "data/hooks", True)

    @staticmethod
    # pyrefly: ignore [not-a-type]
    def Send(url:str, context: str, file_paths: str):
        payload = {
            'content': context
        }
        response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

        if response.status_code == 204:
            print('Message and files sent successfully.')
        else:
            print('Error sending message and files:', response.text)

        for file in file_paths:
            with open(file, 'rb') as file:
                files = {'file': file}
                response = requests.post(url, files=files)

            if response.status_code == 200:
                print('File sent successfully.')
            else:
                print('Error sending file:', response.text)

    @staticmethod
    def Git():
        webbrowser.open('https://github.com/ByteCorum', new=2)
