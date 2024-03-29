SELECT ANIMAL_ID, NAME
FROM (SELECT ANIMAL_ID, AO.NAME, DATEDIFF(AO.DATETIME, AI.DATETIME) AS DATEDIFF
FROM ANIMAL_INS AI JOIN ANIMAL_OUTS AO
USING (ANIMAL_ID)) AS A
ORDER BY DATEDIFF DESC LIMIT 2