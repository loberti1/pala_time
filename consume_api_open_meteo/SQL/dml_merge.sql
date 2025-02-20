MERGE dbo.openmeteo as target
USING dbo.stg_openmeteo as source ON target.id_timestamp=source.id_timestamp
WHEN MATCHED THEN UPDATE SET 
target.temperature_2m = source.temperature_2m,
target.relative_humidity_2m = source.relative_humidity_2m,
target.precipitation = source.precipitation,
target.wind_speed_10m = source.wind_speed_10m 
WHEN NOT MATCHED THEN 
INSERT (id_timestamp,temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m)
VALUES (source.id_timestamp,source.temperature_2m,source.relative_humidity_2m,source.precipitation,source.wind_speed_10m);