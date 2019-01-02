BEGIN TRANSACTION;

DELETE FROM app_backup;
DELETE FROM app_product;

SELECT setval('app_product_id_seq',1, false);
SELECT setval('app_backup_id_seq',1, false);

COMMIT;