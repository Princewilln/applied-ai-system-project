"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from typing import Any, Dict, List

from src.recommender import load_songs, recommend_songs


def format_table(recommendations: List[tuple], k: int = 5) -> str:
    headers = ["Rank", "Song", "Score", "Why"]
    rows = []
    for rank, rec in enumerate(recommendations[:k], start=1):
        song, score, explanation = rec
        rows.append(
            [
                str(rank),
                f"{song['title']} by {song['artist']}",
                f"{score:.2f}",
                explanation,
            ]
        )

    col_widths = [len(header) for header in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            col_widths[idx] = max(col_widths[idx], len(cell))

    def format_row(values: List[str]) -> str:
        return " | ".join(
            value.ljust(col_widths[idx]) for idx, value in enumerate(values)
        )

    divider = "-+-".join("-" * width for width in col_widths)
    lines = [format_row(headers), divider]
    lines.extend(format_row(row) for row in rows)
    return "\n".join(lines)


def build_demo_profiles() -> List[Dict[str, Any]]:
    return [
        {
            "name": "High-Energy Pop",
            "prefs": {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.8,
                "likes_acoustic": False,
            },
        },
        {
            "name": "Chill Lofi",
            "prefs": {
                "favorite_genre": "lofi",
                "favorite_mood": "chill",
                "target_energy": 0.35,
                "likes_acoustic": True,
            },
        },
        {
            "name": "Deep Intense Rock",
            "prefs": {
                "favorite_genre": "rock",
                "favorite_mood": "intense",
                "target_energy": 0.9,
                "likes_acoustic": False,
            },
        },
        {
            "name": "Adversarial Conflicting Preferences",
            "prefs": {
                "favorite_genre": "rock",
                "favorite_mood": "sad",
                "target_energy": 0.9,
                "likes_acoustic": False,
            },
        },
    ]


def print_profile_results(
    profile_name: str,
    user_prefs: Dict[str, Any],
    songs: List[Dict[str, Any]],
    k: int = 5,
    use_experiment: bool = False,
) -> None:
    recommendations = recommend_songs(
        user_prefs, songs, k=k, use_experiment=use_experiment
    )

    print(f"\nProfile: {profile_name}")
    print(
        "User prefs: "
        f"favorite_genre={user_prefs.get('favorite_genre')}, "
        f"favorite_mood={user_prefs.get('favorite_mood')}, "
        f"target_energy={user_prefs.get('target_energy')}, "
        f"likes_acoustic={user_prefs.get('likes_acoustic')}"
    )
    print(f"\nTop {k} recommendations:\n")
    print(format_table(recommendations, k=k))
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print("Running experiment: doubled energy weight and halved genre weight.\n")
    for profile in build_demo_profiles():
        print_profile_results(
            profile["name"],
            profile["prefs"],
            songs,
            k=5,
            use_experiment=True,
        )


if __name__ == "__main__":
    main()
