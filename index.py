import pymongo
client=pymongo.MongoClient('mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority')
db=client['Main_ScrappingTeamData']
collection=db['filter_data']

print(collection.count_documents({}))

all_data=collection.find()

for data in all_data:
    
    Url=data['url']
   
    if "https://breached.vc" in Url:
        filter={'url':data['url']}

        new_url=Url.replace("https://breached.vc", "http://breached65xqh64s7xbkvqgg7bmj4nj7656hcb7x4g42x753r7zmejqd.onion")
        newvalues = { "$set": {'url': new_url } }


        collection.update_one(filter,newvalues )


   