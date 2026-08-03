# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project builds a small music recommender that simulates how a streaming service might connect a user’s taste profile to songs in a catalog. The system uses a simple content-based approach: it looks at song features like genre, mood, energy, and acousticness, compares them to a user’s preferences, and ranks songs by how well they match.

A small stretch feature was also added so the terminal output is easier to read: each recommendation now appears in a simple table with the score and explanation for the ranking.

---

## How The System Works

Real recommendation systems usually combine many signals, such as what a user has listened to, what similar users enjoy, and what the content itself looks like. In this simulation, I focus on the content-based side: the recommender compares a user’s taste profile to the attributes of each song and tries to find songs that feel like the right fit. The system prioritizes clear, interpretable features such as genre, mood, energy, valence, and acousticness, because those are easy to connect to a user’s stated preferences and to a listener’s idea of a song’s "vibe".

### Features used in the simulation

- `Song` features:
  - `genre`
  - `mood`
  - `energy`
  - `tempo_bpm`
  - `valence`
  - `danceability`
  - `acousticness`

- `UserProfile` features:
  - `favorite_genre`
  - `favorite_mood`
  - `target_energy`
  - `likes_acoustic`

### Implementation plan

The plan is to use the expanded catalog in [data/songs.csv](data/songs.csv) and a concrete example user profile with the following preferences:

- favorite genre: `pop`
- favorite mood: `happy`
- target energy: `0.80`
- likes acoustic: `False`

The recommender will read the CSV, evaluate every song one by one, and assign a score using the finalized algorithm recipe below.

### Finalized algorithm recipe

The recommendation rule is a simple weighted recipe built from the song catalog in [data/songs.csv](data/songs.csv):

- +2.0 points for a genre match
- +1.0 point for a mood match
- +1.0 point scaled by energy similarity, where a perfect energy match earns the full point and a larger gap earns less
- smaller bonus points for valence and acousticness to keep the system interpretable

This recipe gives genre a stronger influence than mood, while still letting the energy profile steer results when two songs share the same genre and mood. In practice, a song that matches the user’s favorite genre and mood and also sits near the target energy will rise to the top of the ranking.

### Expected biases

This system may over-prioritize genre, which could cause it to miss some strong songs that match the user’s mood or energy very well but use a different genre. It also relies on a small handcrafted feature set, so it will not understand deeper musical context such as lyrics, artist identity, or listening history.

### Visualizing the data flow

A quick Mermaid flowchart showing how one song moves from the CSV into the ranked recommendation list is available in [docs/recommendation_flow.md](docs/recommendation_flow.md).

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Here is a sample result from the current recommender for a user who likes pop, happy songs, and an energetic feel near 0.8:

```text
User profile: favorite_genre=pop, favorite_mood=happy, target_energy=0.80, likes_acoustic=False

Top recommendations:
1. Sunrise City - Score: 4.46
   Because: matched preferred genre; matched preferred mood; energy close to target 0.80; valence aligned with mood; acousticness was not overly bright

2. Gym Hero - Score: 3.33
   Because: matched preferred genre; mood did not match; energy close to target 0.80; valence aligned with mood; acousticness was not overly bright

3. Rooftop Lights - Score: 2.42
   Because: genre did not match; matched preferred mood; energy close to target 0.80; valence aligned with mood; acousticness was not overly bright
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Phase 4: Evaluation and Explanation

I stress-tested the recommender with four deliberately different user profiles to see how the scoring logic behaves under both ordinary and edge-case conditions. Run the recommender in your terminal and paste the output into the sections below.

```bash
python -m src.main
```

### Profile 1 — High-Energy Pop

```text
(.venv) meltingtech@meltingtech:~/codepath/ai110-module3show-musicrecommendersimulation-starter$ python -m src.main
Loaded songs: 18

Profile: High-Energy Pop
User prefs: favorite_genre=pop, favorite_mood=happy, target_energy=0.8, likes_acoustic=False

Top 5 recommendations:

1. Sunrise City by Neon Echo
   Score: 4.46
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+0.98): close to target0.80; valence aligned with mood; acousticness bonus (+0.24): not overly bright

2. Gym Hero by Max Pulse
   Score: 3.33
   Why: genre match (+2.0); mood mismatch; energy similarity (+0.87): close to target 0.80; valence aligned with mood; acousticness bonus (+0.21): not overly bright

3. Rooftop Lights by Indigo Parade
   Score: 2.42
   Why: genre mismatch; mood match (+1.0); energy similarity (+0.96): close to target 0.80; valence aligned with mood; acousticness bonus (+0.21): not overly bright

4. Velvet Static by Nyra Lane
   Score: 1.40
   Why: genre mismatch; mood mismatch; energy similarity (+0.94): close to target 0.80; valence aligned with mood; acousticness bonus (+0.22): not overly bright

5. Neon Skyline by Aria Vale
   Score: 1.38
   Why: genre mismatch; mood mismatch; energy similarity (+0.92): close to target 0.80; valence aligned with mood; acousticness bonus (+0.23): not overly bright


Profile: Chill Lofi
User prefs: favorite_genre=lofi, favorite_mood=chill, target_energy=0.35, likes_acoustic=True

Top 5 recommendations:

1. Library Rain by Paper Lanterns
   Score: 4.49
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+1.00): close to target0.35; valence aligned with mood; acousticness bonus (+0.24): preferred acoustic profile

2. Midnight Coding by LoRoom
   Score: 4.40
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+0.93): close to target0.35; valence aligned with mood; acousticness bonus (+0.23): preferred acoustic profile

3. Focus Flow by LoRoom
   Score: 3.44
   Why: genre match (+2.0); mood mismatch; energy similarity (+0.95): close to target 0.35; valence aligned with mood; acousticness bonus (+0.24): preferred acoustic profile

4. Spacewalk Thoughts by Orbit Bloom
   Score: 2.39
   Why: genre mismatch; mood match (+1.0); energy similarity (+0.93): close to target 0.35; valence aligned with mood; acousticness bonus (+0.22): preferred acoustic profile

5. Coffee Shop Stories by Slow Stereo
   Score: 1.43
   Why: genre mismatch; mood mismatch; energy similarity (+0.98): close to target 0.35; valence aligned with mood; acousticness bonus (+0.23): preferred acoustic profile


Profile: Deep Intense Rock
User prefs: favorite_genre=rock, favorite_mood=intense, target_energy=0.9, likes_acoustic=False

Top 5 recommendations:

1. Storm Runner by Voltline
   Score: 4.45
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+0.99): close to target0.90; valence aligned with mood; acousticness bonus (+0.23): not overly bright

2. Gym Hero by Max Pulse
   Score: 2.34
   Why: genre mismatch; mood match (+1.0); energy similarity (+0.97): close to target 0.90; valence aligned with mood; acousticness bonus (+0.21): not overly bright

3. Neon Skyline by Aria Vale
   Score: 1.38
   Why: genre mismatch; mood mismatch; energy similarity (+0.98): close to target 0.90; valence aligned with mood; acousticness bonus (+0.23): not overly bright

4. Iron Harbor by Stonecrest
   Score: 1.37
   Why: genre mismatch; mood mismatch; energy similarity (+0.95): close to target 0.90; valence aligned with mood; acousticness bonus (+0.21): not overly bright

5. Velvet Static by Nyra Lane
   Score: 1.34
   Why: genre mismatch; mood mismatch; energy similarity (+0.96): close to target 0.90; valence aligned with mood; acousticness bonus (+0.22): not overly bright


Profile: Adversarial Conflicting Preferences
User prefs: favorite_genre=rock, favorite_mood=sad, target_energy=0.9, likes_acoustic=False

Top 5 recommendations:

1. Storm Runner by Voltline
   Score: 3.44
   Why: genre match (+2.0); mood mismatch; energy similarity (+0.99): close to target 0.90; valence aligned with mood; acousticness bonus (+0.23): not overly bright

2. Neon Skyline by Aria Vale
   Score: 1.43
   Why: genre mismatch; mood mismatch; energy similarity (+0.98): close to target 0.90; valence aligned with mood; acousticness bonus (+0.23): not overly bright

3. Velvet Static by Nyra Lane
   Score: 1.40
   Why: genre mismatch; mood mismatch; energy similarity (+0.96): close to target 0.90; valence aligned with mood; acousticness bonus (+0.22): not overly bright

4. Gym Hero by Max Pulse
   Score: 1.39
   Why: genre mismatch; mood mismatch; energy similarity (+0.97): close to target 0.90; valence aligned with mood; acousticness bonus (+0.21): not overly bright

5. Sunrise City by Neon Echo
   Score: 1.35
   Why: genre mismatch; mood mismatch; energy similarity (+0.92): close to target 0.90; valence aligned with mood; acousticness bonus (+0.24): not overly bright

(.venv) meltingtech@meltingtech:~/codepath/ai110-module3show-musicrecommendersimulation-starter$ 
```

### What these results suggest

- The recommender strongly favors exact genre and mood matches, which makes it feel predictable but also a bit rigid.
- Energy similarity can push a song upward even when it misses on genre or mood, showing that the scoring recipe balances multiple signals.
- The adversarial profile shows that the current logic can still return high-energy songs even when the user mood is contradictory, which is a useful reminder that the system is rule-based rather than emotionally nuanced.

### Step 2: Look for Accuracy and Surprises

Compare the recommendations for at least one profile against your own musical intuition. Ask yourself whether the results feel reasonable and whether anything looks surprising.

For example, in the High-Energy Pop profile, Sunrise City ranked first. That result feels mostly right because the song matches the user’s preferred genre and mood, and its energy is very close to the target value of 0.80. In the current scoring logic in [src/recommender.py](src/recommender.py), this happens because genre contributes +2.0, mood contributes +1.0, and energy contributes a strong similarity bonus. A song that checks multiple boxes can easily rise to the top.

A useful critique is that the system can still feel a bit too rigid. If the same song keeps appearing at the top of every list, it may mean the genre weight is too strong or that the dataset is too small to provide enough variety. That is a sign the recommender is following its rules very literally rather than capturing subtle musical taste.

### Step 3: Run a Small Data Experiment

I tested a weight-shift experiment by doubling the effect of energy and halving the effect of genre. In [src/recommender.py](src/recommender.py), the experimental mode changes the scoring rule so genre contributes 1.0 point for a match and energy contributes 2.0 times the similarity score. I verified the math by running the recommender again with [src/main.py](src/main.py). The recommendations became more energy-driven and a few songs shifted upward because they matched the target energy more closely. That made the results feel different rather than strictly more accurate, which is exactly the kind of sensitivity test this phase is meant to reveal.

## Experiments You Tried

I ran two main experiments while building this recommender.

- Weight-shift experiment: I doubled the effect of energy and reduced the effect of genre. The rankings changed noticeably, and songs that were closer to the target energy moved up even when they did not match the user’s genre as strongly.
- Profile comparison experiment: I tested happy pop, chill lo-fi, intense rock, and an adversarial profile with conflicting preferences. The results shifted in ways that made sense for each profile, which helped confirm that the scoring logic was responding to the input.

---

## Limitations and Risks

This recommender is still a simple classroom-style system, so it has a few important limits.

- It only works with a small catalog of songs, so it cannot capture the full diversity of real music.
- It relies on a few hand-picked features and does not understand artist identity, lyrics, context, or personal taste history.
- It can over-focus on one signal, such as energy, and create narrow or repetitive recommendations.

---

## Reflection

Working through this project helped me understand how recommenders turn simple signals into ranked choices. I learned that a system can look thoughtful even when it is using very basic rules, and that small changes in weighting can strongly affect the results. Using AI tools helped me move faster and organize the work, but I still had to check the outputs carefully because the system could sometimes produce results that looked sensible but were still too rigid. If I kept going, I would want to add more data, more features, and a more realistic way of modeling user taste.

## Sample Recommendation Output

```text
User profile: favorite_genre=pop, favorite_mood=happy, target_energy=0.80, likes_acoustic=False

Top recommendations:
1. Sunrise City — Score: 4.46
2. Gym Hero — Score: 3.33
3. Rooftop Lights — Score: 2.42
```


