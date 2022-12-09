from enum import Enum


class SpotifyScopes(Enum):
    USER_READ_PLAYBACK_STATE: str = "user-read-playback-state"
    USER_MODIFY_PLAYBACK_STATE: str = "user-modify-playback-state"
    PLAYLIST_MODIFY_PUBLIC: str = "playlist-modify-public"
    PLAYLIST_MODIFY_PRIVATE: str = "playlist-modify-private"
    USER_READ_RECENTLY_PLAYED: str = "user-read-recently-played"
    USER_READ_PLAYBACK_POSITION: str = "user-read-playback-position"
    PLAYLIST_READ_PRIVATE: str = "playlist-read-private"
    USER_LIBRARY_MODIFY: str = "user-library-modify"
    USER_READ_CURRENTLY_PLAYING: str = "user-read-currently-playing"
