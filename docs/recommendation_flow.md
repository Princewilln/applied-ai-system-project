# Recommendation Flow

```mermaid
flowchart TD
    A[Input: User Preferences<br/>favorite genre, favorite mood, target energy, acoustic preference] --> B[Load songs from data/songs.csv]
    B --> C[Loop through each song]
    C --> D[Score the song using the recommendation recipe]
    D --> E[Check genre match<br/>+2.0 points]
    D --> F[Check mood match<br/>+1.0 point]
    D --> G[Compare energy to target<br/>+1.0 scaled by similarity]
    D --> H[Add smaller bonuses for valence and acousticness]
    E --> I[Combine points into a total score]
    F --> I
    G --> I
    H --> I
    I --> J[Store song with its score and explanation]
    J --> K[Sort all scored songs from highest to lowest]
    K --> L[Output: Top K recommendations]
