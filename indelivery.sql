SELECT 
  "Couriers".login,
  COUNT("Orders".id) AS orders_in_delivery
FROM "Couriers"
LEFT JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login;
