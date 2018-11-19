BEGIN TRANSACTION;

DELETE FROM app_category_products;
DELETE FROM app_backup;
DELETE FROM app_product;
DELETE FROM app_category;

SELECT setval('app_product_id_seq',1, false);
SELECT setval('app_category_id_seq', 1, false);
SELECT setval('app_backup_id_seq',1, false);

COMMIT;