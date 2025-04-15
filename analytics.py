import pandas as pd

# Load data 
df = pd.read_csv("cleaned_youtube_2025.csv")

# Total number of videos
total_videos = df['total_videos'].sum()
print("Total number of videos:", total_videos)

# Most viewed channel
most_subs_row = df[df['total_subscribers'] == df['total_subscribers'].max()]
print("\n Most viewed channel:")
print(most_subs_row[['channel_name', 'youtuber_name', 'total_subscribers']])

# Average Engagement Score & Content Value Index
avg_engagement = df['engagement_score'].mean()
avg_value_index = df['content_value_index'].mean()
print(f"\n Avg Engagement Score: {avg_engagement:.2f}")
print(f"Avg Content Value Index: {avg_value_index:.2f}")

# Total videos by Metaverse Integration Level 
videos_by_metaverse = df.groupby('metaverse_integration_level')['total_videos'].sum()
print("\n Total videos by Metaverse Integration Level:")
print(videos_by_metaverse)

# Top 3 Youtubers by AI Content (%)
top_ai_content = df.sort_values(by='ai_generated_content_(%)', ascending=False).head(3)
print("\n Top 3 AI-Generated Content Creators:")
print(top_ai_content[['youtuber_name', 'ai_generated_content_(%)']])
