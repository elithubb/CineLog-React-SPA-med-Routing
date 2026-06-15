import { MovieDetail, SearchResponse } from '../types';
import { getFallbackSearch, getFallbackMovieById } from './fallbackData';

const API_KEY = 'b9bd48a6'; // Public demo key often used in tutorials
const BASE_URL = 'https://www.omdbapi.com';

export async function searchMovies(
  query: string,
  type?: string,
  page = 1
): Promise<SearchResponse> {
  try {
    const typeParam = type && type !== 'all' ? `&type=${type}` : '';
    const response = await fetch(
      `${BASE_URL}/?apikey=${API_KEY}&s=${query}${typeParam}&page=${page}`
    );

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data: SearchResponse = await response.json();
    if (data.Response === 'True') {
      return data;
    }

    console.warn(`OMDB API Search failed: ${data.Error || 'Unknown error'}. Falling back to local database.`);
    return getFallbackSearch(query, type);
  } catch (error) {
    console.error(`Error fetching from OMDB API, falling back to local database:`, error);
    return getFallbackSearch(query, type);
  }
}

export async function getMovieById(id: string): Promise<MovieDetail> {
  try {
    const response = await fetch(
      `${BASE_URL}/?apikey=${API_KEY}&i=${id}&plot=full`
    );

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    if (data.Response === 'False') {
      const fallback = getFallbackMovieById(id);
      if (fallback) {
        return fallback;
      }
      throw new Error(data.Error || 'Movie not found');
    }

    return data;
  } catch (error) {
    console.error(`Error fetching movie detail from OMDB API for id ${id}, falling back to local:`, error);
    const fallback = getFallbackMovieById(id);
    if (fallback) {
      return fallback;
    }
    throw error;
  }
}