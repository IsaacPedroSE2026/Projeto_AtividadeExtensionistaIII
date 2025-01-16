

##########################################################################################
#                                                                                        #
#                                                                                        #
#  ESTE CÓDIGO ESTÁ COM MELHORIAS  (criar um único mapa com camadas para cada ano )      #
#                                                                                        #
#  Melhor resultado!!      #
#                                                                                        #
##########################################################################################

# import pandas as pd
# import folium
# from folium.plugins import MarkerCluster

# # Carregar o arquivo Excel
# df = pd.read_excel('IndicadoresAguasPluviais_noite24102024.xlsx')

# # Definir as coordenadas da região metropolitana do Recife para centralizar o mapa
# recife_coords = [-8.0475, -34.8770]

# # Criar o mapa centralizado na região metropolitana do Recife
# mapa = folium.Map(location=recife_coords, zoom_start=11)

# # Criar uma camada para cada ano e adicionar ao controle de camadas
# anos = range(2017, 2023)
# for ano in anos:
#     # Filtrar os dados para o ano específico
#     data_ano = df[df['Ano'] == ano]
    
#     # Criar uma camada de grupo para o ano
#     camada_ano = folium.FeatureGroup(name=f"Ano {ano}")
#     marker_cluster = MarkerCluster().add_to(camada_ano)
    
#     # Adicionar marcadores ao cluster
#     for idx, row in data_ano.iterrows():
#         folium.Marker(
#             location=[row['Latitude'], row['Longitude']],
#             popup=(
#                 f"<b>Ano:</b> {row['Ano']}<br>"
#                 f"<b>Risco de Inundação:</b> {row['Risco de Inundação']}"
#             ),
#         ).add_to(marker_cluster)
    
#     # Adicionar a camada do ano ao mapa
#     camada_ano.add_to(mapa)

# # Adicionar o controle de camadas ao mapa
# folium.LayerControl(collapsed=False).add_to(mapa)

# # Salvar o mapa em um arquivo HTML
# mapa.save('mapa_interativo_todos_os_anos.html')
# print("Mapa interativo com todos os anos salvo em 'mapa_interativo_todos_os_anos.html'")





##########################################################################################
#                                                                                        #
#                                                                                        #
#           ESTE CÓDIGO FUNCIONOU!!!!!!                                                  #
#                                                                                        #
#                                                                                        #
##########################################################################################

# import pandas as pd
# import folium
# from folium.plugins import MarkerCluster, Fullscreen

# # Ler o DataFrame do Excel
# df = pd.read_excel('IndicadoresAguasPluviais_noite24102024.xlsx')

# # Filtrar para os anos de interesse e região metropolitana do Recife
# df = df[(df['Ano'] >= 2017) & (df['Ano'] <= 2022) &
#         (df['Latitude'] >= -8.2) & (df['Latitude'] <= -7.8) &
#         (df['Longitude'] >= -35) & (df['Longitude'] <= -34.5)]

# # Criar o mapa centralizado na Região Metropolitana do Recife
# m = folium.Map(location=[-8.05, -34.87], zoom_start=12)
# Fullscreen().add_to(m)  # Adicionar o plugin Fullscreen

# # Criar um MarkerCluster para agrupar os marcadores
# marker_cluster = MarkerCluster().add_to(m)

# # Adicionar os marcadores ao MarkerCluster
# for index, row in df.iterrows():
#     folium.Marker(
#         location=[row['Latitude'], row['Longitude']],
#         icon=folium.Icon(color='red', icon='info-sign'),  # Icone personalizado
#         popup=f"""
#             <b>Ano:</b> {row['Ano']}<br>
#             <b>Risco de Inundação:</b> {row['Risco de Inundação']}<br>
#         """
#     ).add_to(marker_cluster)

# # Adicionar um controle deslizante para filtrar por ano
# folium.LayerControl().add_to(m)

# m.save('mapa_recife_interativo.html')



##########################################################################################
#                                                                                        #
#                                                                                        #
#           ESTE CÓDIGO ESTÁ COM MELHORIAS  (salva vários mapas por ano )                #
#                                                                                        #
#                                                                                        #
##########################################################################################


import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Carregar o arquivo Excel
df = pd.read_excel('IndicadoresAguasPluviais_noite24102024.xlsx')

# Função para criar o mapa interativo para um ano específico
def criar_mapa_por_ano(data, ano, save_path):
    # Filtrar os dados para o ano específico
    data_ano = data[data['Ano'] == ano]
    
    # Definir as coordenadas de centralização na região metropolitana do Recife
    recife_coords = [-8.0475, -34.8770]
    
    # Criar o mapa centralizado na região metropolitana do Recife
    mapa = folium.Map(
        location=recife_coords,
        zoom_start=11  # Zoom ajustado para visualizar a região metropolitana
    )
    
    # Cluster de marcadores para agrupar os pontos
    marker_cluster = MarkerCluster().add_to(mapa)
    
    # Adicionar cada ponto ao mapa com o popup de informações
    for idx, row in data_ano.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=(
                f"<b>Ano:</b> {row['Ano']}<br>"
                f"<b>Risco de Inundação:</b> {row['Risco de Inundação']}"
            ),
        ).add_to(marker_cluster)
    
    # Salvar o mapa em um arquivo HTML
    mapa.save(save_path)

# Criar e salvar mapas para os anos de 2017 a 2022
anos = range(2017, 2023)
for ano in anos:
    save_path = f'mapa_interativo_{ano}.html'
    criar_mapa_por_ano(df, ano, save_path)
    print(f"Mapa para o ano {ano} salvo em {save_path}")




#    CÓDIGO ABAIxO É UM CÓDIGO RESERVA!!!!

# Criando o ambiente virtual: python -m venv Risco_Alaga

# import pandas as pd
# import folium
# import branca.colormap as cm

# # Ler o DataFrame do Excel
# df = pd.read_excel('IndicadoresAguasPluviais_noite24102024.xlsx')

# # Filtrar para os anos de interesse e região metropolitana do Recife (ajuste os limites conforme necessário)
# df = df[(df['Ano'] >= 2017) & (df['Ano'] <= 2022) &
#         (df['Latitude'] >= -8.2) & (df['Latitude'] <= -7.8) & 
#         (df['Longitude'] >= -35) & (df['Longitude'] <= -34.5)]

# # Criar uma função para criar o mapa para um determinado ano
# def create_map(year):
#     # Filtrar o DataFrame para o ano especificado
#     df_year = df[df['Ano'] == year]

#     # Criar o mapa centralizado na Região Metropolitana do Recife
#     m = folium.Map(location=[-8.05, -34.87], zoom_start=12)

#     # Criar uma paleta de cores para o risco de inundação
#     colormap = cm.linear.YlOrRd_09.scale(df_year['Risco de Inundação'].min(), df_year['Risco de Inundação'].max())

#     # Adicionar marcadores ao mapa com mais detalhes no popup
#     for index, row in df_year.iterrows():
#         folium.CircleMarker(
#             location=[row['Latitude'], row['Longitude']],
#             radius=8,
#             popup=f"""
#                 <b>Ano:</b> {row['Ano']}<br>
#                 <b>Risco de Inundação:</b> {row['Risco de Inundação']}<br>
#             """,
#             fill_color=colormap(row['Risco de Inundação']),
#             color='black',
#             fill_opacity=0.7
#         ).add_to(m)

#     return m

# # Criar um mapa para cada ano de 2017 a 2022
# for year in range(2017, 2023):
#     map = create_map(year)
#     map.save(f'mapa_recife_{year}.html')









