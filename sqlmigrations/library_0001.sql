BEGIN;
CREATE TABLE "rent_rent" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "time_from" datetime NOT NULL, "time_to" datetime NOT NULL, "status" varchar(10) NOT NULL, "book_id" integer NULL REFERENCES "library_book" ("id"));
CREATE INDEX "rent_rent_5a3d3434" ON "rent_rent" ("time_from");
CREATE INDEX "rent_rent_60021dcc" ON "rent_rent" ("time_to");
CREATE INDEX "rent_rent_0a4572cc" ON "rent_rent" ("book_id");

COMMIT;
