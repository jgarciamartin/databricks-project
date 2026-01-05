from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("ParquetEnVolume") \
        .getOrCreate()

    # Datos de ejemplo
    data = [
        (1, "Hola"),
        (2, "Mundo"),
        (3, "Databricks")
    ]

    columns = ["id", "mensaje"]

    df = spark.createDataFrame(data, columns)

    # Ruta del volume
    output_path = "/Volumes/main/default/mi_volume/hola_mundo_parquet"

    # Escritura en Parquet
    df.write \
        .mode("overwrite") \
        .parquet(output_path)

    print(f"Parquet generado en: {output_path}")

    spark.stop()

if __name__ == "__main__":
    main()
