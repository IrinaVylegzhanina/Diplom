SELECT
    o."track",
    CASE
        WHEN o."finished" = TRUE THEN 2
        WHEN o."cancelled" = TRUE THEN -1
        WHEN o."inDelivery" = TRUE THEN 1
        ELSE 0
    END AS STATUS
FROM
    "Orders" AS o;