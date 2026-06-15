import { MovieDetail, SearchResponse } from '../types';

export const FALLBACK_MOVIES: MovieDetail[] = [
  // 🎬 Action & Adventure (avengers)
  {
    imdbID: 'tt0848228',
    Title: 'The Avengers',
    Year: '2012',
    Type: 'movie',
    Poster: '/fallback-posters/tt0848228.jpg',
    Rated: 'PG-13',
    Released: '04 May 2012',
    Runtime: '143 min',
    Genre: 'Action, Sci-Fi',
    Director: 'Joss Whedon',
    Writer: 'Joss Whedon, Zak Penn',
    Actors: 'Robert Downey Jr., Chris Evans, Scarlett Johansson, Mark Ruffalo',
    Plot: "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
    Language: 'English',
    Country: 'United States',
    Awards: 'Nominated for 1 Oscar. 38 wins & 79 nominations total.',
    imdbRating: '8.0',
    BoxOffice: '$623,357,910',
  },
  {
    imdbID: 'tt4632448',
    Title: 'Avengers: Endgame',
    Year: '2019',
    Type: 'movie',
    Poster: '/fallback-posters/tt4632448.jpg',
    Rated: 'PG-13',
    Released: '26 Apr 2019',
    Runtime: '181 min',
    Genre: 'Action, Adventure, Drama',
    Director: 'Anthony Russo, Joe Russo',
    Writer: 'Christopher Markus, Stephen McFeely, Stan Lee',
    Actors: 'Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth',
    Plot: "After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
    Language: 'English, Japanese, Xhosa, German',
    Country: 'United States',
    Awards: 'Nominated for 1 Oscar. 70 wins & 133 nominations total.',
    imdbRating: '8.4',
    BoxOffice: '$858,373,000',
  },

  // 😂 Comedy Hits (funny)
  {
    imdbID: 'tt1119646',
    Title: 'The Hangover',
    Year: '2009',
    Type: 'movie',
    Poster: '/fallback-posters/tt1119646.jpg',
    Rated: 'R',
    Released: '05 Jun 2009',
    Runtime: '100 min',
    Genre: 'Comedy',
    Director: 'Todd Phillips',
    Writer: 'Jon Lucas, Scott Moore',
    Actors: 'Bradley Cooper, Ed Helms, Zach Galifianakis, Justin Bartha',
    Plot: 'Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.',
    Language: 'English, ASL',
    Country: 'United States, Germany',
    Awards: 'Won 1 Golden Globe. 13 wins & 26 nominations total.',
    imdbRating: '7.7',
    BoxOffice: '$277,322,503',
  },
  {
    imdbID: 'tt0829482',
    Title: 'Superbad',
    Year: '2007',
    Type: 'movie',
    Poster: '/fallback-posters/tt0829482.jpg',
    Rated: 'R',
    Released: '17 Aug 2007',
    Runtime: '113 min',
    Genre: 'Comedy',
    Director: 'Greg Mottola',
    Writer: 'Seth Rogen, Evan Goldberg',
    Actors: 'Jonah Hill, Michael Cera, Christopher Mintz-Plasse',
    Plot: 'Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.',
    Language: 'English',
    Country: 'United States',
    Awards: '10 wins & 24 nominations total.',
    imdbRating: '7.6',
    BoxOffice: '$121,463,300',
  },

  // 🎭 Drama Essentials (story)
  {
    imdbID: 'tt0111161',
    Title: 'The Shawshank Redemption',
    Year: '1994',
    Type: 'movie',
    Poster: '/fallback-posters/tt0111161.jpg',
    Rated: 'R',
    Released: '14 Oct 1994',
    Runtime: '142 min',
    Genre: 'Drama',
    Director: 'Frank Darabont',
    Writer: 'Stephen King, Frank Darabont',
    Actors: 'Tim Robbins, Morgan Freeman, Bob Gunton',
    Plot: 'Over the course of several years, two convicts form a friendship, seeking consolation and, eventually, redemption through basic compassion.',
    Language: 'English',
    Country: 'United States',
    Awards: 'Nominated for 7 Oscars. 21 wins & 43 nominations total.',
    imdbRating: '9.3',
    BoxOffice: '$28,699,976',
  },
  {
    imdbID: 'tt0109830',
    Title: 'Forrest Gump',
    Year: '1994',
    Type: 'movie',
    Poster: '/fallback-posters/tt0109830.jpg',
    Rated: 'PG-13',
    Released: '06 Jul 1994',
    Runtime: '142 min',
    Genre: 'Drama, Romance',
    Director: 'Robert Zemeckis',
    Writer: 'Winston Groom, Eric Roth',
    Actors: 'Tom Hanks, Robin Wright, Gary Sinise',
    Plot: 'The history of the United States from the 1950s to the 1970s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart.',
    Language: 'English',
    Country: 'United States',
    Awards: 'Won 6 Oscars. 50 wins & 80 nominations total.',
    imdbRating: '8.8',
    BoxOffice: '$330,252,182',
  },

  // 👻 Horror & Thriller (scary)
  {
    imdbID: 'tt1457767',
    Title: 'The Conjuring',
    Year: '2013',
    Type: 'movie',
    Poster: '/fallback-posters/tt1457767.jpg',
    Rated: 'R',
    Released: '19 Jul 2013',
    Runtime: '112 min',
    Genre: 'Horror, Mystery, Thriller',
    Director: 'James Wan',
    Writer: 'Chad Hayes, Carey W. Hayes',
    Actors: 'Patrick Wilson, Vera Farmiga, Ron Livingston',
    Plot: 'Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.',
    Language: 'English',
    Country: 'United States',
    Awards: '15 wins & 22 nominations total.',
    imdbRating: '7.5',
    BoxOffice: '$137,400,141',
  },
  {
    imdbID: 'tt5052448',
    Title: 'Get Out',
    Year: '2017',
    Type: 'movie',
    Poster: '/fallback-posters/tt5052448.jpg',
    Rated: 'R',
    Released: '24 Feb 2017',
    Runtime: '104 min',
    Genre: 'Horror, Mystery, Thriller',
    Director: 'Jordan Peele',
    Writer: 'Jordan Peele',
    Actors: 'Daniel Kaluuya, Allison Williams, Bradley Whitford',
    Plot: "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception eventually reaches a boiling point.",
    Language: 'English',
    Country: 'United States',
    Awards: 'Won 1 Oscar. 152 wins & 203 nominations total.',
    imdbRating: '7.7',
    BoxOffice: '$176,040,665',
  },

  // 🚀 Sci-Fi Universe (star)
  {
    imdbID: 'tt0816692',
    Title: 'Interstellar',
    Year: '2014',
    Type: 'movie',
    Poster: '/fallback-posters/tt0816692.jpg',
    Rated: 'PG-13',
    Released: '07 Nov 2014',
    Runtime: '169 min',
    Genre: 'Adventure, Drama, Sci-Fi',
    Director: 'Christopher Nolan',
    Writer: 'Jonathan Nolan, Christopher Nolan',
    Actors: 'Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine',
    Plot: "When Earth becomes uninhabitable, a team of explorers undertakes the most important mission in human history: traveling beyond this galaxy to discover whether mankind has a future among the stars.",
    Language: 'English',
    Country: 'United States, United Kingdom',
    Awards: 'Won 1 Oscar. 44 wins & 148 nominations total.',
    imdbRating: '8.7',
    BoxOffice: '$188,020,017',
  },
  {
    imdbID: 'tt1375666',
    Title: 'Inception',
    Year: '2010',
    Type: 'movie',
    Poster: '/fallback-posters/tt1375666.jpg',
    Rated: 'PG-13',
    Released: '16 Jul 2010',
    Runtime: '148 min',
    Genre: 'Action, Adventure, Sci-Fi',
    Director: 'Christopher Nolan',
    Writer: 'Christopher Nolan',
    Actors: 'Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy',
    Plot: 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project.',
    Language: 'English, Japanese, French',
    Country: 'United States, United Kingdom',
    Awards: 'Won 4 Oscars. 157 wins & 220 nominations total.',
    imdbRating: '8.8',
    BoxOffice: '$292,576,195',
  },

  // 📺 Trending Series (honor)
  {
    imdbID: 'tt0903747',
    Title: 'Breaking Bad',
    Year: '2008–2013',
    Type: 'series',
    Poster: '/fallback-posters/tt0903747.jpg',
    Rated: 'TV-MA',
    Released: '20 Jan 2008',
    Runtime: '49 min',
    Genre: 'Crime, Drama, Thriller',
    Director: 'N/A',
    Writer: 'Vince Gilligan',
    Actors: 'Bryan Cranston, Aaron Paul, Anna Gunn, Betsy Brandt',
    Plot: "A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine with a former student in order to secure his family's future.",
    Language: 'English, Spanish',
    Country: 'United States',
    Awards: 'Won 16 Primetime Emmys. 154 wins & 247 nominations total.',
    imdbRating: '9.5',
    BoxOffice: 'N/A',
  },
  {
    imdbID: 'tt5028030',
    Title: 'Stranger Things',
    Year: '2016–',
    Type: 'series',
    Poster: '/fallback-posters/tt5028030.jpg',
    Rated: 'TV-14',
    Released: '15 Jul 2016',
    Runtime: '51 min',
    Genre: 'Drama, Fantasy, Horror',
    Director: 'N/A',
    Writer: 'Matt Duffer, Ross Duffer',
    Actors: 'Millie Bobby Brown, Finn Wolfhard, Winona Ryder, David Harbour',
    Plot: 'When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl.',
    Language: 'English',
    Country: 'United States',
    Awards: 'Won 12 Primetime Emmys. 111 wins & 297 nominations total.',
    imdbRating: '8.7',
    BoxOffice: 'N/A',
  },

  // ⚽ Sports Legends (rocky)
  {
    imdbID: 'tt0075148',
    Title: 'Rocky',
    Year: '1976',
    Type: 'movie',
    Poster: '/fallback-posters/tt0075148.jpg',
    Rated: 'PG',
    Released: '03 Dec 1976',
    Runtime: '120 min',
    Genre: 'Drama, Sport',
    Director: 'John G. Avildsen',
    Writer: 'Sylvester Stallone',
    Actors: 'Sylvester Stallone, Talia Shire, Burt Young',
    Plot: 'A small-time Philadelphia boxer gets a supremely rare chance to fight the world heavyweight champion in a bout in which he strives to go the distance for his self-respect.',
    Language: 'English',
    Country: 'United States',
    Awards: 'Won 3 Oscars. 22 wins & 22 nominations total.',
    imdbRating: '8.1',
    BoxOffice: '$117,235,147',
  },
  {
    imdbID: 'tt1210166',
    Title: 'Moneyball',
    Year: '2011',
    Type: 'movie',
    Poster: '/fallback-posters/tt1210166.jpg',
    Rated: 'PG-13',
    Released: '23 Sep 2011',
    Runtime: '133 min',
    Genre: 'Biography, Drama, Sport',
    Director: 'Bennett Miller',
    Writer: 'Steven Zaillian, Aaron Sorkin, Stan Chervin',
    Actors: 'Brad Pitt, Robin Wright, Jonah Hill',
    Plot: "Oakland A's general manager Billy Beane's successful attempt to assemble a baseball team on a lean budget by employing computer-generated analysis to acquire new players.",
    Language: 'English',
    Country: 'United States',
    Awards: 'Nominated for 6 Oscars. 29 wins & 83 nominations total.',
    imdbRating: '7.6',
    BoxOffice: '$75,608,520',
  },

  // 🦸 Superhero Saga (batman)
  {
    imdbID: 'tt0468569',
    Title: 'The Dark Knight',
    Year: '2008',
    Type: 'movie',
    Poster: '/fallback-posters/tt0468569.jpg',
    Rated: 'PG-13',
    Released: '18 Jul 2008',
    Runtime: '152 min',
    Genre: 'Action, Crime, Drama',
    Director: 'Christopher Nolan',
    Writer: 'Jonathan Nolan, Christopher Nolan, David S. Goyer',
    Actors: 'Christian Bale, Heath Ledger, Aaron Eckhart, Maggie Gyllenhaal',
    Plot: 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
    Language: 'English, Mandarin',
    Country: 'United States, United Kingdom',
    Awards: 'Won 2 Oscars. 162 wins & 163 nominations total.',
    imdbRating: '9.0',
    BoxOffice: '$534,858,444',
  },
  {
    imdbID: 'tt1877830',
    Title: 'The Batman',
    Year: '2022',
    Type: 'movie',
    Poster: '/fallback-posters/tt1877830.jpg',
    Rated: 'PG-13',
    Released: '04 Mar 2022',
    Runtime: '176 min',
    Genre: 'Action, Crime, Drama',
    Director: 'Matt Reeves',
    Writer: 'Matt Reeves, Peter Craig, Bill Finger',
    Actors: 'Robert Pattinson, Zoë Kravitz, Jeffrey Wright, Colin Farrell',
    Plot: 'When a sadistic serial killer begins murdering key political figures in Gotham, Batman is forced to investigate the city\'s hidden corruption and question his family\'s involvement.',
    Language: 'English, Latin',
    Country: 'United States',
    Awards: 'Nominated for 3 Oscars. 32 wins & 157 nominations total.',
    imdbRating: '7.8',
    BoxOffice: '$369,345,583',
  }
];

export function getFallbackSearch(query: string, type?: string): SearchResponse {
  const normQuery = query.toLowerCase().trim();
  
  // Filter by query and type
  let results = FALLBACK_MOVIES.filter(m => {
    // Check type
    if (type && type !== 'all' && m.Type !== type) {
      return false;
    }
    
    // Check keyword matching or general search matching
    if (normQuery === 'avengers') return m.Title.toLowerCase().includes('avengers');
    if (normQuery === 'funny') return m.imdbID === 'tt1119646' || m.imdbID === 'tt0829482'; // Comedy
    if (normQuery === 'story') return m.imdbID === 'tt0111161' || m.imdbID === 'tt0109830'; // Drama
    if (normQuery === 'scary') return m.imdbID === 'tt1457767' || m.imdbID === 'tt5052448'; // Horror
    if (normQuery === 'star') return m.imdbID === 'tt0816692' || m.imdbID === 'tt1375666'; // Sci-Fi
    if (normQuery === 'honor') return m.Type === 'series'; // Series
    if (normQuery === 'rocky') return m.imdbID === 'tt0075148' || m.imdbID === 'tt1210166'; // Sports
    if (normQuery === 'batman') return m.Title.toLowerCase().includes('dark knight') || m.Title.toLowerCase().includes('batman');
    
    // Fallback simple search
    return m.Title.toLowerCase().includes(normQuery) || 
           m.Genre.toLowerCase().includes(normQuery) ||
           m.Actors.toLowerCase().includes(normQuery);
  });

  // If no specific results were found, return a subset of fallback database as default
  if (results.length === 0) {
    results = FALLBACK_MOVIES.filter(m => {
      if (type && type !== 'all' && m.Type !== type) {
        return false;
      }
      return true;
    }).slice(0, 10);
  }

  // Convert MovieDetail[] to Movie[]
  const searchItems = results.map(({ imdbID, Title, Year, Type, Poster }) => ({
    imdbID,
    Title,
    Year,
    Type,
    Poster
  }));

  return {
    Search: searchItems,
    totalResults: searchItems.length.toString(),
    Response: searchItems.length > 0 ? 'True' : 'False'
  };
}

export function getFallbackMovieById(id: string): MovieDetail | null {
  const movie = FALLBACK_MOVIES.find(m => m.imdbID === id);
  return movie || null;
}
