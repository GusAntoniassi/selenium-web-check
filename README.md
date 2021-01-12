# Instalação (execução manual)
Criar virtualenv
```
virtualenv env
``` 

Instalar dependências
```
pip install -r requirements.txt
```

**Importante:** O arquivo `chromedriver` fornecido aqui é o que tem suporte à versão 83 do Chrome/Chromium. Caso o seu sistema use outra versão (`chromium --version` ou `chrome --version`), visite a página de downloads para baixar o driver adequado: https://chromedriver.chromium.org/downloads. O `geckodriver` está disponível em: https://github.com/mozilla/geckodriver/releases

# Execução
Ativar virtualenv
```
source env/bin/activate
```

Executar
```
python3 main.py
``` 