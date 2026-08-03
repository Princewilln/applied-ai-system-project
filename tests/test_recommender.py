import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.recommender import (
    Song,
    UserProfile,
    Recommender,
    evaluate_profile,
    recommend_songs,
    score_song,
    validate_user_profile,
)


def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_score_song_uses_weighted_recipe_for_genre_mood_and_energy():
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False,
    }
    song = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "valence": 0.9,
        "acousticness": 0.2,
    }

    score, reasons = score_song(user_prefs, song)

    assert score >= 3.0
    assert "genre match (+2.0)" in reasons
    assert "mood match (+1.0)" in reasons


def test_validate_user_profile_rejects_out_of_range_inputs():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=1.5,
        likes_acoustic=False,
    )

    is_valid, issues = validate_user_profile(user)

    assert is_valid is False
    assert any("target_energy" in issue for issue in issues)


def test_recommend_songs_promotes_artist_diversity_in_top_results():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    songs = [
        {
            "id": 1,
            "title": "Track A",
            "artist": "Artist One",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 120,
            "valence": 0.9,
            "danceability": 0.8,
            "acousticness": 0.2,
        },
        {
            "id": 2,
            "title": "Track B",
            "artist": "Artist One",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 120,
            "valence": 0.9,
            "danceability": 0.8,
            "acousticness": 0.2,
        },
        {
            "id": 3,
            "title": "Track C",
            "artist": "Artist Two",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 118,
            "valence": 0.9,
            "danceability": 0.8,
            "acousticness": 0.2,
        },
    ]

    results = recommend_songs(
        {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        },
        songs,
        k=2,
    )

    assert len({song["artist"] for song, _, _ in results}) == 2


def test_evaluate_profile_returns_summary_for_sample_input():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()

    result = evaluate_profile(user, rec.songs)

    assert result["valid"] is True
    assert result["top_song"] == "Test Pop Track"
    assert result["confidence"] >= 0.5
