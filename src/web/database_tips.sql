/* Queries para Criação */

CREATE TABLE team_participation
(
    id INTEGER NOT NULL PRIMARY KEY,
    team_name VARCHAR(50),
    team_location VARCHAR(50),
    minutes_played VARCHAR(10) NOT NULL,
    field_goals INTEGER NOT NULL,
    field_goals_attempts INTEGER NOT NULL,
    field_goals_percentage DECIMAL(4,3) NOT NULL,
    three_point_field_goals INTEGER NOT NULL,
    three_point_field_goals_attempts INTEGER NOT NULL,
    three_point_field_goals_percentage DECIMAL(4,3) NOT NULL,
    free_throws INTEGER NOT NULL,
    free_throws_attempts INTEGER NOT NULL,
    free_throws_percentage DECIMAL(4,3) NOT NULL,
    offensive_rebounds INTEGER NOT NULL,
    defensive_rebounds INTEGER NOT NULL,
    total_rebounds INTEGER NOT NULL,
    assists INTEGER NOT NULL,
    steals INTEGER NOT NULL,
    blocks INTEGER NOT NULL,
    turnover INTEGER NOT NULL,
    personal_faults INTEGER NOT NULL,
    points INTEGER NOT NULL,
    mat_count_by_team INTEGER NOT NULL,
    won BIT NOT NULL,
    team_is_home BIT NOT NULL
);
CREATE TABLE match_data(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        fk_team_home INTEGER NOT NULL,
        fk_team_away INTEGER NOT NULL,
        date DATE NOT NULL,
        count INTEGER NOT NULL,
        FOREIGN KEY
(fk_team_home) references team_participation
(id),
        FOREIGN KEY
(fk_team_away) references team_participation
(id)
    );

/* Modelo de INSERT no team_participation */
INSERT INTO team_participation
    (
    team_name,
    team_location,
    minutes_played,
    field_goals,
    field_goals_attempts,
    field_goals_percentage,
    three_point_field_goals,
    three_point_field_goals_attempts,
    three_point_field_goals_percentage,
    free_throws,
    free_throws_attempts,
    free_throws_percentage,
    offensive_rebounds,
    defensive_rebounds,
    total_rebounds,
    assists,
    steals,
    blocks,
    turnover,
    personal_faults,
    points,
    mat_count_by_team,
    won,
    team_is_home)
VALUES
    ('Magic', 'Orlando', '39:56', 7, 20, 0.350, 0, 0, 0.350, 8, 8, 1.000, 4, 5, 9, 1, 1, 0, 5, 4, 22, 3, 1, 0);

/* Modelo de INSERT para match_data */
INSERT INTO match_data
    (
    fk_team_home,
    fk_team_away,
    date,
    count
    )
VALUES
    (
        2,
        1,
        '2018-12-31',
        1
  );