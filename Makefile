data:
	curl "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/CO2%20concentrations%20-%20NOAA%20(2019)/CO2%20concentrations%20-%20NOAA%20(2019).csv" -o seeds/co2_concentrations.csv
	curl "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Literate%20world%20population%20(OurWorldInData%20based%20on%20OECD%20and%20UNESCO)/Literate%20world%20population%20(OurWorldInData%20based%20on%20OECD%20and%20UNESCO).csv" -o seeds/literate_population.csv

	# 2020 Taxi Data (2.2GB)
	curl "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-[01-12].csv" -o "seeds/tripdata_2020-#1.csv"