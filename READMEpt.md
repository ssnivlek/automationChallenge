## Desafio Automação

**Objetivo:** Criar libs de leitura de .pdf e automação de criação de arquivo .xlsx

**Etapas da automação:**

- Baixar pdfs de "Reporte_36~40" do seguinte website:
  https://www.gob.mx/conadesuca/documentos/dieproc-reportes-de-avance-de-produccion-ciclo-azucarero-2020-2021?state=published
- Após realizar a leitura do .pdf e transformar a tabela "Cuadro 7" em um dataframe
- Deletar colunas do dataframe e adicionar uma nova com o período do Reporte
- Transformar o dataframes de todos os Reportes em um único arquivo .xlsx com cada dataframe sendo um sheet do excel.

**_Libs de terceiros utilizadas:_**
_Demais libs listadas no arquivo requirements.txt_

- Camelot
- PyPDF2
- BeautifulSoup
- Requests
- GhostScript
- OpenCV
- XlsxWriter

**Como rodar a aplicação:**
_Após instalar todas as libs necessárias via requirements.txt_, seguir os seguintes passos:
Executar o arquivo `main.py` na pasta `libs/automation`:

    python3 main.py
    ou
    python main.py

_O próprio arquivo possui um exemplo dos parâmetros esperados para rodar a aplicação, utilize-os para ter uma breve noção_

Quaisquer outras dúvidas entrar em contato comigo ;)
