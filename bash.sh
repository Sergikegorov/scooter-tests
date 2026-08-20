# Задание 1
PGPASSWORD=smith psql -U morty -d scooter_rent -c 'SELECT "Couriers".login, COUNT("Orders".id) AS orders_in_delivery FROM "Couriers" LEFT JOIN "Orders" ON "Couriers".id = "Orders"."courierId" WHERE "Orders".inDelivery = true GROUP BY "Couriers".login;'

# Задание 2
PGPASSWORD=smith psql -U morty -d scooter_rent -c 'SELECT id AS tracker, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN inDelivery = true THEN 1 ELSE 0 END AS status FROM "Orders";'