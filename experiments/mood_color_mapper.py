mood_map = {
    "sad": {
        "color": "blue",
        "feeling": "reflective, heavy, emotional",
        "creative_direction": "Write something honest, slow, and personal."
    },
    "hopeful": {
        "color": "yellow",
        "feeling": "warm, forward-looking, open",
        "creative_direction": "Create something about growth, recovery, or new beginnings."
    },
    "dark": {
        "color": "black",
        "feeling": "intense, mysterious, cinematic",
        "creative_direction": "Build a scene with tension, shadows, and inner conflict."
    },
    "victory": {
        "color": "gold",
        "feeling": "confident, powerful, elevated",
        "creative_direction": "Write about overcoming pressure and proving yourself."
    },
    "calm": {
        "color": "green",
        "feeling": "balanced, grounded, peaceful",
        "creative_direction": "Create something minimal, quiet, and reflective."
    }
}

print("Mood Color Mapper")
print("Choose a mood: sad, hopeful, dark, victory, calm")

mood = input("Mood: ").strip().lower()

if mood in mood_map:
    result = mood_map[mood]

    print("\nCreative Mapping:\n")
    print(f"Color: {result['color']}")
    print(f"Feeling: {result['feeling']}")
    print(f"Creative direction: {result['creative_direction']}")
else:
    print("Mood not found. Try: sad, hopeful, dark, victory, calm")