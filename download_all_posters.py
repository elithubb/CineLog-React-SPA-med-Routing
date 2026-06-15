import urllib.request
import urllib.parse
import re
import os

# Comprehensive list of 10 movies/series per category
movies = [
    # 🎬 Action & Adventure (avengers)
    {"imdbID": "tt0848228", "title": "The Avengers", "tmdbID": "24428", "type": "movie"},
    {"imdbID": "tt4632448", "title": "Avengers: Endgame", "tmdbID": "299534", "type": "movie"},
    {"imdbID": "tt0107290", "title": "Jurassic Park", "tmdbID": "329", "type": "movie"},
    {"imdbID": "tt0172495", "title": "Gladiator", "tmdbID": "98", "type": "movie"},
    {"imdbID": "tt1392190", "title": "Mad Max: Fury Road", "tmdbID": "76341", "type": "movie"},
    {"imdbID": "tt0082971", "title": "Raiders of the Lost Ark", "tmdbID": "85", "type": "movie"},
    {"imdbID": "tt0499549", "title": "Avatar", "tmdbID": "19995", "type": "movie"},
    {"imdbID": "tt0325980", "title": "Pirates of the Caribbean: The Curse of the Black Pearl", "tmdbID": "22", "type": "movie"},
    {"imdbID": "tt0095016", "title": "Die Hard", "tmdbID": "562", "type": "movie"},
    {"imdbID": "tt0133093", "title": "The Matrix", "tmdbID": "603", "type": "movie"},

    # 😂 Comedy Hits (funny)
    {"imdbID": "tt1119646", "title": "The Hangover", "tmdbID": "18785", "type": "movie"},
    {"imdbID": "tt0829482", "title": "Superbad", "tmdbID": "8363", "type": "movie"},
    {"imdbID": "tt0357413", "title": "Anchorman: The Legend of Ron Burgundy", "tmdbID": "8699", "type": "movie"},
    {"imdbID": "tt1007898", "title": "Step Brothers", "tmdbID": "12133", "type": "movie"},
    {"imdbID": "tt0109686", "title": "Dumb and Dumber", "tmdbID": "8467", "type": "movie"},
    {"imdbID": "tt0377062", "title": "Mean Girls", "tmdbID": "5825", "type": "movie"},
    {"imdbID": "tt0087332", "title": "Ghostbusters", "tmdbID": "4307", "type": "movie"},
    {"imdbID": "tt0119528", "title": "Liar Liar", "tmdbID": "1624", "type": "movie"},
    {"imdbID": "tt0443176", "title": "Borat", "tmdbID": "496", "type": "movie"},
    {"imdbID": "tt0365748", "title": "Shaun of the Dead", "tmdbID": "747", "type": "movie"},

    # 🎭 Drama Essentials (story)
    {"imdbID": "tt0111161", "title": "The Shawshank Redemption", "tmdbID": "278", "type": "movie"},
    {"imdbID": "tt0109830", "title": "Forrest Gump", "tmdbID": "13", "type": "movie"},
    {"imdbID": "tt0068646", "title": "The Godfather", "tmdbID": "238", "type": "movie"},
    {"imdbID": "tt0110912", "title": "Pulp Fiction", "tmdbID": "680", "type": "movie"},
    {"imdbID": "tt0137523", "title": "Fight Club", "tmdbID": "550", "type": "movie"},
    {"imdbID": "tt0108052", "title": "Schindler's List", "tmdbID": "424", "type": "movie"},
    {"imdbID": "tt0099685", "title": "GoodFellas", "tmdbID": "769", "type": "movie"},
    {"imdbID": "tt0120689", "title": "The Green Mile", "tmdbID": "497", "type": "movie"},
    {"imdbID": "tt2582802", "title": "Whiplash", "tmdbID": "244786", "type": "movie"},
    {"imdbID": "tt1285016", "title": "The Social Network", "tmdbID": "37799", "type": "movie"},

    # 👻 Horror & Thriller (scary)
    {"imdbID": "tt1457767", "title": "The Conjuring", "tmdbID": "138843", "type": "movie"},
    {"imdbID": "tt5052448", "title": "Get Out", "tmdbID": "419430", "type": "movie"},
    {"imdbID": "tt0087800", "title": "A Nightmare on Elm Street", "tmdbID": "377", "type": "movie"},
    {"imdbID": "tt0081505", "title": "The Shining", "tmdbID": "694", "type": "movie"},
    {"imdbID": "tt0077651", "title": "Halloween", "tmdbID": "948", "type": "movie"},
    {"imdbID": "tt1396484", "title": "It", "tmdbID": "346364", "type": "movie"},
    {"imdbID": "tt7784604", "title": "Hereditary", "tmdbID": "493922", "type": "movie"},
    {"imdbID": "tt0054215", "title": "Psycho", "tmdbID": "539", "type": "movie"},
    {"imdbID": "tt6644204", "title": "A Quiet Place", "tmdbID": "447332", "type": "movie"},
    {"imdbID": "tt0070047", "title": "The Exorcist", "tmdbID": "230", "type": "movie"},

    # 🚀 Sci-Fi Universe (star)
    {"imdbID": "tt0816692", "title": "Interstellar", "tmdbID": "157336", "type": "movie"},
    {"imdbID": "tt1375666", "title": "Inception", "tmdbID": "27205", "type": "movie"},
    {"imdbID": "tt0076759", "title": "Star Wars: Episode IV - A New Hope", "tmdbID": "11", "type": "movie"},
    {"imdbID": "tt1856101", "title": "Blade Runner 2049", "tmdbID": "335984", "type": "movie"},
    {"imdbID": "tt3659388", "title": "The Martian", "tmdbID": "286217", "type": "movie"},
    {"imdbID": "tt2543167", "title": "Arrival", "tmdbID": "329865", "type": "movie"},
    {"imdbID": "tt1454468", "title": "Gravity", "tmdbID": "49047", "type": "movie"},
    {"imdbID": "tt1161413", "title": "Dune", "tmdbID": "438631", "type": "movie"},
    {"imdbID": "tt0103064", "title": "Terminator 2: Judgment Day", "tmdbID": "280", "type": "movie"},
    {"imdbID": "tt0078748", "title": "Alien", "tmdbID": "348", "type": "movie"},

    # 📺 Trending Series (honor)
    {"imdbID": "tt0903747", "title": "Breaking Bad", "tmdbID": "1399", "type": "tv"},
    {"imdbID": "tt5028030", "title": "Stranger Things", "tmdbID": "66732", "type": "tv"},
    {"imdbID": "tt0944947", "title": "Game of Thrones", "tmdbID": "1396", "type": "tv"},
    {"imdbID": "tt0386676", "title": "The Office", "tmdbID": "2316", "type": "tv"},
    {"imdbID": "tt1475582", "title": "Sherlock", "tmdbID": "19885", "type": "tv"},
    {"imdbID": "tt0108778", "title": "Friends", "tmdbID": "1668", "type": "tv"},
    {"imdbID": "tt8111088", "title": "The Mandalorian", "tmdbID": "82856", "type": "tv"},
    {"imdbID": "tt3032476", "title": "Better Call Saul", "tmdbID": "60059", "type": "tv"},
    {"imdbID": "tt8162467", "title": "Chernobyl", "tmdbID": "87108", "type": "tv"},
    {"imdbID": "tt2560140", "title": "Attack on Titan", "tmdbID": "1429", "type": "tv"},

    # ⚽ Sports Legends (rocky)
    {"imdbID": "tt0075148", "title": "Rocky", "tmdbID": "1366", "type": "movie"},
    {"imdbID": "tt1210166", "title": "Moneyball", "tmdbID": "70586", "type": "movie"},
    {"imdbID": "tt0210945", "title": "Remember the Titans", "tmdbID": "13909", "type": "movie"},
    {"imdbID": "tt0878804", "title": "The Blind Side", "tmdbID": "22897", "type": "movie"},
    {"imdbID": "tt1979320", "title": "Rush", "tmdbID": "96721", "type": "movie"},
    {"imdbID": "tt3503740", "title": "Ford v Ferrari", "tmdbID": "359724", "type": "movie"},
    {"imdbID": "tt0393162", "title": "Coach Carter", "tmdbID": "14295", "type": "movie"},
    {"imdbID": "tt3076658", "title": "Creed", "tmdbID": "312221", "type": "movie"},
    {"imdbID": "tt1291584", "title": "Warrior", "tmdbID": "59440", "type": "movie"},
    {"imdbID": "tt0117705", "title": "Space Jam", "tmdbID": "2300", "type": "movie"},

    # 🦸 Superhero Saga (batman)
    {"imdbID": "tt0468569", "title": "The Dark Knight", "tmdbID": "155", "type": "movie"},
    {"imdbID": "tt1877830", "title": "The Batman", "tmdbID": "414906", "type": "movie"},
    {"imdbID": "tt4633694", "title": "Spider-Man: Into the Spider-Verse", "tmdbID": "324857", "type": "movie"},
    {"imdbID": "tt0371746", "title": "Iron Man", "tmdbID": "1726", "type": "movie"},
    {"imdbID": "tt3315342", "title": "Logan", "tmdbID": "263115", "type": "movie"},
    {"imdbID": "tt3501632", "title": "Black Panther", "tmdbID": "284054", "type": "movie"},
    {"imdbID": "tt0451279", "title": "Wonder Woman", "tmdbID": "297762", "type": "movie"},
    {"imdbID": "tt0317705", "title": "The Incredibles", "tmdbID": "9806", "type": "movie"},
    {"imdbID": "tt0316654", "title": "Spider-Man 2", "tmdbID": "558", "type": "movie"},
    {"imdbID": "tt0409459", "title": "Watchmen", "tmdbID": "13183", "type": "movie"}
]

# Create folder if not exists
os.makedirs("public/fallback-posters", exist_ok=True)

# Mozilla User-Agent to prevent getting blocked by basic scraping protections
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

print("Starting poster download process for 80 movies/series...")

for m in movies:
    img_path = f"public/fallback-posters/{m['imdbID']}.jpg"
    
    # Check if already exists to save bandwidth
    if os.path.exists(img_path):
        print(f"Skipping '{m['title']}' - Already exists.")
        continue
        
    print(f"\nProcessing '{m['title']}'...")
    
    # Fetch TMDB page
    url = f"https://www.themoviedb.org/{m['type']}/{m['tmdbID']}"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Find poster images in the HTML
            posters = re.findall(r'https://image\.tmdb\.org/t/p/(?:w500|w300|original|w300_and_h450_bestv2)/[^"\s>]+', html)
            raw_posters = re.findall(r'/t/p/[^"\s>]+', html)
            
            final_poster_url = None
            if posters:
                final_poster_url = posters[0]
            elif raw_posters:
                final_poster_url = f"https://image.tmdb.org{raw_posters[0]}"
                
            if final_poster_url:
                # Clean URL
                final_poster_url = final_poster_url.split('"')[0].split('&')[0].split(' ')[0]
                # Normalize size to w500
                final_poster_url = re.sub(r'/t/p/(?:w[0-9]+|original|w300_and_h450_bestv2)', '/t/p/w500', final_poster_url)
                
                print(f"Downloading poster from: {final_poster_url}")
                
                # Download and save
                img_req = urllib.request.Request(final_poster_url, headers=headers)
                with urllib.request.urlopen(img_req) as img_res:
                    with open(img_path, "wb") as f:
                        f.write(img_res.read())
                print(f"Saved: {img_path}")
            else:
                print(f"Could not find poster in HTML for {m['title']}.")
                
    except Exception as e:
        print(f"Error handling {m['title']}: {e}")

print("\nProcess finished.")
