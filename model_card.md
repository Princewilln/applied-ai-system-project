# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender is designed for classroom-style exploration of how content-based recommendation systems work. It suggests songs based on a simple user profile, such as favorite genre, mood, energy level, and whether the user likes acoustic sounds. It assumes the user can describe their taste in a few clear terms, which is helpful for testing the logic but not a full picture of real music listening.

---

## 3. How the Model Works  

The recommender looks at each song and compares it to a user’s taste profile. It pays attention to genre, mood, energy, and a few other musical traits such as valence and acousticness. A song gets a higher score when it matches the user’s preferred genre and mood, and it also gets a boost when its energy level is close to the target. I also added an experiment where energy became more important than genre to test how sensitive the system is to its own weights.

---

## 4. Data  

The system uses a small catalog of 18 songs. Each song includes basic features such as title, artist, genre, mood, energy, and acousticness. The dataset covers a mix of pop, lo-fi, rock, jazz, indie, and other styles, but it is still very limited. Because the catalog is small, the recommender can only learn from a narrow range of musical examples, and it does not include deeper features like lyrics, artist history, or listening behavior.

---

## 5. Strengths  

This system works best when a user has clear and simple preferences. It does a decent job for profiles like “happy pop” or “calm lo-fi” because those preferences are easy to match with the available features. It also gives explanations for why each song was recommended, which makes the behavior easier to understand than a black-box system. In those cases, the results often felt intuitive and easy to explain.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One weakness I noticed is that the recommender can become too focused on a single signal when the scoring weights are changed. In my experiment, making energy matter more caused songs that were close to the target energy to rise quickly even when they did not match the user’s genre or mood as well. That means the system can accidentally create a filter bubble by favoring a narrow type of song and making the recommendations feel less diverse. It also does not capture deeper musical taste, such as artist identity, lyrics, or personal history, so it may miss what a real listener would actually enjoy.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested several very different user profiles to see whether the recommender would respond in a way that made sense. The first profile was a high-energy pop listener, and the top results were songs that matched both the preferred genre and mood. That felt reasonable, although I was a little surprised that Gym Hero kept appearing in some of the results for people who were not explicitly looking for intense pop. It made me realize the system is still picking up energy strongly, even when the user description is more about mood than force.

The chill lo-fi profile produced a very different set of recommendations. Songs with lower energy and more acoustic qualities rose to the top, which made sense because that profile was asking for a calmer, quieter mood. The deep intense rock profile also behaved in a clear way: it preferred songs with high energy and a more forceful tone, so the recommendations shifted toward songs that felt more aggressive and dramatic.

The adversarial profile was the most interesting one. I gave the system a user who wanted rock but also had a sad mood, which is a confusing combination in real life. The results still picked songs that matched the rock genre and energy, but the mood mismatch did not stop them from ranking highly. That told me the system is more comfortable following the visible features in the data than it is handling contradictory tastes.

I also ran a small experiment by changing the weights so energy mattered more and genre mattered less. That changed the rankings noticeably, and it helped me see that the system is quite sensitive to its scoring rules. In plain terms, it is not just saying “this person likes pop” or “this person likes rock”; it is also strongly reacting to how close a song is to the target energy level.

---

## 8. Future Work  

If I kept developing this, I would add more data so the recommender could learn from a larger and more diverse catalog. I would also include more user preferences, such as artist likes, tempo, or favorite decade, so the system could capture more realistic taste. Another improvement would be to make the recommendations more diverse so the top results do not all feel too similar.

---

## 9. Personal Reflection  

The biggest lesson for me was that even a simple recommender can feel surprisingly convincing when the scoring rules are clear and consistent. I was also surprised by how much a small change in the weights could change the whole ranking, which showed me that recommendation systems are very sensitive to the design choices behind them. Using AI tools helped me move faster and structure the project, but I still had to double-check the outputs carefully because the system could look confident while still making obvious mistakes. If I extended this project, I would want to build a more realistic model that uses more user history and a bigger music catalog.
