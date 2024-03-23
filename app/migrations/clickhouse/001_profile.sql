CREATE TABLE IF NOT EXISTS csgo_database.profile (
    game_uuid UUID COMMENT 'UUID game',
    
    begin_at DateTime COMMENT 'Game begin at',
    timestamp UInt32 COMMENT 'Game start timestamp',
    year UInt8 COMMENT 'Game start year',
    month UInt8 COMMENT 'Game start month',
    day UInt8 COMMENT 'Game start day',
    weekday UInt8 COMMENT 'Game start weekday',
    hour UInt8 COMMENT 'Game start hour',
    map_id UInt8 COMMENT 'Map', 

    team_id UInt32 COMMENT 'Team',
    team_opponent_id UInt32 COMMENT 'Team opponent',
    player_id UInt32 COMMENT 'Player',
    player_opponent_id UInt32 COMMENT 'Player opponent',
    kills UInt8 COMMENT 'Kills',
    deaths UInt8 COMMENT 'Deaths',
    assists UInt8 COMMENT 'Assists',
    headshots UInt8 COMMENT 'Headshots',
    flash_assists UInt8 COMMENT 'Kills after flash grenade',
    first_kills_diff Int8 COMMENT 'First kills diff',
    k_d_diff Int8 COMMENT 'Kills deaths diff',
    adr Float32 COMMENT 'ADR',
    kast Float32 COMMENT 'KAST',
    rating Float32 COMMENT 'Rating',

    start_ct UInt8 COMMENT 'Team starts game on ct side',
    total_rounds UInt8 COMMENT 'Toral rounds in game',
    h1_win_round_count UInt8 COMMENT 'Rounds won in 1st part of the game',
    h2_win_round_count UInt8 COMMENT 'Rounds won in 2nd part of the game',
    r1_win UInt8 COMMENT 'Round 1 win',
    r2_win UInt8 COMMENT 'Round 2 win',
    r16_win UInt8 COMMENT 'Round 16 win',
    r17_win UInt8 COMMENT 'Round 17 win',
    h1_exploded_count UInt8 COMMENT 'Bomb exploded in 1st half',
    h1_defused_count UInt8 COMMENT 'Bomb defused in 1st half',
    h1_eliminated_count UInt8 COMMENT 'Opponent team eliminated in 1st half',
    h1_timeout_count UInt8 COMMENT 'Round time expired in 1st half',
    h2_exploded_count UInt8 COMMENT 'Bomb exploded in 2nd half',
    h2_defused_count UInt8 COMMENT 'Bomb defused in 2nd half',
    h2_eliminated_count UInt8 COMMENT 'Opponent team eliminated in 2nd half',
    h2_timeout_count UInt8 COMMENT 'Round time expired in 2nd half',
    win UInt8 COMMENT 'Win',        

    create_date DateTime DEFAULT NOW() COMMENT 'Дата создания',
    update_date DateTime COMMENT 'Дата изменения',
    delete_date DateTime COMMENT 'Дата удаления',
    is_delete Boolean DEFAULT FALSE COMMENT 'Объект удален',

    INDEX idx_map_id map_id TYPE bloom_filter GRANULARITY 5,
    INDEX idx_team_id team_id TYPE bloom_filter GRANULARITY 5,
    INDEX idx_team_opponent_id team_opponent_id TYPE bloom_filter GRANULARITY 5,
    INDEX idx_player_id player_id TYPE bloom_filter GRANULARITY 5,
    INDEX idx_player_opponent_id player_opponent_id TYPE bloom_filter GRANULARITY 5,

) ENGINE = ReplacingMergeTree ()
PARTITION BY
    toYYYYMM (begin_at)
ORDER BY
    (game_uuid);