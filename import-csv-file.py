import pymongo
import  pandas as pd

def create_df_from_csv(csv_file):
    df=pd.read_csv(csv_file)
    return df
    
if __name__=="__main__":
    print("Welcome to py mongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['campaign']
    collection=db['data']
    csv_file=r"C:/Users/DELL/OneDrive/Desktop/Dreammailer backend/Testing CSV - Sheet1.csv"
    data=create_df_from_csv(csv_file)
    data_dic=data.to_dict(orient='records')
    collection.insert_many(data_dic)
    print("Data inserted successfully")

# For retriving
documents = collection.find()
for doc in documents:
    print(doc['First Name'])