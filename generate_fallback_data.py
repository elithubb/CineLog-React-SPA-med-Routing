import urllib.request
import re
import json
import os
import time
from datetime import datetime

# List of movies/series by category
categories = {
    "avengers": [
        {"imdbID": "tt0848228", "title": "The Avengers", "tmdbID": "24428", "type": "movie"},
        {"imdbID": "tt4632448", "title": "Avengers: Endgame", "tmdbID": "299534", "type": "movie"},
        {"imdbID": "tt0107290", "title": "Jurassic Park", "tmdbID": "329", "type": "movie"},
        {"imdbID": "tt0172495", "title": "Gladiator", "tmdbID": "98", "type": "movie"},
        {"imdbID": "tt1392190", "title": "Mad Max: Fury Road", "tmdbID": "76341", "type": "movie"},
        {"imdbID": "tt0082971", "title": "Raiders of the Lost Ark", "tmdbID": "85", "type": "movie"},
        {"imdbID": "tt0499549", "title": "Avatar", "tmdbID": "19995", "type": "movie"},
        {"imdbID": "tt0325980", "title": "Pirates of the Caribbean: The Curse of the Black Pearl", "tmdbID": "22", "type": "movie"},
        {"imdbID": "tt0095016", "title": "Die Hard", "tmdbID": "562", "type": "movie"},
        {"imdbID": "tt0133093", "title": "The Matrix", "tmdbID": "603", "type": "movie"}
    ],
    "funny": [
        {"imdbID": "tt1119646", "title": "The Hangover", "tmdbID": "18785", "type": "movie"},
        {"imdbID": "tt0829482", "title": "Superbad", "tmdbID": "8363", "type": "movie"},
        {"imdbID": "tt0357413", "title": "Anchorman: The Legend of Ron Burgundy", "tmdbID": "8699", "type": "movie"},
        {"imdbID": "tt1007898", "title": "Step Brothers", "tmdbID": "12133", "type": "movie"},
        {"imdbID": "tt0109686", "title": "Dumb and Dumber", "tmdbID": "8467", "type": "movie"},
        {"imdbID": "tt0377062", "title": "Mean Girls", "tmdbID": "5825", "type": "movie"},
        {"imdbID": "tt0087332", "title": "Ghostbusters", "tmdbID": "4307", "type": "movie"},
        {"imdbID": "tt0119528", "title": "Liar Liar", "tmdbID": "1624", "type": "movie"},
        {"imdbID": "tt0443176", "title": "Borat", "tmdbID": "496", "type": "movie"},
        {"imdbID": "tt0365748", "title": "Shaun of the Dead", "tmdbID": "747", "type": "movie"}
    ],
    "story": [
        {"imdbID": "tt0111161", "title": "The Shawshank Redemption", "tmdbID": "278", "type": "movie"},
        {"imdbID": "tt0109830", "title": "Forrest Gump", "tmdbID": "13", "type": "movie"},
        {"imdbID": "tt0068646", "title": "The Godfather", "tmdbID": "238", "type": "movie"},
        {"imdbID": "tt0110912", "title": "Pulp Fiction", "tmdbID": "680", "type": "movie"},
        {"imdbID": "tt0137523", "title": "Fight Club", "tmdbID": "550", "type": "movie"},
        {"imdbID": "tt0108052", "title": "Schindler's List", "tmdbID": "424", "type": "movie"},
        {"imdbID": "tt0099685", "title": "GoodFellas", "tmdbID": "769", "type": "movie"},
        {"imdbID": "tt0120689", "title": "The Green Mile", "tmdbID": "497", "type": "movie"},
        {"imdbID": "tt2582802", "title": "Whiplash", "tmdbID": "244786", "type": "movie"},
        {"imdbID": "tt1285016", "title": "The Social Network", "tmdbID": "37799", "type": "movie"}
    ],
    "scary": [
        {"imdbID": "tt1457767", "title": "The Conjuring", "tmdbID": "138843", "type": "movie"},
        {"imdbID": "tt5052448", "title": "Get Out", "tmdbID": "419430", "type": "movie"},
        {"imdbID": "tt0087800", "title": "A Nightmare on Elm Street", "tmdbID": "377", "type": "movie"},
        {"imdbID": "tt0081505", "title": "The Shining", "tmdbID": "694", "type": "movie"},
        {"imdbID": "tt0077651", "title": "Halloween", "tmdbID": "948", "type": "movie"},
        {"imdbID": "tt1396484", "title": "It", "tmdbID": "346364", "type": "movie"},
        {"imdbID": "tt7784604", "title": "Hereditary", "tmdbID": "493922", "type": "movie"},
        {"imdbID": "tt0054215", "title": "Psycho", "tmdbID": "539", "type": "movie"},
        {"imdbID": "tt6644204", "title": "A Quiet Place", "tmdbID": "447332", "type": "movie"},
        {"imdbID": "tt0070047", "title": "The Exorcist", "tmdbID": "230", "type": "movie"}
    ],
    "star": [
        {"imdbID": "tt0816692", "title": "Interstellar", "tmdbID": "157336", "type": "movie"},
        {"imdbID": "tt1375666", "title": "Inception", "tmdbID": "27205", "type": "movie"},
        {"imdbID": "tt0076759", "title": "Star Wars: Episode IV - A New Hope", "tmdbID": "11", "type": "movie"},
        {"imdbID": "tt1856101", "title": "Blade Runner 2049", "tmdbID": "335984", "type": "movie"},
        {"imdbID": "tt3659388", "title": "The Martian", "tmdbID": "286217", "type": "movie"},
        {"imdbID": "tt2543167", "title": "Arrival", "tmdbID": "329865", "type": "movie"},
        {"imdbID": "tt1454468", "title": "Gravity", "tmdbID": "49047", "type": "movie"},
        {"imdbID": "tt1161413", "title": "Dune", "tmdbID": "438631", "type": "movie"},
        {"imdbID": "tt0103064", "title": "Terminator 2: Judgment Day", "tmdbID": "280", "type": "movie"},
        {"imdbID": "tt0078748", "title": "Alien", "tmdbID": "348", "type": "movie"}
    ],
    "honor": [
        {"imdbID": "tt0903747", "title": "Breaking Bad", "tmdbID": "1399", "type": "tv"},
        {"imdbID": "tt5028030", "title": "Stranger Things", "tmdbID": "66732", "type": "tv"},
        {"imdbID": "tt0944947", "title": "Game of Thrones", "tmdbID": "1396", "type": "tv"},
        {"imdbID": "tt0386676", "title": "The Office", "tmdbID": "2316", "type": "tv"},
        {"imdbID": "tt1475582", "title": "Sherlock", "tmdbID": "19885", "type": "tv"},
        {"imdbID": "tt0108778", "title": "Friends", "tmdbID": "1668", "type": "tv"},
        {"imdbID": "tt8111088", "title": "The Mandalorian", "tmdbID": "82856", "type": "tv"},
        {"imdbID": "tt3032476", "title": "Better Call Saul", "tmdbID": "60059", "type": "tv"},
        {"imdbID": "tt8162467", "title": "Chernobyl", "tmdbID": "87108", "type": "tv"},
        {"imdbID": "tt2560140", "title": "Attack on Titan", "tmdbID": "1429", "type": "tv"}
    ],
    "rocky": [
        {"imdbID": "tt0075148", "title": "Rocky", "tmdbID": "1366", "type": "movie"},
        {"imdbID": "tt1210166", "title": "Moneyball", "tmdbID": "70586", "type": "movie"},
        {"imdbID": "tt0210945", "title": "Remember the Titans", "tmdbID": "13909", "type": "movie"},
        {"imdbID": "tt0878804", "title": "The Blind Side", "tmdbID": "22897", "type": "movie"},
        {"imdbID": "tt1979320", "title": "Rush", "tmdbID": "96721", "type": "movie"},
        {"imdbID": "tt3503740", "title": "Ford v Ferrari", "tmdbID": "359724", "type": "movie"},
        {"imdbID": "tt0393162", "title": "Coach Carter", "tmdbID": "14295", "type": "movie"},
        {"imdbID": "tt3076658", "title": "Creed", "tmdbID": "312221", "type": "movie"},
        {"imdbID": "tt1291584", "title": "Warrior", "tmdbID": "59440", "type": "movie"},
        {"imdbID": "tt0117705", "title": "Space Jam", "tmdbID": "2300", "type": "movie"}
    ],
    "batman": [
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
}

# Flatten list to process unique movies
unique_movies = {}
for cat, m_list in categories.items():
    for m in m_list:
        unique_movies[m["imdbID"]] = m

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def parse_duration(dur_str):
    if not dur_str:
        return "120 min"
    match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?', dur_str)
    if match:
        hours = int(match.group(1)) if match.group(1) else 0
        minutes = int(match.group(2)) if match.group(2) else 0
        total = hours * 60 + minutes
        return f"{total} min"
    return "120 min"

def format_release_date(date_str):
    try:
        dt = datetime.strptime(date_str.split("T")[0], "%Y-%m-%d")
        return dt.strftime("%d %b %Y")
    except Exception:
        return date_str or "N/A"

movie_details = []

print(f"Scraping detailed metadata for {len(unique_movies)} unique movies...")

for idx, (imdb_id, m) in enumerate(unique_movies.items(), 1):
    print(f"[{idx}/{len(unique_movies)}] Fetching {m['title']}...")
    url = f"https://www.themoviedb.org/{m['type']}/{m['tmdbID']}"
    
    # Defaults
    detail = {
        "imdbID": imdb_id,
        "Title": m["title"],
        "Year": "2020",
        "Type": m["type"] if m["type"] != "tv" else "series",
        "Poster": f"/fallback-posters/{imdb_id}.jpg",
        "Rated": "PG-13" if m["type"] == "movie" else "TV-14",
        "Released": "N/A",
        "Runtime": "120 min",
        "Genre": "Action",
        "Director": "N/A",
        "Writer": "N/A",
        "Actors": "N/A",
        "Plot": "No description available.",
        "Language": "English",
        "Country": "United States",
        "Awards": "N/A",
        "imdbRating": "8.0",
        "BoxOffice": "N/A"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # 1. Parse JSON-LD
            json_lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
            if json_lds:
                raw_json = json_lds[0].strip()
                if raw_json.startswith("/* <![CDATA[ */"):
                    raw_json = raw_json.replace("/* <![CDATA[ */", "").replace("/* ]]> */", "").strip()
                
                try:
                    data = json.loads(raw_json)
                    detail["Title"] = data.get("name", m["title"])
                    
                    # Released & Year
                    release_events = data.get("releasedEvent", [])
                    start_date = release_events[0].get("startDate", "") if release_events else ""
                    detail["Released"] = format_release_date(start_date)
                    if start_date:
                        detail["Year"] = start_date.split("-")[0]
                        if m["type"] == "tv":
                            detail["Year"] = f"{detail['Year']}–"
                    
                    # Plot
                    detail["Plot"] = data.get("description", "No description available.").replace("'", "\\'")
                    
                    # Rating
                    rating_data = data.get("aggregateRating", {})
                    rating_val = rating_data.get("ratingValue")
                    if rating_val:
                        detail["imdbRating"] = f"{float(rating_val):.1f}"
                    
                    # Genres
                    genres = data.get("genre", [])
                    if genres:
                        detail["Genre"] = ", ".join(genres)
                        
                    # Runtime
                    detail["Runtime"] = parse_duration(data.get("duration"))
                    
                    # Country
                    country_list = data.get("countryOfOrigin", [])
                    if country_list:
                        countries = [c.get("name") for c in country_list if c.get("name")]
                        if countries:
                            detail["Country"] = ", ".join(countries)
                except Exception as je:
                    print(f"  JSON-LD parse error: {je}")
            
            # 2. Parse Crew (Directors, Writers)
            crew_profiles = re.findall(r'<li class="profile">.*?href="/person/\d+[^"]*">(.*?)</a>.*?(Director|Writer|Screenplay|Creator|Story).*?</li>', html, re.DOTALL)
            directors = []
            writers = []
            for name, role in crew_profiles:
                if "Director" in role or "Creator" in role:
                    if name not in directors:
                        directors.append(name)
                elif role in ["Writer", "Screenplay", "Story"]:
                    if name not in writers:
                        writers.append(name)
            
            if directors:
                detail["Director"] = ", ".join(directors)
            if writers:
                detail["Writer"] = ", ".join(writers)
                
            # 3. Parse Cast (Actors)
            cast_links = re.findall(r'href="/person/\d+[^"]*"[^>]*>(.*?)</a>', html)
            actors = []
            # Filter out director/writer names from actors
            crew_names = set(directors + writers)
            for act in cast_links:
                if act not in crew_names and act not in actors:
                    # Clean tags or extra entities
                    act_cleaned = re.sub(r'<[^>]+>', '', act).strip()
                    if act_cleaned and len(actors) < 4:
                        actors.append(act_cleaned)
            if actors:
                detail["Actors"] = ", ".join(actors)
                
            # 4. Certification (Rating)
            cert_match = re.search(r'<span class="certification"[^>]*>\s*([^<]+?)\s*</span>', html)
            if cert_match:
                detail["Rated"] = cert_match.group(1).strip()
                
            # 5. Box Office / Revenue
            rev_match = re.search(r'<p><strong><bdi>Revenue</bdi></strong>\s*\$([^<]+?)</p>', html)
            if rev_match:
                rev_val = rev_match.group(1).strip().split('.')[0].replace(',', '')
                try:
                    detail["BoxOffice"] = f"${int(rev_val):,}"
                except ValueError:
                    detail["BoxOffice"] = "N/A"
                    
    except Exception as e:
        print(f"  Error reading TMDB for {m['title']}: {e}")
        
    movie_details.append(detail)
    time.sleep(0.1)

# Format CATEGORY_MAP for TS file
category_map_ts = "export const CATEGORY_MAP: Record<string, string[]> = {\n"
for cat_name, m_list in categories.items():
    ids = [m["imdbID"] for m in m_list]
    category_map_ts += f"  '{cat_name}': {json.dumps(ids)},\n"
category_map_ts += "};"

# Output TypeScript Code
ts_code = f"""import {{ MovieDetail, SearchResponse }} from '../types';

{category_map_ts}

export const FALLBACK_MOVIES: MovieDetail[] = {json.dumps(movie_details, indent=2)};

export function getFallbackSearch(query: string, type?: string): SearchResponse {{
  const normQuery = query.toLowerCase().trim();
  
  // Direct category route matching
  if (CATEGORY_MAP[normQuery]) {{
    const ids = CATEGORY_MAP[normQuery];
    let results = FALLBACK_MOVIES.filter(m => ids.includes(m.imdbID));
    
    if (type && type !== 'all') {{
      results = results.filter(m => m.Type === type);
    }}
    
    const searchItems = results.map(({{ imdbID, Title, Year, Type, Poster }}) => ({{
      imdbID,
      Title,
      Year,
      Type,
      Poster
    }}));

    return {{
      Search: searchItems,
      totalResults: searchItems.length.toString(),
      Response: searchItems.length > 0 ? 'True' : 'False'
    }};
  }}
  
  // Custom text-based search
  let results = FALLBACK_MOVIES.filter(m => {{
    if (type && type !== 'all' && m.Type !== type) {{
      return false;
    }}
    
    return m.Title.toLowerCase().includes(normQuery) || 
           m.Genre.toLowerCase().includes(normQuery) ||
           m.Actors.toLowerCase().includes(normQuery);
  }});

  // Default fallback if search query has no matches
  if (results.length === 0) {{
    results = FALLBACK_MOVIES.filter(m => {{
      if (type && type !== 'all' && m.Type !== type) {{
        return false;
      }}
      return true;
    }}).slice(0, 10);
  }}

  const searchItems = results.map(({{ imdbID, Title, Year, Type, Poster }}) => ({{
    imdbID,
    Title,
    Year,
    Type,
    Poster
  }}));

  return {{
    Search: searchItems,
    totalResults: searchItems.length.toString(),
    Response: searchItems.length > 0 ? 'True' : 'False'
  }};
}}

export function getFallbackMovieById(id: string): MovieDetail | null {{
  const movie = FALLBACK_MOVIES.find(m => m.imdbID === id);
  return movie || null;
}}
"""

with open("src/services/fallbackData.ts", "w", encoding="utf-8") as f:
    f.write(ts_code)

print("\nSuccessfully updated src/services/fallbackData.ts with 80 high-quality movies!")
