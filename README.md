# 🎵 Applied AI System: Music Recommender Simulation

## Project Identity and Original Scope

This project extends a prior classroom-style music recommender prototype into a small applied AI system. The base project’s original scope was to represent a song catalog and a user taste profile, then use a content-based ranking rule to recommend songs based on clearly interpretable musical attributes.

The original system goal was simple and useful:

- model songs as structured records
- represent a user’s preferences in a compact profile
- score each song against that profile
- explain why a recommendation was ranked highly

This final version keeps that original behavior but adds a stronger applied-AI framing by making the system more explainable, more testable, and more reliable through a small evaluation and guardrail layer.

---

## What Makes This an Applied AI System

The resulting system is an end-to-end recommendation workflow that demonstrates:

- data loading from a real CSV catalog
- rule-based scoring logic for content-based retrieval
- explanation generation for each ranked result
- a reliability check for profile validation
- a repeatable evaluation summary for sample inputs

The new AI feature added here is a reliability mechanism: the system now validates the incoming user profile and produces a small evaluation summary that can tell whether the profile is usable and how stable the top-ranked recommendation appears to be.

This matters because even a small recommendation system can look convincing while silently accepting bad inputs or over-weighting one signal. The guardrail layer helps reduce that risk.

---

## System Architecture

The architecture diagram is maintained in [diagrams/architecture.mmd](diagrams/architecture.mmd). The current implementation follows this flow:

1. A user profile is supplied by the caller.
2. The catalog is loaded from the CSV dataset.
3. The recommender scores each song using the weighted recipe.
4. A reliability layer validates input constraints and summarizes the result.
5. The ranked list and explanation are returned to the user.

---

## Recommendation Logic

The scoring recipe is intentionally simple and interpretable:

- +2.0 points for a genre match
- +1.0 point for a mood match
- +1.0 point scaled by energy similarity to the target energy
- smaller bonus points for valence and acousticness alignment

This design makes the system easy to inspect, easy to explain, and easy to test.

---

## Repository Layout

- [src/recommender.py](src/recommender.py): score logic, profile validation, and explanation helpers
- [src/main.py](src/main.py): CLI runner that prints demo profiles and recommendations
- [data/songs.csv](data/songs.csv): song catalog used by the system
- [tests/test_recommender.py](tests/test_recommender.py): regression tests for ranking behavior and reliability checks
- [docs/recommendation_flow.md](docs/recommendation_flow.md): documentation of the recommendation pipeline
- [model_card.md](model_card.md): model and system behavior documentation
- [ai_interactions.md](ai_interactions.md): AI collaboration notes

---

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the system demo

```bash
python -m src.main
```

### 4. Run the test suite

```bash
pytest
```

---

## Verified End-to-End Example

The following output was produced by running the current demo and is representative of the actual end-to-end workflow.

```text
Loaded songs: 18
Running experiment: doubled energy weight and halved genre weight.

Profile: High-Energy Pop
User prefs: favorite_genre=pop, favorite_mood=happy, target_energy=0.8, likes_acoustic=False

Top 5 recommendations:

Rank | Song                            | Score | Why
-----+---------------------------------+-------+--------------------------------
1    | Sunrise City by Neon Echo       | 4.45  | genre match (+1.0); mood match (+1.0); energy similarity (+1.96): close to target 0.80; valence aligned with mood; acousticness bonus (+0.24): not overly bright
2    | Rooftop Lights by Indigo Parade | 3.38  | genre mismatch; mood match (+1.0); energy similarity (+1.92): close to target 0.80; valence aligned with mood; acousticness bonus (+0.21): not overly bright
3    | Gym Hero by Max Pulse           | 3.19  | genre match (+1.0); mood mismatch; energy similarity (+1.74): close to target 0.80; valence aligned with mood; acousticness bonus (+0.21): not overly bright
4    | Velvet Static by Nyra Lane      | 2.33  | genre mismatch; mood mismatch; energy similarity (+1.88): close to target 0.80; valence aligned with mood; acousticness bonus (+0.22): not overly bright
5    | Night Drive Loop by Neon Echo   | 2.32  | genre mismatch; mood mismatch; energy similarity (+1.90): close to target 0.80; valence aligned with mood; acousticness bonus (+0.24): not overly bright
```

This shows the full workflow working end-to-end: input profile → load songs → rank songs → return explainable outputs.

---

## Reliability and Guardrail Behavior

The reliability layer is a lightweight input validation and evaluation harness.

### Example guardrail result

Input profile:

- favorite genre: pop
- favorite mood: happy
- target energy: 0.8
- likes acoustic: False

Behavior:

- profile passes validation because the values are within the expected domain
- evaluation summary confirms the profile is usable and a top song can be identified

### Example failure case

Input profile:

- favorite genre: pop
- favorite mood: happy
- target energy: 1.5
- likes acoustic: False

Behavior:

- the profile is rejected because `target_energy` is outside the valid expected range
- the reliability layer returns a clear issue list explaining the validation problem

This keeps the system from silently producing misleading recommendations from malformed or low-quality inputs.

---

## Evaluation Notes

The project was evaluated against a few clearly different preference profiles:

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock

These tests help confirm that the system responds in a consistent and explainable way to different user tastes. The current recommendation logic is deliberately transparent, which makes it easier to diagnose whether the recommendation pattern is reasonable or unstable.

---

## AI Collaboration Reflection

During development, AI assistance helped structure the recommendation runner and format output in a more readable way. It was especially useful for drafting clean table formatting and speeding up the initial project structure.

A helpful suggestion was to convert the terminal output into a table so the score and explanation were easier to compare. A weaker suggestion was that some of the early output format looked polished even when the underlying logic had not yet been fully validated. That experience reinforced the need to manually verify results rather than trust presentation alone.

The main limitation of the current system is that it depends on a small, handcrafted feature set and a narrow catalog. In future work, the system could be expanded with richer retrieval, more diverse input filtering, or a larger evaluation harness to improve trustworthiness and realism.


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


