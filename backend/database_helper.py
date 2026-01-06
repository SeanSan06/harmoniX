def update_database_helper():
    # Put data into SQLite database
    connection = get_connection()
    cursor = connection.cursor()

    ## Statistics Data
    cursor.execute(""" 
        UPDATE statistics
        SET
            total_songs_transferred_field = total_songs_transferred_field + ?,
            total_playlists_transferred_field = total_playlists_transferred_field + ?,
            total_time_saved_field = total_time_saved_field + ?
        WHERE id_field = 1
    """, (
        songs_transferred,
        1,
        total_time_saved,
    )
    )
    cursor.execute("""
        UPDATE statistics
        SET avg_time_per_song_field = 
            CASE
                WHEN total_songs_transferred_field > 0
                THEN total_time_saved_field / total_songs_transferred_field
                ELSE 0
            END
        WHERE id_field = 1
    """)

    ## Genre Data
    for genre_key, genre_value in genre_counter.items():
        cursor.execute("""
            INSERT INTO genres (genre_name, genre_count)
            VALUES (?, ?)
            ON CONFLICT(genre_name)
            DO UPDATE SET genre_count = genre_count + excluded.genre_count
        """, (
            genre_key,
            genre_value
        )
        )

    connection.commit()
    connection.close()