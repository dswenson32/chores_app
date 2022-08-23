DROP TABLE IF EXISTS chores;

CREATE TABLE chores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_performed TIMESTAMP NULL,
    chore_name TEXT NOT NULL,
    frequency TEXT NOT NULL
);

-- frequency = d,w,m