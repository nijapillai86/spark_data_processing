import boto3
import yaml
import json
from spark import init_spark
from utils import export_to_csv
#from pyspark import SparkContext, SparkConf
from pyspark.sql.functions import udf
from pyspark.sql.types import StructField, StructType, StringType, IntegerType
from patient_info import get_personal_details, get_condition
import pandas as pd

# Initialise spark
SPARK = init_spark()

def filtering_process(dataFrame):
    print("Drop Duplicates")
    dataFrame.dropDuplicates().show()
    dataFrame.createOrReplaceTempView("table1")
    df3 = SPARK.sql("select first_name, last_name, age, condition from table1 where age>75")
    # df2 = SPARK.sql("select first_name from table1")
    df3.show()
    # Filter or where
    # dataFrame.filter(dataFrame.age == 72).show()

def create_df(data = []):
    sc = StructType([
        StructField('id', StringType()),
        StructField('first_name', StringType()),
        StructField('last_name', StringType()),
        StructField('date_of_birth', StringType()),
        StructField('age', IntegerType()),
        StructField('file_name', StringType()),
        StructField('condition', StringType()),
    ])
    df = SPARK.createDataFrame(data, sc)
    return df

def read_from_s3(bucket, doctor):
    count = 20
    df = create_df()
    for p_obj in bucket.objects.filter(Prefix=doctor):
        if count >0:
            patient   = p_obj.get()
            data      = json.loads(json.loads(json.dumps(patient['Body'].read().decode("utf-8"))))
            patient_info = get_personal_details(data)
            resultant_df = spark_process(patient_info)
            print("Resultant df")
            #resultant_df.show()
            df = df.union(resultant_df)
            df.show()
            count -=1
    return df

def spark_process(patient_info):
    
    # Convert list to RDD
    sc = StructType([
        StructField('id', StringType()),
        StructField('first_name', StringType()),
        StructField('last_name', StringType()),
        StructField('date_of_birth', StringType()),
        StructField('age', IntegerType()),
        StructField('file_name', StringType()),
        StructField('file', StringType()),
    ])
    df = SPARK.createDataFrame(patient_info, sc)
    df.show()
    try:
        condition_extract_udf = udf(get_condition)
        df = df.withColumn('condition', condition_extract_udf(df.file))
        
        df = df.select("id","first_name", "last_name", "date_of_birth", "age", "file_name", "condition")
        return df
    except Exception as ex:
        print(ex)
        raise Exception(ex)
    

def connect_to_s3(CONFIG):
    """
    Returns:
    """
    aws_access_key_id     = CONFIG['s3']['aws_access_key_id']
    aws_secret_access_key = CONFIG['s3']['aws_secret_access_key']
    try:
        client = boto3.resource('s3', aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key)
        return client

    except Exception as exp:
        print("Error connecting to S3: " + str(exp))

def get_available_physician_folders(client, bucket):
    """
    Args:
        client:
        bucket:
    Returns:
    """
    paginator = client.meta.client.get_paginator('list_objects')
    result = paginator.paginate(Bucket=bucket, Delimiter='/')
    # List all available doctors
    doctors_folders = []
    
    for prefix in result.search('CommonPrefixes'):
        doctors_folders.append(prefix.get('Prefix'))

    return doctors_folders

def load_config(conf_file):
    with open(conf_file) as f:
        conf_data = yaml.safe_load(f)
        return conf_data
    return None

def main():
	# Load config file
	CONFIG = load_config("config.yaml")
    # connect to s3 bucket specified in config file
	s3_client = connect_to_s3(CONFIG)
	bucket = s3_client.Bucket(CONFIG['s3']['bucket_name'])
	physician_foldernames = get_available_physician_folders(s3_client, CONFIG['s3']['bucket_name'])
	for physician_foldername in physician_foldernames:
		# print(physician_foldername)
		if physician_foldername == CONFIG['s3']['s3_folder']+"/":
			result_df = read_from_s3(bucket, physician_foldername);export_to_csv(result_df);
            # filtering_process(result_df)

if __name__ == "__main__":
	main()
