SELECT weather1.id
FROM Weather weather1
JOIN Weather weather2 ON DATEDIFF(weather1.recordDate, weather2.recordDate) = 1 WHERE weather1.temperature > weather2.temperature;
