#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
import datetime
import os.path
import math
from sodapy import Socrata
pd.options.display.float_format = '{:,}'.format


# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("www.datos.gov.co", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(www.datos.gov.co,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("gt2j-8ykr", limit=4900000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

for col in results_df.columns: 
    print(col) 

print(results_df.departamento_nom.unique())
print(results_df.head(50))

#Colombia

casos_confirmados_total = len(results_df)

casos_total_millon = int((casos_confirmados_total/50372424)*1000000)

Total_fallecidos = len(results_df[results_df.recuperado == "Fallecido"])

Total_fallecidos_millon = int((Total_fallecidos/50372424)*1000000)

Total_recuperados = len(results_df[results_df.recuperado == "Recuperado"])

Total_criticos = len(results_df[results_df.estado == 'Grave'])

#rows with a 'not available' value  
not_available_data= len(results_df[results_df.recuperado == "N/A"])

Total_activos = casos_confirmados_total - (Total_recuperados + Total_fallecidos + not_available_data)

##


# # Amazonas

amazonas_df = results_df[results_df.departamento_nom == "AMAZONAS"]

amazonas_casos_total = len(amazonas_df)

amazonas_casos_millon = int((amazonas_casos_total/80577)*1000000)

amazonas_fallecidos = len(amazonas_df[amazonas_df.recuperado == "Fallecido"])

amazonas_fallecidos_millon = int((amazonas_fallecidos/80577)*1000000)

amazonas_recuperados = len(amazonas_df[amazonas_df.recuperado == "Recuperado"])

amazonas_criticos = len(amazonas_df[amazonas_df.estado == "Grave"])

amazonas_na_values = len(amazonas_df[amazonas_df.recuperado == "N/A"])

amazonas_activos = amazonas_casos_total - (amazonas_recuperados + amazonas_fallecidos + amazonas_na_values)

####


##Antioquia

antioquia_df = results_df[results_df.departamento_nom == "ANTIOQUIA"]

antioquia_casos_total = len(antioquia_df)

antioquia_casos_millon = int((antioquia_casos_total/6855517)*1000000)

antioquia_fallecidos = len(antioquia_df[antioquia_df.recuperado == "Fallecido"])

antioquia_fallecidos_millon = int((antioquia_fallecidos/6855517)*1000000)

antioquia_recuperados = len(antioquia_df[antioquia_df.recuperado == "Recuperado"])

antioquia_criticos = len(antioquia_df[antioquia_df.estado == "Grave"])

antioquia_na_values = len(antioquia_df[antioquia_df.recuperado == "N/A"])

antioquia_activos = antioquia_casos_total - (antioquia_recuperados + antioquia_fallecidos + antioquia_na_values)

###Arauca

arauca_df = results_df[results_df.departamento_nom == "ARAUCA"]

arauca_casos_total = len(arauca_df)

arauca_casos_millon = int((arauca_casos_total/275814)*1000000)

arauca_fallecidos = len(arauca_df[arauca_df.recuperado == "Fallecido"])

arauca_fallecidos_millon = int((arauca_fallecidos/275814)*1000000)

arauca_recuperados = len(arauca_df[arauca_df.recuperado == "Recuperado"])

arauca_criticos = len(arauca_df[arauca_df.estado == "Grave"])

arauca_na_values = len(arauca_df[arauca_df.recuperado == "N/A"])

arauca_activos = arauca_casos_total - (arauca_recuperados + arauca_fallecidos + arauca_na_values)

###


##Atlántico


atlantico_df = results_df[results_df.departamento_nom == "ATLANTICO"]

atlantico_casos_total = len(atlantico_df)

atlantico_casos_millon = int((atlantico_casos_total/1362823)*1000000)

atlantico_fallecidos = len(atlantico_df[atlantico_df.recuperado == "Fallecido"])

atlantico_fallecidos_millon = int((atlantico_fallecidos/1362823)*1000000)

atlantico_recuperados = len(atlantico_df[atlantico_df.recuperado == "Recuperado"])

atlantico_criticos = len(atlantico_df[atlantico_df.estado == "Grave"])

atlantico_na_values = len(atlantico_df[atlantico_df.recuperado == "N/A"])

atlantico_activos = atlantico_casos_total - (atlantico_recuperados + atlantico_fallecidos + atlantico_na_values)

###

###Barranquilla D.E.

barranquilla_df = results_df[results_df.departamento_nom == "BARRANQUILLA"]

barranquilla_casos_total = len(barranquilla_df)

barranquilla_casos_millon = int((barranquilla_casos_total/1243113)*1000000)

barranquilla_fallecidos = len(barranquilla_df[barranquilla_df.recuperado == "Fallecido"])

barranquilla_fallecidos_millon = int((barranquilla_fallecidos/1243113)*1000000)

barranquilla_recuperados = len(barranquilla_df[barranquilla_df.recuperado == "Recuperado"])

barranquilla_criticos = len(barranquilla_df[barranquilla_df.estado == "Grave"])

barranquilla_na_values = len(barranquilla_df[barranquilla_df.recuperado == "N/A"])

barranquilla_activos = barranquilla_casos_total - (barranquilla_recuperados + barranquilla_fallecidos + barranquilla_na_values)

####

##Bolivar


bolivar_df = results_df[results_df.departamento_nom == "BOLIVAR"]

bolivar_casos_total = len(bolivar_df)

bolivar_casos_millon = int((bolivar_casos_total/2223201)*1000000)

bolivar_fallecidos = len(bolivar_df[bolivar_df.recuperado == "Fallecido"])

bolivar_fallecidos_millon = int((bolivar_fallecidos/2223201)*1000000)

bolivar_recuperados = len(bolivar_df[bolivar_df.recuperado == "Recuperado"])

bolivar_criticos = len(bolivar_df[bolivar_df.estado == "Grave"])

bolivar_na_values = len(bolivar_df[bolivar_df.recuperado == "N/A"])

bolivar_activos = bolivar_casos_total - (bolivar_recuperados + bolivar_fallecidos + bolivar_na_values)

###

##Boyaca


boyaca_df = results_df[results_df.departamento_nom == "BOYACA"]

boyaca_casos_total = len(boyaca_df)

boyaca_casos_millon = int((boyaca_casos_total/1285296)*1000000)

boyaca_fallecidos = len(boyaca_df[boyaca_df.recuperado == "Fallecido"])

boyaca_fallecidos_millon = int((boyaca_fallecidos/1285296)*1000000)

boyaca_recuperados = len(boyaca_df[boyaca_df.recuperado == "Recuperado"])

boyaca_criticos = len(boyaca_df[boyaca_df.estado == "Grave"])

boyaca_na_values = len(boyaca_df[boyaca_df.recuperado == "N/A"])

boyaca_activos = boyaca_casos_total - (boyaca_recuperados + boyaca_fallecidos + boyaca_na_values)

####

##Caldas

caldas_df = results_df[results_df.departamento_nom == "CALDAS"]

caldas_casos_total = len(caldas_df)

caldas_casos_millon = int((caldas_casos_total/997890)*1000000)

caldas_fallecidos = len(caldas_df[caldas_df.recuperado == "Fallecido"])

caldas_fallecidos_millon = int((caldas_fallecidos/997890)*1000000)

caldas_recuperados = len(caldas_df[caldas_df.recuperado == "Recuperado"])

caldas_criticos = len(caldas_df[caldas_df.estado == "Grave"])

caldas_na_values = len(caldas_df[caldas_df.recuperado == "N/A"])

caldas_activos = caldas_casos_total - (caldas_recuperados + caldas_fallecidos + caldas_na_values)

####

##Caqueta


caqueta_df = results_df[results_df.departamento_nom == "CAQUETA"]

caqueta_casos_total = len(caqueta_df)

caqueta_casos_millon = int((caqueta_casos_total/997890)*1000000)

caqueta_fallecidos = len(caqueta_df[caqueta_df.recuperado == "Fallecido"])

caqueta_fallecidos_millon = int((caqueta_fallecidos/997890)*1000000)

caqueta_recuperados = len(caqueta_df[caqueta_df.recuperado == "Recuperado"])

caqueta_criticos = len(caqueta_df[caqueta_df.estado == "Grave"])

caqueta_na_values = len(caqueta_df[caqueta_df.recuperado == "N/A"])

caqueta_activos = caqueta_casos_total - (caqueta_recuperados + caqueta_fallecidos + caqueta_na_values)

###

###Casanare


casanare_df = results_df[results_df.departamento_nom == "CASANARE"]

casanare_casos_total = len(casanare_df)

casanare_casos_millon = int((casanare_casos_total/387822)*1000000)

casanare_fallecidos = len(casanare_df[casanare_df.recuperado == "Fallecido"])

casanare_fallecidos_millon = int((casanare_fallecidos/387822)*1000000)

casanare_recuperados = len(casanare_df[casanare_df.recuperado == "Recuperado"])

casanare_criticos = len(casanare_df[casanare_df.estado == "Grave"])

casanare_na_values = len(casanare_df[casanare_df.recuperado == "N/A"])

casanare_activos = casanare_casos_total - (casanare_recuperados + casanare_fallecidos + casanare_na_values)

###

###Cauca


cauca_df = results_df[results_df.departamento_nom == "CAUCA"]

cauca_casos_total = len(cauca_df)

cauca_casos_millon = int((cauca_casos_total/1442614)*1000000)

cauca_fallecidos = len(cauca_df[cauca_df.recuperado == "Fallecido"])

cauca_fallecidos_millon = int((cauca_fallecidos/1442614)*1000000)

cauca_recuperados = len(cauca_df[cauca_df.recuperado == "Recuperado"])

cauca_criticos = len(cauca_df[cauca_df.estado == "Grave"])

cauca_na_values = len(cauca_df[cauca_df.recuperado == "N/A"])

cauca_activos = cauca_casos_total - (cauca_recuperados + cauca_fallecidos + cauca_na_values)

###

#### Cesar

cesar_df = results_df[results_df.departamento_nom == "CESAR"]

cesar_casos_total = len(cesar_df)

cesar_casos_millon = int((cesar_casos_total/1091458)*1000000)

cesar_fallecidos = len(cesar_df[cesar_df.recuperado == "Fallecido"])

cesar_fallecidos_millon = int((cesar_fallecidos/1091458)*1000000)

cesar_recuperados = len(cesar_df[cesar_df.recuperado == "Recuperado"])

cesar_criticos = len(cesar_df[cesar_df.estado == "Grave"])

cesar_na_values = len(cesar_df[cesar_df.recuperado == "N/A"])

cesar_activos = cesar_casos_total - (cesar_recuperados + cesar_fallecidos + cesar_na_values)

####

###chocó


choco_df = results_df[results_df.departamento_nom == "CHOCO"]

choco_casos_total = len(choco_df)

choco_casos_millon = int((choco_casos_total/525351)*1000000)

choco_fallecidos = len(choco_df[choco_df.recuperado == "Fallecido"])

choco_fallecidos_millon = int((choco_fallecidos/525351)*1000000)

choco_recuperados = len(choco_df[choco_df.recuperado == "Recuperado"])

choco_criticos = len(choco_df[choco_df.estado == "Grave"])

choco_na_values = len(choco_df[choco_df.recuperado == "N/A"])

choco_activos = choco_casos_total - (choco_recuperados + choco_fallecidos + choco_na_values)

####


###Cordoba

cordoba_df = results_df[results_df.departamento_nom == "CORDOBA"]

cordoba_casos_total = len(cordoba_df)

cordoba_casos_millon = int((cordoba_casos_total/1838574)*1000000)

cordoba_fallecidos = len(cordoba_df[cordoba_df.recuperado == "Fallecido"])

cordoba_fallecidos_millon = int((cordoba_fallecidos/1838574)*1000000)

cordoba_recuperados = len(cordoba_df[cordoba_df.recuperado == "Recuperado"])

cordoba_criticos = len(cordoba_df[cordoba_df.estado == "Grave"])

cordoba_na_values = len(cordoba_df[cordoba_df.recuperado == "N/A"])

cordoba_activos = cordoba_casos_total - (cordoba_recuperados + cordoba_fallecidos + cordoba_na_values)

###

###Cundinamarca

cundinamarca_df = results_df[results_df.departamento_nom == "CUNDINAMARCA"]

cundinamarca_casos_total = len(cundinamarca_df)

cundinamarca_casos_millon = int((cundinamarca_casos_total/1226488)*1000000)

cundinamarca_fallecidos = len(cundinamarca_df[cundinamarca_df.recuperado == "Fallecido"])

cundinamarca_fallecidos_millon = int((cundinamarca_fallecidos/1226488)*1000000)

cundinamarca_recuperados = len(cundinamarca_df[cundinamarca_df.recuperado == "Recuperado"])

cundinamarca_criticos = len(cundinamarca_df[cundinamarca_df.estado == "Grave"])

cundinamarca_na_values = len(cundinamarca_df[cundinamarca_df.recuperado == "N/A"])

cundinamarca_activos = cundinamarca_casos_total - (cundinamarca_recuperados + cundinamarca_fallecidos + cundinamarca_na_values)

###

###Guainía



guainia_df = results_df[results_df.departamento_nom == "GUAINIA"]

guainia_casos_total = len(guainia_df)

guainia_casos_millon = int((guainia_casos_total/44844)*1000000)

guainia_fallecidos = len(guainia_df[guainia_df.recuperado == "Fallecido"])

guainia_fallecidos_millon = int((guainia_fallecidos/44844)*1000000)

guainia_recuperados = len(guainia_df[guainia_df.recuperado == "Recuperado"])

guainia_criticos = len(guainia_df[guainia_df.estado == "Grave"])

guainia_na_values = len(guainia_df[guainia_df.recuperado == "N/A"])

guainia_activos = guainia_casos_total - (guainia_recuperados + guainia_fallecidos + guainia_na_values)

###

##Guaviare


guaviare_df = results_df[results_df.departamento_nom == "GUAVIARE"]

guaviare_casos_total = len(guaviare_df)

guaviare_casos_millon = int((guaviare_casos_total/119214)*1000000)

guaviare_fallecidos = len(guaviare_df[guaviare_df.recuperado == "Fallecido"])

guaviare_fallecidos_millon = int((guaviare_fallecidos/119214)*1000000)

guaviare_recuperados = len(guaviare_df[guaviare_df.recuperado == "Recuperado"])

guaviare_criticos = len(guaviare_df[guaviare_df.estado == "Grave"])

guaviare_na_values = len(guaviare_df[guaviare_df.recuperado == "N/A"])

guaviare_activos = guaviare_casos_total - (guaviare_recuperados + guaviare_fallecidos + guaviare_na_values)

###

##Huila


huila_df = results_df[results_df.departamento_nom == "HUILA"]

huila_casos_total = len(huila_df)

huila_casos_millon = int((huila_casos_total/1226488)*1000000)

huila_fallecidos = len(huila_df[huila_df.recuperado == "Fallecido"])

huila_fallecidos_millon = int((huila_fallecidos/1226488)*1000000)

huila_recuperados = len(huila_df[huila_df.recuperado == "Recuperado"])

huila_criticos = len(huila_df[huila_df.estado == "Grave"])

huila_na_values = len(huila_df[huila_df.recuperado == "N/A"])

huila_activos = huila_casos_total - (huila_recuperados + huila_fallecidos + huila_na_values)

###

###La Guajira


guajira_df = results_df[results_df.departamento_nom == "GUAJIRA"]

guajira_casos_total = len(guajira_df)

guajira_casos_millon = int((guajira_casos_total/1101626)*1000000)

guajira_fallecidos = len(guajira_df[guajira_df.recuperado == "Fallecido"])

guajira_fallecidos_millon = int((guajira_fallecidos/1101626)*1000000)

guajira_recuperados = len(guajira_df[guajira_df.recuperado == "Recuperado"])

guajira_criticos = len(guajira_df[guajira_df.estado == "Grave"])

guajira_na_values = len(guajira_df[guajira_df.recuperado == "N/A"])

guajira_activos = guajira_casos_total - (guajira_recuperados + guajira_fallecidos + guajira_na_values)

####################################

####Magdalena


magdalena_df = results_df[results_df.departamento_nom == "MAGDALENA"]

magdalena_casos_total = len(magdalena_df)

magdalena_casos_millon = int((magdalena_casos_total/1326341)*1000000)

magdalena_fallecidos = len(magdalena_df[magdalena_df.recuperado == "Fallecido"])

magdalena_fallecidos_millon = int((magdalena_fallecidos/1326341)*1000000)

magdalena_recuperados = len(magdalena_df[magdalena_df.recuperado == "Recuperado"])

magdalena_criticos = len(magdalena_df[magdalena_df.estado == "Grave"])

magdalena_na_values = len(magdalena_df[magdalena_df.recuperado == "N/A"])

magdalena_activos = magdalena_casos_total - (magdalena_recuperados + magdalena_fallecidos + magdalena_na_values)

#################

###Meta


meta_df = results_df[results_df.departamento_nom == "META"]

meta_casos_total = len(meta_df)

meta_casos_millon = int((meta_casos_total/1056066)*1000000)

meta_fallecidos = len(meta_df[meta_df.recuperado == "Fallecido"])

meta_fallecidos_millon = int((meta_fallecidos/1056066)*1000000)

meta_recuperados = len(meta_df[meta_df.recuperado == "Recuperado"])

meta_criticos = len(meta_df[meta_df.estado == "Grave"])

meta_na_values = len(meta_df[meta_df.recuperado == "N/A"])

meta_activos = meta_casos_total - (meta_recuperados + meta_fallecidos + meta_na_values)

#######################


###Nariño

nariño_df = results_df[results_df.departamento_nom == "NARIÑO"]

nariño_casos_total = len(nariño_df)

nariño_casos_millon = int((nariño_casos_total/1851658)*1000000)

nariño_fallecidos = len(nariño_df[nariño_df.recuperado == "Fallecido"])

nariño_fallecidos_millon = int((nariño_fallecidos/1851658)*1000000)

nariño_recuperados = len(nariño_df[nariño_df.recuperado == "Recuperado"])

nariño_criticos = len(nariño_df[nariño_df.estado == "Grave"])

nariño_na_values = len(nariño_df[nariño_df.recuperado == "N/A"])

nariño_activos = nariño_casos_total - (nariño_recuperados + nariño_fallecidos + nariño_na_values)

##########

###N. de santander

nsantander_df = results_df[results_df.departamento_nom == "NORTE SANTANDER"]

nsantander_casos_total = len(nsantander_df)

nsantander_casos_millon = int((nsantander_casos_total/1414032)*1000000)

nsantander_fallecidos = len(nsantander_df[nsantander_df.recuperado == "Fallecido"])

nsantander_fallecidos_millon = int((nsantander_fallecidos/1414032)*1000000)

nsantander_recuperados = len(nsantander_df[nsantander_df.recuperado == "Recuperado"])

nsantander_criticos = len(nsantander_df[nsantander_df.estado == "Grave"])

nsantander_na_values = len(nsantander_df[nsantander_df.recuperado == "N/A"])

nsantander_activos = nsantander_casos_total - (nsantander_recuperados + nsantander_fallecidos + nsantander_na_values)

############

###Putumayo

putumayo_df = results_df[results_df.departamento_nom == "PUTUMAYO"]

putumayo_casos_total = len(putumayo_df)

putumayo_casos_millon = int((putumayo_casos_total/369332)*1000000)

putumayo_fallecidos = len(putumayo_df[putumayo_df.recuperado == "Fallecido"])

putumayo_fallecidos_millon = int((putumayo_fallecidos/369332)*1000000)

putumayo_recuperados = len(putumayo_df[putumayo_df.recuperado == "Recuperado"])

putumayo_criticos = len(putumayo_df[putumayo_df.estado == "Grave"])

putumayo_na_values = len(putumayo_df[putumayo_df.recuperado == "N/A"])

putumayo_activos = putumayo_casos_total - (putumayo_recuperados + putumayo_fallecidos + putumayo_na_values)

#########


##Quindio


quindio_df = results_df[results_df.departamento_nom == "QUINDIO"]

quindio_casos_total = len(quindio_df)

quindio_casos_millon = int((quindio_casos_total/581534)*1000000)

quindio_fallecidos = len(quindio_df[quindio_df.recuperado == "Fallecido"])

quindio_fallecidos_millon = int((quindio_fallecidos/581.534)*1000000)

quindio_recuperados = len(quindio_df[quindio_df.recuperado == "Recuperado"])

quindio_criticos = len(quindio_df[quindio_df.estado == "Grave"])

quindio_na_values = len(quindio_df[quindio_df.recuperado == "N/A"])

quindio_activos = quindio_casos_total - (quindio_recuperados + quindio_fallecidos + quindio_na_values)


##############

###Risaralda

risaralda_df = results_df[results_df.departamento_nom == "RISARALDA"]

risaralda_casos_total = len(risaralda_df)

risaralda_casos_millon = int((risaralda_casos_total/978.182)*1000000)

risaralda_fallecidos = len(risaralda_df[risaralda_df.recuperado == "Fallecido"])

risaralda_fallecidos_millon = int((risaralda_fallecidos/978.182)*1000000)

risaralda_recuperados = len(risaralda_df[risaralda_df.recuperado == "Recuperado"])

risaralda_criticos = len(risaralda_df[risaralda_df.estado == "Grave"])

risaralda_na_values = len(risaralda_df[risaralda_df.recuperado == "N/A"])

risaralda_activos = risaralda_casos_total - (risaralda_recuperados + risaralda_fallecidos + risaralda_na_values)

##################


###San Andrés

sanandres_df = results_df[results_df.departamento_nom == "SAN ANDRES"]

sanandres_casos_total = len(sanandres_df)

sanandres_casos_millon = int((sanandres_casos_total/79693)*1000000)

sanandres_fallecidos = len(sanandres_df[sanandres_df.recuperado == "Fallecido"])

sanandres_fallecidos_millon = int((sanandres_fallecidos/79693)*1000000)

sanandres_recuperados = len(sanandres_df[sanandres_df.recuperado == "Recuperado"])

sanandres_criticos = len(sanandres_df[sanandres_df.estado == "Grave"])

sanandres_na_values = len(sanandres_df[sanandres_df.recuperado == "N/A"])

sanandres_activos = sanandres_casos_total - (sanandres_recuperados + sanandres_fallecidos + sanandres_na_values)

#########


###Santander

santander_df = results_df[results_df.departamento_nom == "SANTANDER"]

santander_casos_total = len(santander_df)

santander_casos_millon = int((santander_casos_total/2110608)*1000000)

santander_fallecidos = len(santander_df[santander_df.recuperado == "Fallecido"])

santander_fallecidos_millon = int((santander_fallecidos/2110608)*1000000)

santander_recuperados = len(santander_df[santander_df.recuperado == "Recuperado"])

santander_criticos = len(santander_df[santander_df.estado == "Grave"])

santander_na_values = len(santander_df[santander_df.recuperado == "N/A"])

santander_activos = santander_casos_total - (santander_recuperados + santander_fallecidos + santander_na_values)


#########


####Sucre


sucre_df = results_df[results_df.departamento_nom == "SUCRE"]

sucre_casos_total = len(sucre_df)

sucre_casos_millon = int((sucre_casos_total/894734)*1000000)

sucre_fallecidos = len(sucre_df[sucre_df.recuperado == "Fallecido"])

sucre_fallecidos_millon = int((sucre_fallecidos/894734)*1000000)

sucre_recuperados = len(sucre_df[sucre_df.recuperado == "Recuperado"])

sucre_criticos = len(sucre_df[sucre_df.estado == "Grave"])

sucre_na_values = len(sucre_df[sucre_df.recuperado == "N/A"])

sucre_activos = sucre_casos_total - (sucre_recuperados + sucre_fallecidos + sucre_na_values)

#########

####Tolima


tolima_df = results_df[results_df.departamento_nom == "TOLIMA"]

tolima_casos_total = len(tolima_df)

tolima_casos_millon = int((tolima_casos_total/1427423)*1000000)

tolima_fallecidos = len(tolima_df[tolima_df.recuperado == "Fallecido"])

tolima_fallecidos_millon = int((tolima_fallecidos/1427423)*1000000)

tolima_recuperados = len(tolima_df[tolima_df.recuperado == "Recuperado"])

tolima_criticos = len(tolima_df[tolima_df.estado == "Grave"])

tolima_na_values = len(tolima_df[tolima_df.recuperado == "N/A"])

tolima_activos = tolima_casos_total - (tolima_recuperados + tolima_fallecidos + tolima_na_values)


########


###Valle del cauca

vcauca_df = results_df[results_df.departamento_nom == "VALLE"]

vcauca_casos_total = len(vcauca_df)

vcauca_casos_millon = int((vcauca_casos_total/4852896)*1000000)

vcauca_fallecidos = len(vcauca_df[vcauca_df.recuperado == "Fallecido"])

vcauca_fallecidos_millon = int((vcauca_fallecidos/4852896)*1000000)

vcauca_recuperados = len(vcauca_df[vcauca_df.recuperado == "Recuperado"])

vcauca_criticos = len(vcauca_df[vcauca_df.estado == "Grave"])

vcauca_na_values = len(vcauca_df[vcauca_df.recuperado == "N/A"])

vcauca_activos = vcauca_casos_total - (vcauca_recuperados + vcauca_fallecidos + vcauca_na_values)


#############

###Vaupés


vaupes_df = results_df[results_df.departamento_nom == "VAUPES"]

vaupes_casos_total = len(vaupes_df)

vaupes_casos_millon = int((vaupes_casos_total/45822)*1000000)

vaupes_fallecidos = len(vaupes_df[vaupes_df.recuperado == "Fallecido"])

vaupes_fallecidos_millon = int((vaupes_fallecidos/45822)*1000000)

vaupes_recuperados = len(vaupes_df[vaupes_df.recuperado == "Recuperado"])

vaupes_criticos = len(vaupes_df[vaupes_df.estado == "Grave"])

vaupes_na_values = len(vaupes_df[vaupes_df.recuperado == "N/A"])

vaupes_activos = vaupes_casos_total - (vaupes_recuperados + vaupes_fallecidos + vaupes_na_values)

############

###Vichada


vichada_df = results_df[results_df.departamento_nom == "VICHADA"]

vichada_casos_total = len(vichada_df)

vichada_casos_millon = int((vichada_casos_total/2891713)*1000000)

vichada_fallecidos = len(vichada_df[vichada_df.recuperado == "Fallecido"])

vichada_fallecidos_millon = int((vichada_fallecidos/2891713)*1000000)

vichada_recuperados = len(vichada_df[vichada_df.recuperado == "Recuperado"])

vichada_criticos = len(vichada_df[vichada_df.estado == "Grave"])

vichada_na_values = len(vichada_df[vichada_df.recuperado == "N/A"])

vichada_activos = vichada_casos_total - (vichada_recuperados + vichada_fallecidos + vichada_na_values)

departamentos = ['TOTAL','AMAZONAS','ANTIOQUIA','ARAUCA','ATLANTICO','BARRANQUILLA','BOLIVAR','BOYACA','CALDAS','CAQUETA','CASANARE','CAUCA','CESAR','CHOCO','CORDOBA','CUNDINAMARCA','GUAINÍA','GUAVIARE','HUILA','LA GUAJIRA','MAGDALENA','META','NARIÑO','NORTE DE SANTANNDER','PUTUMAYO','QUINDÍO','RISARALDA','SAN ANDRÉS Y PROVIDENCIA','SANTANDER','SUCRE','TOLIMA','VALLE DEL CAUCA','VAUPÉS','VICHADA']
departamentos_length = [casos_confirmados_total,amazonas_casos_total,antioquia_casos_total, arauca_casos_total, atlantico_casos_total,barranquilla_casos_total,bolivar_casos_total,boyaca_casos_total,caldas_casos_total,caqueta_casos_total,casanare_casos_total,cauca_casos_total,cesar_casos_total,choco_casos_total,cordoba_casos_total,cundinamarca_casos_total,guainia_casos_total, guaviare_casos_total,huila_casos_total,guajira_casos_total,magdalena_casos_total,meta_casos_total,nariño_casos_total,nsantander_casos_total,putumayo_casos_total,quindio_casos_total,risaralda_casos_total,sanandres_casos_total,santander_casos_total,sucre_casos_total,tolima_casos_total,vcauca_casos_total,vaupes_casos_total,vichada_casos_total]
departamentos_fallecidos = [Total_fallecidos,amazonas_fallecidos,antioquia_fallecidos,arauca_fallecidos,atlantico_fallecidos,barranquilla_fallecidos,bolivar_fallecidos,boyaca_fallecidos,caldas_fallecidos,caqueta_fallecidos,casanare_fallecidos,cauca_fallecidos,cesar_fallecidos,choco_fallecidos,cordoba_fallecidos,cundinamarca_fallecidos,guainia_fallecidos,guaviare_fallecidos,huila_fallecidos,guajira_fallecidos,magdalena_fallecidos,meta_fallecidos,nariño_fallecidos,nsantander_fallecidos,putumayo_fallecidos,quindio_fallecidos,risaralda_fallecidos,sanandres_fallecidos,santander_fallecidos,sucre_fallecidos,tolima_fallecidos,vcauca_fallecidos,vaupes_fallecidos,vichada_fallecidos]
departamentos_y_length = list(zip(departamentos,departamentos_length))
departamentos_y_fallecidos = list(zip(departamentos,departamentos_fallecidos))

yesterday = (datetime.date.today() - datetime.timedelta(days=1))

def listado_de_lengths(departamento,dataframelength):  
    with open('listado.txt' ,"a") as f:
        if departamento == 'VICHADA':
            f.write( f"{departamento.lower()},{datetime.date.today()},{dataframelength}\n\n\n")
        else:
            f.write( f"{departamento.lower()},{datetime.date.today()},{dataframelength}\n")

#### escribir el total de casos de cada dept en listado.txt
for x in departamentos_y_length:
    listado_de_lengths(x[0],x[1]) 

read_text = open('listado.txt', 'r')
read_line = read_text.readlines()

#### se lee listado.txt y se busca la cifra del dpto del dia anterior, luego lo append en lista_cambios y por ultimo asigno la cifra obtenida con la variable correspondiente
lista_cambios = []
def diferencia(dept,dept_casos):
  for i in read_line:
    if dept.lower() in i and str(yesterday) in i:
      l1 = i.split(',')
      cambios_total = dept_casos - int(l1[2])
      lista_cambios.append(cambios_total)
      break
         



def listado_de_fallecidos(departamento,casos_fallecidos):
    with open('fallecidos.txt', 'a') as f:
        if departamento == 'VICHADA':
            f.write( f"{departamento.lower()},{datetime.date.today()},{casos_fallecidos}\n\n\n")
        else:
            f.write( f"{departamento.lower()},{datetime.date.today()},{casos_fallecidos}\n")

#### escribir el total de casos de fallecidos de cada dept en fallecidos.txt

for x in departamentos_y_fallecidos:
    listado_de_fallecidos(x[0],x[1]) 

read_text_fallecidos = open('fallecidos.txt', 'r')
read_line_fallecidos = read_text_fallecidos.readlines()

lista_cambios_fallecidos = []
def diferencia_fallecidos(dept,dept_fallecidos):
    for i in read_line_fallecidos:
        if dept.lower() in i and str(yesterday) in i:
            l2 = i.split(',')
            cambios_total_fallecidos = dept_fallecidos - int(l2[2])
            lista_cambios_fallecidos.append(cambios_total_fallecidos)
            break

for x in departamentos_y_fallecidos:
    diferencia_fallecidos(x[0],x[1])

cambios_fallecidos_total = lista_cambios_fallecidos[0]
amazonas_cambios_fallecidos = lista_cambios_fallecidos[1]
antioquia_cambios_fallecidos = lista_cambios_fallecidos[2]
arauca_cambios_fallecidos = lista_cambios_fallecidos[3]
atlantico_cambios_fallecidos = lista_cambios_fallecidos[4]
barranquilla_cambios_fallecidos = lista_cambios_fallecidos[5]
bolivar_cambios_fallecidos = lista_cambios_fallecidos[6]
boyaca_cambios_fallecidos = lista_cambios_fallecidos[7]
caldas_cambios_fallecidos = lista_cambios_fallecidos[8]
caqueta_cambios_fallecidos = lista_cambios_fallecidos[9]
casanare_cambios_fallecidos = lista_cambios_fallecidos[10]
cauca_cambios_fallecidos = lista_cambios_fallecidos[11]
cesar_cambios_fallecidos = lista_cambios_fallecidos[12]
choco_cambios_fallecidos = lista_cambios_fallecidos[13]
cordoba_cambios_fallecidos = lista_cambios_fallecidos[14]
cundinamarca_cambios_fallecidos = lista_cambios_fallecidos[15]
guainia_cambios_fallecidos = lista_cambios_fallecidos[16]
guaviare_cambios_fallecidos = lista_cambios_fallecidos[17]
huila_cambios_fallecidos = lista_cambios_fallecidos[18]
guajira_cambios_fallecidos = lista_cambios_fallecidos[19]
magdalena_cambios_fallecidos = lista_cambios_fallecidos[20]
meta_cambios_fallecidos = lista_cambios_fallecidos[21]
nariño_cambios_fallecidos = lista_cambios_fallecidos[22]
nsantander_cambios_fallecidos = lista_cambios_fallecidos[23]
putumayo_cambios_fallecidos = lista_cambios_fallecidos[24]
quindio_cambios_fallecidos = lista_cambios_fallecidos[25]
risaralda_cambios_fallecidos = lista_cambios_fallecidos[26]
sanandres_cambios_fallecidos = lista_cambios_fallecidos[27]
santander_cambios_fallecidos = lista_cambios_fallecidos[28]
sucre_cambios_fallecidos = lista_cambios_fallecidos[29]
tolima_cambios_fallecidos = lista_cambios_fallecidos[30]
vcauca_cambios_fallecidos = lista_cambios_fallecidos[31]
vaupes_cambios_fallecidos = lista_cambios_fallecidos[32]
vichada_cambios_fallecidos = lista_cambios_fallecidos[33]


for x in departamentos_y_length:
    diferencia(x[0],x[1])

cambios_hoy_total = lista_cambios[0]
amazonas_cambios_hoy = lista_cambios[1]
antioquia_cambios_hoy = lista_cambios[2]
arauca_cambios_hoy = lista_cambios[3]
atlantico_cambios_hoy = lista_cambios[4]
barranquilla_cambios_hoy = lista_cambios[5]
bolivar_cambios_hoy = lista_cambios[6]
boyaca_cambios_hoy = lista_cambios[7]
caldas_cambios_hoy = lista_cambios[8]
caqueta_cambios_hoy = lista_cambios[9]
casanare_cambios_hoy = lista_cambios[10]
cauca_cambios_hoy = lista_cambios[11]
cesar_cambios_hoy = lista_cambios[12]
choco_cambios_hoy = lista_cambios[13]
cordoba_cambios_hoy = lista_cambios[14]
cundinamarca_cambios_hoy = lista_cambios[15]
guainia_cambios_hoy = lista_cambios[16]
guaviare_cambios_hoy = lista_cambios[17]
huila_cambios_hoy = lista_cambios[18]
guajira_cambios_hoy = lista_cambios[19]
magdalena_cambios_hoy = lista_cambios[20]
meta_cambios_hoy = lista_cambios[21]
nariño_cambios_hoy = lista_cambios[22]
nsantander_cambios_hoy = lista_cambios[23]
putumayo_cambios_hoy = lista_cambios[24]
quindio_cambios_hoy = lista_cambios[25]
risaralda_cambios_hoy = lista_cambios[26]
sanandres_cambios_hoy = lista_cambios[27]
santander_cambios_hoy = lista_cambios[28]
sucre_cambios_hoy = lista_cambios[29]
tolima_cambios_hoy = lista_cambios[30]
vcauca_cambios_hoy = lista_cambios[31]
vaupes_cambios_hoy = lista_cambios[32]
vichada_cambios_hoy = lista_cambios[33]