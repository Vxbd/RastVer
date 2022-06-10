# RastVer (Rastrexador de información Verificada)

Descripción: Rastrexador baseado en Scrapy e Python.
O seu obxectivo é extraer breves textos de novas
e a súa clasificación de veracidade da páxina 
mediabiasfactcheck.com. Parte inicial TFG.

Requisitos:
-----------------
- Python 3.8
- Scrapy 2.6.1


Uso:
-----------------
Unha vez con todas as dependencias resoltas, situámonos
no diretoriorio RastVer do proxecto onde se atopa este arquivo
e chamamos a scrapy indicándolle a araña que debe executar.

-> scrapy crawl rastver

Na súa configuración actual o programa xerará un ficheiro coa 
co nome rastverDATA.txt cos datos obtidos, a par, na terminal 
irá aparecendo o tipo de páxina que se está a rastrexar e outra 
moita información. 


Axustes:
-----------------
Existe un ficheiro settings.py onde se pode modificar configuracións de Scrapy. Destacamos dous:

-> Xerar un documento de log:
En lugar de ter a saída pola terminal obtemos un documento con todos 
estes datos. Especialmente útil para a súa execución final. Descoemntar 
as liñas 92 e 93 que conteñen:
#LOG_STDOUT = True
#LOG_FILE = directorio do ficheiro de destino

-> Cambiar o retardo entre peticións:
Dispoñeible na liña 29. Pode ser necesario modificalo dependendo da rede
onde se estea a executar ou se se modifica a páxina obxectivo.
DOWNLOAD_DELAY = 1

Modificacións:
-----------------
A araña que realiza o seguimento de links é spiders/rastver.py. Fai uso da clase New. 