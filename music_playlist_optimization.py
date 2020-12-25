def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """

    cur_size = 0
    cur_playlist = []
    song_names = []
    song_lens = []
    song_sizes = []
    count = 0

    for song in songs:
        song_names.append(song[0])
        song_lens.append(song[1])
        song_sizes.append(song[2])

    while cur_size < max_size:
        if not song_names:
            return cur_playlist
        if cur_size + min(song_sizes) >= max_size:
            return cur_playlist
        elif count == 0 and cur_size + song_sizes[0] <= max_size:
            cur_size += song_sizes[0]
            cur_playlist.append(song_names.pop(0))
            song_lens.pop(0)
            song_sizes.pop(0)
        elif count == 0 and cur_size + song_sizes[0] >= max_size:
            return cur_playlist
        else:
            cur_size += min(song_sizes)
            cur_playlist.append(song_names.pop(song_sizes.index(min(song_sizes))))
            song_lens.pop(song_sizes.index(min(song_sizes)))
            song_sizes.pop(song_sizes.index(min(song_sizes)))
        count += 1

    return cur_playlist