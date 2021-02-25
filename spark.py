from pyspark.sql import SparkSession

# Initialize spark
def init_spark():
    appName = "test_spark"
    master = "local"
    # Create Spark session
    spark = SparkSession.builder \
            .appName(appName) \
            .master(master) \
            .getOrCreate()
    return spark
    '''
	spark_builder = (
            SparkSession
                .builder
                .appName("test_spark"))
	spark = spark_builder.getOrCreate()
    '''
	
