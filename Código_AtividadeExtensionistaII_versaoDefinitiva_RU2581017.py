##########################################################################################
#                                                                                        #
#         ATIVIDADE EXTENSIONISTA II                                                     #
#         RISCO DE INUNDAÇÃO EM ÁREAS URBANAS NA REGIÃO METROPOLITANA DO RECIFE – PE     #
#         ISAAC PEDRO DA SILVA - RU 2581017                                              #
#                                                                                        #
##########################################################################################

# Caregamento das bibliotecas e módulos
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Carregamento o arquivo Excel
# df = pd.read_excel('IndicadoresAguasPluviais_noite24102024.xlsx')

# Definição de função para criar um mapa interativo para um ano específico
# def criar_mapa_por_ano(data, ano, save_path):
#     # Cria um filtro para os dados de um ano específico
#     data_ano = data[data['Ano'] == ano]
    
#     # É preciso definir as coordenadas de centralização na região metropolitana do Recife
#     recife_coords = [-8.0475, -34.8770]
    
#     # Criação do mapa centralizado e já com um zoom ajustado na RMR
#     mapa = folium.Map(
#         location=recife_coords,
#         zoom_start=11 
#     )
    
#     # Criação de um cluster de marcadores para agrupar os pontos
#     marker_cluster = MarkerCluster().add_to(mapa)
    
#     # Adiciona cada ponto ao mapa com o popup de informações
#     for idx, row in data_ano.iterrows():
#         folium.Marker(
#             location=[row['Latitude'], row['Longitude']],
#             popup=(
#                 f"<b>Ano:</b> {row['Ano']}<br>"
#                 f"<b>Risco de Inundação:</b> {row['Risco de Inundação']}"
#             ),
#         ).add_to(marker_cluster)
    
#     # Salva o mapa em um arquivo HTML
#     mapa.save(save_path)

# # Cria e salva os mapas para os anos de 2017 a 2022
# anos = range(2017, 2023)
# for ano in anos:
#     save_path = f'mapa_interativo_{ano}.html'
#     criar_mapa_por_ano(df, ano, save_path)
#     print(f"Mapa para o ano {ano} salvo em {save_path}")
    
    
    
    
##########################################################################################
#                                                                                        #
#         ATIVIDADE EXTENSIONISTA II                                                     #
#         RISCO DE INUNDAÇÃO EM ÁREAS URBANAS NA REGIÃO METROPOLITANA DO RECIFE – PE     #
#         ISAAC PEDRO DA SILVA - RU 2581017                                              #
#                                                                                        #
#         (Na versão abaixo, foi adicionado um controle para selecionar os anos)         #
#         (QUE SERÁ A EVOLUÇÃO DA PRIMEIRA VERSÃO, SOLICITADA PELOS USUÁRIOS)            #
#                                                                                        #
##########################################################################################

import folium
from folium.plugins import MarkerCluster

df = pd.read_excel('IndicadoresAguasPluviais_noite24102024.xlsx')

recife_coords = [-8.0475, -34.8770]

mapa = folium.Map(location=recife_coords, zoom_start=11)

#Criar uma camada para cada ano e adicionar ao controle de camadas
anos = range(2017, 2023)
for ano in anos:
    data_ano = df[df['Ano'] == ano]
    camada_ano = folium.FeatureGroup(name=f"Ano {ano}")
    marker_cluster = MarkerCluster().add_to(camada_ano)
    for idx, row in data_ano.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=(
                f"<b>Ano:</b> {row['Ano']}<br>"
                f"<b>Risco de Inundação:</b> {row['Risco de Inundação']}"
            ),
        ).add_to(marker_cluster)
    
    # Adicionar a camada do ano ao mapa
    camada_ano.add_to(mapa)

#Adicionar o controle de camadas ao mapa
folium.LayerControl(collapsed=False).add_to(mapa)

mapa.save('mapa_interativo_todos_os_anos.html')
print("Mapa interativo com todos os anos salvo em 'mapa_interativo_todos_os_anos.html'")