CREATE TABLE "dados" (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `cod` text,
    `name` text,
    `gender` text,
    `brithday` text NOT NULL,
    `collect_date` text,
    `send_date` text
);
