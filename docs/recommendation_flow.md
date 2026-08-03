# Recommendation Flow

```mermaid
flowchart TD
    A[Input: User Preferences<br/>favorite genre, favorite mood, target energy, acoustic preference] --> B[Validate profile input]
    B --> C{Profile valid?}
    C -- Yes --> D[Load songs from data/songs.csv]
    C -- No --> E[Return clear issue list and stop]
    D --> F[Loop through each song]
    F --> G[Score the song using the recommendation recipe]
    G --> H[Check genre match<br/>+2.0 points]
    G --> I[Check mood match<br/>+1.0 point]
    G --> J[Compare energy to target<br/>+1.0 scaled by similarity]
    G --> K[Add smaller bonuses for valence and acousticness]
    H --> L[Combine points into a total score]
    I --> L
    J --> L
    K --> L
    L --> M[Store song with its score and explanation]
    M --> N[Sort all scored songs from highest to lowest]
    N --> O[Evaluate profile summary<br/>valid, top song, confidence]
    O --> P[Output: Top K recommendations]
    P --> Q[Human review or test validation]
```

The verified implementation follows a small reliability loop in addition to the scoring loop. The profile validator checks whether the user input is in a sensible range before the system continues, and the evaluation step then returns a compact summary describing whether the profile passed the guardrail and how much confidence to place in the top result. This makes the recommendation pipeline more transparent without changing the underlying content-based approach.
