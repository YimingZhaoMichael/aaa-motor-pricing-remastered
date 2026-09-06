DROP TABLE IF EXISTS policies;

CREATE TABLE policies (
    policy_id       INTEGER PRIMARY KEY,
    claim_nb        INTEGER NOT NULL,
    exposure        REAL NOT NULL,
    area            TEXT NOT NULL,
    veh_power       INTEGER NOT NULL,
    veh_age         INTEGER NOT NULL,
    driv_age        INTEGER NOT NULL,
    bonus_malus     INTEGER NOT NULL,
    veh_brand       TEXT NOT NULL,
    veh_gas         TEXT NOT NULL,
    density         INTEGER NOT NULL,
    region          TEXT NOT NULL
);