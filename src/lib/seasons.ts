import { getCollection, type CollectionEntry } from "astro:content";

export type BlogEntry = CollectionEntry<"blog">;
export type SeasonEntry = CollectionEntry<"season">;

export const getPublishedSeasons = async () => {
  const seasons = await getCollection("season", (season) => season.data.status === "published");
  return seasons.sort((a, b) => b.data.seasonNumber - a.data.seasonNumber);
};

export const getSortedArticles = async () => {
  const articles = await getCollection("blog");
  return articles.sort((a, b) => {
    const seasonDelta = (a.data.seasonNumber ?? 999) - (b.data.seasonNumber ?? 999);
    if (seasonDelta !== 0) return seasonDelta;

    const episodeDelta = (a.data.episodeNumber ?? 999) - (b.data.episodeNumber ?? 999);
    if (episodeDelta !== 0) return episodeDelta;

    return b.data.timestamp.valueOf() - a.data.timestamp.valueOf();
  });
};

export const getEpisodesForSeason = async (seasonSlug: string) => {
  const articles = await getCollection("blog", (article) => article.data.season === seasonSlug);
  return articles.sort((a, b) => {
    const episodeDelta = (a.data.episodeNumber ?? 999) - (b.data.episodeNumber ?? 999);
    if (episodeDelta !== 0) return episodeDelta;

    return a.data.timestamp.valueOf() - b.data.timestamp.valueOf();
  });
};

export const groupArticlesBySeason = (articles: BlogEntry[], seasons: SeasonEntry[]) => {
  const seasonMap = new Map(seasons.map((season) => [season.data.slug, season]));
  const groups = seasons.map((season) => ({
    season,
    articles: articles.filter((article) => article.data.season === season.data.slug),
  }));

  const standalone = articles.filter((article) => !article.data.season || !seasonMap.has(article.data.season));

  return {
    groups: groups.filter((group) => group.articles.length > 0),
    standalone,
  };
};

export const episodeLabel = (article: BlogEntry["data"]) => {
  if (typeof article.episodeNumber !== "number") return article.title;
  if (article.seasonNumber === 0) return `Pilot ${article.episodeNumber}: ${article.episodeTitle ?? article.title}`;
  return `Episode ${article.episodeNumber}: ${article.episodeTitle ?? article.title}`;
};
