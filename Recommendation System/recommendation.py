datasets = {
    "movies": [
        {"id": 1, "title": "Inception", "genres": ["Sci-Fi", "Action"]},
        {"id": 2, "title": "The Matrix", "genres": ["Sci-Fi", "Action"]},
        {"id": 3, "title": "Titanic", "genres": ["Romance", "Drama"]},
        {"id": 4, "title": "Avengers", "genres": ["Action", "Adventure"]},
        {"id": 5, "title": "The Notebook", "genres": ["Romance", "Drama"]},
        {"id": 6, "title": "Interstellar", "genres": ["Sci-Fi", "Adventure"]},
    ],
    "books": [
        {"id": 1, "title": "1984", "genres": ["Dystopian", "Political Fiction"]},
        {"id": 2, "title": "Pride and Prejudice", "genres": ["Romance", "Classic"]},
        {"id": 3, "title": "Dune", "genres": ["Sci-Fi", "Adventure"]},
        {"id": 4, "title": "The Great Gatsby", "genres": ["Classic", "Tragedy"]},
        {"id": 5, "title": "The Hobbit", "genres": ["Fantasy", "Adventure"]},
    ],
    "products": [
        {"id": 1, "title": "iPhone 14", "genres": ["Electronics", "Smartphone"]},
        {"id": 2, "title": "MacBook Air", "genres": ["Electronics", "Laptop"]},
        {"id": 3, "title": "AirPods Pro", "genres": ["Electronics", "Audio"]},
        {"id": 4, "title": "Kindle", "genres": ["Electronics", "Reading"]},
        {"id": 5, "title": "Fitbit Charge", "genres": ["Fitness", "Wearable"]},
    ]
}

def banner(text): print(f"\n{'='*40}\n {text}\n{'='*40}")

def choose_category():
    banner("Choose a Category")
    for i, cat in enumerate(["Movies", "Books", "Products"], 1):
        print(f"{i}. {cat}")
    return {"1": "movies", "2": "books", "3": "products"}.get(input(" Enter choice (1/2/3): ").strip())

def show_items(items):
    banner("Available Items")
    for item in items:
        print(f"[{item['id']}] {item['title']} — 📂 {', '.join(item['genres'])}")

def get_liked(items):
    liked = set()
    print("\nEnter item IDs you like (type 'done' to finish):")
    while True:
        entry = input("ID: ").strip()
        if entry.lower() == "done": break
        if entry.isdigit():
            item_id = int(entry)
            match = next((i for i in items if i["id"] == item_id), None)
            if match:
                if item_id not in liked:
                    liked.add(item_id)
                    print(f"✅ Added: {match['title']}")
                else: print("⚠ Already added.")
            else: print(" Invalid ID.")
        else: print(" Enter a number or 'done'.")
    return [i for i in items if i["id"] in liked]

def build_profile(liked):
    profile = {}
    for item in liked:
        for g in item["genres"]:
            profile[g] = profile.get(g, 0) + 1
    return profile

def recommend(all_items, liked, profile):
    liked_ids = {i["id"] for i in liked}
    recs = []
    for item in all_items:
        if item["id"] in liked_ids: continue
        score = sum(profile.get(g, 0) for g in item["genres"])
        if score: recs.append((item, score))
    return sorted(recs, key=lambda x: x[1], reverse=True)

def show_recs(recs):
    banner("Your Recommendations")
    if not recs:
        print(" No matches found.")
    else:
        for item, score in recs:
            print(f" {item['title']} — 📂 {', '.join(item['genres'])} | 🔢 Score: {score}")

def main():
    category = choose_category()
    if not category: print(" Invalid choice."); return
    items = datasets[category]
    show_items(items)
    liked = get_liked(items)
    if not liked: print("⚠ No items selected."); return
    banner("Items You Liked")
    for i in liked: print(f" {i['title']} — 📂 {', '.join(i['genres'])}")
    profile = build_profile(liked)
    recs = recommend(items, liked, profile)
    show_recs(recs)
    print("\n✨ Thanks for using the recommender!")

main()
