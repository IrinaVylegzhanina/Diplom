SELECT
    c."login",
    count(o)
FROM
    "Orders" o
    INNER JOIN "Couriers" c ON o."courierId" = c."id"
WHERE
    o."inDelivery" = TRUE
GROUP BY
    c."id";