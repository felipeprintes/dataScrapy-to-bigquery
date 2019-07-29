from google.cloud import storage
client = storage.Client()
bucket = client.get_bucket('ibge_scrapy')
blob = bucket.blob('data_to_bq.json')
blob.upload_from_filename('data_to_bq.json')