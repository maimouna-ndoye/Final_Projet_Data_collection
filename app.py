import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
st.markdown("<h1 style='text-align: center; color: black;'>Projet 3 </h1>", unsafe_allow_html=True)
st.markdown("this app is for my final projet in data collection")
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def load(dataframe, title, key, key1) :
    # Créer 3 colonnes avec celle du milieu plus large
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button(title, key1):
            st.subheader('Display data dimension')
            st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
            st.dataframe(dataframe)

            csv = convert_df(dataframe)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Data.csv',
                mime='text/csv',
                key = key)
            
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def load_vetements_hommes(mul_page):
    df=pd.DataFrame()
    #loop over pages indexes
    for index in range(1,(mul_page)+1):
        url1 = f'https://sn.coinafrique.com/categorie/vetements-homme?page={index}'
        # get the html code of the page using the get function requests
        res = get(url1)
        # store the html code in a beautifulsoup objet with a html parser (a parser allows to easily navigate through the html code)
        soup1 = bs(res.content, 'html.parser')
        containers1=soup1.find_all('div','col s6 m4 l3')
        # scrape for all data
        data=[]
        for container1 in containers1:
            try:
                type_clothes=container1.find('p','ad__card-description').a.text
                #print(type_clothes)
                #scrape price
                price=container1.find('p','ad__card-price').a.text.replace('CFA', '')
                #print(price)
                adress=container1.find('p','ad__card-location').span.text
                img_link=container1.find('img','ad__card-img')['src']


                dic={
                    'type_clothes':type_clothes,
                    'price':price,
                    'adress':adress,
                    'img_link':img_link
                }
                data.append(dic)
            except:
                pass
            DF=pd.DataFrame(data)
            df = pd.concat([df, DF], axis = 0).reset_index(drop = True)
            # Clean data
            df_clean = df.drop_duplicates()
            df_clean = df_clean[df_clean['price'] != 'Prix sur demande']
            df_clean['price'] = df_clean['price'].str.replace('CFA', '')
            df_clean['price'] = df_clean['price'].str.replace(' ', '')
            df_clean['price'] = pd.to_numeric(df_clean['price'])
            df_clean.to_csv("vetements_hommes_clean.csv", index = False)
    return df


def load_chaussures_hommes(mul_page):
    df=pd.DataFrame()
    #loop over pages indexes
    for index in range(1,(mul_page)+1):
        url2 = f'https://sn.coinafrique.com/categorie/chaussures-homme?page={index}'
        # get the html code of the page using the get function requests
        res = get(url2)
        # store the html code in a beautifulsoup objet with a html parser (a parser allows to easily navigate through the html code)
        soup2 = bs(res.content, 'html.parser')
        containers2=soup2.find_all('div','col s6 m4 l3')
        # scrape for all data
        data=[]
        for container2 in containers2:
            try:
                type_clothes=container2.find('p','ad__card-description').a.text
                #print(type_clothes)
                #scrape price
                price=container2.find('p','ad__card-price').a.text
                #print(price)
                adress=container2.find('p','ad__card-location').span.text
                img_link=container2.find('img','ad__card-img')['src']
                dic={
                    'type_clothes':type_clothes,
                    'price':price,
                    'adress':adress,
                    'img_link':img_link
                }
                data.append(dic)
            except:
                pass
            DF=pd.DataFrame(data)
            df = pd.concat([df, DF], axis = 0).reset_index(drop = True)
             # Clean data
            df_clean = df.drop_duplicates()
            df_clean = df_clean[df_clean['price'] != 'Prix sur demande']
            df_clean['price'] = df_clean['price'].str.replace('CFA', '')
            df_clean['price'] = df_clean['price'].str.replace(' ', '')
            df_clean['price'] = pd.to_numeric(df_clean['price'])
            df_clean.to_csv("chaussures_hommes_clean.csv", index = False)
    return df

def load_vetements_enfants(mul_page):
    df=pd.DataFrame()
    #loop over pages indexes
    for index in range(1,(mul_page)+1):
        url3 = f'https://sn.coinafrique.com/categorie/vetements-enfants?page={index}'
        # get the html code of the page using the get function requests
        res = get(url3)
        # store the html code in a beautifulsoup objet with a html parser (a parser allows to easily navigate through the html code)
        soup3 = bs(res.content, 'html.parser')
        containers3=soup3.find_all('div','col s6 m4 l3')
        # scrape for all data
        data=[]
        for container3 in containers3:
            try:
                type_clothes=container3.find('p','ad__card-description').a.text
                #print(type_clothes)
                #scrape price
                price=container3.find('p','ad__card-price').a.text
                #print(price)
                adress=container3.find('p','ad__card-location').span.text
                img_link=container3.find('img','ad__card-img')['src']
                dic={
                    'type_clothes':type_clothes,
                    'price':price,
                    'adress':adress,
                    'img_link':img_link
                }
                data.append(dic)
            except:
                pass
            DF=pd.DataFrame(data)
            df = pd.concat([df, DF], axis = 0).reset_index(drop = True)
             # Clean data
            df_clean = df.drop_duplicates()
            df_clean = df_clean[df_clean['price'] != 'Prix sur demande']
            df_clean['price'] = df_clean['price'].str.replace('CFA', '')
            df_clean['price'] = df_clean['price'].str.replace(' ', '')
            df_clean['price'] = pd.to_numeric(df_clean['price'])
            df_clean.to_csv("vetements_enfants_clean.csv", index = False)
    return df


def load_chaussures_enfants(mul_page):
    df=pd.DataFrame()
    #loop over pages indexes
    for index in range(1,(mul_page)+1):
        url4 = f'https://sn.coinafrique.com/categorie/chaussures-enfants?page={index}'
        # get the html code of the page using the get function requests
        res = get(url4)
        # store the html code in a beautifulsoup objet with a html parser (a parser allows to easily navigate through the html code)
        soup4 = bs(res.content, 'html.parser')
        containers4=soup4.find_all('div','col s6 m4 l3')
        # scrape for all data
        data=[]
        for container4 in containers4:
            try:
                type_clothes=container4.find('p','ad__card-description').a.text
                #print(type_clothes)
                #scrape price
                price=container4.find('p','ad__card-price').a.text
                #print(price)
                adress=container4.find('p','ad__card-location').span.text
                img_link=container4.find('img','ad__card-img')['src']
                dic={
                    'type_clothes':type_clothes,
                    'price':price,
                    'adress':adress,
                    'img_link':img_link
                }
                data.append(dic)
            except:
                pass
        DF=pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0).reset_index(drop = True)
        # Clean data
        df_clean = df.drop_duplicates()
        df_clean = df_clean[df_clean['price'] != 'Prix sur demande']
        df_clean['price'] = df_clean['price'].str.replace('CFA', '')
        df_clean['price'] = df_clean['price'].str.replace(' ', '')
        df_clean['price'] = pd.to_numeric(df_clean['price'])
        df_clean.to_csv("chaussures_enfants_clean.csv", index = False)
    return df


st.sidebar.header('User Input Features')
Pages = st.sidebar.selectbox('Pages indexes', list([int(p) for p in np.arange(2, 600)]))
Choices = st.sidebar.selectbox('Options', ['Scrape data using beautifulSoup', 'Download scraped data', 'Dashbord of the data', 'Evaluate the App'])

# Background function
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('/home/students-aimssn/Documents/Data_collection/exampleApp/image_back.jpeg') 

local_css('style.css')  

if Choices=='Scrape data using beautifulSoup':

    
    vetements_hommes_mul_pag=load_vetements_hommes(Pages)
    chaussures_hommes_mul_pag=load_chaussures_hommes(Pages)
    vetements_enfants_mul_pag=load_vetements_enfants(Pages)
    chaussures_enfants_mul_pag=load_chaussures_enfants(Pages)

    

    load(vetements_hommes_mul_pag,'vetements_hommes','1','101')
    load(chaussures_hommes_mul_pag,'chaussures_hommes','2','102')
    load(vetements_enfants_mul_pag,'vetements_enfants','3','103')
    load(chaussures_enfants_mul_pag,'chaussures_enfants','4','104')


    


elif Choices == 'Download scraped data':
    vetements_hommes=pd.read_csv('data/url1_wc.csv') 
    chaussures_hommes=pd.read_csv('data/url2_wc.csv')
    vetements_enfants=pd.read_csv('data/url3_wc.csv')
    chaussures_enfants=pd.read_csv('data/url4_wc.csv')


    load(vetements_hommes,'vetements_hommes_data','5','105')
    load(chaussures_hommes,'chaussures_hommes_data','6','106')
    load(vetements_enfants,'vetements_enfants_data','7','107')
    load(chaussures_enfants,'chaussures_enfants_data','8','108')

elif Choices == 'Dashbord of the data':
    data1 = pd.read_csv('vetements_hommes_clean.csv')
    data2 = pd.read_csv('chaussures_hommes_clean.csv')
    data3 = pd.read_csv('vetements_enfants_clean.csv')
    data4 = pd.read_csv('chaussures_enfants_clean.csv')
   
    st.subheader("📊 Dashboard — Analysis of the 4 categories")
    
    # Métriques globales en haut
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.metric("👔 Men's Clothing", f"{len(data1):,}", f"{data1['price'].mean():,.0f} CFA avg")
    with col_m2:
        st.metric("👞 Men's Shoes", f"{len(data2):,}", f"{data2['price'].mean():,.0f} CFA avg")
    with col_m3:
        st.metric("👶 Children's Clothing", f"{len(data3):,}", f"{data3['price'].mean():,.0f} CFA avg")
    with col_m4:
        st.metric("👟 Children's Shoes", f"{len(data4):,}", f"{data4['price'].mean():,.0f} CFA avg")
    
    st.markdown("---")

    st.markdown("### 🏆 Top 5 most common articles")

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        top5_vh = data1['type_clothes'].value_counts()[:5]
        colors1 = sns.color_palette("Blues_r", len(top5_vh))
        bars1 = ax1.barh(range(len(top5_vh)), top5_vh.values, color=colors1, edgecolor='black', linewidth=1.5)
        ax1.set_yticks(range(len(top5_vh)))
        ax1.set_yticklabels(top5_vh.index, fontsize=11)
        ax1.set_xlabel("Number", fontsize=12, fontweight='bold')
        ax1.set_title("🔵 Top 5 men's clothing items", fontsize=14, fontweight='bold', pad=15)
        ax1.grid(axis='x', alpha=0.3, linestyle='--')
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        
        # Ajouter les valeurs sur les barres
        for i, bar in enumerate(bars1):
            width = bar.get_width()
            ax1.text(width + 1, bar.get_y() + bar.get_height()/2, 
                    f'{int(width)}', ha='left', va='center', fontweight='bold', fontsize=10)
        
        plt.tight_layout()
        st.pyplot(fig1)
        plt.close()

    with col2:
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        top5_ch = data2['type_clothes'].value_counts()[:5]
        colors2 = sns.color_palette("Greens_r", len(top5_ch))
        bars2 = ax2.barh(range(len(top5_ch)), top5_ch.values, color=colors2, edgecolor='black', linewidth=1.5)
        ax2.set_yticks(range(len(top5_ch)))
        ax2.set_yticklabels(top5_ch.index, fontsize=11)
        ax2.set_xlabel("Number", fontsize=12, fontweight='bold')
        ax2.set_title("🟢 Top 5 men's shoes", fontsize=14, fontweight='bold', pad=15)
        ax2.grid(axis='x', alpha=0.3, linestyle='--')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        
        for i, bar in enumerate(bars2):
            width = bar.get_width()
            ax2.text(width + 1, bar.get_y() + bar.get_height()/2, 
                    f'{int(width)}', ha='left', va='center', fontweight='bold', fontsize=10)
        
        plt.tight_layout()
        st.pyplot(fig2)
        plt.close()

    st.markdown("---")

    st.markdown("### 💰 Average price per item type")

    col3, col4 = st.columns(2)

    with col3:
        fig3, ax3 = plt.subplots(figsize=(12, 6))
        avg_price_vh = data1.groupby('type_clothes')['price'].mean().sort_values(ascending=False)[:10]
        colors3 = sns.color_palette("viridis", len(avg_price_vh))
        bars3 = ax3.bar(range(len(avg_price_vh)), avg_price_vh.values, color=colors3, 
                       edgecolor='black', linewidth=1.5, alpha=0.8)
        ax3.set_xticks(range(len(avg_price_vh)))
        ax3.set_xticklabels(avg_price_vh.index, rotation=45, ha='right', fontsize=10)
        ax3.set_ylabel('Average Price (CFA)', fontsize=12, fontweight='bold')
        ax3.set_title("🔵 Average price — Men's clothing (Top 10)", fontsize=14, fontweight='bold', pad=15)
        ax3.grid(axis='y', alpha=0.3, linestyle='--')
        ax3.spines['top'].set_visible(False)
        ax3.spines['right'].set_visible(False)
        
        # Ajouter les valeurs sur les barres
        for bar in bars3:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height + 500,
                    f'{int(height):,}', ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        plt.tight_layout()
        st.pyplot(fig3)
        plt.close()

    with col4:
        fig4, ax4 = plt.subplots(figsize=(12, 6))
        avg_price_ch = data2.groupby('type_clothes')['price'].mean().sort_values(ascending=False)[:10]
        colors4 = sns.color_palette("plasma", len(avg_price_ch))
        bars4 = ax4.bar(range(len(avg_price_ch)), avg_price_ch.values, color=colors4, 
                       edgecolor='black', linewidth=1.5, alpha=0.8)
        ax4.set_xticks(range(len(avg_price_ch)))
        ax4.set_xticklabels(avg_price_ch.index, rotation=45, ha='right', fontsize=10)
        ax4.set_ylabel('Average Price (CFA)', fontsize=12, fontweight='bold')
        ax4.set_title("🟢 Average price — Men's shoes (Top 10)", fontsize=14, fontweight='bold', pad=15)
        ax4.grid(axis='y', alpha=0.3, linestyle='--')
        ax4.spines['top'].set_visible(False)
        ax4.spines['right'].set_visible(False)
        
        for bar in bars4:
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height + 500,
                    f'{int(height):,}', ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        plt.tight_layout()
        st.pyplot(fig4)
        plt.close()

    st.markdown("---")

    st.markdown("### 📈 Price Distribution")

    col5, col6 = st.columns(2)

    with col5:
        fig5, ax5 = plt.subplots(figsize=(10, 6))
        # Histogramme avec KDE
        n, bins, patches = ax5.hist(data1["price"], bins=40, color='#667eea', alpha=0.7, 
                                     edgecolor='black', linewidth=1.2)
        
        # Colorer les barres en dégradé
        cm = plt.cm.Blues
        for i, patch in enumerate(patches):
            patch.set_facecolor(cm(i / len(patches)))
        
        # Ajouter les lignes de statistiques
        mean_val = data1["price"].mean()
        median_val = data1["price"].median()
        ax5.axvline(mean_val, color='red', linestyle='--', linewidth=2.5, 
                   label=f'Mean: {mean_val:,.0f} CFA')
        ax5.axvline(median_val, color='green', linestyle='--', linewidth=2.5, 
                   label=f'Median: {median_val:,.0f} CFA')
        
        ax5.set_xlabel('Price (CFA)', fontsize=12, fontweight='bold')
        ax5.set_ylabel('Frequency', fontsize=12, fontweight='bold')
        ax5.set_title("🔵 Price Distribution — Men's Clothing", fontsize=14, fontweight='bold', pad=15)
        ax5.legend(fontsize=11, frameon=True, shadow=True)
        ax5.grid(axis='y', alpha=0.3, linestyle='--')
        ax5.spines['top'].set_visible(False)
        ax5.spines['right'].set_visible(False)
        
        plt.tight_layout()
        st.pyplot(fig5)
        plt.close()

    with col6:
        fig6, ax6 = plt.subplots(figsize=(10, 6))
        n, bins, patches = ax6.hist(data2["price"], bins=40, color='#48bb78', alpha=0.7, 
                                     edgecolor='black', linewidth=1.2)
        
        cm = plt.cm.Greens
        for i, patch in enumerate(patches):
            patch.set_facecolor(cm(i / len(patches)))
        
        mean_val = data2["price"].mean()
        median_val = data2["price"].median()
        ax6.axvline(mean_val, color='red', linestyle='--', linewidth=2.5, 
                   label=f'Mean: {mean_val:,.0f} CFA')
        ax6.axvline(median_val, color='orange', linestyle='--', linewidth=2.5, 
                   label=f'Median: {median_val:,.0f} CFA')
        
        ax6.set_xlabel('Price (CFA)', fontsize=12, fontweight='bold')
        ax6.set_ylabel('Frequency', fontsize=12, fontweight='bold')
        ax6.set_title("🟢 Price Distribution — Men's shoes", fontsize=14, fontweight='bold', pad=15)
        ax6.legend(fontsize=11, frameon=True, shadow=True)
        ax6.grid(axis='y', alpha=0.3, linestyle='--')
        ax6.spines['top'].set_visible(False)
        ax6.spines['right'].set_visible(False)
        
        plt.tight_layout()
        st.pyplot(fig6)
        plt.close()

    st.markdown("---")

    st.markdown("### 👶 Analysis — Children")

    col7, col8 = st.columns(2)

    with col7:
        fig7, ax7 = plt.subplots(figsize=(10, 8))
        top5_clothes_children = data3['type_clothes'].value_counts().head(5)
        
        # Palette de couleurs moderne
        colors7 = sns.color_palette("Set2", len(top5_clothes_children))
        
        # Créer le pie chart avec effet d'explosion
        wedges, texts, autotexts = ax7.pie(
            top5_clothes_children.values,
            labels=top5_clothes_children.index,
            autopct='%1.1f%%',
            startangle=140,
            colors=colors7,
            explode=[0.05] * len(top5_clothes_children),
            shadow=True,
            textprops={'fontsize': 11, 'fontweight': 'bold'}
        )
        
        # Améliorer le style des pourcentages
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(12)
            autotext.set_fontweight('bold')
        
        ax7.set_title("🟡 Top 5 children's clothing items", fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        st.pyplot(fig7)
        plt.close()

    with col8:
        fig8, ax8 = plt.subplots(figsize=(10, 6))
        top5_ce = data4['type_clothes'].value_counts()[:5]
        colors8 = sns.color_palette("Oranges_r", len(top5_ce))
        bars8 = ax8.barh(range(len(top5_ce)), top5_ce.values, color=colors8, 
                        edgecolor='black', linewidth=1.5)
        ax8.set_yticks(range(len(top5_ce)))
        ax8.set_yticklabels(top5_ce.index, fontsize=11)
        ax8.set_xlabel('Number', fontsize=12, fontweight='bold')
        ax8.set_title("🟠 Top 5 children's shoes", fontsize=14, fontweight='bold', pad=15)
        ax8.grid(axis='x', alpha=0.3, linestyle='--')
        ax8.spines['top'].set_visible(False)
        ax8.spines['right'].set_visible(False)
        
        for i, bar in enumerate(bars8):
            width = bar.get_width()
            ax8.text(width + 1, bar.get_y() + bar.get_height()/2, 
                    f'{int(width)}', ha='left', va='center', fontweight='bold', fontsize=10)
        
        plt.tight_layout()
        st.pyplot(fig8)
        plt.close()
    
    st.markdown("---")
    
    # Section bonus: Comparaison globale
    st.markdown("### 📊 Global Comparison")
    
    fig9, (ax9_1, ax9_2) = plt.subplots(1, 2, figsize=(16, 6))
    
    categories = ['Men\nClothing', 'Men\nShoes', 'Children\nClothing', 'Children\nShoes']
    counts = [len(data1), len(data2), len(data3), len(data4)]
    avg_prices = [data1['price'].mean(), data2['price'].mean(), 
                  data3['price'].mean(), data4['price'].mean()]
    colors_comp = ['#667eea', '#48bb78', '#f6ad55', '#fc8181']
    
    # Graphique 1: Nombre d'articles
    bars9_1 = ax9_1.bar(categories, counts, color=colors_comp, edgecolor='black', linewidth=2, alpha=0.8)
    ax9_1.set_ylabel('Number of Articles', fontsize=12, fontweight='bold')
    ax9_1.set_title('Number of Articles per Category', fontsize=14, fontweight='bold', pad=15)
    ax9_1.grid(axis='y', alpha=0.3, linestyle='--')
    ax9_1.spines['top'].set_visible(False)
    ax9_1.spines['right'].set_visible(False)
    
    for bar in bars9_1:
        height = bar.get_height()
        ax9_1.text(bar.get_x() + bar.get_width()/2., height + 5,
                  f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Graphique 2: Prix moyens
    bars9_2 = ax9_2.bar(categories, avg_prices, color=colors_comp, edgecolor='black', linewidth=2, alpha=0.8)
    ax9_2.set_ylabel('Average Price (CFA)', fontsize=12, fontweight='bold')
    ax9_2.set_title('Average Price per Category', fontsize=14, fontweight='bold', pad=15)
    ax9_2.grid(axis='y', alpha=0.3, linestyle='--')
    ax9_2.spines['top'].set_visible(False)
    ax9_2.spines['right'].set_visible(False)
    
    for bar in bars9_2:
        height = bar.get_height()
        ax9_2.text(bar.get_x() + bar.get_width()/2., height + 500,
                  f'{int(height):,}', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    plt.tight_layout()
    st.pyplot(fig9)
    plt.close()
    


else :
    
    st.markdown("<h3 style='text-align: center;'>Give your Feedback</h3>", unsafe_allow_html=True)

    # centrer les deux boutons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Kobo Evaluation Form"):
            st.markdown(
                '<meta http-equiv="refresh" content="0; url=https://ee.kobotoolbox.org/x/pvCTlOly">',
                unsafe_allow_html=True
            )

    with col2:
        if st.button("Google Forms Evaluation"):
            st.markdown(
                '<meta http-equiv="refresh" content="0; url=https://docs.google.com/forms/d/e/1FAIpQLSfhhmTZNu1wZrYr8oFCLy_sgHIUa5oRNlShUYFo_YTZx_OW1w/viewform?usp=sharing&ouid=115563387567840475182">',
                unsafe_allow_html=True
            )