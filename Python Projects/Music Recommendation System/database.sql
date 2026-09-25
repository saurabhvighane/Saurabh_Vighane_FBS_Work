-- =========================================
-- MUSIC RECOMMENDATION SYSTEM
-- DATABASE SETUP
-- =========================================

CREATE DATABASE IF NOT EXISTS music_recommendation;

USE music_recommendation;


-- =========================================
-- SONGS TABLE
-- =========================================

CREATE TABLE IF NOT EXISTS songs (
    song_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    language VARCHAR(100),
    mood VARCHAR(100)
);


-- =========================================
-- USERS TABLE
-- =========================================

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);


-- =========================================
-- RECOMMENDATION HISTORY TABLE
-- =========================================

CREATE TABLE IF NOT EXISTS recommendation_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    searched_song VARCHAR(255) NOT NULL,
    recommended_song VARCHAR(255) NOT NULL,
    recommended_artist VARCHAR(255) NOT NULL,
    recommendation_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);