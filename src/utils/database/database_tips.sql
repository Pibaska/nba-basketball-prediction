/* Queries para Criação */

CREATE TABLE IF NOT EXISTS participation (
        participation_id        INTEGER NOT NULL PRIMARY KEY,
        fk_team_id              INTEGER NOT NULL,
        team_name               VARCHAR(50),
        team_is_home            BIT NOT NULL,
        minutes_played          VARCHAR(10) NOT NULL,
        field_goals             INTEGER NOT NULL,
        field_goals_attempts    INTEGER NOT NULL,
        field_goals_percentage  DECIMAL(4,3) NOT NULL,
        three_point_field_goals INTEGER NOT NULL,
        three_point_field_goals_attempts INTEGER NOT NULL,
        three_point_field_goals_percentage DECIMAL(4,3) NOT NULL,
        free_throws             INTEGER NOT NULL,
        free_throws_attempts    INTEGER NOT NULL,
        free_throws_percentage  DECIMAL(4,3) NOT NULL,
        offensive_rebounds      INTEGER NOT NULL,
        defensive_rebounds      INTEGER NOT NULL,
        total_rebounds          INTEGER NOT NULL,
        assists                 INTEGER NOT NULL,
        steals                  INTEGER NOT NULL,
        blocks                  INTEGER NOT NULL,
        turnover                INTEGER NOT NULL,
        personal_faults         INTEGER NOT NULL,
        points                  INTEGER NOT NULL,
        mat_count_by_team       INTEGER NOT NULL,
        won                     BIT NOT NULL,
        FOREIGN KEY (fk_team_id) REFERENCES team (team_id)
    );
    CREATE TABLE IF NOT EXISTS match_data(
        match_id                    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        fk_participation_home       INTEGER NOT NULL,
        fk_participation_away       INTEGER NOT NULL,
        date                        DATE NOT NULL,
        FOREIGN KEY (fk_participation_home) references participation (participation_id),
        FOREIGN KEY (fk_participation_away) references participation (participation_id)
    );
    CREATE TABLE IF NOT EXISTS team (
        team_id         INTEGER NOT NULL PRIMARY KEY,
        team_name       VARCHAR(50),
        team_abv        VARCHAR(10)
    );
    


/* Modelo de INSERT no participation */
INSERT INTO participation (
    participation_id,
    fk_team_id,
    team_name,
    team_is_home,
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
    won
) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?),
        [1, 12, 'Washington Wizards', 1, '60', 8, '20', 0.4, 1, 3, 0.333, 4, 6, 0.667, 1, 8, 9, 3, 1, 1, 1, 5, 21, 42, 0]
        [2, 1, 'Vancouver Grizzlies', 0, '60', 9, '21', 0.429, 2, 3, 0.667, 6, 6, 1.0, 3, 7, 10, 5, 0, 2, 1, 4, 26, 42, 0]
/* Modelo de INSERT para match_data */
INSERT INTO match_data
    (
    fk_participation_home,
    fk_participation_away,
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