SELECT
    c.login,
    COUNT(*)
FROM
    "Couriers" AS c
    INNER JOIN "Orders" AS o ON o."courierId" = c.id
WHERE
    o."inDelivery" = TRUE
GROUP BY
    c.login;