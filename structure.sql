CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0
);

-- Puedes incluir más tablas o datos iniciales
INSERT INTO tasks (title, completed) VALUES ('Tarea de ejemplo', 0);
