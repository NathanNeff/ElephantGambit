INSERT INTO TABLE ElephantGambit.raw_json_avro
        SELECT line AS rawjson 
        FROM ElephantGambit.for_compressing;
