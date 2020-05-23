# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head())
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))

better_event=data['Better_Event'].value_counts().index[0]
print(better_event)
# Data Loading 

top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries.drop(top_countries.index[-1])
print(top_countries.head())

# Summer or Winter

def top_ten(top_countries,col):
    country_list=[]
    top_t=top_countries.nlargest(10,col)
    country_list=list(top_t['Country_Name'])
    return country_list
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
# Top 10
common=[x for x in top_10_summer if x in top_10_winter and x in top_10]
print(common)
common1=np.intersect1d(top_10_summer,top_10_winter,top_10)
summer_df=data[data['Country_Name'].isin(top_10_summer)]
print(top_10_summer)
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]


# Plotting top 10
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xticks(rotation=90)
plt.show()
plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
plt.xticks(rotation=90)
plt.show()
plt.bar(top_df['Country_Name'],top_df['Total_Medals'])
plt.xticks(rotation=90)
plt.show()

summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df[summer_df['Golden_Ratio']==summer_df['Golden_Ratio'].max()]['Country_Name'].to_string(index=False)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'].to_string(index=False)

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'].to_string(index=False)
print(top_country_gold)
print(summer_country_gold)
print(winter_country_gold)
# Top Performing Countries
print(data.tail())
data_1=data.drop(data.index[-1])
print(data_1.tail())
data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
print(data_1.head())

most_points=data_1['Total_Points'].max()
best_country=data_1[data_1['Total_Points']==most_points]['Country_Name'].to_string(index=False)
print(best_country)
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)# Best in the world 


# Plotting the best



