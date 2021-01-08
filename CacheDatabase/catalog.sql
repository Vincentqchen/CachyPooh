BEGIN;
--
-- Create model YTVideo
--
CREATE TABLE "catalog_ytvideo" ("id" serial NOT NULL PRIMARY KEY, "vid_id" varchar(600) NOT NULL, "title" varchar(600) NOT NULL, "length" varchar(600) NOT NULL, "views" integer NOT NULL, "date" date NOT NULL, "ytType" varchar(30) NOT NULL);
COMMIT;
